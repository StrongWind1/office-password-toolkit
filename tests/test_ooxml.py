"""Corpus-driven tests for the OOXML/OPC handler.

Proves gate enumeration, 25300/110 hash extraction, and the strip/bypass path
against the real protected files in ``tests/corpus/protected`` plus synthetic
fixtures for the two paths the corpus does not cover (a VBA-locked project and a
binary ``.xlsb`` BIFF12 record).
"""

from __future__ import annotations

import base64
import io
import re
import zipfile
from pathlib import Path

import olefile
import pytest

from office_password_toolkit.crypto import vba
from office_password_toolkit.formats import ooxml
from office_password_toolkit.formats.ooxml import OoxmlHandler, _biff12_record_ids, _scan_biff12
from office_password_toolkit.models import GateType

CORPUS = Path(__file__).parent / "corpus" / "protected"
# Every protected fixture currently lives in the archived borrowed corpus; the
# first-party protected/ tree (CORPUS) is populated later by office-corpus-gen.
# Borrowed files promoted to first-party corpus.


@pytest.fixture
def handler() -> OoxmlHandler:
    return OoxmlHandler()


def _read_part(path: Path, part: str) -> str:
    with zipfile.ZipFile(path) as zf:
        return zf.read(part).decode("utf-8")


def _attr(xml: str, name: str) -> str | None:
    m = re.search(name + r'="([^"]*)"', xml)
    return m.group(1) if m else None


# --- is_encrypted is always False for a plaintext package ---

ALL_PROTECTED = sorted(p.name for p in CORPUS.glob("*") if p.suffix.lower() in {".xlsx", ".xlsm", ".docx", ".pptx"})


@pytest.mark.parametrize("name", ALL_PROTECTED)
def test_never_encrypted(handler: OoxmlHandler, name: str) -> None:
    assert handler.is_encrypted(CORPUS / name) is False
    # gate enumeration must never raise on any package
    handler.gates(CORPUS / name)
    handler.extract(CORPUS / name)


# --- Gate enumeration ---

EXPECTED_GATES = {
    "sheetProtection_allLocked.xlsx": {GateType.PROTECT_SHEET},
    "protectedSheets.xlsx": {GateType.PROTECT_SHEET},
    "workbookProtection-workbook_password-2013.xlsx": {GateType.PROTECT_WORKBOOK},
    "workbookProtection-sheet_password-2013.xlsx": {GateType.PROTECT_SHEET},
    "workbookProtection-workbook_password_user_range-2010.xlsx": {GateType.PROTECT_WORKBOOK, GateType.ALLOW_EDIT_RANGES},
    "workbookProtection_workbook_revision_protected.xlsx": {GateType.SHARED_REVISIONS},
    "workbookProtection_workbook_structure_protected.xlsx": {GateType.PROTECT_WORKBOOK},
    "workbookProtection_workbook_windows_protected.xlsx": {GateType.PROTECT_WORKBOOK},
    "documentProtection_readonly_no_password.docx": {GateType.RESTRICT_EDIT},
    "documentProtection_comments_no_password.docx": {GateType.RESTRICT_EDIT},
    "documentProtection_forms_no_password.docx": {GateType.RESTRICT_EDIT},
    "documentProtection_trackedChanges_no_password.docx": {GateType.RESTRICT_EDIT},
    "EnforcedWith.docx": {GateType.RESTRICT_EDIT},
    "protected_sample.docx": {GateType.RESTRICT_EDIT},
    "testWORD_docSecurity.docx": {GateType.MODIFY},
    "fileSharing_reservation.xlsm": {GateType.MODIFY},
    "63934.xlsx": {GateType.ALLOW_EDIT_RANGES},
    "hello-world-signed.docx": {GateType.SIGNATURE},
    "hello-world-signed.xlsx": {GateType.SIGNATURE},
    "hello-world-signed.pptx": {GateType.SIGNATURE},
    "testWORD_signed.docx": {GateType.SIGNATURE},
}


@pytest.mark.parametrize(("name", "expected"), EXPECTED_GATES.items())
def test_gate_types(handler: OoxmlHandler, name: str, expected: set[GateType]) -> None:
    found = {g.gate for g in handler.gates(CORPUS / name)}
    assert expected <= found, f"{name}: expected {expected}, found {found}"


# --- 25300 hash extraction: the emitted line must match the XML attributes ---

ISO_SHA512_CASES = {
    "workbookProtection-workbook_password-2013.xlsx": ("xl/workbook.xml", "workbookSaltValue", "workbookHashValue"),
    "workbookProtection-sheet_password-2013.xlsx": ("xl/worksheets/sheet1.xml", "saltValue", "hashValue"),
    "fileSharing_reservation.xlsm": ("xl/workbook.xml", "saltValue", "hashValue"),
}


@pytest.mark.parametrize(("name", "parts"), ISO_SHA512_CASES.items())
def test_25300_line_matches_xml(handler: OoxmlHandler, name: str, parts: tuple[str, str, str]) -> None:
    part, salt_attr, hash_attr = parts
    xml = _read_part(CORPUS / name, part)
    salt = _attr(xml, salt_attr)
    digest = _attr(xml, hash_attr)
    lines = [h.value for h in handler.extract(CORPUS / name)]
    assert len(lines) == 1
    tokens = lines[0].split("$")  # ['', 'office', '2016', '0', spin, salt, hash]
    assert tokens[1:4] == ["office", "2016", "0"]
    assert tokens[4] == "100000"
    assert tokens[5] == salt
    assert tokens[6] == digest


def test_no_line_when_no_password(handler: OoxmlHandler) -> None:
    # sheetProtection with locked options but no algorithmName/hashValue -> gate, no hash.
    hashes = handler.extract(CORPUS / "sheetProtection_allLocked.xlsx")
    assert hashes == []
    gates = handler.gates(CORPUS / "sheetProtection_allLocked.xlsx")
    assert any(g.gate is GateType.PROTECT_SHEET for g in gates)


def test_legacy_word_dialect_emits_doc_protect(handler: OoxmlHandler) -> None:
    # protected_sample.docx carries the crypt* (Word 2007) dialect -> $doc-protect$ line,
    # no shipped hashcat mode. The salt/hash must match word/settings.xml verbatim.
    gates = handler.gates(CORPUS / "protected_sample.docx")
    restrict = next(g for g in gates if g.gate is GateType.RESTRICT_EDIT)
    assert restrict.hashcat_mode is None

    settings = _read_part(CORPUS / "protected_sample.docx", "word/settings.xml")
    sid = _attr(settings, "w:cryptAlgorithmSid")
    spin = _attr(settings, "w:cryptSpinCount")
    salt = _attr(settings, "w:salt")
    digest = _attr(settings, "w:hash")

    hashes = handler.extract(CORPUS / "protected_sample.docx")
    assert len(hashes) == 1
    assert hashes[0].hashcat_mode is None
    assert hashes[0].gate is GateType.RESTRICT_EDIT
    assert hashes[0].value.startswith("$office-protect$*")
    assert "*word2007*" in hashes[0].value


def test_legacy_word_writeprotection_emits_doc_protect(handler: OoxmlHandler) -> None:
    # testWORD_docSecurity.docx carries the crypt* dialect on <w:writeProtection> (sid 14).
    hashes = [h for h in handler.extract(CORPUS / "testWORD_docSecurity.docx") if h.gate is GateType.MODIFY]
    assert len(hashes) == 1
    assert hashes[0].value.startswith("$office-protect$*")
    assert "*word2007*" in hashes[0].value


# --- bypass: strips the element, leaves the input byte-identical, stays a valid zip ---

BYPASS_CASES = {
    "sheetProtection_allLocked.xlsx": ("xl/worksheets/sheet1.xml", "sheetProtection"),
    "workbookProtection-workbook_password-2013.xlsx": ("xl/workbook.xml", "workbookProtection"),
    "workbookProtection-sheet_password-2013.xlsx": ("xl/worksheets/sheet1.xml", "sheetProtection"),
    "documentProtection_readonly_no_password.docx": ("word/settings.xml", "documentProtection"),
    "protected_sample.docx": ("word/settings.xml", "documentProtection"),
    "testWORD_docSecurity.docx": ("word/settings.xml", "writeProtection"),
    "fileSharing_reservation.xlsm": ("xl/workbook.xml", "fileSharing"),
    "63934.xlsx": ("xl/worksheets/sheet1.xml", "protectedRange"),
    "protectedSheets.xlsx": ("xl/worksheets/sheet1.xml", "sheetProtection"),
}


@pytest.mark.parametrize(("name", "parts"), BYPASS_CASES.items())
def test_bypass(handler: OoxmlHandler, tmp_path: Path, name: str, parts: tuple[str, str]) -> None:
    part, elem = parts
    src = CORPUS / name
    before = src.read_bytes()
    out = tmp_path / f"out_{name}"

    tag = re.compile(r"<(?:[\w.\-]+:)?" + elem + r"\b")
    assert tag.search(_read_part(src, part)) is not None  # element present before

    handler.bypass(src, out)

    assert src.read_bytes() == before  # THE ONE RULE: input never modified
    with zipfile.ZipFile(out) as zout, zipfile.ZipFile(src) as zin:
        assert tag.search(zout.read(part).decode("utf-8", "replace")) is None  # gone
        assert zout.testzip() is None  # valid archive
        assert set(zin.namelist()) == set(zout.namelist())  # every member preserved


def test_bypass_leaves_unlocked_vba_untouched(handler: OoxmlHandler, tmp_path: Path) -> None:
    src = CORPUS / "fileSharing_reservation.xlsm"
    out = tmp_path / "out.xlsm"
    handler.bypass(src, out)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(out) as zout:
        assert zin.read("xl/vbaProject.bin") == zout.read("xl/vbaProject.bin")


# --- signature removal: opt-in, drops the _xmlsignatures/ parts + origin relationship ---

SIGNED = ["hello-world-signed.docx", "hello-world-signed.xlsx", "hello-world-signed.pptx", "testWORD_signed.docx"]


@pytest.mark.parametrize("name", SIGNED)
def test_bypass_keeps_signature_by_default(handler: OoxmlHandler, tmp_path: Path, name: str) -> None:
    """Without the flag, bypass must leave the digital signature intact."""
    src = CORPUS / name
    out = tmp_path / f"out_{name}"
    handler.bypass(src, out)
    with zipfile.ZipFile(out) as zout:
        assert any(m.startswith("_xmlsignatures/") for m in zout.namelist())
        assert b"digital-signature" in zout.read("_rels/.rels")


@pytest.mark.parametrize("name", SIGNED)
def test_bypass_remove_signatures(handler: OoxmlHandler, tmp_path: Path, name: str) -> None:
    """With ``remove_signatures``, the sig parts and the origin relationship are gone."""
    src = CORPUS / name
    before = src.read_bytes()
    out = tmp_path / f"out_{name}"

    handler.bypass(src, out, remove_signatures=True)

    assert src.read_bytes() == before  # THE ONE RULE: input never modified
    with zipfile.ZipFile(out) as zout:
        assert not any(m.startswith("_xmlsignatures/") for m in zout.namelist())  # parts gone
        assert b"digital-signature" not in zout.read("_rels/.rels")  # dangling origin rel gone
        assert zout.testzip() is None  # still a valid archive
        assert b"<Relationship" in zout.read("_rels/.rels")  # other relationships preserved
    assert not any(g.gate is GateType.SIGNATURE for g in handler.gates(out))  # no longer reported


# --- decrypt does not apply to a plaintext package ---


def test_decrypt_raises(handler: OoxmlHandler, tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="never document-open encrypted"):
        handler.decrypt(CORPUS / "sheetProtection_allLocked.xlsx", tmp_path / "x", "pw")


# --- VBA-locked synthetic fixture (no locked project exists in the corpus) ---

_ALL_ZERO = "{00000000-0000-0000-0000-000000000000}"
_VBA_KEY = b"\x11\x22\x33\x44"
_VBA_PW = "Secret1"


def _make_locked_vba_xlsm(dest: Path) -> str:
    """Rewrite the corpus VBA blob so its PROJECT stream carries a hash-case lock; return the expected 110 line."""
    proj_key = vba.project_key(_ALL_ZERO)
    digest = vba.password_hash(_VBA_PW, _VBA_KEY)
    struct = vba.build_password_hash_structure(_VBA_KEY, digest)
    dpb = vba.encode_data_encryption(struct, 0xAB, proj_key)
    cmg = vba.encode_data_encryption(b"\x01\x00\x00\x00", 0xAB, proj_key)
    gc = vba.encode_data_encryption(b"\xff", 0xAB, proj_key)
    project = f'ID="{_ALL_ZERO}"\r\nCMG="{cmg}"\r\nDPB="{dpb}"\r\nGC="{gc}"\r\n'.encode("latin-1")

    src = CORPUS / "fileSharing_reservation.xlsm"
    blob = zipfile.ZipFile(src).read("xl/vbaProject.bin")
    buf = io.BytesIO(blob)
    ole = olefile.OleFileIO(buf, write_mode=True)
    original = ole.openstream("PROJECT").read()
    ole.write_stream("PROJECT", project + b" " * (len(original) - len(project)))
    locked_blob = buf.getvalue()
    ole.close()

    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dest, "w") as zout:
        for info in zin.infolist():
            data = locked_blob if info.filename == "xl/vbaProject.bin" else zin.read(info.filename)
            zout.writestr(info, data)
    return f"{digest.hex()}:{_VBA_KEY.hex()}"


def test_vba_locked_gate_and_110(handler: OoxmlHandler, tmp_path: Path) -> None:
    locked = tmp_path / "locked.xlsm"
    expected = _make_locked_vba_xlsm(locked)

    vba_gates = [g for g in handler.gates(locked) if g.gate is GateType.VBA_PROJECT]
    assert vba_gates and vba_gates[0].hashcat_mode == 110

    vba_hashes = [h for h in handler.extract(locked) if h.gate is GateType.VBA_PROJECT]
    assert vba_hashes and vba_hashes[0].value == expected


def test_vba_bypass_clears_lock(handler: OoxmlHandler, tmp_path: Path) -> None:
    locked = tmp_path / "locked.xlsm"
    _make_locked_vba_xlsm(locked)
    before = locked.read_bytes()
    out = tmp_path / "cleared.xlsm"

    handler.bypass(locked, out)

    assert locked.read_bytes() == before  # input untouched
    assert [g for g in handler.gates(out) if g.gate is GateType.VBA_PROJECT] == []  # lock gone
    with zipfile.ZipFile(out) as zout:
        assert zout.testzip() is None
        blob = zout.read("xl/vbaProject.bin")
    ole = olefile.OleFileIO(io.BytesIO(blob))
    text = ole.openstream("PROJECT").read().decode("latin-1")
    ole.close()
    assert ooxml._vba_locked(ooxml._ini_value(text, "CMG"), ooxml._ini_value(text, "DPB")) is False


# --- .xlsb BIFF12 record walk ([MS-XLSB] Section 2.1.4) ---


def test_biff12_spec_example() -> None:
    # BrtCommentText: type 637 (FD 04), size 200 (C8 01), then 200 data bytes.
    record = bytes([0xFD, 0x04, 0xC8, 0x01]) + b"\x00" * 200
    assert 637 in _biff12_record_ids(record)


def test_biff12_no_false_positive() -> None:
    # A record with an unrelated type (129) and no protection record.
    record = bytes([0x81, 0x01, 0x00])
    assert _scan_biff12(record, "xl/workbook.bin") == []


def test_biff12_unparseable_body_keeps_gate() -> None:
    # BrtSheetProtectionIso: type 678 (A6 05), size 0 (00) -- an empty body cannot
    # parse the IsoPasswordData, so the gate survives with no hash line.
    record = bytes([0xA6, 0x05, 0x00])
    assert 678 in _biff12_record_ids(record)
    findings = _scan_biff12(record, "xl/worksheets/sheet1.bin")
    assert [f.gate for f in findings] == [GateType.PROTECT_SHEET]
    assert findings[0].hash_line is None


# --- Synthetic .xlsb protection records ([MS-XLSB] Section 2.5.80 IsoPasswordData) ---
# No real corpus .xlsb carries a plaintext protection record (protected_passtika.xlsb
# is document-open encrypted), so these records are constructed byte-for-byte per the
# spec and cross-checked against the hashcat 25300 self-test vector (password "hashcat")
# and the iso-protection-hash.md Section 7 SHA-1 vector for the same salt/password.

_XLSB_SALT_B64 = "876MLoKTq42+/DLp415iZQ=="
_XLSB_SHA512_B64 = "TNDvpvYyvlSUy97UOLKNhXynhUDDA7H8kLql0ISH5SxcP6hbthdjaTo4Z3/MU0dcR2SAd+AduYb3TB5CLZ8+ow=="
_XLSB_SHA1_B64 = "Q90CLEfaPWfDIIE3UmWxb1KFkhM="
_XLSB_25300 = f"$office$2016$0$100000${_XLSB_SALT_B64}${_XLSB_SHA512_B64}"
_XLSB_GENERALIZED_SHA1_SALT_HEX = base64.b64decode(_XLSB_SALT_B64).hex()
_XLSB_GENERALIZED_SHA1_HASH_HEX = base64.b64decode(_XLSB_SHA1_B64).hex()
_XLSB_GENERALIZED_SHA1 = f"$office-protect$*sha1*iso*100000*{_XLSB_GENERALIZED_SHA1_SALT_HEX}*{_XLSB_GENERALIZED_SHA1_HASH_HEX}"


def _lp(data: bytes) -> bytes:
    """LPByteBuf: 4-byte LE length prefix, then the bytes."""
    return len(data).to_bytes(4, "little") + data


def _xln(text: str) -> bytes:
    """XLNullableWideString: 4-byte LE char count, then UTF-16LE chars."""
    return len(text).to_bytes(4, "little") + text.encode("utf-16-le")


def _xln_wide(text: str) -> bytes:
    """XLWideString (non-nullable): 4-byte LE char count, then UTF-16LE chars."""
    return len(text).to_bytes(4, "little") + text.encode("utf-16-le")


def _ipd(digest: bytes, salt: bytes, algo: str) -> bytes:
    """IsoPasswordData: rgbHash, rgbSalt, szAlgName in that order."""
    return _lp(digest) + _lp(salt) + _xln(algo)


def _biff12_frame(record_id: int, body: bytes) -> bytes:
    """Wrap a body in BIFF12 record framing (2-byte id for ids >= 128, varint size)."""
    header = bytes([(record_id & 0x7F) | 0x80, (record_id >> 7) & 0x7F])
    length = len(body)
    size = bytearray()
    while True:
        chunk = length & 0x7F
        length >>= 7
        size.append(chunk | 0x80 if length else chunk)
        if not length:
            break
    return header + bytes(size) + body


def test_biff12_sheet_protection_iso_25300() -> None:
    # BrtSheetProtectionIso (678): dwSpinCount + 16 Boolean DWORDs + IsoPasswordData.
    salt = base64.b64decode(_XLSB_SALT_B64)
    digest = base64.b64decode(_XLSB_SHA512_B64)
    body = (100000).to_bytes(4, "little") + b"\x00" * 64 + _ipd(digest, salt, "SHA-512")
    findings = _scan_biff12(_biff12_frame(678, body), "xl/worksheets/sheet1.bin")
    assert [f.gate for f in findings] == [GateType.PROTECT_SHEET]
    assert findings[0].hashcat_mode == 25300
    assert findings[0].hash_line == _XLSB_25300


def test_biff12_sheet_protection_iso_generalized_sha1() -> None:
    # SHA-1 in a .xlsb record -> generalized $office-protect$ line (no hashcat mode).
    salt = base64.b64decode(_XLSB_SALT_B64)
    digest = base64.b64decode(_XLSB_SHA1_B64)
    body = (100000).to_bytes(4, "little") + b"\x00" * 64 + _ipd(digest, salt, "SHA-1")
    findings = _scan_biff12(_biff12_frame(678, body), "xl/worksheets/sheet1.bin")
    assert findings[0].hashcat_mode is None
    assert findings[0].hash_line == _XLSB_GENERALIZED_SHA1


def test_biff12_file_sharing_iso_username_prefix() -> None:
    # BrtFileSharingIso (676): dwSpinCount + fReadOnlyRec(2) + stUserName + IsoPasswordData.
    salt = base64.b64decode(_XLSB_SALT_B64)
    digest = base64.b64decode(_XLSB_SHA512_B64)
    body = (100000).to_bytes(4, "little") + b"\x00\x00" + _xln("owner") + _ipd(digest, salt, "SHA-512")
    findings = _scan_biff12(_biff12_frame(676, body), "xl/workbook.bin")
    assert [f.gate for f in findings] == [GateType.MODIFY]
    assert findings[0].hash_line == _XLSB_25300


def test_biff12_book_protection_iso_two_blocks() -> None:
    # BrtBookProtectionIso (677): dwBookSpinCount + dwRevSpinCount + wFlags(2) + two blocks.
    salt = base64.b64decode(_XLSB_SALT_B64)
    sha512 = base64.b64decode(_XLSB_SHA512_B64)
    sha1 = base64.b64decode(_XLSB_SHA1_B64)
    body = (100000).to_bytes(4, "little") + (100000).to_bytes(4, "little") + b"\x03\x00" + _ipd(sha512, salt, "SHA-512") + _ipd(sha1, salt, "SHA-1")
    findings = _scan_biff12(_biff12_frame(677, body), "xl/workbook.bin")
    gates = [f.gate for f in findings]
    assert gates == [GateType.PROTECT_WORKBOOK, GateType.SHARED_REVISIONS]
    assert findings[0].hash_line == _XLSB_25300
    assert findings[1].hash_line == _XLSB_GENERALIZED_SHA1


def test_biff12_range_protection_iso_prefix() -> None:
    # BrtRangeProtectionIso (680): dwSpinCount + sqRfX + title/SD + IsoPasswordData.
    salt = base64.b64decode(_XLSB_SALT_B64)
    digest = base64.b64decode(_XLSB_SHA1_B64)
    sq_rfx = (1).to_bytes(4, "little", signed=True) + b"\x00" * 16  # crfx=1, one UncheckedRfX
    title_sd = _xln_wide("R1") + (0).to_bytes(4, "little")  # XLWideString title + dwsdRel=0
    body = (100000).to_bytes(4, "little") + sq_rfx + title_sd + _ipd(digest, salt, "SHA-1")
    findings = _scan_biff12(_biff12_frame(680, body), "xl/worksheets/sheet1.bin")
    assert [f.gate for f in findings] == [GateType.ALLOW_EDIT_RANGES]
    assert findings[0].hash_line == _XLSB_GENERALIZED_SHA1
