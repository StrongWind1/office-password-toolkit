# SPDX-License-Identifier: Apache-2.0
"""Centralised hash and KDF operations for every format handler.

All hash-related third-party imports (``argon2-cffi``) are contained in this
single module alongside the stdlib ``hashlib`` / ``hmac`` wrappers. Protocol
modules import hash primitives from here rather than reaching into libraries
directly, so a dependency change only touches this file.

Pure-Python MD4 (RFC 1320) and MD2 (RFC 1319) implementations live here because
they are absent from most OpenSSL builds (and therefore from ``hashlib``) but are
required by the [MS-OFFCRYPTO] agile encryption scheme (Section 2.3.4.10) and
the ISO write-protection KDF (Section 2.4.2.4), which allow any CNG-registered
hash as a parameter. Neither algorithm is selected by us — the on-disk file
format names them. Both are cryptographically broken and reproduced here solely
to audit files that use them.

The implementations are translated from pycryptodome's public-domain C source
(``src/MD4.c`` and ``src/MD2.c``, A.M. Kuchling) into idiomatic Python.
"""

from __future__ import annotations

import hashlib
import hmac
import logging
import struct
from collections.abc import Callable
from typing import Final, Protocol

from argon2.low_level import ARGON2_VERSION as _ARGON2_VERSION
from argon2.low_level import Type as _Argon2Type
from argon2.low_level import hash_secret_raw as _hash_secret_raw

logger = logging.getLogger(__name__)


# --- Public API ---------------------------------------------------------------


def digest(name: str, data: bytes) -> bytes:
    """Hash ``data`` with the named algorithm and return the raw digest.

    Accepts any hashlib name (``sha1``, ``sha256``, ``sha384``, ``sha512``,
    ``md5``) plus ``md4`` and ``md2`` which route to the pure-Python
    implementations below. This is the single entry point that replaces
    scattered hashlib/legacy_hashes dispatch across the codebase.
    """
    if name == "md4":
        return md4(data)
    if name == "md2":
        return md2(data)
    return hashlib.new(name, data, usedforsecurity=False).digest()


class _HashLike(Protocol):
    """Structural type for objects returned by :func:`new`."""

    def update(self, data: bytes, /) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...


class _LegacyHashWrapper:
    """Wrap a pure-Python hash function (md2/md4) in the hashlib._Hash interface.

    Provides ``.update()`` / ``.digest()`` / ``.hexdigest()`` so callers that
    need a streaming hash constructor (e.g. the ISO protection KDF spin loop)
    can use MD4/MD2 with the same API as hashlib objects.
    """

    def __init__(self, func: _HashFunc, data: bytes = b"") -> None:
        self._func = func
        self._data = bytearray(data)

    def update(self, data: bytes) -> None:
        """Append ``data`` to the message."""
        self._data += data

    def digest(self) -> bytes:
        """Return the digest of all data fed so far."""
        return self._func(bytes(self._data))

    def hexdigest(self) -> str:
        """Return the hex-encoded digest."""
        return self.digest().hex()


# Callable type for the pure-Python hash functions (md4, md2).
_HashFunc = Callable[[bytes], bytes]


def new(name: str, data: bytes = b"") -> _HashLike:
    """Return a hashlib-compatible hash object for the named algorithm.

    For standard algorithms (sha1, sha256, etc.) delegates to ``hashlib.new()``.
    For ``md4`` and ``md2`` returns a :class:`_LegacyHashWrapper` that provides
    the same ``.update()`` / ``.digest()`` interface over the pure-Python
    implementation. Used by the ISO protection KDF where the spin loop needs a
    constructor rather than a one-shot digest.
    """
    if name == "md4":
        return _LegacyHashWrapper(md4, data)
    if name == "md2":
        return _LegacyHashWrapper(md2, data)
    return hashlib.new(name, data, usedforsecurity=False)


def pbkdf2_hmac_sha1(key: bytes, salt: bytes, iterations: int, dklen: int) -> bytes:
    """PBKDF2-HMAC-SHA1 key derivation (RFC 2898).

    The PBKDF2 PRF is always HMAC-SHA1 for both ODF profiles (the SHA-256
    profile uses SHA-256 only for the start key and checksum, never the stretch).
    """
    return hashlib.pbkdf2_hmac("sha1", key, salt, iterations, dklen=dklen)


def argon2id(*, secret: bytes, salt: bytes, time_cost: int, memory_cost: int, parallelism: int, hash_len: int) -> bytes:
    """Argon2id key derivation (RFC 9106).

    Used by ODF 1.3 "Wholesome Encryption" (LibreOffice 24.8+, tdf#105844).
    Wraps ``argon2-cffi``'s low-level binding with the v1.3 version constant.
    """
    return _hash_secret_raw(secret=secret, salt=salt, time_cost=time_cost, memory_cost=memory_cost, parallelism=parallelism, hash_len=hash_len, type=_Argon2Type.ID, version=_ARGON2_VERSION)


def compare_digest(a: bytes, b: bytes) -> bool:
    """Constant-time digest comparison. Re-exports ``hmac.compare_digest``."""
    return hmac.compare_digest(a, b)


# --- MD4 (RFC 1320) ----------------------------------------------------------

_MASK32: Final = 0xFFFFFFFF  # 32-bit bitmask for unsigned arithmetic


def _md4_f(x: int, y: int, z: int) -> int:
    """MD4 round-1 auxiliary function F(X,Y,Z) = (X AND Y) OR (NOT X AND Z) per RFC 1320."""
    return (x & y) | (~x & _MASK32 & z)


def _md4_g(x: int, y: int, z: int) -> int:
    """MD4 round-2 auxiliary function G(X,Y,Z) = (X AND Y) OR (X AND Z) OR (Y AND Z) per RFC 1320."""
    return (x & y) | (x & z) | (y & z)


def _md4_h(x: int, y: int, z: int) -> int:
    """MD4 round-3 auxiliary function H(X,Y,Z) = X XOR Y XOR Z per RFC 1320."""
    return x ^ y ^ z


def _rol32(value: int, n: int) -> int:
    """Rotate a 32-bit value left by ``n`` bits."""
    return ((value << n) | (value >> (32 - n))) & _MASK32


def _md4_compress(state: list[int], block: bytes) -> None:
    """Process one 64-byte block, updating the 4-word state in place."""
    x = list(struct.unpack_from("<16I", block))
    a, b, c, d = state

    # Round 1 — F function, no additive constant.
    for k, s in [(0, 3), (1, 7), (2, 11), (3, 19), (4, 3), (5, 7), (6, 11), (7, 19), (8, 3), (9, 7), (10, 11), (11, 19), (12, 3), (13, 7), (14, 11), (15, 19)]:
        a = _rol32((a + _md4_f(b, c, d) + x[k]) & _MASK32, s)
        a, b, c, d = d, a, b, c

    # Round 2 — G function, constant 0x5A827999.
    for k, s in [(0, 3), (4, 5), (8, 9), (12, 13), (1, 3), (5, 5), (9, 9), (13, 13), (2, 3), (6, 5), (10, 9), (14, 13), (3, 3), (7, 5), (11, 9), (15, 13)]:
        a = _rol32((a + _md4_g(b, c, d) + x[k] + 0x5A827999) & _MASK32, s)
        a, b, c, d = d, a, b, c

    # Round 3 — H function, constant 0x6ED9EBA1.
    for k, s in [(0, 3), (8, 9), (4, 11), (12, 15), (2, 3), (10, 9), (6, 11), (14, 15), (1, 3), (9, 9), (5, 11), (13, 15), (3, 3), (11, 9), (7, 11), (15, 15)]:
        a = _rol32((a + _md4_h(b, c, d) + x[k] + 0x6ED9EBA1) & _MASK32, s)
        a, b, c, d = d, a, b, c

    state[0] = (state[0] + a) & _MASK32
    state[1] = (state[1] + b) & _MASK32
    state[2] = (state[2] + c) & _MASK32
    state[3] = (state[3] + d) & _MASK32


def md4(data: bytes) -> bytes:
    """Return the 16-byte MD4 digest of ``data`` (RFC 1320)."""
    state = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]
    bit_len = len(data) * 8

    # Pad: append 0x80, then zeros to 56 mod 64, then 8-byte LE bit length.
    padded = data + b"\x80"
    padded += b"\x00" * ((55 - len(data) % 64) % 64)
    padded += struct.pack("<Q", bit_len)

    for offset in range(0, len(padded), 64):
        _md4_compress(state, padded[offset : offset + 64])

    return struct.pack("<4I", *state)


# --- MD2 (RFC 1319) ----------------------------------------------------------

# The S-box from the RFC, reproduced verbatim (pycryptodome uses the same table).
_MD2_S: Final = bytes(
    [
        41,
        46,
        67,
        201,
        162,
        216,
        124,
        1,
        61,
        54,
        84,
        161,
        236,
        240,
        6,
        19,
        98,
        167,
        5,
        243,
        192,
        199,
        115,
        140,
        152,
        147,
        43,
        217,
        188,
        76,
        130,
        202,
        30,
        155,
        87,
        60,
        253,
        212,
        224,
        22,
        103,
        66,
        111,
        24,
        138,
        23,
        229,
        18,
        190,
        78,
        196,
        214,
        218,
        158,
        222,
        73,
        160,
        251,
        245,
        142,
        187,
        47,
        238,
        122,
        169,
        104,
        121,
        145,
        21,
        178,
        7,
        63,
        148,
        194,
        16,
        137,
        11,
        34,
        95,
        33,
        128,
        127,
        93,
        154,
        90,
        144,
        50,
        39,
        53,
        62,
        204,
        231,
        191,
        247,
        151,
        3,
        255,
        25,
        48,
        179,
        72,
        165,
        181,
        209,
        215,
        94,
        146,
        42,
        172,
        86,
        170,
        198,
        79,
        184,
        56,
        210,
        150,
        164,
        125,
        182,
        118,
        252,
        107,
        226,
        156,
        116,
        4,
        241,
        69,
        157,
        112,
        89,
        100,
        113,
        135,
        32,
        134,
        91,
        207,
        101,
        230,
        45,
        168,
        2,
        27,
        96,
        37,
        173,
        174,
        176,
        185,
        246,
        28,
        70,
        97,
        105,
        52,
        64,
        126,
        15,
        85,
        71,
        163,
        35,
        221,
        81,
        175,
        58,
        195,
        92,
        249,
        206,
        186,
        197,
        234,
        38,
        44,
        83,
        13,
        110,
        133,
        40,
        132,
        9,
        211,
        223,
        205,
        244,
        65,
        129,
        77,
        82,
        106,
        220,
        55,
        200,
        108,
        193,
        171,
        250,
        36,
        225,
        123,
        8,
        12,
        189,
        177,
        74,
        120,
        136,
        149,
        139,
        227,
        99,
        232,
        109,
        233,
        203,
        213,
        254,
        59,
        0,
        29,
        57,
        242,
        239,
        183,
        14,
        102,
        88,
        208,
        228,
        166,
        119,
        114,
        248,
        235,
        117,
        75,
        10,
        49,
        68,
        80,
        180,
        143,
        237,
        31,
        26,
        219,
        153,
        141,
        51,
        159,
        17,
        131,
        20,
    ]
)


def md2(data: bytes) -> bytes:
    """Return the 16-byte MD2 digest of ``data`` (RFC 1319)."""
    checksum = bytearray(16)
    x = bytearray(48)

    # Pad: append N bytes of value N, where N = 16 - (len % 16).
    pad_len = 16 - (len(data) % 16)
    padded = data + bytes([pad_len] * pad_len)

    # Process each 16-byte block: update X state and checksum.
    prev_l = 0
    for offset in range(0, len(padded), 16):
        block = padded[offset : offset + 16]
        for j in range(16):
            x[16 + j] = block[j]
            x[32 + j] = block[j] ^ x[j]
            checksum[j] ^= _MD2_S[block[j] ^ prev_l]
            prev_l = checksum[j]

        t = 0
        for j in range(18):
            for k in range(48):
                x[k] ^= _MD2_S[t]
                t = x[k]
            t = (t + j) & 0xFF

    # Final block: process the checksum as a 16-byte message block.
    for j in range(16):
        x[16 + j] = checksum[j]
        x[32 + j] = checksum[j] ^ x[j]

    t = 0
    for j in range(18):
        for k in range(48):
            x[k] ^= _MD2_S[t]
            t = x[k]
        t = (t + j) & 0xFF

    return bytes(x[:16])
