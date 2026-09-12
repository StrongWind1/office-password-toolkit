"""OdfHandler container tests -- driven over the real corpus ODT plus synthetic
unencrypted bodies for the sheet/section BYPASS path (the corpus has no
unencrypted-but-protected ODF sample).

Proves against ``tests/corpus/encrypted/testODTEncrypted.odt`` (password "tika"):
is_encrypted True; gates() reports the ODF-1.2 OPEN gate (mode 18400); extract()
emits the content.xml ``$odf$`` line byte-for-byte matching ``libreoffice2john``;
decrypt() rebuilds a valid ODF zip (mimetype first + stored, content.xml readable
XML, encryption-data dropped) and raises ValueError on a wrong password; bypass()
leaves an encrypted input untouched while producing a valid package.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import zipfile
import zlib
from pathlib import Path

import pytest
from argon2.low_level import ARGON2_VERSION, Type, hash_secret_raw
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from office_password_toolkit.formats.odf import OdfHandler
from office_password_toolkit.models import GateType, HashScheme, RecoveryClass

CORPUS = Path(__file__).parent / "corpus" / "encrypted"
# Borrowed files promoted to first-party corpus.
ODT = CORPUS / "testODTEncrypted.odt"

# content.xml $odf$ line from `libreoffice2john testODTEncrypted.odt` (mode 18400),
# verbatim (metadata stripped). extract() must reproduce this byte-for-byte.
LIBREOFFICE2JOHN_CONTENT = "$odf$*1*1*100000*32*d286185bbbe75063ad09b7cd22c2e79816982263ddbbd96fa66121bd06041c72*16*cb242939e23fcc7c04e27206868b8a56*16*a64e3f0c73c89bba6ffb12f1e07f0b3c*0*cb1b623c4ffc22d49efb010002dd05cc68b91bcb8c2d2c2b0e0b46223b0fa3813a5b545985728e74570f12375c7e49fa48ff46c4945b04401d8718d418f0134d454bb6ab7578aecf067cc9e7f551bf407c0554915f23027afa45c5f6537be818ca7bab10c790d599e6b0e0c0d90a2faa202a52cca61ffa96f0c2f390030b00da7511549781f550c26952c65a3cd2d9cb0699d060059b6c41c69494896c7e99a286cc35511e265eb29d283510d2c295ca1faff65df65108d383951ce30755cc5e1253aae54e57ac52be4795d98029c9f89213f7856b38594d7d7358811327ec19dde0cad1b1b7afe1bc079af5ce1360138629f62048f296af566a55df008c0f7632ebdbeb8e6408a3195729189d12c953303f25773883a392046bae4faf7680ab6321d1e7912c91454e07d8dc42c6de9a57d53dfe66a1100229514f0e407a664710a0335cfc8d3a02db5baa1a2bc3b4967db54dd4ffb36c783eb324b69fceccb34d36aac19c0464cf58194e6e8706b9e8fc1280b14c4da47ff4ba185ecff2a41648d2cefcb6e18ce184201dcb681b79d63418a1709de654d2aeaabefc185062a71ec06e2dafcb6eb7bfea44d7121f3890aafaba5996a40b1ea535d4b4d29f204bdc86f9a0e9eea741e00f56d132593f0de3179a0088be469e0f563c0d330898ec6539b22e17d6afa373fc386cef0fb48742b112f89b8765d57ffa1031351ef06ee983514ea9606362e7661bc7ac81e5cbe0780c4c249d68589051037bf5025221c8027b672593103492ae7eace2f09f7a5344b6ae37fc328fe57b77029192e53cf8eecd88dd50b8792d273125b3bdd741bf8b0c365721e1457ab73a410ec66d86c2214899928c5178d3c381ea6a48050eec66dbe2a7ad09f72ed9fd10771fc0cdadd329db2527cd84304906e158b01f2236462f06daadcbaea6b84509bb17a617b9c55e498b823e9ecf433490dc977e4b1fc3a9e4e2e25a12aead2fcdbb9b7e5ca6a15357a033738a5a364632d4bb6c872916276dcf0e86b880e9b4fcc2711aeb091f1a8d79e171a5209cafb6d5f8a1612659999873a4600eb9fe18402d6c716d0c2d866b8d4d80ecd0247ff3be1ad3f021d1f1126579b624e8671f8282e3d6d8d160b8cf591af07ae5247802e4422f1bba28935220589c890bfec8ec7f7b733594d01f576ee748544e7278b42223c6d3382bd6a0bdac6f8036b9dace4b4294434233af3ad4de2bec61fca5227389332628036a3755e9755a047fdc91eaf4e44034ae7a58be3a090287a77c3763c53b103534cb5081d14f8d8cc22033d4d1c0670008506d3e59b26b10fee97d68204c55c90ff44b9b2b322510a3daa2a9a2ce868fe88fbd6a1ce3596b793ceaad922d3a453f931beed90141c4f2b52acf39bf7df85ebb56949874c898f4921b7ec6cae7acc434886a3e759641700422d4a18b80"


def _password() -> str:
    data = json.loads((CORPUS.parent / "passwords.json").read_text())
    return data["encrypted/testODTEncrypted.odt"]


def _build_odf(path: Path, mimetype: str, content: str) -> None:
    """Write a minimal *unencrypted* ODF package (mimetype first + stored)."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        zi = zipfile.ZipInfo("mimetype")
        zi.compress_type = zipfile.ZIP_STORED
        z.writestr(zi, mimetype)
        z.writestr("content.xml", content)
        z.writestr(
            "META-INF/manifest.xml",
            f'<?xml version="1.0"?><manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0"><manifest:file-entry manifest:full-path="/" manifest:media-type="{mimetype}"/><manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/></manifest:manifest>',
        )


def test_is_encrypted():
    assert OdfHandler().is_encrypted(ODT) is True


def test_gates_reports_open_aes():
    gates = OdfHandler().gates(ODT)
    assert len(gates) == 1
    gate = gates[0]
    assert gate.gate is GateType.OPEN
    assert gate.recovery is RecoveryClass.CRACK
    assert gate.scheme is HashScheme.ODF
    assert gate.hashcat_mode == 18400


def test_extract_matches_libreoffice2john():
    hashes = OdfHandler().extract(ODT)
    assert hashes  # one line per encrypted member
    assert all(h.scheme is HashScheme.ODF and h.hashcat_mode == 18400 for h in hashes)
    # The content.xml member reproduces the libreoffice2john reference exactly.
    assert any(h.value == LIBREOFFICE2JOHN_CONTENT for h in hashes)


def test_decrypt_produces_valid_odf(tmp_path):
    out = tmp_path / "decrypted.odt"
    OdfHandler().decrypt(ODT, out, _password())
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
        assert names[0] == "mimetype"
        assert z.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
        assert z.read("mimetype") == b"application/vnd.oasis.opendocument.text"
        assert z.read("content.xml").startswith(b"<?xml")
        assert b"encryption-data" not in z.read("META-INF/manifest.xml")
    # The input is never modified.
    assert ODT.read_bytes() == Path(ODT).read_bytes()


def test_decrypt_wrong_password_raises(tmp_path):
    with pytest.raises(ValueError, match="incorrect password"):
        OdfHandler().decrypt(ODT, tmp_path / "bad.odt", "not-the-password")


def test_bypass_leaves_encrypted_input_valid(tmp_path):
    out = tmp_path / "bypassed.odt"
    OdfHandler().bypass(ODT, out)
    with zipfile.ZipFile(out) as z:
        assert z.namelist()[0] == "mimetype"
        assert z.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
        # Open-encryption is untouched: content.xml stays ciphertext.
    assert OdfHandler().is_encrypted(out) is True


def test_sheet_protection_gate_and_bypass(tmp_path):
    ods = tmp_path / "sheet.ods"
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<office:document-content xmlns:office="urn:o" xmlns:table="urn:t">'
        "<office:body><office:spreadsheet>"
        '<table:table table:name="S1" table:protected="true" table:protection-key="abc==" '
        'table:protection-key-digest-algorithm="http://www.w3.org/2000/09/xmldsig#sha256">'
        "</table:table></office:spreadsheet></office:body></office:document-content>"
    )
    _build_odf(ods, "application/vnd.oasis.opendocument.spreadsheet", content)

    handler = OdfHandler()
    assert handler.is_encrypted(ods) is False
    gates = handler.gates(ods)
    assert [g.gate for g in gates] == [GateType.PROTECT_SHEET]
    assert gates[0].recovery is RecoveryClass.STRIP

    out = tmp_path / "sheet_bypass.ods"
    handler.bypass(ods, out)
    with zipfile.ZipFile(out) as z:
        text = z.read("content.xml").decode()
    assert 'table:protected="false"' in text
    assert "protection-key" not in text
    assert handler.gates(out) == []


def test_section_protection_gate_and_bypass(tmp_path):
    odt = tmp_path / "section.odt"
    content = '<?xml version="1.0" encoding="UTF-8"?><office:document-content xmlns:office="urn:o" xmlns:text="urn:tx"><office:body><office:text><text:section text:name="Sec1" text:protected="true" text:protection-key="zz=="><text:p>hi</text:p></text:section></office:text></office:body></office:document-content>'
    _build_odf(odt, "application/vnd.oasis.opendocument.text", content)

    handler = OdfHandler()
    gates = handler.gates(odt)
    assert [g.gate for g in gates] == [GateType.SECTION]
    assert gates[0].recovery is RecoveryClass.STRIP

    out = tmp_path / "section_bypass.odt"
    handler.bypass(odt, out)
    with zipfile.ZipFile(out) as z:
        text = z.read("content.xml").decode()
    assert 'text:protected="false"' in text
    assert "protection-key" not in text
    assert handler.gates(out) == []


def test_unencrypted_plain_file_has_no_gates(tmp_path):
    odt = tmp_path / "plain.odt"
    _build_odf(odt, "application/vnd.oasis.opendocument.text", '<?xml version="1.0"?><office:document-content xmlns:office="urn:o"/>')
    handler = OdfHandler()
    assert handler.is_encrypted(odt) is False
    assert handler.gates(odt) == []
    assert handler.extract(odt) == []


# --- ODF 1.3 "Wholesome Encryption" (synthetic; no real LibreOffice sample) ---
#
# There is no ODF 1.3 corpus file, so these build a spec-valid Argon2id + AES-GCM
# package (LibreOffice core ZipFile.cxx / ciphercontext.cxx recipe) and round-trip
# it through the handler. Synthetic validation only.

_NS = "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0"
_LOEXT = "urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0"
_GCM_URI = "http://www.w3.org/2009/xmlenc11#aes256-gcm"
_ARGON2_URN = "urn:org:documentfoundation:names:experimental:office:manifest:argon2id"
_SHA256_STARTKEY = "http://www.w3.org/2001/04/xmlenc#sha256"


def _build_odf13(path: Path, password: str, plaintext: bytes) -> None:
    """Write a synthetic, spec-valid ODF 1.3 (Argon2id + AES-GCM) package."""
    salt, iv = os.urandom(16), os.urandom(12)
    t_cost, memory_kib, lanes = 3, 65536, 4
    deflate = zlib.compressobj(9, zlib.DEFLATED, -15)
    compressed = deflate.compress(plaintext) + deflate.flush()
    start_key = hashlib.sha256(password.encode("utf-8")).digest()
    key = hash_secret_raw(secret=start_key, salt=salt, time_cost=t_cost, memory_cost=memory_kib, parallelism=lanes, hash_len=32, type=Type.ID, version=ARGON2_VERSION)
    member = iv + AESGCM(key).encrypt(iv, compressed, None)  # IV || ciphertext || tag

    b64_salt = base64.b64encode(salt).decode("ascii")
    b64_iv = base64.b64encode(iv).decode("ascii")
    mimetype = "application/vnd.oasis.opendocument.text"
    manifest = (
        f'<?xml version="1.0" encoding="UTF-8"?>'
        f'<manifest:manifest xmlns:manifest="{_NS}" xmlns:loext="{_LOEXT}">'
        f'<manifest:file-entry manifest:full-path="/" manifest:media-type="{mimetype}"/>'
        f'<manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml" manifest:size="{len(compressed)}">'
        f"<manifest:encryption-data>"
        f'<manifest:algorithm manifest:algorithm-name="{_GCM_URI}" manifest:initialisation-vector="{b64_iv}"/>'
        f'<manifest:key-derivation manifest:key-derivation-name="{_ARGON2_URN}" manifest:key-size="32" manifest:salt="{b64_salt}" loext:argon2-iterations="{t_cost}" loext:argon2-memory="{memory_kib}" loext:argon2-lanes="{lanes}"/>'
        f'<manifest:start-key-generation manifest:start-key-generation-name="{_SHA256_STARTKEY}" manifest:key-size="32"/>'
        f"</manifest:encryption-data></manifest:file-entry></manifest:manifest>"
    ).encode()

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        zi = zipfile.ZipInfo("mimetype")
        zi.compress_type = zipfile.ZIP_STORED
        z.writestr(zi, mimetype)
        z.writestr("content.xml", member)
        z.writestr("META-INF/manifest.xml", manifest)


def test_odf13_is_encrypted_and_gate(tmp_path):
    odt = tmp_path / "wholesome.odt"
    _build_odf13(odt, "Secret123!", b"<?xml version='1.0'?><office:document-content>body</office:document-content>")
    handler = OdfHandler()
    assert handler.is_encrypted(odt) is True
    gates = handler.gates(odt)
    assert [g.gate for g in gates] == [GateType.OPEN]
    gate = gates[0]
    assert gate.recovery is RecoveryClass.CRACK
    assert gate.scheme is HashScheme.ODF
    # No hashcat mode exists for Argon2id + AES-GCM.
    assert gate.hashcat_mode is None


def test_odf13_extract_emits_extended_line(tmp_path):
    odt = tmp_path / "wholesome.odt"
    _build_odf13(odt, "Secret123!", b"<?xml version='1.0'?><office:document-content>body</office:document-content>")
    hashes = OdfHandler().extract(odt)
    assert len(hashes) == 1
    h = hashes[0]
    assert h.scheme is HashScheme.ODF
    assert h.hashcat_mode is None  # ODF 1.3 has no GPU mode
    assert h.value.startswith("$odf$*sha256*argon2*aes256gcm*")
    assert len(h.value.split("*")) == 11  # unified ODF format


def test_odf13_decrypt_round_trip(tmp_path):
    plaintext = b"<?xml version='1.0' encoding='UTF-8'?><office:document-content>wholesome payload</office:document-content>"
    odt = tmp_path / "wholesome.odt"
    _build_odf13(odt, "Secret123!", plaintext)
    out = tmp_path / "decrypted.odt"
    OdfHandler().decrypt(odt, out, "Secret123!")
    with zipfile.ZipFile(out) as z:
        assert z.namelist()[0] == "mimetype"
        assert z.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
        assert z.read("content.xml") == plaintext
        assert b"encryption-data" not in z.read("META-INF/manifest.xml")
    # The input package is never modified.
    assert odt.read_bytes() == Path(odt).read_bytes()


def test_odf13_decrypt_wrong_password_raises(tmp_path):
    odt = tmp_path / "wholesome.odt"
    _build_odf13(odt, "right", b"<?xml version='1.0'?><doc>x</doc>")
    with pytest.raises(ValueError, match="incorrect password"):
        OdfHandler().decrypt(odt, tmp_path / "bad.odt", "wrong")
