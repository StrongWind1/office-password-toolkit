"""Tests for the Outlook PST handler.

The corpus has NO ``.pst``/``.ost`` sample (see ``tests/corpus/MANIFEST.md``), so
these tests drive the handler over minimal *synthetic* NDB files that we build
here byte-for-byte to match [MS-PST]. We build BOTH dialects -- Unicode (Outlook
2003+, 64-bit BIDs) and ANSI (Outlook 97-2002, 32-bit BIDs) -- each with an
"!BDN" header carrying a ``bCryptMethod`` byte, a node BTree with a single
NID_MESSAGE_STORE leaf, a block BTree pointing at one data block, and a
Property-Context heap in that block carrying ``PidTagPstPassword`` (0x67FF0003) =
CRC-32 of a password. This exercises the full walk (header -> ROOT -> NBT -> BBT
-> block -> HN -> BTH -> property) that a real PST would need, without shipping a
proprietary sample file. Everything here is therefore synthetic-only.
"""

from __future__ import annotations

import struct
from pathlib import Path

import pytest

from office_password_toolkit.crypto import pst
from office_password_toolkit.formats.base import HandlerNotImplementedError
from office_password_toolkit.formats.outlook import OutlookHandler
from office_password_toolkit.models import GateType, RecoveryClass

# --- Synthetic NDB layout (all offsets are [MS-PST] Section 2.2.2.* driven) ---

_UNI_HEADER_LEN = 564
_ANSI_HEADER_LEN = 512
_NBT_IB = 0x400
_BBT_IB = 0x600
_BLOCK_IB = 0x800
_BID = 4  # data block BID (low bits clear: reserved=0, internal=0)

_CRYPT_NONE = 0x00
_CRYPT_PERMUTE = 0x01
_CRYPT_CYCLIC = 0x02
_CRYPT_EDP = 0x10

_PC_LEN = 38  # decoded Property-Context heap length


def _decoded_pc(crc_value: int) -> bytes:
    """Decoded Property-Context heap carrying PidTagPstPassword = crc_value.

    The Heap-on-Node / LTP layout is identical for ANSI and Unicode (HIDs are
    always 4 bytes), so one builder serves both dialects.
    """
    buf = bytearray(_PC_LEN)
    # HNHDR: ibHnpm, bSig=0xEC, bClientSig=0xBC (PC), hidUserRoot=0x20, fill=0.
    struct.pack_into("<H", buf, 0, 28)
    buf[2] = 0xEC
    buf[3] = 0xBC
    struct.pack_into("<I", buf, 4, 0x20)  # HID -> allocation #1
    # Allocation #1 [12:20] -- BTHHEADER: bType=0xB5, cbKey=2, cbEnt=8, levels=0.
    buf[12] = 0xB5
    buf[13] = 2
    buf[14] = 8
    buf[15] = 0
    struct.pack_into("<I", buf, 16, 0x40)  # hidRoot -> allocation #2
    # Allocation #2 [20:28] -- PC record: wPropId=0x67FF, wPropType=0x0003, value.
    struct.pack_into("<H", buf, 20, 0x67FF)
    struct.pack_into("<H", buf, 22, 0x0003)
    struct.pack_into("<I", buf, 24, crc_value)
    # HNPAGEMAP at 28: cAlloc=2, cFree=0, rgibAlloc = [12, 20, 28].
    struct.pack_into("<HH", buf, 28, 2, 0)
    struct.pack_into("<HHH", buf, 32, 12, 20, 28)
    return bytes(buf)


def _encode(data: bytes, crypt: int) -> bytes:
    if crypt == _CRYPT_PERMUTE:
        return pst.permute_decode(data, encode=True)
    if crypt == _CRYPT_CYCLIC:
        return pst.cyclic_decode(data, _BID)
    return data


def _btpage(entry: bytes, entry_size: int, *, unicode: bool) -> bytes:
    """A 512-byte leaf BTPAGE holding a single entry (dialect counter offsets)."""
    page = bytearray(512)
    page[: len(entry)] = entry
    cent, cbent, clevel = (488, 490, 491) if unicode else (496, 498, 499)
    page[cent] = 1  # cEnt
    page[cent + 1] = 16  # cEntMax (arbitrary)
    page[cbent] = entry_size  # cbEnt
    page[clevel] = 0  # cLevel = leaf
    return bytes(page)


def build_pst(crypt: int, crc_value: int, *, unicode: bool = True) -> bytes:
    """Assemble a minimal valid PST (ANSI or Unicode) with the given cipher/password CRC."""
    data = _decoded_pc(crc_value)
    encoded = _encode(data, crypt)
    cb = len(data)

    if unicode:
        header = bytearray(_UNI_HEADER_LEN)
        struct.pack_into("<H", header, 0x0A, 23)  # wVer = Unicode
        header[0x200] = 0x80  # bSentinel
        header[0x201] = crypt  # bCryptMethod
        struct.pack_into("<Q", header, 0x00E0, _NBT_IB)  # ROOT BREFNBT.ib
        struct.pack_into("<Q", header, 0x00F0, _BBT_IB)  # ROOT BREFBBT.ib
        nbtentry = struct.pack("<QQQII", 0x21, _BID, 0, 0, 0)  # nid,bidData,bidSub,nidParent,pad
        nbt_page = _btpage(nbtentry, 32, unicode=True)
        bbtentry = struct.pack("<QQHHI", _BID, _BLOCK_IB, cb, 1, 0)  # BREF,cb,cRef,pad
        bbt_page = _btpage(bbtentry, 24, unicode=True)
    else:
        header = bytearray(_ANSI_HEADER_LEN)
        struct.pack_into("<H", header, 0x0A, 14)  # wVer = ANSI
        header[0x1CC] = 0x80  # bSentinel
        header[0x1CD] = crypt  # bCryptMethod
        struct.pack_into("<I", header, 0x00BC, _NBT_IB)  # ROOT BREFNBT.ib
        struct.pack_into("<I", header, 0x00C4, _BBT_IB)  # ROOT BREFBBT.ib
        nbtentry = struct.pack("<IIII", 0x21, _BID, 0, 0)  # nid,bidData,bidSub,nidParent
        nbt_page = _btpage(nbtentry, 16, unicode=False)
        bbtentry = struct.pack("<IIHH", _BID, _BLOCK_IB, cb, 1)  # BREF,cb,cRef
        bbt_page = _btpage(bbtentry, 12, unicode=False)
    header[0:4] = b"!BDN"

    # Data block: encoded data + padding + BLOCKTRAILER, 64-byte aligned. The
    # trailer field order differs by dialect ([MS-PST] Section 2.2.2.8.1).
    block = bytearray(64)
    block[:cb] = encoded
    if unicode:
        struct.pack_into("<H", block, 48, cb)  # trailer.cb
        struct.pack_into("<H", block, 50, 0)  # trailer.wSig
        struct.pack_into("<I", block, 52, pst.pst_crc32(encoded))  # trailer.dwCRC
        struct.pack_into("<Q", block, 56, _BID)  # trailer.bid
    else:
        struct.pack_into("<H", block, 52, cb)  # trailer.cb
        struct.pack_into("<H", block, 54, 0)  # trailer.wSig
        struct.pack_into("<I", block, 56, _BID)  # trailer.bid (ANSI precedes dwCRC)
        struct.pack_into("<I", block, 60, pst.pst_crc32(encoded))  # trailer.dwCRC

    out = bytearray(_BLOCK_IB + 64)
    out[0 : len(header)] = header
    out[_NBT_IB : _NBT_IB + 512] = nbt_page
    out[_BBT_IB : _BBT_IB + 512] = bbt_page
    out[_BLOCK_IB : _BLOCK_IB + 64] = block
    return bytes(out)


def _read_stored_crc(raw: bytes, crypt: int) -> int:
    """Decode the message-store block back out and read the stored CRC DWORD."""
    encoded = raw[_BLOCK_IB : _BLOCK_IB + _PC_LEN]
    if crypt == _CRYPT_PERMUTE:
        decoded = pst.permute_decode(encoded)
    elif crypt == _CRYPT_CYCLIC:
        decoded = pst.cyclic_decode(encoded, _BID)
    else:
        decoded = encoded
    return struct.unpack_from("<I", decoded, 24)[0]


def _trailer_crc(raw: bytes, *, unicode: bool) -> int:
    """Read the block-trailer dwCRC from the built block (dialect offset)."""
    offset = _BLOCK_IB + (52 if unicode else 60)
    return struct.unpack_from("<I", raw, offset)[0]


# --- Cipher primitives ----------------------------------------------------


def test_permute_round_trips() -> None:
    blob = bytes(range(256)) * 3
    assert pst.permute_decode(pst.permute_decode(blob, encode=True)) == blob


def test_cyclic_round_trips() -> None:
    blob = bytes(range(256)) * 3
    assert pst.cyclic_decode(pst.cyclic_decode(blob, _BID), _BID) == blob


# --- is_encrypted / gates -------------------------------------------------


def test_is_encrypted_always_false(tmp_path: Path) -> None:
    path = tmp_path / "sample.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, pst.password_crc(b"secret")))
    assert OutlookHandler().is_encrypted(path) is False


def test_gates_permute_with_password(tmp_path: Path) -> None:
    path = tmp_path / "sample.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, pst.password_crc(b"secret")))
    gates = OutlookHandler().gates(path)
    by_type = {g.gate: g for g in gates}
    assert by_type.keys() == {GateType.MAIL_BODY, GateType.OPEN}
    assert by_type[GateType.MAIL_BODY].recovery is RecoveryClass.DECODE
    assert "NDB_CRYPT_PERMUTE" in by_type[GateType.MAIL_BODY].note
    assert "0x0201" in by_type[GateType.MAIL_BODY].where  # Unicode crypt offset
    assert by_type[GateType.OPEN].recovery is RecoveryClass.STRIP


def test_gates_cyclic_cipher_name(tmp_path: Path) -> None:
    path = tmp_path / "cyclic.pst"
    path.write_bytes(build_pst(_CRYPT_CYCLIC, pst.password_crc(b"hunter2")))
    gates = {g.gate: g for g in OutlookHandler().gates(path)}
    assert "NDB_CRYPT_CYCLIC" in gates[GateType.MAIL_BODY].note
    assert GateType.OPEN in gates


def test_gates_no_password(tmp_path: Path) -> None:
    path = tmp_path / "nopass.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, 0))
    gates = {g.gate for g in OutlookHandler().gates(path)}
    assert gates == {GateType.MAIL_BODY}  # zero CRC => no OPEN gate


def test_gates_edp_is_none(tmp_path: Path) -> None:
    path = tmp_path / "edp.pst"
    path.write_bytes(build_pst(_CRYPT_EDP, pst.password_crc(b"secret")))
    gates = {g.gate: g for g in OutlookHandler().gates(path)}
    assert gates[GateType.MAIL_BODY].recovery is RecoveryClass.NONE
    assert GateType.OPEN not in gates  # EDP block cannot be decoded to find it


def test_gates_ansi_with_password(tmp_path: Path) -> None:
    path = tmp_path / "ansi.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, pst.password_crc(b"secret"), unicode=False))
    by_type = {g.gate: g for g in OutlookHandler().gates(path)}
    assert by_type.keys() == {GateType.MAIL_BODY, GateType.OPEN}
    assert "NDB_CRYPT_PERMUTE" in by_type[GateType.MAIL_BODY].note
    assert "0x01CD" in by_type[GateType.MAIL_BODY].where  # ANSI crypt offset
    assert by_type[GateType.OPEN].recovery is RecoveryClass.STRIP


def test_gates_ansi_cyclic(tmp_path: Path) -> None:
    path = tmp_path / "ansi_cyclic.pst"
    path.write_bytes(build_pst(_CRYPT_CYCLIC, pst.password_crc(b"secret"), unicode=False))
    gates = {g.gate: g for g in OutlookHandler().gates(path)}
    assert "NDB_CRYPT_CYCLIC" in gates[GateType.MAIL_BODY].note
    assert GateType.OPEN in gates


# --- extract ($pst$ line) -------------------------------------------------


def test_extract_returns_empty_for_pst(tmp_path: Path) -> None:
    """PST CRC-32 is not crackable -- extract() returns nothing, gates() reports the OPEN gate."""
    crc = pst.password_crc(b"secret")
    path = tmp_path / "sample.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, crc))
    assert OutlookHandler().extract(path) == []
    gates = OutlookHandler().gates(path)
    assert any(g.gate is GateType.OPEN and g.recovery is RecoveryClass.STRIP for g in gates)


def test_extract_returns_empty_for_pst_ansi(tmp_path: Path) -> None:
    """Same as above for ANSI PST dialect."""
    crc = pst.password_crc(b"secret")
    path = tmp_path / "ansi.pst"
    path.write_bytes(build_pst(_CRYPT_CYCLIC, crc, unicode=False))
    assert OutlookHandler().extract(path) == []


def test_extract_empty_without_password(tmp_path: Path) -> None:
    path = tmp_path / "nopass.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, 0))
    assert OutlookHandler().extract(path) == []


def test_extract_empty_for_edp(tmp_path: Path) -> None:
    path = tmp_path / "edp.pst"
    path.write_bytes(build_pst(_CRYPT_EDP, pst.password_crc(b"secret")))
    assert OutlookHandler().extract(path) == []


# --- bypass (STRIP) -------------------------------------------------------


def test_bypass_zeros_password_and_leaves_input_untouched(tmp_path: Path) -> None:
    crypt = _CRYPT_PERMUTE
    path = tmp_path / "sample.pst"
    out = tmp_path / "stripped.pst"
    original = build_pst(crypt, pst.password_crc(b"secret"))
    path.write_bytes(original)

    OutlookHandler().bypass(path, out)

    # The input file is byte-for-byte unchanged.
    assert path.read_bytes() == original
    stripped = out.read_bytes()
    # The stored CRC is now zero and the block trailer CRC still validates.
    assert _read_stored_crc(stripped, crypt) == 0
    encoded = stripped[_BLOCK_IB : _BLOCK_IB + _PC_LEN]
    assert _trailer_crc(stripped, unicode=True) == pst.pst_crc32(encoded)
    # And the OPEN gate is gone from the stripped copy.
    assert GateType.OPEN not in {g.gate for g in OutlookHandler().gates(out)}


def test_bypass_cyclic(tmp_path: Path) -> None:
    crypt = _CRYPT_CYCLIC
    path = tmp_path / "cyclic.pst"
    out = tmp_path / "cyclic_stripped.pst"
    path.write_bytes(build_pst(crypt, pst.password_crc(b"secret")))
    OutlookHandler().bypass(path, out)
    assert _read_stored_crc(out.read_bytes(), crypt) == 0


def test_bypass_ansi(tmp_path: Path) -> None:
    crypt = _CRYPT_PERMUTE
    path = tmp_path / "ansi.pst"
    out = tmp_path / "ansi_stripped.pst"
    original = build_pst(crypt, pst.password_crc(b"secret"), unicode=False)
    path.write_bytes(original)

    OutlookHandler().bypass(path, out)

    assert path.read_bytes() == original  # input untouched
    stripped = out.read_bytes()
    assert _read_stored_crc(stripped, crypt) == 0
    # The ANSI block-trailer dwCRC (offset 60) is repaired over the re-encoded data.
    encoded = stripped[_BLOCK_IB : _BLOCK_IB + _PC_LEN]
    assert _trailer_crc(stripped, unicode=False) == pst.pst_crc32(encoded)
    assert GateType.OPEN not in {g.gate for g in OutlookHandler().gates(out)}


def test_bypass_ansi_cyclic(tmp_path: Path) -> None:
    path = tmp_path / "ansi_cyclic.pst"
    out = tmp_path / "ansi_cyclic_stripped.pst"
    path.write_bytes(build_pst(_CRYPT_CYCLIC, pst.password_crc(b"secret"), unicode=False))
    OutlookHandler().bypass(path, out)
    assert _read_stored_crc(out.read_bytes(), _CRYPT_CYCLIC) == 0


def test_bypass_edp_raises(tmp_path: Path) -> None:
    path = tmp_path / "edp.pst"
    out = tmp_path / "edp_out.pst"
    path.write_bytes(build_pst(_CRYPT_EDP, pst.password_crc(b"secret")))
    with pytest.raises(HandlerNotImplementedError):
        OutlookHandler().bypass(path, out)


def test_bypass_refuses_same_path(tmp_path: Path) -> None:
    path = tmp_path / "sample.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, pst.password_crc(b"secret")))
    with pytest.raises(ValueError, match="differ"):
        OutlookHandler().bypass(path, path)


# --- decode_body (DECODE) -------------------------------------------------


def test_decode_body_permute_unicode(tmp_path: Path) -> None:
    crc = pst.password_crc(b"secret")
    path = tmp_path / "sample.pst"
    out = tmp_path / "decoded.pst"
    original = build_pst(_CRYPT_PERMUTE, crc)
    path.write_bytes(original)

    OutlookHandler().decode_body(path, out)

    assert path.read_bytes() == original  # input untouched
    decoded = out.read_bytes()
    # bCryptMethod is now NDB_CRYPT_NONE, so the block data is stored in the clear.
    assert decoded[0x201] == _CRYPT_NONE
    assert decoded[_BLOCK_IB : _BLOCK_IB + _PC_LEN] == _decoded_pc(crc)
    # The trailer CRC now validates over the plaintext bytes.
    plain = decoded[_BLOCK_IB : _BLOCK_IB + _PC_LEN]
    assert _trailer_crc(decoded, unicode=True) == pst.pst_crc32(plain)
    # A reader now sees NONE for the body and the password CRC is still present.
    gates = {g.gate: g for g in OutlookHandler().gates(out)}
    assert gates[GateType.MAIL_BODY].recovery is RecoveryClass.DECODE
    assert "plaintext" in gates[GateType.MAIL_BODY].note
    assert GateType.OPEN in gates


def test_decode_body_cyclic_ansi(tmp_path: Path) -> None:
    crc = pst.password_crc(b"secret")
    path = tmp_path / "ansi.pst"
    out = tmp_path / "ansi_decoded.pst"
    path.write_bytes(build_pst(_CRYPT_CYCLIC, crc, unicode=False))

    OutlookHandler().decode_body(path, out)

    decoded = out.read_bytes()
    assert decoded[0x1CD] == _CRYPT_NONE
    assert decoded[_BLOCK_IB : _BLOCK_IB + _PC_LEN] == _decoded_pc(crc)
    plain = decoded[_BLOCK_IB : _BLOCK_IB + _PC_LEN]
    assert _trailer_crc(decoded, unicode=False) == pst.pst_crc32(plain)


def test_decode_body_permute_ansi(tmp_path: Path) -> None:
    crc = pst.password_crc(b"secret")
    path = tmp_path / "ansi.pst"
    out = tmp_path / "ansi_decoded.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, crc, unicode=False))
    OutlookHandler().decode_body(path, out)
    decoded = out.read_bytes()
    assert decoded[0x1CD] == _CRYPT_NONE
    assert decoded[_BLOCK_IB : _BLOCK_IB + _PC_LEN] == _decoded_pc(crc)


def test_decode_body_raises_on_plaintext(tmp_path: Path) -> None:
    # Nothing to decode -> the operation must fail honestly, not copy unchanged.
    path = tmp_path / "plain.pst"
    out = tmp_path / "plain_out.pst"
    path.write_bytes(build_pst(_CRYPT_NONE, pst.password_crc(b"secret")))
    with pytest.raises(HandlerNotImplementedError):
        OutlookHandler().decode_body(path, out)
    assert not out.exists()


def test_decode_body_raises_on_edp(tmp_path: Path) -> None:
    path = tmp_path / "edp.pst"
    out = tmp_path / "edp_out.pst"
    path.write_bytes(build_pst(_CRYPT_EDP, pst.password_crc(b"secret")))
    with pytest.raises(HandlerNotImplementedError):
        OutlookHandler().decode_body(path, out)
    assert not out.exists()


def test_decode_body_refuses_same_path(tmp_path: Path) -> None:
    path = tmp_path / "sample.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, pst.password_crc(b"secret")))
    with pytest.raises(ValueError, match="differ"):
        OutlookHandler().decode_body(path, path)


def test_decode_then_strip_round_trip(tmp_path: Path) -> None:
    # DECODE to plaintext, then STRIP the (now plaintext) password on the copy.
    crc = pst.password_crc(b"secret")
    path = tmp_path / "sample.pst"
    decoded_path = tmp_path / "decoded.pst"
    stripped = tmp_path / "stripped.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, crc))

    OutlookHandler().decode_body(path, decoded_path)
    OutlookHandler().bypass(decoded_path, stripped)

    result = stripped.read_bytes()
    assert result[0x201] == _CRYPT_NONE
    assert _read_stored_crc(result, _CRYPT_NONE) == 0
    assert GateType.OPEN not in {g.gate for g in OutlookHandler().gates(stripped)}


# --- decrypt --------------------------------------------------------------


def test_decrypt_raises(tmp_path: Path) -> None:
    path = tmp_path / "sample.pst"
    out = tmp_path / "out.pst"
    path.write_bytes(build_pst(_CRYPT_PERMUTE, pst.password_crc(b"secret")))
    with pytest.raises(HandlerNotImplementedError):
        OutlookHandler().decrypt(path, out, "secret")
