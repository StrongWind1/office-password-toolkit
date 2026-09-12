"""Corpus-driven tests for the OLE/CFB handler.

These exercise the real encrypted files in ``tests/corpus`` end to end: extraction
lines are pinned byte-for-byte against ``office2john`` output, decryption must yield
a valid container, and bypass must leave the input untouched.
"""

from __future__ import annotations

import hashlib
import io
import json
import zipfile
from pathlib import Path

import olefile
import pytest

from office_password_toolkit.formats.ole import OleHandler
from office_password_toolkit.models import GateType

CORPUS = Path(__file__).parent / "corpus"
# Borrowed files promoted to first-party corpus.
PASSWORDS = json.loads((CORPUS / "passwords.json").read_text())
HANDLER = OleHandler()

# Expected OPEN hash lines, taken verbatim from `office2john <file>` (minus John's
# trailing ":::::"/summary metadata, which is not part of the hashcat hash).
EXPECTED_OPEN = {
    "encrypted/ecma376standard_password.docx": "$office$*2007*20*128*16*e88266490c5bd1eebd2b4394e3f830ef*516f732e966fac17b1c5d7d8cc36c928*2b6168dabe2911ad2bd37c1746745c14d3cf1bb1",
    "encrypted/example_password.docx": "$office$*2013*100000*256*16*cbca1c999343fbad92075634150034b0*39eea54e26e514798c284bc7714d38ac*14376d6d817334e6b0ff4fd8221a7c678e5d8a784e8f999f4c188930c36a4b29",
    "encrypted/example_password.xlsx": "$office$*2013*100000*256*16*69035a89b22ce6d55eec2034d35821ba*e846343475cb215c1e0b1880601c1dbc*3535172cb015061586d7ad55edb1a104760056e5e49f500099a36e903ffc87fb",
    "encrypted/rc4cryptoapi_password.doc": "$oldoffice$4*389eb85ba016979b45872262bd473d33*ae9b4378c00439b8b41d20a7e60d5472*55f5f2601bc97515cb1908e1ad706e50c3734500",
    "encrypted/rc4cryptoapi_password.xls": "$oldoffice$4*ff6b27f7b025eb08a8aca2c4477cc064*b948eea818830e56ce56a60c822e7cb3*55bb40447d2bae6b938d9ff54366053628abc435",
    "encrypted/rc4cryptoapi_password.ppt": "$oldoffice$4*ae1414da8e02732fed62ac2bc9b72087*93b4d451c5438c2aebea4591089e0ff6*b5b49908fee194bfb294ec2e33d7b02f4ac2d0dc",
    "encrypted/password_tika_binaryrc4.doc": "$oldoffice$1*885b682da0c8d9cf5e428d9d9ef8af23*f1039a1caa71f390f0858ed2741fc099*720017dd3ba5999d070ef4ff0a196e76",
    "encrypted/password.xls": "$oldoffice$0*68a75dab8dff01c4fa376368e65efc5f*daa7a36e2421fba36ab4ec92fa2aa09a*f7896935e1c3adb71628edb7543c09fa",
    "encrypted/protect.xlsx": "$office$*2007*20*128*16*3a33d19bab466719032d7d3d4f0d3738*7d023231098ac3ecb5eda9247ec4fc54*ee646b3de6a48ccfd8a3b49efaa8127101dfa286",
    "encrypted/50833.xls": "$oldoffice$0*2c8556096f59ef0180278bfcf2b8f918*f7bb5c8cc636a2f10bfc896cfe0c7cc4*ebefa6b9d5f6d1efac02985a4ced79a2",
    "encrypted/Password_Protected-hello.ppt": "$oldoffice$3*f6726d94e45f60d10be156898925b9e0*9f1820becc60e92cd1cef3662e635941*fcf938c2ce4992b3c2202d84ea1123b46ff0185a*fe9c15136749148c8084837194a351ab9a42b599e02485850acc89bb88fc33a4",
    "encrypted/testPPT_protected_passtika.ppt": "$oldoffice$3*70352ce4b27a877dec6e04431c967189*a3a8565d9ae2861375d097916ccbaf14*32842208e285f9678a4bf8016639ac905533f778*83d9ab9f115e405ecb0a30fd224ea1bc314ebb30101be432c267079de9da7f94",
}


def _corpus(name: str) -> Path:
    # Prefer the first-party corpus; fall back to the archived borrowed corpus so
    # the suite stays green until office-corpus-gen populates the primary tree.
    for base in (CORPUS,):
        path = base / name
        if path.exists():
            return path
    pytest.skip(f"corpus file missing: {name}")


def _open_hash(path: Path) -> str | None:
    for extracted in HANDLER.extract(path):
        if extracted.gate is GateType.OPEN:
            return extracted.value
    return None


@pytest.mark.parametrize("name", sorted(EXPECTED_OPEN))
def test_extract_matches_office2john(name: str) -> None:
    assert _open_hash(_corpus(name)) == EXPECTED_OPEN[name]


@pytest.mark.parametrize(
    "name",
    [
        "encrypted/rc4cryptoapi_password.doc",
        "encrypted/rc4cryptoapi_password.xls",
        "encrypted/rc4cryptoapi_password.ppt",
        "encrypted/password.xls",
        "encrypted/50833.xls",
        "encrypted/ecma376standard_password.docx",
        "encrypted/example_password.docx",
        "encrypted/protect.xlsx",
    ],
)
def test_is_encrypted_true_for_keyed_schemes(name: str) -> None:
    assert HANDLER.is_encrypted(_corpus(name)) is True


@pytest.mark.parametrize(
    "name",
    [
        "encrypted/xor-encryption-abc.xls",
        "encrypted/xor_password_123456789012345.xls",
    ],
)
def test_is_encrypted_false_for_xor(name: str) -> None:
    # XOR obfuscation is a keyless DECODE scramble, not a keyed scheme.
    assert HANDLER.is_encrypted(_corpus(name)) is False
    gates = HANDLER.gates(_corpus(name))
    open_gates = [g for g in gates if g.gate is GateType.OPEN]
    assert open_gates and open_gates[0].recovery.value == "decode"


def test_rc4_48bit_gate_detection() -> None:
    """48-bit RC4-CryptoAPI keys must produce an OPEN gate with recovery=CRACK.

    Regression test for the bug where the cryptography library's ARC4 rejected
    48-bit (6-byte) keys, causing verify() to throw ValueError and gate
    enumeration to silently return zero gates (reported as 'open' instead of
    'encrypted:rc4-sha1').
    """
    path = _corpus("lab/o2003__excel13.xls")
    assert HANDLER.is_encrypted(path) is True
    gates = HANDLER.gates(path)
    open_gates = [g for g in gates if g.gate is GateType.OPEN]
    assert len(open_gates) == 1
    assert open_gates[0].recovery.value == "crack"


def test_rc4_48bit_hash_extraction() -> None:
    """48-bit RC4-CryptoAPI must produce a $oldoffice$4 hash (digit 4 = key > 40-bit)."""
    path = _corpus("lab/o2003__excel13.xls")
    line = _open_hash(path)
    assert line is not None
    assert line.startswith("$oldoffice$4*")


def test_rc4_48bit_verify_does_not_crash() -> None:
    """rc4_crypt must accept 6-byte keys without raising ValueError."""
    from office_password_toolkit.crypto.rc4legacy import rc4_crypt

    key = b"\x01\x02\x03\x04\x05\x06"
    data = b"hello world"
    encrypted = rc4_crypt(key, data)
    decrypted = rc4_crypt(key, encrypted)
    assert decrypted == data


@pytest.mark.parametrize(
    ("name", "kind"),
    [
        ("encrypted/ecma376standard_password.docx", "zip"),
        ("encrypted/example_password.docx", "zip"),
        ("encrypted/example_password.xlsx", "zip"),
        ("encrypted/protect.xlsx", "zip"),
        ("encrypted/50833.xls", "ole"),
        ("encrypted/rc4cryptoapi_password.xls", "ole"),
        ("encrypted/rc4cryptoapi_password.doc", "ole"),
        ("encrypted/rc4cryptoapi_password.ppt", "ole"),
    ],
)
def test_decrypt_yields_valid_container(tmp_path: Path, name: str, kind: str) -> None:
    src = _corpus(name)
    out = tmp_path / "plain.out"
    HANDLER.decrypt(src, out, PASSWORDS[name])
    data = out.read_bytes()
    if kind == "zip":
        assert zipfile.is_zipfile(io.BytesIO(data))
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            assert "[Content_Types].xml" in archive.namelist()
    else:
        assert olefile.isOleFile(str(out))
        # The decrypted legacy document must no longer read as encrypted.
        assert HANDLER.is_encrypted(out) is False


def test_decrypt_wrong_password_raises(tmp_path: Path) -> None:
    src = _corpus("encrypted/rc4cryptoapi_password.xls")
    with pytest.raises(ValueError, match="incorrect password"):
        HANDLER.decrypt(src, tmp_path / "x", "definitely-wrong")


@pytest.mark.parametrize(
    "name",
    [
        "encrypted/50833.xls",
        "encrypted/rc4cryptoapi_password.doc",
        "encrypted/rc4cryptoapi_password.ppt",
        "encrypted/xor_password_123456789012345.xls",
    ],
)
def test_bypass_new_file_input_untouched(tmp_path: Path, name: str) -> None:
    src = _corpus(name)
    before = hashlib.sha256(src.read_bytes()).hexdigest()
    out = tmp_path / "bypassed.out"
    HANDLER.bypass(src, out)
    assert olefile.isOleFile(str(out))
    assert hashlib.sha256(src.read_bytes()).hexdigest() == before  # input never modified
