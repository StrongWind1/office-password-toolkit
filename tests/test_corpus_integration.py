"""End-to-end integration tests against the REAL corpus files.

These exercise the actual handlers on genuine producer output (msoffcrypto / tika /
poi / LibreOffice samples), not synthetic fixtures -- the difference between "the
crypto reproduces a published vector" and "a real encrypted file decrypts". Files
live in ``tests/corpus/`` with passwords in ``tests/corpus/passwords.json``.

Each case skips (rather than fails) when its file is absent, so the suite still runs
against a trimmed corpus, but asserts hard when the file is present.
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import pytest

from office_password_toolkit.bypass import bypass_file
from office_password_toolkit.decrypt import decrypt_file
from office_password_toolkit.detect import detect
from office_password_toolkit.extract import extract_hashes

CORPUS = Path(__file__).parent / "corpus"
# Borrowed files promoted to first-party corpus.

_OLE_MAGIC = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"
_ZIP_MAGIC = b"PK\x03\x04"


def _find(rel: str) -> Path | None:
    """Locate a corpus file by relative path or bare name.

    Resolves against the first-party corpus first, then the archived borrowed
    corpus, so the suite stays green until office-corpus-gen fills the primary tree.
    """
    for base in (CORPUS,):
        direct = base / rel
        if direct.exists():
            return direct
    for base in (CORPUS,):
        matches = list(base.rglob(Path(rel).name))
        if matches:
            return matches[0]
    return None


def _kind(data: bytes) -> str:
    if data.startswith(_ZIP_MAGIC):
        return "zip"
    if data.startswith(_OLE_MAGIC):
        return "ole"
    return "other"


# (relative path, password, expected output container | "any") -- all real producer output.
DECRYPT_CASES = [
    ("encrypted/ecma376standard_password.docx", "Password1234_", "zip"),  # ECMA-376 standard (9400)
    ("encrypted/example_password.docx", "Password1234_", "zip"),  # agile SHA-512/AES-256 (9600)
    ("encrypted/example_password.xlsx", "Password1234_", "zip"),  # agile (9600)
    ("encrypted/protect.xlsx", "VelvetSweatshop", "zip"),  # VelvetSweatshop default
    ("encrypted/rc4cryptoapi_password.doc", "Password1234_", "ole"),  # RC4-CryptoAPI (9800)
    ("encrypted/rc4cryptoapi_password.ppt", "Password1234_", "ole"),  # PowerPoint RC4-CryptoAPI
    ("encrypted/testAccess2_encrypted.accdb", "tika", "any"),  # REAL Access ACE agile (per-page)
    ("encrypted/encrypted_scriptsig_lo242.odt", "password", "zip"),  # REAL ODF 1.3 Argon2id
    ("encrypted/encrypted_scriptsig_odf13.odt", "password", "zip"),  # REAL ODF 1.3 PBKDF2 + Basic macros
    ("encrypted/testODTEncrypted.odt", "tika", "zip"),  # ODF 1.2 AES-256-CBC (18400)
    ("encrypted/protected_upper_case.docx", "password", "zip"),  # uppercase ENCRYPTIONINFO stream
]


@pytest.mark.parametrize(("rel", "password", "want"), DECRYPT_CASES)
def test_real_file_decrypts(tmp_path: Path, rel: str, password: str, want: str) -> None:
    src = _find(rel)
    if src is None:
        pytest.skip(f"corpus file {rel} not present")
    before = src.read_bytes()
    out = tmp_path / ("out" + src.suffix)
    decrypt_file(src, out, password)
    data = out.read_bytes()
    assert len(data) > 0
    if want != "any":
        assert _kind(data) == want
    if _kind(data) == "zip":
        assert zipfile.is_zipfile(io.BytesIO(data))
    assert src.read_bytes() == before  # THE ONE RULE: input never modified


def test_real_agile_and_standard_extract_lines(tmp_path: Path) -> None:
    """A genuine encrypted docx/xlsx yields the expected hashcat line prefix."""
    for rel, prefix in [
        ("encrypted/example_password.docx", "$office$*2013*"),
        ("encrypted/ecma376standard_password.docx", "$office$*2007*"),
        ("encrypted/rc4cryptoapi_password.doc", "$oldoffice$"),
    ]:
        src = _find(rel)
        if src is None:
            continue
        hashes = extract_hashes(src)
        assert hashes, rel
        assert hashes[0].value.startswith(prefix), (rel, hashes[0].value[:30])


def test_xor_bypass_changes_file_and_preserves_input(tmp_path: Path) -> None:
    """Regression: opt bypass on a legacy XOR .xls used to report success while
    leaving the file byte-identical. It must now produce a different, gate-free file
    and never touch the input."""
    src = _find("encrypted/xor-encryption-abc.xls")
    if src is None:
        pytest.skip("xor .xls sample not present")
    before = src.read_bytes()
    out = tmp_path / "out.xls"
    bypass_file(src, out)
    assert out.read_bytes() != before  # the bug: output used to equal the input
    assert src.read_bytes() == before  # input untouched
    assert detect(out).encrypted is False


def test_officexor_gates_still_reported(tmp_path: Path) -> None:
    """XOR-obfuscated files report a DECODE gate but no extract hash (not crackable)."""
    src = _find("encrypted/xor-encryption-abc.xls")
    if src is None:
        pytest.skip("xor .xls sample not present")
    hashes = extract_hashes(src)
    assert len(hashes) == 0
    from office_password_toolkit.detect import detect
    from office_password_toolkit.formats import handler_for
    from office_password_toolkit.models import GateType, RecoveryClass

    result = detect(src)
    handler = handler_for(result.container)
    gates = handler.gates(src)
    assert any(g.gate is GateType.OPEN and g.recovery is RecoveryClass.DECODE for g in gates)
