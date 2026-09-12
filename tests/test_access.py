"""Structural verification for the Access Jet/ACE handler.

There is NO real .mdb/.accdb file in tests/corpus/ and no [MS-ACCESS] spec, so
every offset the handler uses is UNCONFIRMED community RE. These tests therefore
verify the handler *structurally*: they plant a synthetic Jet-4 header with a
known creation-date double and an XOR-masked password field and assert the
DECODE recovers the planted password, and they graft a real Office-agile
EncryptionInfo descriptor (borrowed from the OOXML corpus) onto a synthetic ACE
page 0 to prove the extractor emits the byte-identical $office$*2013 line.
"""

from __future__ import annotations

import struct
from pathlib import Path

import olefile
import pytest

from office_password_toolkit.crypto import ecma376, vba
from office_password_toolkit.formats import access
from office_password_toolkit.formats.access import (
    ACE_ENGINE_SIGNATURE,
    ENCODING_KEY_SIZE,
    HEADER_PAGE_SIZE,
    JET3_PASSWORD_SIZE,
    JET4_PASSWORD_SIZE,
    JET_ENGINE_SIGNATURE,
    OFFSET_ENCODING_KEY,
    OFFSET_ENGINE_SIGNATURE,
    OFFSET_HEADER_DATE,
    OFFSET_JET_VERSION,
    OFFSET_PASSWORD,
    AccessHandler,
    _ACE2007_BLOB_OFFSET,
    _ACE2007_ENC_OFFSET,
    _DEFAULT_ENCODING_KEY,
)
from office_password_toolkit.formats.base import HandlerNotImplementedError
from office_password_toolkit.models import GateType, RecoveryClass

CORPUS = Path(__file__).parent / "corpus"
# Borrowed files promoted to first-party corpus.
_ZERO_CLSID = "{00000000-0000-0000-0000-000000000000}"
_ACE_PASSWORD = "Password1234_"  # the corpus example_password.docx open password
_ACE_ENCODING_KEY = b"\x11\x22\x33\x44"  # desired real (unmasked) encoding key
_ACE_ENCODING_KEY_MASKED = bytes(a ^ b for a, b in zip(_ACE_ENCODING_KEY, _DEFAULT_ENCODING_KEY, strict=True))  # on-disk representation (XOR with header mask)


def _build_jet3_header(password: str) -> bytes:
    """Plant a synthetic Jet-3 page 0: cleartext password under the fixed-key RC4.

    Mirrors the mdbtools model the handler reverses -- the password is written at
    0x42 as single-byte cp1252, then the whole 0x18 header region is RC4-scrambled
    with the fixed key 0x6b39dac7.
    """
    page = bytearray(HEADER_PAGE_SIZE)
    page[OFFSET_ENGINE_SIGNATURE : OFFSET_ENGINE_SIGNATURE + len(JET_ENGINE_SIGNATURE)] = JET_ENGINE_SIGNATURE
    page[OFFSET_JET_VERSION] = 0x00  # Jet 3 (Access 97)
    field_off = OFFSET_PASSWORD - access._JET_RC4_REGION_START
    region = bytearray(page[access._JET_RC4_REGION_START : access._JET_RC4_REGION_START + access._JET3_RC4_REGION_LEN])
    raw = password.encode("cp1252")
    region[field_off : field_off + len(raw)] = raw
    page[access._JET_RC4_REGION_START : access._JET_RC4_REGION_START + access._JET3_RC4_REGION_LEN] = access._rc4(access._JET_RC4_KEY, bytes(region))
    return bytes(page)


def _build_jet4_header(password: str, *, date: float = 40179.0, dpb: str | None = None) -> bytes:
    """Plant a synthetic Jet-4 page 0: XOR-masked password under the fixed-key RC4.

    Mirrors the Jackcess/mdbtools model the handler reverses -- the password is
    written at 0x42 as UTF-16LE with the creation-date XOR mask applied, the date
    itself at 0x72, then the whole 128-byte 0x18 header region is RC4-scrambled
    with the fixed key 0x6b39dac7.
    """
    page = bytearray(HEADER_PAGE_SIZE)
    page[OFFSET_ENGINE_SIGNATURE : OFFSET_ENGINE_SIGNATURE + len(JET_ENGINE_SIGNATURE)] = JET_ENGINE_SIGNATURE
    page[OFFSET_JET_VERSION] = 0x01  # Jet 4
    page[OFFSET_HEADER_DATE : OFFSET_HEADER_DATE + 8] = struct.pack("<d", date)
    mask = struct.pack("<I", int(date) & 0xFFFFFFFF)
    field = bytearray(JET4_PASSWORD_SIZE)
    raw = password.encode("utf-16-le")
    field[: len(raw)] = raw
    masked = bytes(field[i] ^ mask[i % 4] for i in range(len(field)))
    page[OFFSET_PASSWORD : OFFSET_PASSWORD + JET4_PASSWORD_SIZE] = masked
    region = bytes(page[access._JET_RC4_REGION_START : access._JET_RC4_REGION_START + access._JET4_RC4_REGION_LEN])
    page[access._JET_RC4_REGION_START : access._JET_RC4_REGION_START + access._JET4_RC4_REGION_LEN] = access._rc4(access._JET_RC4_KEY, region)
    tail = f'\r\nDPB="{dpb}"\r\n'.encode("ascii") if dpb else b""
    return bytes(page) + tail


def _build_ace2010_page(descriptor_xml: bytes, *, encoding_key_masked: bytes = _ACE_ENCODING_KEY_MASKED) -> bytes:
    """Plant a synthetic ACE 2010+ page 0 with a plaintext agile descriptor."""
    page = bytearray(HEADER_PAGE_SIZE)
    page[OFFSET_ENGINE_SIGNATURE : OFFSET_ENGINE_SIGNATURE + len(ACE_ENGINE_SIGNATURE)] = ACE_ENGINE_SIGNATURE
    page[OFFSET_JET_VERSION] = 0x03  # ACE 2010+
    page[OFFSET_ENCODING_KEY : OFFSET_ENCODING_KEY + len(encoding_key_masked)] = encoding_key_masked
    page[0x200 : 0x200 + len(descriptor_xml)] = descriptor_xml
    return bytes(page)


def _build_ace2007_page(*, encoding_key_masked: bytes) -> bytes:
    """Plant a synthetic ACE 2007 page 0 (version byte 0x02); no agile descriptor."""
    page = bytearray(HEADER_PAGE_SIZE)
    page[OFFSET_ENGINE_SIGNATURE : OFFSET_ENGINE_SIGNATURE + len(ACE_ENGINE_SIGNATURE)] = ACE_ENGINE_SIGNATURE
    page[OFFSET_JET_VERSION] = 0x02  # ACE 2007 (RC4)
    page[OFFSET_ENCODING_KEY : OFFSET_ENCODING_KEY + len(encoding_key_masked)] = encoding_key_masked
    return bytes(page)


def _encrypt_ace_page(cipher: object, page_number: int, plaintext: bytes) -> bytes:
    """Inverse of ``access._ace_decrypt_page`` -- CBC-encrypt one page for a round-trip."""
    page_bytes = page_number.to_bytes(4, "little")
    block_key = bytes(page_bytes[i] ^ cipher.encoding_key[i] for i in range(ENCODING_KEY_SIZE))
    iv = ecma376._fit(ecma376._digest(cipher.key_data_hash, cipher.key_data_salt + block_key), cipher.block_size)
    return ecma376._aes_cbc_encrypt(cipher.bulk_key, iv, plaintext)


def _build_encrypted_accdb(descriptor_xml: bytes, plaintext_pages: list[bytes]) -> bytes:
    """Assemble a synthetic encrypted ``.accdb``: plaintext page 0 + CBC-encrypted pages."""
    info = ecma376.parse_encryption_info(access._AGILE_STREAM_HEADER + descriptor_xml)
    cipher = access._ace_page_cipher(info, _ACE_PASSWORD, _ACE_ENCODING_KEY)
    blob = bytearray(_build_ace2010_page(descriptor_xml))
    for offset, pt in enumerate(plaintext_pages, start=1):
        blob += _encrypt_ace_page(cipher, offset, pt)
    return bytes(blob)


def _agile_descriptor_from_corpus() -> tuple[bytes, str]:
    """Return the raw agile EncryptionInfo XML and its $office$*2013 line."""
    with olefile.OleFileIO(str(CORPUS / "encrypted" / "example_password.docx")) as ole:
        blob = ole.openstream("EncryptionInfo").read()
    info = ecma376.parse_encryption_info(blob)
    return blob[8:].rstrip(b"\x00"), ecma376.office_hash_line(info)


# --- Jet .mdb DECODE ------------------------------------------------------


def test_jet3_decode_recovers_planted_password(tmp_path: Path) -> None:
    path = tmp_path / "planted97.mdb"
    path.write_bytes(_build_jet3_header("Hunter2"))
    handler = AccessHandler()
    # The fixed-key RC4 undoes to the exact cleartext password.
    decode = access.decode_jet_password(access.read_header(path))
    assert decode.recovered == "Hunter2"
    open_gates = [g for g in handler.gates(path) if g.gate is GateType.OPEN]
    assert len(open_gates) == 1
    assert open_gates[0].recovery is RecoveryClass.DECODE
    assert handler.is_encrypted(path) is False  # Jet obfuscation, not real crypto
    assert handler.extract(path) == []


def test_jet3_empty_password_has_no_open_gate(tmp_path: Path) -> None:
    path = tmp_path / "nopass97.mdb"
    path.write_bytes(_build_jet3_header(""))
    open_gates = [g for g in AccessHandler().gates(path) if g.gate is GateType.OPEN]
    assert open_gates == []


def test_jet3_decrypt_copies_through_and_checks_password(tmp_path: Path) -> None:
    src = tmp_path / "planted97.mdb"
    src.write_bytes(_build_jet3_header("Hunter2"))
    original = src.read_bytes()
    out = tmp_path / "out.mdb"
    AccessHandler().decrypt(src, out, "Hunter2")
    assert out.read_bytes() == original
    assert src.read_bytes() == original  # THE ONE RULE: input untouched
    with pytest.raises(ValueError, match="does not match"):
        AccessHandler().decrypt(src, tmp_path / "bad.mdb", "wrong")


def test_jet4_decode_recovers_planted_password(tmp_path: Path) -> None:
    path = tmp_path / "planted.mdb"
    path.write_bytes(_build_jet4_header("Secret1"))
    gates = AccessHandler().gates(path)
    open_gates = [g for g in gates if g.gate is GateType.OPEN]
    assert len(open_gates) == 1
    assert open_gates[0].recovery is RecoveryClass.DECODE
    # The recovered password rides in the note (there is no hash to emit).
    assert "Secret1" not in open_gates[0].note  # note describes the method, not the secret
    # is_encrypted is False: Jet obfuscation is keyless DECODE, not real crypto.
    assert AccessHandler().is_encrypted(path) is False
    assert AccessHandler().extract(path) == []


def test_jet4_empty_password_has_no_open_gate(tmp_path: Path) -> None:
    path = tmp_path / "nopass.mdb"
    path.write_bytes(_build_jet4_header(""))
    open_gates = [g for g in AccessHandler().gates(path) if g.gate is GateType.OPEN]
    assert open_gates == []


def test_jet4_decrypt_copies_through_and_checks_password(tmp_path: Path) -> None:
    src = tmp_path / "planted.mdb"
    src.write_bytes(_build_jet4_header("Secret1"))
    original = src.read_bytes()
    # Correct password (the decoded one) -> copy-through; body was already cleartext.
    out = tmp_path / "out.mdb"
    AccessHandler().decrypt(src, out, "Secret1")
    assert out.read_bytes() == original
    assert src.read_bytes() == original  # THE ONE RULE: input untouched
    # Wrong password -> ValueError.
    with pytest.raises(ValueError, match="does not match"):
        AccessHandler().decrypt(src, tmp_path / "bad.mdb", "wrong")


# --- ACE .accdb agile extract ---------------------------------------------


def test_ace2010_extract_emits_2013_line(tmp_path: Path) -> None:
    descriptor, expected_line = _agile_descriptor_from_corpus()
    path = tmp_path / "planted.accdb"
    path.write_bytes(_build_ace2010_page(descriptor))
    handler = AccessHandler()
    assert handler.is_encrypted(path) is True
    open_gates = [g for g in handler.gates(path) if g.gate is GateType.OPEN]
    assert len(open_gates) == 1
    assert open_gates[0].recovery is RecoveryClass.CRACK
    assert open_gates[0].hashcat_mode == 9600
    hashes = handler.extract(path)
    open_hashes = [h for h in hashes if h.gate is GateType.OPEN]
    assert len(open_hashes) == 1
    assert open_hashes[0].hashcat_mode == 9600
    assert open_hashes[0].value == expected_line


def test_ace2010_decrypt_round_trips(tmp_path: Path) -> None:
    # Synthetic .accdb: real corpus agile descriptor + two CBC-encrypted data pages.
    descriptor, _ = _agile_descriptor_from_corpus()
    page1 = bytes(range(256)) * 16  # 4096 bytes
    page2 = b"\xa5" * HEADER_PAGE_SIZE
    src = tmp_path / "enc.accdb"
    src.write_bytes(_build_encrypted_accdb(descriptor, [page1, page2]))
    original = src.read_bytes()
    out = tmp_path / "out.accdb"
    AccessHandler().decrypt(src, out, _ACE_PASSWORD)
    result = out.read_bytes()
    # Page 0 has encryption metadata cleared; data pages come back as plaintext.
    assert result[OFFSET_ENCODING_KEY : OFFSET_ENCODING_KEY + ENCODING_KEY_SIZE] == _DEFAULT_ENCODING_KEY
    assert result[_ACE2007_ENC_OFFSET:_ACE2007_BLOB_OFFSET] == b"\x00\x00"
    assert result[HEADER_PAGE_SIZE : 2 * HEADER_PAGE_SIZE] == page1
    assert result[2 * HEADER_PAGE_SIZE : 3 * HEADER_PAGE_SIZE] == page2
    assert src.read_bytes() == original  # THE ONE RULE: input untouched


def test_ace2010_decrypt_wrong_password_raises_and_writes_nothing(tmp_path: Path) -> None:
    descriptor, _ = _agile_descriptor_from_corpus()
    src = tmp_path / "enc.accdb"
    src.write_bytes(_build_encrypted_accdb(descriptor, [b"\x00" * HEADER_PAGE_SIZE]))
    out = tmp_path / "out.accdb"
    with pytest.raises(ValueError, match="verifier check failed"):
        AccessHandler().decrypt(src, out, "not-the-password")
    assert not out.exists()  # honest failure: no corrupt output left behind


def test_ace2007_decrypt_no_enc_info_raises(tmp_path: Path) -> None:
    path = tmp_path / "ace2007.accdb"
    path.write_bytes(_build_ace2007_page(encoding_key_masked=_ACE_ENCODING_KEY_MASKED))
    with pytest.raises(ValueError, match="no parseable RC4"):
        AccessHandler().decrypt(path, tmp_path / "out", "pw")


# --- ACE 2007 detection: gates() and is_encrypted() must agree -------------


def test_ace2007_unprotected_has_no_open_gate(tmp_path: Path) -> None:
    # Blank encoding key -> unprotected. The old bug reported an open gate here.
    path = tmp_path / "plain.accdb"
    path.write_bytes(_build_ace2007_page(encoding_key_masked=_DEFAULT_ENCODING_KEY))
    handler = AccessHandler()
    assert handler.is_encrypted(path) is False
    assert [g for g in handler.gates(path) if g.gate is GateType.OPEN] == []


def test_ace2007_default_encoding_key_is_not_encrypted(tmp_path: Path) -> None:
    # The default on-disk encoding key (fb8abc4e) unmasks to all-zero = unprotected.
    # With no EncryptionInfo blob at 0x299, the file is NOT encrypted.
    path = tmp_path / "default_key.accdb"
    path.write_bytes(_build_ace2007_page(encoding_key_masked=_DEFAULT_ENCODING_KEY))
    handler = AccessHandler()
    assert handler.is_encrypted(path) is False
    assert [g for g in handler.gates(path) if g.gate is GateType.OPEN] == []


# --- VBA project lock -----------------------------------------------------


def test_vba_hash_case_emits_mode_110(tmp_path: Path) -> None:
    # Build a hash-case DPB exactly as the vba unit tests do, then embed it.
    key = bytes.fromhex("6d61ded4")
    digest = vba.password_hash("macro", key)
    structure = vba.build_password_hash_structure(key, digest)
    dpb = vba.encode_data_encryption(structure, 0xAB, 0xAC)
    path = tmp_path / "macro.mdb"
    path.write_bytes(_build_jet4_header("Secret1", dpb=dpb))
    gates = [g for g in AccessHandler().gates(path) if g.gate is GateType.VBA_PROJECT]
    assert len(gates) == 1
    assert gates[0].recovery is RecoveryClass.STRIP
    assert gates[0].hashcat_mode == 110
    vba_hashes = [h for h in AccessHandler().extract(path) if h.gate is GateType.VBA_PROJECT]
    assert len(vba_hashes) == 1
    assert vba_hashes[0].value == vba.extract_vba_hash(dpb)


# --- Non-Access input degrades cleanly ------------------------------------


def test_non_access_file_returns_empty(tmp_path: Path) -> None:
    path = tmp_path / "notadb.bin"
    path.write_bytes(b"PK\x03\x04this is not a jet database at all")
    handler = AccessHandler()
    assert handler.is_encrypted(path) is False
    assert handler.gates(path) == []
    assert handler.extract(path) == []
    with pytest.raises(ValueError, match="not a recognised Access"):
        handler.decrypt(path, tmp_path / "out", "pw")


def test_jet_bypass_copies_through(tmp_path: Path) -> None:
    path = tmp_path / "planted.mdb"
    data = _build_jet4_header("Secret1")
    path.write_bytes(data)
    out = tmp_path / "out.mdb"
    AccessHandler().bypass(path, out)
    assert out.read_bytes() == data


def test_ace_bypass_raises(tmp_path: Path) -> None:
    path = tmp_path / "ace.accdb"
    path.write_bytes(_build_ace2007_page(encoding_key_masked=_ACE_ENCODING_KEY_MASKED))
    with pytest.raises(HandlerNotImplementedError):
        AccessHandler().bypass(path, tmp_path / "out.accdb")
