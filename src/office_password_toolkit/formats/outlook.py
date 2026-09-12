# SPDX-License-Identifier: Apache-2.0
r"""Outlook handler -- ``.pst`` / ``.ost`` node-database files ([MS-PST]).

A Personal Folders file carries two entirely separate, weak protections and
**no** document-open encryption at all -- so this handler never emits a crackable
hash and :meth:`OutlookHandler.is_encrypted` always reports ``False``:

* **Open password** -- an optional, UI-only gate. [MS-PST] Section 2.4.3.3 is
  explicit that the password "is not used to secure the PST data in any way": the
  only stored material is a single CRC-32 of the password text in the tagged
  property ``PidTagPstPassword`` (``0x67FF0003``) on the message-store node
  (``NID_MESSAGE_STORE`` = ``0x0021``). A 32-bit CRC guards nothing, so the fast
  path is STRIP -- zero the DWORD and Outlook opens the store with no prompt.
* **Body cipher** -- a keyless whole-file obfuscation selected by the
  ``bCryptMethod`` header byte ([MS-PST] Section 2.2.2.6): ``NDB_CRYPT_PERMUTE``
  (Section 5.1) or ``NDB_CRYPT_CYCLIC`` (Section 5.2). Neither takes a password;
  both are pure DECODE. The only exception is ``NDB_CRYPT_EDPCRYPTED`` (``0x10``,
  enterprise EDP/WIP), which is real encryption keyed off-file -> NONE.

The actual byte plumbing (the CRC-32, the two cipher tables, the STRIP plan) lives
in the verified :mod:`~office_password_toolkit.crypto.pst` primitive; this handler
only walks the on-disk node/block BTrees ([MS-PST] Section 2.2.2.7) to reach the
message-store property context and locate the DWORD. The walk is spec-faithful for
both Unicode (Outlook 2003+) and ANSI (Outlook 97-2002) PSTs; non-trivial
shapes (data trees, EDP) raise :class:`HandlerNotImplementedError` from
:meth:`bypass` rather than risk corrupting a file we cannot round-trip.

Import rules: crypto + models + base + stdlib only -- no sibling handler, no
:mod:`~office_password_toolkit.detect`.
"""

from __future__ import annotations

import logging
import struct
from dataclasses import dataclass
from typing import TYPE_CHECKING, BinaryIO, Final

from typing_extensions import override

from office_password_toolkit.crypto import pst
from office_password_toolkit.formats.base import FormatHandler, HandlerNotImplementedError
from office_password_toolkit.models import ContainerKind, ExtractedHash, Gate, GateType, RecoveryClass

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)

# --- Header markers ([MS-PST] Section 2.2.2.6) ----------------------------

# dwMagic sentinel at offset 0; the "!BDN" tag identifies every NDB file.
_PST_MAGIC: Final = b"!BDN"

# wVer (offset 0x0A) distinguishes the two on-disk dialects: 14/15 = ANSI,
# >= 23 = Unicode. Unicode is the format Outlook 2003+ writes and the only one
# whose BTree/BREF layout this handler walks. The _NdbProfile dataclass makes
# the BTree walk dialect-agnostic, so ANSI PSTs are also walked.
_UNICODE_MIN_VER: Final = 23

# bCryptMethod byte -- version-dependent absolute offset. [MS-PST] Section
# 2.2.2.6 places it right after bSentinel (0x80): 0x0201 in the Unicode header,
# 0x01CD in the ANSI header.
_CRYPT_OFFSET_UNICODE: Final = 0x0201
_CRYPT_OFFSET_ANSI: Final = 0x01CD

# bCryptMethod values, [MS-PST] Section 2.2.2.6 (mpbCryptMethod). PERMUTE is the
# Outlook default ("compressible encryption"); EDP is the only value that means
# real, off-file encryption.
_CRYPT_NONE: Final = 0x00
_CRYPT_PERMUTE: Final = 0x01
_CRYPT_CYCLIC: Final = 0x02
_CRYPT_EDP: Final = 0x10

# The advisory PidTagPstPassword verifier has no dedicated HashScheme: it is a
# bare CRC-32 of the password with no hashcat/John mode (pst-crc32.md Section 9),
# and HashScheme lives in models.py. We surface the $pst$ line through extract for
# pipeline uniformity, tagging it with the nearest bare-password-verifier scheme
# (VBA is likewise verifier = H(password), recovered by dictionary/collide rather
# than by decrypting ciphertext) and a None hashcat mode. The authoritative
# payload is always the emitted ``.value`` string, not this metadata tag.
# Friendly cipher names for the MAIL_BODY gate note.
_CRYPT_NAMES: Final[dict[int, str]] = {
    _CRYPT_NONE: "NDB_CRYPT_NONE (plaintext)",
    _CRYPT_PERMUTE: "NDB_CRYPT_PERMUTE",
    _CRYPT_CYCLIC: "NDB_CRYPT_CYCLIC",
    _CRYPT_EDP: "NDB_CRYPT_EDPCRYPTED (EDP/WIP)",
}

# We read this many header bytes up front; the 512-byte ANSI header and the
# 564-byte Unicode header both fit.
_HEADER_READ_LEN: Final = 0x0400

# --- BTree page + block invariants shared by both dialects ----------------

# Every BTPAGE is 512 bytes regardless of dialect ([MS-PST] Section 2.2.2.7).
_PAGE_SIZE: Final = 512

# Guard against a malformed/circular tree; real PST BTrees are only a few levels.
_MAX_BTREE_DEPTH: Final = 8

# Blocks are allocated in multiples of 64 bytes ([MS-PST] Section 2.2.2.8).
_BLOCK_ALIGN: Final = 64

# --- Node / block identifiers ([MS-PST] Section 2.2.2.1 / 2.2.2.2) --------

# The NID is a 4-byte value in both dialects; only the low 32 bits of the (8-byte,
# zero-extended) Unicode nid field are the node id, so mask before comparing.
_NID_MASK: Final = 0xFFFFFFFF

# A BID's low bit (r) is reserved and MUST be ignored before a BBT lookup
# ([MS-PST] Section 2.2.2.2); mask it off when matching a block.
_BID_RESERVED_MASK: Final = ~1

# The BID's second-lowest bit (i) marks an "Internal" block (XBLOCK/XXBLOCK/
# SLBLOCK/SIBLOCK metadata). Only external (end-user) data blocks are body-encoded
# ([MS-PST] Section 4.1), so the body-cipher decode must skip internal blocks.
_BID_INTERNAL_MASK: Final = 0x02


@dataclass(frozen=True)
class _NdbProfile:
    """The field widths and header offsets that differ between ANSI and Unicode NDB.

    [MS-PST] keeps the same logical structures for both on-disk dialects but
    changes pointer widths (BID/IB/nid: 8 bytes Unicode, 4 bytes ANSI) and, as a
    knock-on, the absolute header offsets, the BTPAGE counter positions and the
    BLOCKTRAILER layout. Bundling them keeps the walk functions dialect-agnostic
    and under the parameter budget instead of branching on ``is_unicode``
    everywhere. Sub-entry offsets that follow directly from ``ptr`` (btkey, bid,
    ib, cb positions inside an entry) are derived at the call site from ``ptr``.

    Attributes:
        is_unicode: True for the Unicode dialect (Outlook 2003+), False for ANSI.
        ptr: BID/IB/nid field width in bytes (8 Unicode, 4 ANSI).
        crypt_offset: Absolute file offset of ``bCryptMethod`` (0x0201 / 0x01CD).
        nbt_ib_offset: Absolute file offset of ``ROOT.BREFNBT.ib`` (0x00E0 / 0x00BC).
        bbt_ib_offset: Absolute file offset of ``ROOT.BREFBBT.ib`` (0x00F0 / 0x00C4).
        page_cent_offset: BTPAGE ``cEnt`` byte offset (488 / 496).
        page_cbent_offset: BTPAGE ``cbEnt`` byte offset (490 / 498).
        page_clevel_offset: BTPAGE ``cLevel`` byte offset (491 / 499).
        trailer_size: BLOCKTRAILER size in bytes (16 / 12).
        trailer_crc_offset: ``dwCRC`` offset inside the trailer (4 Unicode / 8 ANSI).

    """

    is_unicode: bool
    ptr: int
    crypt_offset: int
    nbt_ib_offset: int
    bbt_ib_offset: int
    page_cent_offset: int
    page_cbent_offset: int
    page_clevel_offset: int
    trailer_size: int
    trailer_crc_offset: int


# Unicode ROOT ([MS-PST] Section 2.2.2.5) sits at header offset 0xB4; BREFNBT.ib
# lands at 0xE0 and BREFBBT.ib at 0xF0 (root + 0x34 BREFBBT + 8 for ib). The
# Unicode BLOCKTRAILER is {cb(2), wSig(2), dwCRC(4), bid(8)} so dwCRC is at +4.
_UNICODE_PROFILE: Final = _NdbProfile(
    is_unicode=True,
    ptr=8,
    crypt_offset=_CRYPT_OFFSET_UNICODE,
    nbt_ib_offset=0x00E0,
    bbt_ib_offset=0x00F0,
    page_cent_offset=488,
    page_cbent_offset=490,
    page_clevel_offset=491,
    trailer_size=16,
    trailer_crc_offset=4,
)
# ANSI ROOT sits at header offset 0xA4 (40 bytes); BREFNBT.ib lands at 0xBC and
# BREFBBT.ib at 0xC4 (root + 0x1C BREFBBT + 4 for ib). The ANSI BLOCKTRAILER
# swaps the field order to {cb(2), wSig(2), bid(4), dwCRC(4)} so dwCRC is at +8.
_ANSI_PROFILE: Final = _NdbProfile(
    is_unicode=False,
    ptr=4,
    crypt_offset=_CRYPT_OFFSET_ANSI,
    nbt_ib_offset=0x00BC,
    bbt_ib_offset=0x00C4,
    page_cent_offset=496,
    page_cbent_offset=498,
    page_clevel_offset=499,
    trailer_size=12,
    trailer_crc_offset=8,
)

# --- Heap-on-Node / Property-Context signatures ([MS-PST] Sections 2.3.1-2.3.3) ---

_HN_HEADER_SIG: Final = 0xEC  # HNHDR.bSig
_HN_CLIENT_PC: Final = 0xBC  # HNHDR.bClientSig for a Property Context (bTypePC)
_BTH_HEADER_SIG: Final = 0xB5  # BTHHEADER.bType (bTypeBTH)

# Minimum decoded lengths for the HNHDR (12 bytes) and the BTHHEADER (8 bytes).
_HNHDR_MIN_LEN: Final = 12
_BTHHEADER_MIN_LEN: Final = 8

# A PC record ([MS-PST] Section 2.3.3.3) is {wPropId(2), wPropType(2), dwValueHnid(4)}.
# For PidTagPstPassword (PtypInteger32) the CRC is stored inline in dwValueHnid.
_PC_RECORD_SIZE: Final = 8
_PST_PASSWORD_PROP_ID: Final = pst.PID_TAG_PST_PASSWORD >> 16  # 0x67FF

# HID decoding ([MS-PST] Section 2.2.2.1): the allocation index is bits 5..15
# (1-based), the block index is bits 16..31. Everything here is a single-block HN.
_HID_INDEX_SHIFT: Final = 5
_HID_INDEX_MASK: Final = 0x07FF
_HID_BLOCK_SHIFT: Final = 16


@dataclass(frozen=True)
class _NdbHeader:
    """The header fields this handler needs from an NDB file ([MS-PST] Section 2.2.2.6)."""

    profile: _NdbProfile  # the ANSI/Unicode layout selected by wVer
    crypt_method: int
    nbt_ib: int | None  # byte offset of the node-BTree root page
    bbt_ib: int | None  # byte offset of the block-BTree root page


@dataclass(frozen=True)
class _PasswordLocation:
    """Where the PidTagPstPassword CRC lives, enough to read it or zero it."""

    data_ib: int  # byte offset of the message-store block data
    data_cb: int  # length of that block data (excludes trailer/padding)
    value_offset: int  # offset of the 4-byte CRC within the *decoded* data
    crc_value: int  # the CRC currently stored (0 == no password)
    crypt_method: int  # body cipher covering the block
    bid: int  # block BID (the cyclic-cipher key source)
    trailer_crc_ib: int  # absolute offset of the block-trailer dwCRC to fix


def _round_up(value: int, multiple: int) -> int:
    """Round ``value`` up to the next multiple of ``multiple`` (block allocation)."""
    return ((value + multiple - 1) // multiple) * multiple


def _read_uint(buffer: bytes, offset: int, size: int) -> int:
    """Read a little-endian unsigned integer of ``size`` bytes (BID/IB/nid width).

    A single width-parameterised reader lets the walk functions handle the 8-byte
    Unicode and 4-byte ANSI pointer fields ([MS-PST] Section 2.2.2.2-2.2.2.4)
    without a per-call ``struct`` format string. Callers MUST have length-checked
    the slice; a short slice would silently yield a smaller integer.
    """
    return int.from_bytes(buffer[offset : offset + size], "little")


def _decode_body(data: bytes, crypt: int, key: int) -> bytes:
    """Decode a block's data through the keyless body cipher ([MS-PST] Sections 5.1-5.2)."""
    if crypt == _CRYPT_PERMUTE:
        return pst.permute_decode(data)
    if crypt == _CRYPT_CYCLIC:
        return pst.cyclic_decode(data, key)
    # NDB_CRYPT_NONE: the block is already plaintext.
    return data


def _encode_body(data: bytes, crypt: int, key: int) -> bytes:
    """Re-encode block data after an edit (inverse of :func:`_decode_body`)."""
    if crypt == _CRYPT_PERMUTE:
        return pst.permute_decode(data, encode=True)
    if crypt == _CRYPT_CYCLIC:
        # The cyclic cipher is symmetric -- the same routine encodes and decodes.
        return pst.cyclic_decode(data, key)
    return data


def _read_at(handle: BinaryIO, offset: int, size: int) -> bytes:
    """Read ``size`` bytes at ``offset`` from an open file (random access)."""
    handle.seek(offset)
    return handle.read(size)


def _parse_header(raw: bytes) -> _NdbHeader | None:
    """Parse the NDB header, returning None if ``raw`` is not a PST/OST file.

    Reads the magic, the ANSI/Unicode discriminator and the ``bCryptMethod``
    byte, plus (for Unicode) the two BTree-root byte offsets from ROOT. Malformed
    input yields None so detection never crashes.
    """
    if not raw.startswith(_PST_MAGIC):
        return None
    try:
        (wver,) = struct.unpack_from("<H", raw, 0x0A)
    except struct.error:
        return None
    profile = _UNICODE_PROFILE if wver >= _UNICODE_MIN_VER else _ANSI_PROFILE
    # Bail out cleanly if the file is too short to hold the fields we index into,
    # so detection never raises on a truncated or non-PST file.
    needed = max(profile.crypt_offset + 1, profile.nbt_ib_offset + profile.ptr, profile.bbt_ib_offset + profile.ptr)
    if len(raw) < needed:
        return None
    crypt_method = raw[profile.crypt_offset]
    nbt_ib = _read_uint(raw, profile.nbt_ib_offset, profile.ptr)
    bbt_ib = _read_uint(raw, profile.bbt_ib_offset, profile.ptr)
    return _NdbHeader(profile=profile, crypt_method=crypt_method, nbt_ib=nbt_ib, bbt_ib=bbt_ib)


def _iter_leaf_entries(handle: BinaryIO, page_ib: int, profile: _NdbProfile, depth: int = 0) -> list[bytes]:
    """Return every leaf entry under the BTree page at ``page_ib``.

    A BTPAGE ([MS-PST] Section 2.2.2.7.7) is either a leaf (cLevel 0) whose
    entries are the caller's records, or an intermediate page whose BTENTRYs each
    point at a child page. We recurse into children, collecting leaf entries. The
    ``profile`` fixes the counter offsets and the BTENTRY child-pointer width so
    the same walk serves both ANSI and Unicode pages.
    """
    if depth > _MAX_BTREE_DEPTH:
        return []
    page = _read_at(handle, page_ib, _PAGE_SIZE)
    if len(page) < _PAGE_SIZE:
        return []
    count = page[profile.page_cent_offset]
    entry_size = page[profile.page_cbent_offset]
    level = page[profile.page_clevel_offset]
    if entry_size == 0:
        return []
    if level == 0:
        return [page[i * entry_size : (i + 1) * entry_size] for i in range(count)]
    # Intermediate page: a BTENTRY is {btkey(ptr), BREF{bid(ptr), ib(ptr)}}, so the
    # child page's byte offset (ib) sits 2*ptr bytes into the entry.
    child_ib_offset = 2 * profile.ptr
    entries: list[bytes] = []
    for i in range(count):
        entry = page[i * entry_size : (i + 1) * entry_size]
        if len(entry) < child_ib_offset + profile.ptr:
            continue
        child_ib = _read_uint(entry, child_ib_offset, profile.ptr)
        entries.extend(_iter_leaf_entries(handle, child_ib, profile, depth + 1))
    return entries


def _find_message_store_bid(handle: BinaryIO, nbt_ib: int, profile: _NdbProfile) -> int | None:
    """Return the data BID of NID_MESSAGE_STORE from the node BTree, or None.

    An NBTENTRY ([MS-PST] Section 2.2.2.7.7.4) is {nid, bidData, bidSub,
    nidParent, ...}; nid and bidData are the first two pointer-width fields. We
    match the low 32 bits of nid against NID_MESSAGE_STORE (0x0021).
    """
    for entry in _iter_leaf_entries(handle, nbt_ib, profile):
        if len(entry) < 2 * profile.ptr:
            continue
        nid = _read_uint(entry, 0, profile.ptr)
        bid_data = _read_uint(entry, profile.ptr, profile.ptr)
        if (nid & _NID_MASK) == pst.NID_MESSAGE_STORE:
            return bid_data
    return None


def _parse_bbtentry(entry: bytes, profile: _NdbProfile) -> tuple[int, int, int] | None:
    """Decode a leaf BBTENTRY to (bid, ib, cb), or None if it is too short.

    A BBTENTRY ([MS-PST] Section 2.2.2.7.7.3) is {BREF{bid(ptr), ib(ptr)}, cb(2),
    cRef(2), ...}; the raw-data size ``cb`` follows the BREF at offset 2*ptr.
    """
    if len(entry) < 2 * profile.ptr + 2:
        return None
    bid = _read_uint(entry, 0, profile.ptr)
    ib = _read_uint(entry, profile.ptr, profile.ptr)
    cb = _read_uint(entry, 2 * profile.ptr, 2)
    return bid, ib, cb


def _iter_block_refs(handle: BinaryIO, bbt_ib: int, profile: _NdbProfile) -> list[tuple[int, int, int]]:
    """Return (bid, ib, cb) for every leaf BBTENTRY in the block BTree.

    Used by the body-cipher DECODE path to enumerate every block; the caller
    filters out internal blocks (which are not body-encoded).
    """
    refs: list[tuple[int, int, int]] = []
    for entry in _iter_leaf_entries(handle, bbt_ib, profile):
        parsed = _parse_bbtentry(entry, profile)
        if parsed is not None:
            refs.append(parsed)
    return refs


def _find_block_ref(handle: BinaryIO, bbt_ib: int, target_bid: int, profile: _NdbProfile) -> tuple[int, int, int] | None:
    """Return (bid, ib, cb) for ``target_bid`` from the block BTree, or None.

    BIDs are matched with the reserved low bit masked ([MS-PST] Section 2.2.2.2).
    """
    wanted = target_bid & _BID_RESERVED_MASK
    for entry in _iter_leaf_entries(handle, bbt_ib, profile):
        parsed = _parse_bbtentry(entry, profile)
        if parsed is None:
            continue
        bid, ib, cb = parsed
        if (bid & _BID_RESERVED_MASK) == wanted:
            return bid, ib, cb
    return None


def _resolve_hid(decoded: bytes, page_map_offset: int, hid: int) -> tuple[int, int] | None:
    """Resolve an HID to its (offset, length) within a single-block HN.

    Per [MS-PST] Section 2.2.2.1 the allocation index is bits 5..15 (1-based) and
    the block index is bits 16..31. This handler only supports the first HN block
    (block index 0); anything else means a data tree we do not walk.
    """
    index = (hid >> _HID_INDEX_SHIFT) & _HID_INDEX_MASK
    if (hid >> _HID_BLOCK_SHIFT) != 0 or index == 0:
        return None
    # HNPAGEMAP ([MS-PST] Section 2.3.1.5): cAlloc(2), cFree(2), rgibAlloc[cAlloc+1].
    try:
        (alloc_count,) = struct.unpack_from("<H", decoded, page_map_offset)
        if index > alloc_count:
            return None
        start, end = struct.unpack_from("<HH", decoded, page_map_offset + 4 + (index - 1) * 2)
    except struct.error:
        return None
    if end < start or end > len(decoded):
        return None
    return int(start), int(end - start)


def _pc_record_array(decoded: bytes, page_map_offset: int, hid_user_root: int) -> tuple[int, int] | None:
    """Resolve the flat PC record array from the BTH header, or None.

    Reads the BTHHEADER ([MS-PST] Section 2.3.2.1): bType(1), cbKey(1), cbEnt(1),
    bIdxLevels(1), hidRoot(4). PidTagPstPassword lives in a flat (bIdxLevels 0)
    BTH, so a non-zero level is treated as unsupported.
    """
    bth = _resolve_hid(decoded, page_map_offset, hid_user_root)
    if bth is None:
        return None
    bth_offset, bth_len = bth
    if bth_len < _BTHHEADER_MIN_LEN or decoded[bth_offset] != _BTH_HEADER_SIG or decoded[bth_offset + 3] != 0:
        return None
    (hid_root,) = struct.unpack_from("<I", decoded, bth_offset + 4)
    return _resolve_hid(decoded, page_map_offset, hid_root)


def _pc_password_value_offset(decoded: bytes) -> int | None:
    """Return the offset of the PidTagPstPassword CRC within a decoded PC block.

    Parses the Heap-on-Node header ([MS-PST] Section 2.3.1), then the
    Property-Context BTH ([MS-PST] Section 2.3.2/2.3.3), and scans the flat record
    array for property 0x67FF. Returns None if the block is not a PC, uses a
    multi-level BTH, or lacks the property.
    """
    if len(decoded) < _HNHDR_MIN_LEN:
        return None
    # HNHDR: ibHnpm(2), bSig(1), bClientSig(1), hidUserRoot(4), rgbFillLevel(4).
    (page_map_offset,) = struct.unpack_from("<H", decoded, 0)
    if decoded[2] != _HN_HEADER_SIG or decoded[3] != _HN_CLIENT_PC:
        return None
    (hid_user_root,) = struct.unpack_from("<I", decoded, 4)
    records = _pc_record_array(decoded, page_map_offset, hid_user_root)
    if records is None:
        return None
    rec_offset, rec_len = records
    for pos in range(rec_offset, rec_offset + rec_len - _PC_RECORD_SIZE + 1, _PC_RECORD_SIZE):
        (prop_id,) = struct.unpack_from("<H", decoded, pos)
        if prop_id == _PST_PASSWORD_PROP_ID:
            # The 4-byte inline value follows wPropId(2) + wPropType(2).
            return pos + 4
    return None


def _locate_password(handle: BinaryIO, header: _NdbHeader) -> _PasswordLocation | None:
    """Walk the NDB (ANSI or Unicode) to the message-store CRC, or None if unreachable.

    Returns None for anything this handler does not walk (EDP, data trees, a store
    with no password property) so callers can decide whether that is a "no gate"
    (gates) or an unsupported operation (bypass).
    """
    profile = header.profile
    # EDP blocks are real ciphertext -- there is no plaintext PC to find.
    if header.nbt_ib is None or header.bbt_ib is None or header.crypt_method == _CRYPT_EDP:
        return None
    bid = _find_message_store_bid(handle, header.nbt_ib, profile)
    if bid is None:
        return None
    block = _find_block_ref(handle, header.bbt_ib, bid, profile)
    if block is None:
        return None
    block_bid, ib, cb = block
    data = _read_at(handle, ib, cb)
    if len(data) < cb:
        return None
    decoded = _decode_body(data, header.crypt_method, block_bid & _NID_MASK)
    value_offset = _pc_password_value_offset(decoded)
    if value_offset is None or value_offset + 4 > len(decoded):
        return None
    (crc_value,) = struct.unpack_from("<I", decoded, value_offset)
    alloc = _round_up(cb + profile.trailer_size, _BLOCK_ALIGN)
    trailer_crc_ib = ib + alloc - profile.trailer_size + profile.trailer_crc_offset
    return _PasswordLocation(
        data_ib=ib,
        data_cb=cb,
        value_offset=value_offset,
        crc_value=crc_value,
        crypt_method=header.crypt_method,
        bid=block_bid,
        trailer_crc_ib=trailer_crc_ib,
    )


class OutlookHandler(FormatHandler):
    """Handler for the Outlook PST/OST container ([MS-PST])."""

    container = ContainerKind.PST

    @override
    def is_encrypted(self, path: Path) -> bool:
        """Report ``False`` -- a PST carries no password-derived encryption.

        The body cipher is keyless obfuscation and the open "password" is an
        advisory CRC-32; neither keys any ciphertext. Even the EDP variant is not
        file-recoverable, so there is nothing to decrypt with a password and this
        reports ``False`` for every PST (see ``docs/reference/gates.md``, .pst row).
        """
        header = self._read_header(path)
        _ = header
        return False

    @override
    def gates(self, path: Path) -> list[Gate]:
        """Enumerate the MAIL_BODY cipher gate and, if present, the OPEN password.

        The MAIL_BODY gate is always present (DECODE, or NONE for EDP) and its note
        names the cipher from ``bCryptMethod``. The OPEN gate is added only when a
        non-zero ``PidTagPstPassword`` is actually found in the message store --
        its recovery is STRIP because the CRC guards nothing.
        """
        header = self._read_header(path)
        if header is None:
            return []
        gates: list[Gate] = [self._mail_body_gate(header)]
        open_gate = self._open_gate(path, header)
        if open_gate is not None:
            gates.append(open_gate)
        logger.debug("gates: %d gates, crypt=0x%02x", len(gates), header.crypt_method)
        return gates

    @override
    def extract(self, path: Path) -> list[ExtractedHash]:
        """Return an empty list -- the PST advisory CRC-32 is not a crackable hash.

        The 32-bit CRC verifier is recovered instantly by the COLLIDE/STRIP paths
        (``opt advanced collide`` / ``opt advanced bypass``), not by GPU cracking.
        The gate is surfaced by :meth:`gates`; no hash line is emitted.
        """
        _ = path
        return []

    @override
    def bypass(self, path: Path, out: Path, *, remove_signatures: bool = False) -> None:
        r"""Write a copy of ``path`` to ``out`` with the open password stripped.

        Locates ``PidTagPstPassword`` in the message-store property context, zeros
        the DWORD (per :func:`pst.describe_password_strip`), fixes the affected
        block-trailer CRC, and writes the result to ``out`` -- the store then opens
        with no prompt. Both ANSI and Unicode stores are walked. The input is
        read-only and never touched. Raises :class:`HandlerNotImplementedError`
        when the property cannot be reached safely (EDP cipher, data-tree message
        store) rather than corrupt the file. ``remove_signatures`` is accepted for
        interface parity but ignored -- a PST carries no digital-signature gate.
        """
        _ = remove_signatures  # PST/OST has no digital-signature gate
        if out == path:
            msg = "bypass output path must differ from the input path"
            raise ValueError(msg)
        header = self._read_header(path)
        if header is None:
            msg = "not a PST/OST file (missing !BDN header)"
            raise ValueError(msg)
        try:
            with path.open("rb") as handle:
                location = _locate_password(handle, header)
        except OSError as exc:
            msg = "could not read the PST while locating the password"
            raise HandlerNotImplementedError(msg, self.container.value) from exc
        if location is None:
            operation = "PST password strip (property not reachable: EDP cipher or data-tree message store)"
            raise HandlerNotImplementedError(operation, self.container.value)
        logger.debug("bypass: zeroing PidTagPstPassword at data_ib=0x%x (was CRC=0x%08x)", location.data_ib, location.crc_value)
        buffer = bytearray(path.read_bytes())
        self._zero_password(buffer, location)
        logger.debug("bypass: wrote %d bytes to %s", len(buffer), out)
        out.write_bytes(buffer)

    def decode_body(self, path: Path, out: Path) -> None:
        """Write a plaintext-cipher copy of ``path`` with the keyless body decoded.

        Decodes every external (non-internal) data block through the NDB body
        cipher ([MS-PST] Sections 5.1-5.2), recomputes each affected block-trailer
        ``dwCRC`` over the now-plaintext bytes ([MS-PST] Section 2.2.2.8), and
        rewrites ``bCryptMethod`` to ``NDB_CRYPT_NONE`` (0x00) so any reader opens
        the copy without cipher logic (pst-body-cipher.md Section 8). Works for both
        ANSI and Unicode. The input is read-only and never touched.

        This is a DECODE operation, not a password decrypt -- the body cipher takes
        no key. It raises :class:`HandlerNotImplementedError` when there is nothing
        to decode (already ``NDB_CRYPT_NONE``) or the body is genuine cryptography
        (``NDB_CRYPT_EDPCRYPTED``); it never writes an unchanged copy while claiming
        success.
        """
        if out == path:
            msg = "decode output path must differ from the input path"
            raise ValueError(msg)
        header = self._read_header(path)
        if header is None:
            msg = "not a PST/OST file (missing !BDN header)"
            raise ValueError(msg)
        crypt = header.crypt_method
        if crypt == _CRYPT_NONE:
            operation = "PST body decode (already NDB_CRYPT_NONE; nothing to decode)"
            raise HandlerNotImplementedError(operation, self.container.value)
        if crypt not in (_CRYPT_PERMUTE, _CRYPT_CYCLIC) or header.bbt_ib is None:
            operation = "PST body decode (EDP/WIP or unknown cipher is not keyless-decodable)"
            raise HandlerNotImplementedError(operation, self.container.value)
        cipher_name = "permute" if crypt == _CRYPT_PERMUTE else "cyclic"
        logger.debug("decode_body: cipher=%s, walking block BTree", cipher_name)
        try:
            with path.open("rb") as handle:
                refs = _iter_block_refs(handle, header.bbt_ib, header.profile)
        except OSError as exc:
            operation = "PST body decode (could not read the block BTree)"
            raise HandlerNotImplementedError(operation, self.container.value) from exc
        logger.debug("decode_body: %d block refs found", len(refs))
        buffer = bytearray(path.read_bytes())
        if not self._decode_all_blocks(buffer, refs, header):
            operation = "PST body decode (no external data blocks found to decode)"
            raise HandlerNotImplementedError(operation, self.container.value)
        buffer[header.profile.crypt_offset] = _CRYPT_NONE
        logger.debug("decode_body: decoded %d blocks, set bCryptMethod=0x00, wrote %d bytes to %s", len(refs), len(buffer), out)
        out.write_bytes(buffer)

    @override
    def decrypt(self, path: Path, out: Path, password: str) -> None:
        """Reject decryption -- a PST has no document-open encryption to undo.

        The body cipher is keyless (recover it with a reader, not a password) and
        the open password guards nothing, so there is no password-keyed ciphertext
        to decrypt. This raises instead of pretending to.
        """
        _ = (path, out, password)
        operation = "PST files have no document-open encryption — the CRC-32 password is advisory only"
        raise HandlerNotImplementedError(operation, self.container.value)

    # --- Internal helpers -------------------------------------------------

    def _read_header(self, path: Path) -> _NdbHeader | None:
        """Read and parse the NDB header, returning None on any read/parse failure.

        Detection must never crash on malformed input, so read and struct errors
        collapse to None (treated as "not a usable PST").
        """
        try:
            with path.open("rb") as handle:
                raw = handle.read(_HEADER_READ_LEN)
        except OSError:
            return None
        return _parse_header(raw)

    def _mail_body_gate(self, header: _NdbHeader) -> Gate:
        """Build the MAIL_BODY gate from the header's ``bCryptMethod``.

        DECODE for the keyless permute/cyclic ciphers; NONE for EDP, which is real
        off-file encryption and not recoverable from the file alone. The ``where``
        note reports the dialect-specific ``bCryptMethod`` offset.
        """
        crypt_method = header.crypt_method
        cipher_name = _CRYPT_NAMES.get(crypt_method, f"unknown (0x{crypt_method:02X})")
        recovery = RecoveryClass.NONE if crypt_method == _CRYPT_EDP else RecoveryClass.DECODE
        return Gate(
            gate=GateType.MAIL_BODY,
            recovery=recovery,
            where=f"NDB header bCryptMethod (offset 0x{header.profile.crypt_offset:04X})",
            note=f"keyless body cipher: {cipher_name}",
        )

    def _open_gate(self, path: Path, header: _NdbHeader) -> Gate | None:
        """Return the OPEN-password gate when a non-zero CRC is present, else None.

        A missing property or a zero value means "no password", and any structural
        limit (EDP, data tree) simply yields None here -- we never fabricate a gate
        we could not confirm.
        """
        try:
            with path.open("rb") as handle:
                location = _locate_password(handle, header)
        except (OSError, struct.error, ValueError, IndexError):
            return None
        if location is None or location.crc_value == 0:
            return None
        return Gate(
            gate=GateType.OPEN,
            recovery=RecoveryClass.STRIP,
            where="PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE (0x0021)",
            note=f"advisory CRC-32 open password (0x{location.crc_value:08x}); guards nothing -- zero it to open with no prompt",
        )

    def _zero_password(self, buffer: bytearray, location: _PasswordLocation) -> None:
        """Zero the password DWORD in ``buffer`` and repair the block-trailer CRC.

        Decodes the message-store block, clears the 4-byte CRC value, re-encodes
        the whole block and rewrites the trailer ``dwCRC`` ([MS-PST] Section
        2.2.2.8) over the re-encoded bytes so the file stays self-consistent.
        """
        start = location.data_ib
        end = start + location.data_cb
        key = location.bid & _NID_MASK
        decoded = bytearray(_decode_body(bytes(buffer[start:end]), location.crypt_method, key))
        decoded[location.value_offset : location.value_offset + 4] = b"\x00\x00\x00\x00"
        encoded = _encode_body(bytes(decoded), location.crypt_method, key)
        buffer[start:end] = encoded
        new_crc = pst.pst_crc32(encoded)
        struct.pack_into("<I", buffer, location.trailer_crc_ib, new_crc)

    def _decode_all_blocks(self, buffer: bytearray, refs: list[tuple[int, int, int]], header: _NdbHeader) -> bool:
        """Decode every external data block in ``buffer`` in place; return whether any changed.

        Internal blocks (BID ``i``-bit set: XBLOCK/XXBLOCK/SLBLOCK/SIBLOCK) hold
        metadata and are never body-encoded ([MS-PST] Section 4.1), so they are
        skipped -- decoding them would corrupt the block tree. Each decoded block's
        trailer ``dwCRC`` is recomputed over the plaintext bytes so the copy stays
        self-consistent once ``bCryptMethod`` is set to NONE.
        """
        profile = header.profile
        crypt = header.crypt_method
        changed = False
        for bid, ib, cb in refs:
            # Skip internal (non-data) blocks and empty payloads.
            if bid & _BID_INTERNAL_MASK or cb == 0:
                continue
            end = ib + cb
            if end > len(buffer):
                continue  # malformed reference -- leave it untouched
            decoded = _decode_body(bytes(buffer[ib:end]), crypt, bid & _NID_MASK)
            buffer[ib:end] = decoded
            # Recompute the trailer dwCRC over the plaintext at the dialect offset.
            alloc = _round_up(cb + profile.trailer_size, _BLOCK_ALIGN)
            crc_ib = ib + alloc - profile.trailer_size + profile.trailer_crc_offset
            if crc_ib + 4 <= len(buffer):
                struct.pack_into("<I", buffer, crc_ib, pst.pst_crc32(decoded))
            changed = True
        return changed
