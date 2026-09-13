# SPDX-License-Identifier: Apache-2.0
"""Outlook PST advisory password and keyless NDB body cipher ([MS-PST]).

A Personal Folders file (``.pst``) carries two entirely separate, weak
protections, both handled here:

* **Open password** -- an optional, UI-only gate. [MS-PST] Section 2.4.3.3 is
  explicit that "the PST password is just implemented at the UI level ... The
  password itself is not used to secure the PST data in any way." The only
  stored material is a single CRC-32 of the password text in the tagged
  property ``PidTagPstPassword`` (``0x67FF0003``) on the message-store node.
  Because a 32-bit CRC is invertible, there is nothing to brute-force: you
  either STRIP the property (set it to ``0`` = "no password") or COLLIDE it
  (append four tuning bytes to force any target CRC).

* **Body cipher** -- a keyless whole-file obfuscation over the non-internal NDB
  data blocks, selected by the ``bCryptMethod`` header byte: NDB_CRYPT_PERMUTE
  (a fixed 256-byte substitution, [MS-PST] Section 5.1) or NDB_CRYPT_CYCLIC (a
  per-block substitution keyed by the block's own BID, [MS-PST] Section 5.2).
  Neither takes a password; both are pure DECODE. [MS-PST] Section 4.1 calls
  them "two keyless cipher algorithms ... only provide data obfuscation and can
  be conveniently decoded once the exact encoding algorithm is understood."

Nothing in this module is a GPU cracking target. The three recovery paths it
supports are DECODE (body cipher), COLLIDE (CRC forge) and STRIP (zero the
property). The [MS-PST] CRC uses seed ``0`` and no pre/post inversion, so it is
NOT the same value as ``zlib.crc32`` -- see :func:`pst_crc32`.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Final

logger = logging.getLogger(__name__)

# --- CRC-32 ([MS-PST] Section 5.3) ---

# [MS-PST] Section 5.3 reproduces the canonical reflected CRC-32 lookup table
# (CrcTableOffset32[256], polynomial 0xEDB88320). We build it at import time and
# assert its published first-row values below, which is cheaper to audit than a
# 256-entry literal and guarantees byte-for-byte agreement with the spec table
# (0x00000000, 0x77073096, 0xEE0E612C, 0x990951BA, 0x076DC419, ...).
_CRC_POLY: Final = 0xEDB88320  # reflected IEEE 802.3 polynomial, [MS-PST] Section 5.3
_MASK32: Final = 0xFFFFFFFF


def _build_crc_table() -> tuple[int, ...]:
    """Generate the reflected CRC-32 table from the polynomial.

    Uses the standard byte-at-a-time reflected algorithm from RFC 1952 Section 8
    (GZIP CRC). Equivalent to the literal CrcTableOffset32[256] printed in
    [MS-PST] Section 5.3; generating it keeps the reflected polynomial visible
    instead of hiding it inside 256 magic constants.
    """
    table = []
    for index in range(256):
        crc = index
        for _ in range(8):
            crc = (_CRC_POLY ^ (crc >> 1)) if (crc & 1) else (crc >> 1)
        table.append(crc & _MASK32)
    return tuple(table)


_CRC_TABLE: Final = _build_crc_table()

# Sanity anchor to [MS-PST] Section 5.3: the published first row of the table.
# If a future refactor breaks the polynomial this catches it at import time.
if _CRC_TABLE[0:5] != (0x00000000, 0x77073096, 0xEE0E612C, 0x990951BA, 0x076DC419):  # pragma: no cover
    msg = "CRC-32 table does not match [MS-PST] Section 5.3"
    raise RuntimeError(msg)


def pst_crc32(data: bytes, seed: int = 0) -> int:
    """Return the [MS-PST] Section 5.3 CRC-32 of ``data``.

    This is the exact ``ComputeCRC`` routine from the spec: table-driven,
    reflected, seeded with ``dwCRC`` (0 in the PidTagPstPassword context) and
    with **no** pre- or post-inversion. That last detail matters -- the standard
    ``zlib.crc32`` seeds the register with ``0xFFFFFFFF`` and XORs the result
    with ``0xFFFFFFFF``, so ``pst_crc32(data) != zlib.crc32(data)`` in general.
    The PST file uses this same CRC for its own block and page checksums.

    Args:
        data: The bytes to checksum.
        seed: Initial ``dwCRC`` value; MUST be 0 for the open-password verifier.

    Returns:
        The 32-bit CRC as an unsigned integer.

    """
    crc = seed & _MASK32
    for byte in data:
        # crc = CrcTableOffset32[(crc XOR b) AND 0xFF] XOR (crc >> 8), per spec.
        crc = _CRC_TABLE[(crc ^ byte) & 0xFF] ^ (crc >> 8)
    return int(crc & _MASK32)


def password_crc(password: bytes) -> int:
    """Return the PidTagPstPassword verifier for a password.

    Per [MS-PST] Section 2.4.3.3 the stored DWORD is ``CRC-32(password bytes)``
    with seed 0. The spec says only "the password text" and does not pin the
    encoding; in practice the CRC is taken over the raw ANSI/MBCS bytes with no
    trailing NUL, so this function operates on the caller-supplied ``bytes`` and
    leaves the encoding decision to the caller (encode ``str`` as needed before
    calling). A stored value of 0 means "no password is set".

    Args:
        password: The password already encoded to its on-the-wire bytes.

    Returns:
        The 32-bit verifier stored in property 0x67FF0003.

    """
    return pst_crc32(password, seed=0)


# --- NDB body cipher tables ([MS-PST] Section 5.1) ---

# mpbbCrypt[768] from [MS-PST] Section 5.1, reproduced verbatim as its three
# 256-byte sub-tables. mpbbR is the forward (encode) substitution, mpbbI is its
# inverse (decode), and mpbbS is a self-inverse involution used only by the
# cyclic mixer. The design relations mpbbI == mpbbR^-1 and mpbbS[mpbbS[x]] == x
# are what make the cyclic routine a single symmetric encode/decode function.
_MPBB_R: Final = (
    65,
    54,
    19,
    98,
    168,
    33,
    110,
    187,
    244,
    22,
    204,
    4,
    127,
    100,
    232,
    93,
    30,
    242,
    203,
    42,
    116,
    197,
    94,
    53,
    210,
    149,
    71,
    158,
    150,
    45,
    154,
    136,
    76,
    125,
    132,
    63,
    219,
    172,
    49,
    182,
    72,
    95,
    246,
    196,
    216,
    57,
    139,
    231,
    35,
    59,
    56,
    142,
    200,
    193,
    223,
    37,
    177,
    32,
    165,
    70,
    96,
    78,
    156,
    251,
    170,
    211,
    86,
    81,
    69,
    124,
    85,
    0,
    7,
    201,
    43,
    157,
    133,
    155,
    9,
    160,
    143,
    173,
    179,
    15,
    99,
    171,
    137,
    75,
    215,
    167,
    21,
    90,
    113,
    102,
    66,
    191,
    38,
    74,
    107,
    152,
    250,
    234,
    119,
    83,
    178,
    112,
    5,
    44,
    253,
    89,
    58,
    134,
    126,
    206,
    6,
    235,
    130,
    120,
    87,
    199,
    141,
    67,
    175,
    180,
    28,
    212,
    91,
    205,
    226,
    233,
    39,
    79,
    195,
    8,
    114,
    128,
    207,
    176,
    239,
    245,
    40,
    109,
    190,
    48,
    77,
    52,
    146,
    213,
    14,
    60,
    34,
    50,
    229,
    228,
    249,
    159,
    194,
    209,
    10,
    129,
    18,
    225,
    238,
    145,
    131,
    118,
    227,
    151,
    230,
    97,
    138,
    23,
    121,
    164,
    183,
    220,
    144,
    122,
    92,
    140,
    2,
    166,
    202,
    105,
    222,
    80,
    26,
    17,
    147,
    185,
    82,
    135,
    88,
    252,
    237,
    29,
    55,
    73,
    27,
    106,
    224,
    41,
    51,
    153,
    189,
    108,
    217,
    148,
    243,
    64,
    84,
    111,
    240,
    198,
    115,
    184,
    214,
    62,
    101,
    24,
    68,
    31,
    221,
    103,
    16,
    241,
    12,
    25,
    236,
    174,
    3,
    161,
    20,
    123,
    169,
    11,
    255,
    248,
    163,
    192,
    162,
    1,
    247,
    46,
    188,
    36,
    104,
    117,
    13,
    254,
    186,
    47,
    181,
    208,
    218,
    61,
)
_MPBB_S: Final = (
    20,
    83,
    15,
    86,
    179,
    200,
    122,
    156,
    235,
    101,
    72,
    23,
    22,
    21,
    159,
    2,
    204,
    84,
    124,
    131,
    0,
    13,
    12,
    11,
    162,
    98,
    168,
    118,
    219,
    217,
    237,
    199,
    197,
    164,
    220,
    172,
    133,
    116,
    214,
    208,
    167,
    155,
    174,
    154,
    150,
    113,
    102,
    195,
    99,
    153,
    184,
    221,
    115,
    146,
    142,
    132,
    125,
    165,
    94,
    209,
    93,
    147,
    177,
    87,
    81,
    80,
    128,
    137,
    82,
    148,
    79,
    78,
    10,
    107,
    188,
    141,
    127,
    110,
    71,
    70,
    65,
    64,
    68,
    1,
    17,
    203,
    3,
    63,
    247,
    244,
    225,
    169,
    143,
    60,
    58,
    249,
    251,
    240,
    25,
    48,
    130,
    9,
    46,
    201,
    157,
    160,
    134,
    73,
    238,
    111,
    77,
    109,
    196,
    45,
    129,
    52,
    37,
    135,
    27,
    136,
    170,
    252,
    6,
    161,
    18,
    56,
    253,
    76,
    66,
    114,
    100,
    19,
    55,
    36,
    106,
    117,
    119,
    67,
    255,
    230,
    180,
    75,
    54,
    92,
    228,
    216,
    53,
    61,
    69,
    185,
    44,
    236,
    183,
    49,
    43,
    41,
    7,
    104,
    163,
    14,
    105,
    123,
    24,
    158,
    33,
    57,
    190,
    40,
    26,
    91,
    120,
    245,
    35,
    202,
    42,
    176,
    175,
    62,
    254,
    4,
    140,
    231,
    229,
    152,
    50,
    149,
    211,
    246,
    74,
    232,
    166,
    234,
    233,
    243,
    213,
    47,
    112,
    32,
    242,
    31,
    5,
    103,
    173,
    85,
    16,
    206,
    205,
    227,
    39,
    59,
    218,
    186,
    215,
    194,
    38,
    212,
    145,
    29,
    210,
    28,
    34,
    51,
    248,
    250,
    241,
    90,
    239,
    207,
    144,
    182,
    139,
    181,
    189,
    192,
    191,
    8,
    151,
    30,
    108,
    226,
    97,
    224,
    198,
    193,
    89,
    171,
    187,
    88,
    222,
    95,
    223,
    96,
    121,
    126,
    178,
    138,
)
_MPBB_I: Final = (
    71,
    241,
    180,
    230,
    11,
    106,
    114,
    72,
    133,
    78,
    158,
    235,
    226,
    248,
    148,
    83,
    224,
    187,
    160,
    2,
    232,
    90,
    9,
    171,
    219,
    227,
    186,
    198,
    124,
    195,
    16,
    221,
    57,
    5,
    150,
    48,
    245,
    55,
    96,
    130,
    140,
    201,
    19,
    74,
    107,
    29,
    243,
    251,
    143,
    38,
    151,
    202,
    145,
    23,
    1,
    196,
    50,
    45,
    110,
    49,
    149,
    255,
    217,
    35,
    209,
    0,
    94,
    121,
    220,
    68,
    59,
    26,
    40,
    197,
    97,
    87,
    32,
    144,
    61,
    131,
    185,
    67,
    190,
    103,
    210,
    70,
    66,
    118,
    192,
    109,
    91,
    126,
    178,
    15,
    22,
    41,
    60,
    169,
    3,
    84,
    13,
    218,
    93,
    223,
    246,
    183,
    199,
    98,
    205,
    141,
    6,
    211,
    105,
    92,
    134,
    214,
    20,
    247,
    165,
    102,
    117,
    172,
    177,
    233,
    69,
    33,
    112,
    12,
    135,
    159,
    116,
    164,
    34,
    76,
    111,
    191,
    31,
    86,
    170,
    46,
    179,
    120,
    51,
    80,
    176,
    163,
    146,
    188,
    207,
    25,
    28,
    167,
    99,
    203,
    30,
    77,
    62,
    75,
    27,
    155,
    79,
    231,
    240,
    238,
    173,
    58,
    181,
    89,
    4,
    234,
    64,
    85,
    37,
    81,
    229,
    122,
    137,
    56,
    104,
    82,
    123,
    252,
    39,
    174,
    215,
    189,
    250,
    7,
    244,
    204,
    142,
    95,
    239,
    53,
    156,
    132,
    43,
    21,
    213,
    119,
    52,
    73,
    182,
    18,
    10,
    127,
    113,
    136,
    253,
    157,
    24,
    65,
    125,
    147,
    216,
    88,
    44,
    206,
    254,
    36,
    175,
    222,
    184,
    54,
    200,
    161,
    128,
    166,
    153,
    152,
    168,
    47,
    14,
    129,
    101,
    115,
    228,
    194,
    162,
    138,
    212,
    225,
    17,
    208,
    8,
    139,
    42,
    242,
    237,
    154,
    100,
    63,
    193,
    108,
    249,
    236,
)


def permute_decode(data: bytes, *, encode: bool = False) -> bytes:
    """Apply NDB_CRYPT_PERMUTE ([MS-PST] Section 5.1) to ``data``.

    A plain monoalphabetic byte substitution: decode maps every byte through
    ``mpbbI``, encode maps it through ``mpbbR``. (The spec's DWORD-at-a-time loop
    is only an alignment optimization; semantically it is one table lookup per
    byte.) Because ``mpbbI == mpbbR^-1``, ``permute_decode`` and its ``encode``
    counterpart are exact inverses.

    Args:
        data: The block payload (``cb`` data bytes; the BLOCKTRAILER is excluded).
        encode: ``True`` to encode via ``mpbbR``; default ``False`` decodes via ``mpbbI``.

    Returns:
        The transformed bytes.

    """
    table = _MPBB_R if encode else _MPBB_I
    logger.debug("PST permute %s: %d bytes", "encode" if encode else "decode", len(data))
    return bytes(table[byte] for byte in data)


def cyclic_decode(data: bytes, key: int) -> bytes:
    """Apply NDB_CRYPT_CYCLIC ([MS-PST] Section 5.2) to ``data``.

    This cipher is symmetric -- the same routine encodes and decodes -- so there
    is no ``encode`` flag. ``key`` is the low 32 bits of the data block's BID
    (public metadata from the unencrypted block BTree). The 16-bit mixer ``w``
    starts at ``key ^ (key >> 16)`` and increments by one for every byte, folding
    each byte through mpbbR / mpbbS / mpbbI with ``w``'s two halves added and
    subtracted around them.

    Args:
        data: The block payload (``cb`` data bytes).
        key: The low DWORD of the block's BID ([MS-PST] Section 5.2 ``dwKey``).

    Returns:
        The transformed bytes.

    """
    # Initial 16-bit mixer derived from the block BID, per [MS-PST] Section 5.2.
    mixer = (key ^ (key >> 16)) & 0xFFFF
    out = bytearray(len(data))
    for i, byte in enumerate(data):
        low = mixer & 0xFF  # low byte of w
        high = (mixer >> 8) & 0xFF  # high byte of w
        value = (byte + low) & 0xFF
        value = _MPBB_R[value]
        value = (value + high) & 0xFF
        value = _MPBB_S[value]
        value = (value - high) & 0xFF
        value = _MPBB_I[value]
        value = (value - low) & 0xFF
        out[i] = value
        mixer = (mixer + 1) & 0xFFFF  # advance the mixer every byte
    return bytes(out)


# --- CRC collision (COLLIDE path) ---


def crc_collision(target_crc: int) -> bytes:
    """Return a 4-byte string whose :func:`pst_crc32` equals ``target_crc``.

    The [MS-PST] CRC uses seed 0 with no post-inversion, so the CRC of an
    all-zero message is 0 and the map from a 4-byte input to its 32-bit CRC is
    *linear* over GF(2) and bijective. We therefore express the target as an XOR
    of the per-input-bit CRC contributions and solve the resulting 32x32 system
    by Gaussian elimination, yielding the unique four bytes that hash to
    ``target_crc``. Feeding those bytes as the "password" satisfies the
    PidTagPstPassword check instantly (the COLLIDE path) -- it is not the human
    original, just a value with the same CRC.

    Args:
        target_crc: The stored PidTagPstPassword DWORD to collide with.

    Returns:
        A 4-byte string ``b`` such that ``pst_crc32(b) == target_crc & 0xFFFFFFFF``.

    """
    target = target_crc & _MASK32

    # Column j is the CRC produced by the 4-byte input with only bit j set; by
    # linearity the CRC of any 4-byte input is the XOR of the columns for its
    # set bits. We build an XOR basis over these columns while tracking which
    # input bits (the "mask") produce each pivot.
    pivots: dict[int, tuple[int, int]] = {}  # high bit position -> (input mask, crc value)
    for bit in range(32):
        mask = 1 << bit
        value = pst_crc32(mask.to_bytes(4, "little"))
        while value:
            head = value.bit_length() - 1
            if head in pivots:
                pivot_mask, pivot_value = pivots[head]
                mask ^= pivot_mask
                value ^= pivot_value
            else:
                pivots[head] = (mask, value)
                break

    # Reduce the target against the basis; the accumulated input mask is the
    # 32-bit integer whose little-endian bytes hash to target.
    solution = 0
    remainder = target
    while remainder:
        head = remainder.bit_length() - 1
        pivot_mask, pivot_value = pivots[head]
        solution ^= pivot_mask
        remainder ^= pivot_value
    result = solution.to_bytes(4, "little")
    logger.debug("CRC collision: target=0x%08x result=%s", target_crc, result.hex())
    return result


# --- STRIP path (PidTagPstPassword removal) ---

# Full tag for the open-password verifier: PidTagPstPassword high word 0x67FF
# with PtypInteger32 type 0x0003, per [MS-PST] Section 2.4.3.3.
PID_TAG_PST_PASSWORD: Final = 0x67FF0003
# Message store node id, [MS-PST] Section 2.4.4.1; carries the store PC.
NID_MESSAGE_STORE: Final = 0x0021


@dataclass(frozen=True)
class PasswordStripPlan:
    """Instructions for zeroing the PST open password (STRIP path).

    The handler performs the actual property-context edit; this record just
    documents the target so the STRIP path is spec-traceable. Setting the
    property value to 0 means "no password", so the store opens with no prompt.

    Attributes:
        property_tag: The property to overwrite (``PidTagPstPassword``).
        node_id: The node whose PC holds the property (``NID_MESSAGE_STORE``).
        new_value: The DWORD to store; 0 disables the password gate.

    """

    property_tag: int = PID_TAG_PST_PASSWORD
    node_id: int = NID_MESSAGE_STORE
    new_value: int = 0


def describe_password_strip() -> PasswordStripPlan:
    """Return where and how to zero PidTagPstPassword for the STRIP path.

    Offset logic ([MS-PST] Section 2.4.3.3 + Section 2.4.4.1): the open password
    lives as tagged property ``0x67FF0003`` inside the property context (PC) of
    the message-store node ``NID_MESSAGE_STORE`` (``0x0021``), which is reached
    from the header root. To strip it, locate that property's leaf in the PC BTH
    (the value is a 4-byte little-endian DWORD stored inline in the PC record,
    since PtypInteger32 fits in the value field) and overwrite the DWORD with 0
    -- a zero value means "no password", so Outlook opens the store without a
    prompt. The body cipher is unaffected because it was never keyed by this
    property.

    Returns:
        A :class:`PasswordStripPlan` naming the property, node and target value.

    """
    return PasswordStripPlan()
