"""Round-2 gap tests for the OLE handler and XOR primitives.

Grouped by the audited gap each test closes. Where a real corpus file exists the test
is driven by it and cross-checked against msoffcrypto-tool at development time (the
expected bytes are baked here so the suite is self-contained). Where no real sample
exists the fixture is a synthetic-but-spec-valid structure built to the [MS-*] byte
layout, exercised through the same production parser a real file would hit.
"""

from __future__ import annotations

import hashlib
import io
import struct
import zipfile
from pathlib import Path

import olefile
import pytest

from office_password_toolkit.crypto import ecma376, vba
from office_password_toolkit.crypto import xor as xormod
from office_password_toolkit.formats import ole as O
from office_password_toolkit.formats.ole import OleHandler
from office_password_toolkit.models import GateType

CORPUS = Path(__file__).parent / "corpus" / "encrypted"
# Borrowed files promoted to first-party corpus.
HANDLER = OleHandler()


def _corpus(name: str) -> Path:
    # First-party corpus first, archived borrowed corpus as fallback (keeps the
    # suite green until office-corpus-gen fills the primary tree).
    for base in (CORPUS,):
        path = base / name
        if path.exists():
            return path
    pytest.skip(f"corpus file missing: {name}")


def _workbook_bytes(path: Path) -> bytes:
    ole = olefile.OleFileIO(str(path))
    name = "Workbook" if ole.exists("Workbook") else "Book"
    data = ole.openstream(name).read()
    ole.close()
    return data


def test_xor_extract_returns_empty() -> None:
    """XOR verifiers are not crackable -- extract() returns nothing, gates() reports DECODE."""
    path = _corpus("xor-encryption-abc.xls")
    assert HANDLER.extract(path) == []
    gates = HANDLER.gates(path)
    from office_password_toolkit.models import GateType, RecoveryClass

    assert any(g.gate is GateType.OPEN and g.recovery is RecoveryClass.DECODE for g in gates)


# --- Item 1: XOR "password to open" DECODE (decrypt) ---------------------------

# sha256 of the correctly decoded Workbook stream, cross-checked byte-for-byte against
# `msoffcrypto-tool xor-encryption-abc.xls out -p abc` at development time.
_ABC_DECODED_WORKBOOK_SHA256 = "37f88cd9ec3c3ce8119e8d99222f65ba2282bff4ed3a8123f03c7cf0e01db5b9"


def test_xls_xor_decrypt_matches_msoffcrypto(tmp_path: Path) -> None:
    src = _corpus("xor-encryption-abc.xls")
    out = tmp_path / "decoded.xls"
    HANDLER.decrypt(src, out, "abc")
    assert olefile.isOleFile(str(out))
    assert hashlib.sha256(_workbook_bytes(out)).hexdigest() == _ABC_DECODED_WORKBOOK_SHA256
    assert HANDLER.is_encrypted(out) is False


def test_xls_xor_decrypt_wrong_password_raises(tmp_path: Path) -> None:
    src = _corpus("xor-encryption-abc.xls")
    with pytest.raises(ValueError, match="incorrect password"):
        HANDLER.decrypt(src, tmp_path / "x.xls", "not-the-password")


def test_doc_method2_transform_round_trips() -> None:
    # No .doc XOR sample exists in the corpus, so exercise the Method 2 (Word) transform
    # and 32-bit verifier the decrypt path relies on (self-inverse, first 68 bytes kept).
    array = xormod.create_xor_array_method1("secret")
    body = bytes(range(256)) * 2
    once = xormod.xor_transform_method2(body, array, 68)
    assert xormod.xor_transform_method2(once, array, 68) == body
    assert O._doc_xor_password_ok("secret", xormod.password_verifier_method2("secret")) is True
    assert O._doc_xor_password_ok("wrong", xormod.password_verifier_method2("secret")) is False


# --- Item 2: bypass must decode-then-strip, never no-op --------------------------


@pytest.mark.parametrize("name", ["xor-encryption-abc.xls", "xor_password_123456789012345.xls"])
def test_xor_bypass_changes_file_and_removes_protection(tmp_path: Path, name: str) -> None:
    src = _corpus(name)
    before = hashlib.sha256(src.read_bytes()).hexdigest()
    out = tmp_path / "bypassed.xls"
    HANDLER.bypass(src, out)
    # Output is a valid OLE, actually differs from the input, and the input is untouched.
    assert olefile.isOleFile(str(out))
    assert _workbook_bytes(out) != _workbook_bytes(src)
    assert hashlib.sha256(src.read_bytes()).hexdigest() == before
    # The XOR "password to open" protection is gone (FilePass neutralised).
    assert HANDLER.is_encrypted(out) is False
    assert not HANDLER.gates(out)


def test_reconstruct_password_is_verifier_validated() -> None:
    # Password-free reconstruction with NOTHING known must still recover a short password
    # via the pad bytes + brute, proven by the 32-bit XorKey+verifier match.
    key = xormod.create_xor_key_method1("ab")
    verifier = xormod.password_verifier_method1("ab")
    recovered = xormod.reconstruct_password(key, verifier, [None] * 16, max_brute=2)
    assert recovered is not None
    assert xormod.create_xor_array_method1(recovered) == xormod.create_xor_array_method1("ab")


# --- Item 4: BOF.dt routes protect-WORKBOOK vs protect-SHEET --------------------


def _biff_record(rt: int, body: bytes) -> bytes:
    return struct.pack("<HH", rt, len(body)) + body


def _biff_bof(dt: int) -> bytes:
    return _biff_record(0x0809, struct.pack("<HH", 0x0600, dt) + bytes(12))


def test_password_record_routed_by_bof_dt() -> None:
    workbook = (
        _biff_bof(0x0005)  # globals substream
        + _biff_record(0x0013, struct.pack("<H", 0x1234))
        + _biff_record(0x000A, b"")  # EOF
        + _biff_bof(0x0010)  # worksheet substream
        + _biff_record(0x0013, struct.pack("<H", 0x5678))
        + _biff_record(0x000A, b"")
    )
    gates = {r.gate: r.verifier for r in O._xls_protection_records(workbook)}
    assert gates[GateType.PROTECT_WORKBOOK] == 0x1234
    assert gates[GateType.PROTECT_SHEET] == 0x5678


# --- Item 7: FeatProtection allow-edit-ranges ----------------------------------


def _feat_protection_body(wpassword: int, c_ref: int = 0) -> bytes:
    """Build a Feat record body for ISFPROTECTION ([MS-XLS] Section 2.4.99 / 2.5.124).

    Layout: isf(2) + reserved1(1) + reserved2(4) + cRef(2) + Ref8[cRef] + cbFeatData(4)
    + reserved3(2) + fSD(4) + wPassword(2).
    """
    isf = struct.pack("<H", 0x0002)  # ISFPROTECTION
    reserved1 = b"\x00"
    reserved2 = b"\x00\x00\x00\x00"
    cref = struct.pack("<H", c_ref)
    refs = b"\x00" * (8 * c_ref)  # each Ref8 is 8 bytes
    cb_feat_data = struct.pack("<I", 6)  # fSD(4) + wPassword(2) = 6
    reserved3 = b"\x00\x00"
    fsd = struct.pack("<I", 0)
    wpass = struct.pack("<H", wpassword)
    return isf + reserved1 + reserved2 + cref + refs + cb_feat_data + reserved3 + fsd + wpass


def test_featprotection_allow_edit_ranges_enumerated_and_stripped() -> None:
    body = _feat_protection_body(0xABCD)
    workbook = _biff_bof(0x0005) + _biff_record(0x0867, body) + _biff_record(0x000A, b"")
    records = O._xls_protection_records(workbook)
    assert [r.gate for r in records] == [GateType.ALLOW_EDIT_RANGES]
    assert records[0].verifier == 0xABCD
    stripped = O._strip_xls_verifiers(workbook)
    assert stripped is not None
    assert not O._xls_protection_records(stripped)  # verifier zeroed -> no longer a gate


def test_featprotection_with_refs() -> None:
    body = _feat_protection_body(0x9999, c_ref=2)
    workbook = _biff_bof(0x0005) + _biff_record(0x0867, body) + _biff_record(0x000A, b"")
    records = O._xls_protection_records(workbook)
    assert len(records) == 1
    assert records[0].verifier == 0x9999


def test_featprotection_non_protection_isf_ignored() -> None:
    body = struct.pack("<H", 0x0003) + b"\x00" * 20  # isf=3 (not ISFPROTECTION)
    workbook = _biff_bof(0x0005) + _biff_record(0x0867, body) + _biff_record(0x000A, b"")
    assert not O._xls_protection_records(workbook)


def test_filesharing_verifier_read_at_offset_two() -> None:
    # excel.md: FileSharing wResPass is at body+2 (not body+0).
    body = struct.pack("<HH", 0x0000, 0x4321)  # fReadOnlyRec, then wResPass
    workbook = _biff_bof(0x0005) + _biff_record(0x005B, body) + _biff_record(0x000A, b"")
    records = O._xls_protection_records(workbook)
    assert records[0].gate is GateType.MODIFY
    assert records[0].verifier == 0x4321


# --- Item 6: non-default agile tuple emits the generalized $office-open$ line ---


def _agile_info(hash_algorithm: str, key_bits: int) -> ecma376.EncryptionInfo:
    return ecma376.EncryptionInfo(
        kind=ecma376.EncryptionKind.AGILE,
        version_major=4,
        version_minor=4,
        salt=bytes(16),
        key_bits=key_bits,
        spin_count=100000,
        hash_algorithm=hash_algorithm,
        cipher_algorithm="AES",
        cipher_chaining="ChainingModeCBC",
        block_size=16,
        hash_size=48,
        enc_verifier=bytes(16),
        enc_verifier_hash=bytes(64),
    )


def test_non_default_agile_tuple_uses_unified_line() -> None:
    """A non-default agile tuple (not 9500/9600) emits the unified $office-open$ line."""
    info = _agile_info("SHA384", 192)
    assert O._modern_scheme(info) == (None, None)
    line = ecma376.unified_office_line(info)
    assert line.startswith("$office-open$*sha384*aes192*cbc*")


# --- Item 8: .doc restrict-editing (Dop) ---------------------------------------


def _word_fib_with_table(dop: bytes, sttb: bytes) -> tuple[bytes, bytes]:
    """Build a WordDocument FIB whose FibRgFcLcb points at a synthetic Table stream."""
    table = dop + sttb
    fib = bytearray()
    fib += struct.pack("<H", 0xA5EC) + bytes(30)  # FibBase
    csw = 14
    fib += struct.pack("<H", csw) + bytes(csw * 2)
    cslw = 22
    fib += struct.pack("<H", cslw) + bytes(cslw * 4)
    cb = 93
    fib += struct.pack("<H", cb)
    blob = bytearray(cb * 8)
    struct.pack_into("<II", blob, 31 * 8, 0, len(dop))  # fcDop / lcbDop
    struct.pack_into("<II", blob, 32 * 8, len(dop), len(sttb))  # fcSttbfAssoc / lcb
    fib += blob
    return bytes(fib), table


def _dop(flags2: int, l_key: int) -> bytes:
    dop = bytearray(84)
    struct.pack_into("<I", dop, 4, flags2)
    struct.pack_into("<I", dop, 80, l_key)
    return bytes(dop)


def test_dop_restrict_edit_parsed_and_stripped() -> None:
    flags2 = (1 << 25) | (1 << 30)  # fProtEnabled + fLockRev ([MS-DOC] Section 2.7.2)
    word_document, table = _word_fib_with_table(_dop(flags2, 0xDEADBEEF), b"")
    parsed = O._parse_dop_protection(word_document, table)
    assert parsed is not None
    assert parsed.l_key_prot_doc == 0xDEADBEEF
    assert parsed.protected is True
    stripped_table = O._strip_dop_protection(table, parsed)
    reparsed = O._parse_dop_protection(word_document, stripped_table)
    assert reparsed is not None
    assert reparsed.l_key_prot_doc == 0
    assert reparsed.protected is False


# --- Item 9: .doc write-reservation cleartext (SttbfAssoc[0x11]) ----------------


def _sttbf_assoc(entries: dict[int, str], count: int = 18) -> bytes:
    out = bytearray(struct.pack("<HHH", 0xFFFF, count, 0))
    for i in range(count):
        text = entries.get(i, "")
        encoded = text.encode("utf-16-le")
        out += struct.pack("<H", len(text)) + encoded
    return bytes(out)


def test_sttbf_assoc_write_reservation_readable() -> None:
    sttb = _sttbf_assoc({0x11: "letmein"})
    word_document, table = _word_fib_with_table(_dop(0, 0), sttb)
    assert O._sttbf_assoc_string(word_document, table, 0x11) == "letmein"


# --- Item 10: .ppt ModifyPasswordAtom (RT_CString 0x0FBA, recInstance 0x003) ----


def _ppt_rh(rec_ver: int, rec_instance: int, rec_type: int, rec_len: int) -> bytes:
    return struct.pack("<HHI", (rec_instance << 4) | rec_ver, rec_type, rec_len)


def _ppt_with_modify_password(password: str) -> bytes:
    body = password.encode("utf-16-le")
    atom = _ppt_rh(0x0, 0x003, 0x0FBA, len(body)) + body
    tag = _ppt_rh(0xF, 0x000, 0x1388, len(atom)) + atom  # a container (recVer=0xF)
    return _ppt_rh(0xF, 0x000, 0x03E8, len(tag)) + tag  # DocumentContainer-like


def test_ppt_modify_password_read_and_stripped() -> None:
    ppt = _ppt_with_modify_password("topsecret")
    found = O._ppt_find_modify_password(ppt)
    assert found is not None
    assert found.password == "topsecret"
    stripped = O._ppt_strip_modify_password(ppt, found)
    assert len(stripped) == len(ppt)  # same-size edit for the in-place writer
    after = O._ppt_find_modify_password(stripped)
    assert after is not None
    assert after.password == "\x00" * len("topsecret")  # password bytes cleared


# --- Item 3: VBA project lock strip (PROJECT stream, same-size) -----------------

# A real PROJECT stream (ID from [MS-OVBA] Section 3.1.6; DPB is the reproducible
# hash-case vector B from vba-project-password.md Section 7).
_PROJECT_STREAM = b'ID="{917DED54-440B-4FD1-A5C1-74ACF261E600}"\r\nCMG="0705D8E3D8EDDBF1DBF1DBF1DBF1"\r\nDPB="ABA907551A721A72E58E1B720BA11E90F33273CEBFD8361EBFE81C9567CBE16B5639865DDB"\r\nGC="1517CAF1D6F9D7F9D706"\r\n'


def test_vba_project_strip_is_same_size_and_clears_state() -> None:
    modified = O._clear_vba_protection(_PROJECT_STREAM)
    assert modified is not None
    # Same size so olefile.write_stream can store it in place.
    assert len(modified) == len(_PROJECT_STREAM)
    # DPB is renamed to DPx (the VBE can no longer find the password state).
    assert b'DPx="' in modified
    assert b'DPB="' not in modified
    # CMG re-encodes to a cleared protection state (no fUserProtected/fHostProtected/fVBEProtected).
    text = modified.decode("latin-1")
    cmg_hex = next(line for line in text.splitlines() if line.startswith("CMG=")).split('"')[1]
    assert vba.decode_data_encryption(cmg_hex) == b"\x00\x00\x00\x00"


def test_vba_project_strip_none_when_no_protection() -> None:
    assert O._clear_vba_protection(b'ID="{00000000-0000-0000-0000-000000000000}"\r\n') is None


# --- Guard: existing modern/RC4 decrypt still yields a valid container -----------


def test_modern_wrapper_decrypt_still_works(tmp_path: Path) -> None:
    src = _corpus("protect.xlsx")
    out = tmp_path / "plain.xlsx"
    HANDLER.decrypt(src, out, "VelvetSweatshop")
    with zipfile.ZipFile(io.BytesIO(out.read_bytes())) as archive:
        assert "[Content_Types].xml" in archive.namelist()
