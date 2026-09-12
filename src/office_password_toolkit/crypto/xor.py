# SPDX-License-Identifier: Apache-2.0
"""Legacy XOR-obfuscation password primitives ([MS-OFFCRYPTO] Section 2.3.7).

This module implements the whole legacy "XOR obfuscation" family used by the
binary Office formats (Excel 97-2003 ``.xls``, Word 97-2003 ``.doc``):

* The 16-bit verifier (Method 1, Excel) -- a bespoke rotate-and-XOR feedback
  over the ANSI password bytes, finalised by XOR with ``0xCE4B``.
* The 16-bit ``XorKey`` -- an intermediate value folded out of fixed lookup
  tables (``InitialCode`` / ``XorMatrix``), stored by Excel and forming the
  high half of the Word verifier.
* The 16-byte obfuscation array -- the repeating pad the document body is
  XORed against. It is derived purely from the password, so recovering it
  (and thus decoding the file) never requires knowing the password itself.
* The 32-bit verifier (Method 2, Word) -- ``(XorKey << 16) | verifier16``,
  stored verbatim in ``FibBase.lKey``.
* The Method 1 body transform (XOR + 8-bit rotate) used to decode/encode the
  obfuscated stream regions.

None of this is cryptographically strong: the verifiers are short, unsalted,
non-iterated checksums, and the body transform is fully reversible from the
password-derived array. These primitives exist to *collide* a matching
password or to *bypass* the obfuscation entirely, not to slow-hash-crack.

Passwords here are single-byte (ANSI) strings of length 0-15 -- NOT the
UTF-16LE encoding used by newer Office crypto. For pure-ASCII input the byte
value equals the character value; non-ASCII input is reduced to single bytes
per [MS-OFFCRYPTO] Section 2.3.7.4 (out of scope for these helpers, which take
the already-reduced latin-1 form).
"""

from __future__ import annotations

import itertools
import logging
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = logging.getLogger(__name__)

# --- Method 1 verifier constants ([MS-OFFCRYPTO] Section 2.3.7.1) ---

# Finalisation constant XORed into the folded register.
_XOR_FINAL: Final = 0xCE4B
# The verifier feedback register is 15 bits wide: the high bit (bit 14) rotates
# back into bit 0 on each shift, and bit 15 is always cleared.
_MASK_15: Final = 0x7FFF
_HIGH_BIT: Final = 0x4000
# The obfuscation array is always exactly 16 bytes ([MS-OFFCRYPTO] Section 2.3.7.2).
_XOR_ARRAY_LEN: Final = 16

# --- XorKey / obfuscation-array tables ([MS-OFFCRYPTO] Section 2.3.7.2) ---
# Reproduced verbatim from the CreateXorArray_Method1 pseudocode. These are
# fixed compile-time tables -- there is no salt or per-file material.

# 15 pad bytes appended after the password to fill the 16-byte array.
_PAD_ARRAY: Final[tuple[int, ...]] = (
    0xBB, 0xFF, 0xFF, 0xBA, 0xFF, 0xFF, 0xB9, 0x80,
    0x00, 0xBE, 0x0F, 0x00, 0xBF, 0x0F, 0x00,
)  # fmt: skip

# 15 seed words, indexed by (password length - 1), that seed the XorKey fold.
_INITIAL_CODE: Final[tuple[int, ...]] = (
    0xE1F0, 0x1D0F, 0xCC9C, 0x84C0, 0x110C,
    0x0E10, 0xF1CE, 0x313E, 0x1872, 0xE139,
    0xD40F, 0x84F9, 0x280C, 0xA96A, 0x4EC3,
)  # fmt: skip

# 105 mixing words consumed 7-at-a-time per password character, walking DOWN
# from index 0x68 (=104). A 15-char password consumes all 105 entries.
_XOR_MATRIX: Final[tuple[int, ...]] = (
    0xAEFC, 0x4DD9, 0x9BB2, 0x2745, 0x4E8A, 0x9D14, 0x2A09,
    0x7B61, 0xF6C2, 0xFDA5, 0xEB6B, 0xC6F7, 0x9DCF, 0x2BBF,
    0x4563, 0x8AC6, 0x05AD, 0x0B5A, 0x16B4, 0x2D68, 0x5AD0,
    0x0375, 0x06EA, 0x0DD4, 0x1BA8, 0x3750, 0x6EA0, 0xDD40,
    0xD849, 0xA0B3, 0x5147, 0xA28E, 0x553D, 0xAA7A, 0x44D5,
    0x6F45, 0xDE8A, 0xAD35, 0x4A4B, 0x9496, 0x390D, 0x721A,
    0xEB23, 0xC667, 0x9CEF, 0x29FF, 0x53FE, 0xA7FC, 0x5FD9,
    0x47D3, 0x8FA6, 0x0F6D, 0x1EDA, 0x3DB4, 0x7B68, 0xF6D0,
    0xB861, 0x60E3, 0xC1C6, 0x93AD, 0x377B, 0x6EF6, 0xDDEC,
    0x45A0, 0x8B40, 0x06A1, 0x0D42, 0x1A84, 0x3508, 0x6A10,
    0xAA51, 0x4483, 0x8906, 0x022D, 0x045A, 0x08B4, 0x1168,
    0x76B4, 0xED68, 0xCAF1, 0x85C3, 0x1BA7, 0x374E, 0x6E9C,
    0x3730, 0x6E60, 0xDCC0, 0xA9A1, 0x4363, 0x86C6, 0x1DAD,
    0x3331, 0x6662, 0xCCC4, 0x89A9, 0x0373, 0x06E6, 0x0DCC,
    0x1021, 0x2042, 0x4084, 0x8108, 0x1231, 0x2462, 0x48C4,
)  # fmt: skip

# Top index into _XOR_MATRIX where the per-character walk begins.
_MATRIX_TOP: Final = 0x68

# Maximum password length the format supports.
_MAX_PASSWORD_LEN: Final = 15


def _password_bytes(password: str) -> bytes:
    """Reduce a password string to its single-byte (ANSI) form.

    Legacy XOR obfuscation operates on single-byte characters, not UTF-16LE.
    We map via latin-1 (identity for code points 0x00-0xFF); callers needing
    the full [MS-OFFCRYPTO] Section 2.3.7.4 locale reductions must pre-reduce.
    """
    return password.encode("latin-1", errors="replace")


def _ror8(value: int) -> int:
    """Rotate an 8-bit value right by one bit (the spec's ``Ror`` helper).

    Per [MS-OFFCRYPTO] Section 2.3.7.2: ``(byte / 2) | (byte * 128)`` mod 0x100.
    """
    return ((value >> 1) | (value << 7)) & 0xFF


def _xor_ror(byte1: int, byte2: int) -> int:
    """Return ``Ror(byte1 XOR byte2)`` -- the spec's ``XorRor`` helper.

    Used to fold each password/pad byte into an obfuscation-array slot
    ([MS-OFFCRYPTO] Section 2.3.7.2).
    """
    return _ror8(byte1 ^ byte2)


def password_verifier_method1(password: str) -> int:
    """Return the 16-bit XOR-obfuscation verifier for ``password``.

    Implements ``CreatePasswordVerifier_Method1`` ([MS-OFFCRYPTO] Section 2.3.7.1):
    the password bytes (length-prefixed, ANSI, processed in reverse) are folded
    through a 15-bit rotate-left-and-XOR, then XORed with ``0xCE4B``. This is the
    verifier Excel stores for legacy XOR "password to open" and the 16-bit
    protection records.
    """
    body = _password_bytes(password)
    # PasswordArray = [length byte] ++ password bytes.
    array = bytes([len(body) & 0xFF]) + body
    verifier = 0
    # Fold every byte in REVERSE order: 15-bit left-rotate then XOR the byte.
    for byte in reversed(array):
        wrapped = 1 if verifier & _HIGH_BIT else 0
        verifier = (((verifier << 1) & _MASK_15) | wrapped) ^ byte
    return verifier ^ _XOR_FINAL


def create_xor_key_method1(password: str) -> int:
    """Return the 16-bit ``XorKey`` for ``password``.

    Implements ``CreateXorKey_Method1`` ([MS-OFFCRYPTO] Section 2.3.7.2): seed
    from ``InitialCode[len-1]`` then, for each password byte in reverse, run 7
    conditional XORs against ``XorMatrix`` entries walked downward from index
    ``0x68``. Excel stores this value directly (``XORObfuscation.key``) and it
    forms the high 16 bits of the Word 32-bit verifier. It is also the source
    of the ``Hi``/``Lo`` bytes that build the 16-byte obfuscation array.
    """
    body = _password_bytes(password)
    # The spec is undefined for the empty/oversized password; guard the index.
    if not body or len(body) > _MAX_PASSWORD_LEN:
        msg = f"password length must be 1..{_MAX_PASSWORD_LEN}, got {len(body)}"
        raise ValueError(msg)
    xor_key = _INITIAL_CODE[len(body) - 1]
    current = _MATRIX_TOP
    for char in reversed(body):
        c = char
        for _ in range(7):
            # Only mix in the matrix word when bit 6 of the (shifting) char is set.
            if c & 0x40:
                xor_key ^= _XOR_MATRIX[current]
            c = (c * 2) & 0xFF  # left-shift within an 8-bit register
            current -= 1
    return xor_key & 0xFFFF


def create_xor_array_method1(password: str) -> bytes:
    """Return the 16-byte obfuscation array for ``password``.

    Implements ``CreateXorArray_Method1`` ([MS-OFFCRYPTO] Section 2.3.7.2): the
    password bytes and ``PadArray`` bytes are each folded (via ``XorRor``) with
    alternating high/low bytes of the ``XorKey`` into a fixed 16-slot layout.
    The document body is later XORed against this array (see ``xor_decode_method1``),
    so possessing it is sufficient to decode the file without the password.
    """
    body = _password_bytes(password)
    if not body or len(body) > _MAX_PASSWORD_LEN:
        msg = f"password length must be 1..{_MAX_PASSWORD_LEN}, got {len(body)}"
        raise ValueError(msg)
    xor_key = create_xor_key_method1(password)
    hi = (xor_key >> 8) & 0xFF  # most significant byte of XorKey
    lo = xor_key & 0xFF  # least significant byte of XorKey
    n = len(body)
    obf = bytearray(16)

    index = n
    # Odd-length passwords place one leading pad byte + the final password byte.
    if index % 2 == 1:
        obf[index] = _xor_ror(_PAD_ARRAY[0], hi)
        index -= 1
        obf[index] = _xor_ror(body[n - 1], lo)
    # Walk the remaining password bytes downward, two per turn (Hi then Lo).
    while index > 0:
        index -= 1
        obf[index] = _xor_ror(body[index], hi)
        index -= 1
        obf[index] = _xor_ror(body[index], lo)
    # Fill the tail with PadArray bytes, again alternating Hi/Lo.
    index = 15
    pad_index = 15 - n
    while pad_index > 0:
        obf[index] = _xor_ror(_PAD_ARRAY[pad_index], hi)
        index -= 1
        pad_index -= 1
        obf[index] = _xor_ror(_PAD_ARRAY[pad_index], lo)
        index -= 1
        pad_index -= 1
    return bytes(obf)


def password_verifier_method2(password: str) -> int:
    """Return the 32-bit Word XOR-obfuscation verifier (``FibBase.lKey``).

    Implements ``CreatePasswordVerifier_Method2`` ([MS-OFFCRYPTO] Section 2.3.7.4):
    packs the ``XorKey`` into the high 16 bits and the Method 1 verifier into the
    low 16 bits. Word stores this whole 32-bit value in ``FibBase.lKey`` at offset
    0x0E of the ``WordDocument`` stream.
    """
    key_high = create_xor_key_method1(password)
    key_low = password_verifier_method1(password)
    return ((key_high << 16) | key_low) & 0xFFFFFFFF


def xor_decode_method1(data: bytes, xor_array: bytes, start_offset: int = 0) -> bytes:
    """Decode a Method 1 (Excel/Word) obfuscated body region.

    Implements ``DecryptData_Method1`` ([MS-OFFCRYPTO] Section 2.3.7.3): each byte
    is XORed with the current 16-byte-array element, then rotated right 5 bits;
    the array index advances (mod 16) for every byte consumed.

    ``start_offset`` seeds the rolling array index -- the Excel path indexes the
    array by the byte's true stream offset modulo 16, so a region that does not
    begin at a 16-byte boundary must pass its starting offset here.
    """
    if len(xor_array) != _XOR_ARRAY_LEN:
        msg = f"xor_array must be exactly 16 bytes, got {len(xor_array)}"
        raise ValueError(msg)
    out = bytearray(len(data))
    idx = start_offset % 16
    for i, byte in enumerate(data):
        value = byte ^ xor_array[idx]
        # Rotate the 8-bit result right by 5 (equivalently left by 3).
        value = ((value >> 5) | (value << 3)) & 0xFF
        out[i] = value
        idx = (idx + 1) % 16
    return bytes(out)


def xor_encode_method1(data: bytes, xor_array: bytes, start_offset: int = 0) -> bytes:
    """Encode a Method 1 body region -- the exact inverse of ``xor_decode_method1``.

    Implements ``EncryptData_Method1`` ([MS-OFFCRYPTO] Section 2.3.7.3): each byte
    is rotated left 5 bits, then XORed with the current array element. Provided so
    callers (and the round-trip self-test) can reproduce an obfuscated stream from
    plaintext.
    """
    if len(xor_array) != _XOR_ARRAY_LEN:
        msg = f"xor_array must be exactly 16 bytes, got {len(xor_array)}"
        raise ValueError(msg)
    out = bytearray(len(data))
    idx = start_offset % 16
    for i, byte in enumerate(data):
        # Rotate left 5 first, then XOR -- undoes the decode's XOR-then-ror5.
        value = ((byte << 5) | (byte >> 3)) & 0xFF
        out[i] = value ^ xor_array[idx]
        idx = (idx + 1) % 16
    return bytes(out)


def xor_transform_method2(data: bytes, xor_array: bytes, start_offset: int = 0) -> bytes:
    """Apply the Method 2 (Word) body transform to ``data`` ([MS-OFFCRYPTO] Section 2.3.7.6).

    Unlike the Excel Method 1 transform, Method 2 is a plain XOR against the 16-byte
    array with a skip rule and no rotate: a byte is left unchanged when its input
    value is ``0x00`` OR when ``input XOR arrayElement`` would be ``0x00`` -- otherwise
    it becomes ``input XOR arrayElement``. The array index still advances (mod 16) for
    every byte consumed, so a region that does not begin at a 16-byte boundary must
    pass its true stream offset via ``start_offset`` (the ``WordDocument`` stream keeps
    its first 68 bytes untransformed, so its body is transformed with ``start_offset=68``).

    Because XOR is symmetric and the skip rule is self-consistent, this single function
    is both the encode and the decode -- calling it twice returns the original bytes.
    """
    if len(xor_array) != _XOR_ARRAY_LEN:
        msg = f"xor_array must be exactly 16 bytes, got {len(xor_array)}"
        raise ValueError(msg)
    out = bytearray(len(data))
    idx = start_offset % 16
    for i, byte in enumerate(data):
        transformed = byte ^ xor_array[idx]
        # Per Section 2.3.7.6 the byte is untouched when input is 0x00 or the XOR
        # result is 0x00; every other byte takes the XOR value.
        out[i] = byte if byte == 0x00 or transformed == 0x00 else transformed
        idx = (idx + 1) % 16
    return bytes(out)


# --- Password-free obfuscation-array reconstruction (bypass without the password) ---


def _rol1(value: int) -> int:
    """Rotate an 8-bit value left by one bit -- the inverse of the spec's ``Ror``."""
    return ((value << 1) | (value >> 7)) & 0xFF


def _pad_array_positions(password_len: int, xor_key: int) -> dict[int, int]:
    """Return the obfuscation-array bytes that are fixed by ``PadArray`` alone.

    In ``CreateXorArray_Method1`` ([MS-OFFCRYPTO] Section 2.3.7.2) the password bytes
    occupy array positions ``0..N-1`` and the constant ``PadArray`` bytes occupy the
    remaining high positions. Those pad-derived bytes depend only on the stored
    ``XorKey`` (its ``Hi``/``Lo`` halves), never on the password, so they can be
    rebuilt for a bypass with no password in hand. Returns ``{position: byte}`` for
    exactly the pad positions of a length-``password_len`` password.
    """
    hi = (xor_key >> 8) & 0xFF
    lo = xor_key & 0xFF
    positions: dict[int, int] = {}
    index = 15
    pad_index = 15 - password_len
    # Mirror the pad-fill order of CreateXorArray_Method1 exactly.
    if password_len % 2 == 1:
        positions[password_len] = _xor_ror(_PAD_ARRAY[0], hi)
    while pad_index > 0:
        positions[index] = _xor_ror(_PAD_ARRAY[pad_index], hi)
        index -= 1
        pad_index -= 1
        positions[index] = _xor_ror(_PAD_ARRAY[pad_index], lo)
        index -= 1
        pad_index -= 1
    return positions


def _password_byte_from_array(position: int, array_byte: int, xor_key: int) -> int:
    """Invert one password-position array byte back to its ANSI password byte.

    Per ``CreateXorArray_Method1``, a password byte at ``position`` is stored as
    ``Ror(password_byte XOR K)`` where ``K`` is the low byte of ``XorKey`` at even
    positions and the high byte at odd positions ([MS-OFFCRYPTO] Section 2.3.7.2 /
    Section 2.3.7.5). Rotating left and XORing ``K`` back recovers the password byte.
    """
    k = (xor_key & 0xFF) if position % 2 == 0 else ((xor_key >> 8) & 0xFF)
    return _rol1(array_byte) ^ k


def reconstruct_password(xor_key: int, verifier: int, known_array: Sequence[int | None], max_brute: int = 2) -> str | None:
    """Recover the ANSI password of an XOR-obfuscated document without being given it.

    A bypass never receives the password, but the 16-byte obfuscation array is fully
    determined by the password, so recovering the array (or the password behind it) is
    enough to decode the body. ``known_array`` is a 16-element sequence of the array
    bytes the caller could pin from known plaintext (``None`` where unknown). This
    routine walks every possible password length, fills the pad positions from the
    stored ``XorKey`` (see :func:`_pad_array_positions`), inverts the known password
    positions, then brute-forces up to ``max_brute`` still-unknown password bytes.

    Correctness is NOT heuristic: each candidate is accepted only when it reproduces
    BOTH the stored 16-bit ``XorKey`` (``CreateXorKey_Method1``) and the stored 16-bit
    verifier (``CreatePasswordVerifier_Method1``) -- a 32-bit equality with negligible
    false-positive odds. Returns the recovered password (latin-1 text) or ``None`` when
    no length resolves within the brute budget.
    """
    if len(known_array) != _XOR_ARRAY_LEN:
        msg = f"known_array must have 16 entries, got {len(known_array)}"
        raise ValueError(msg)
    for length in range(1, _MAX_PASSWORD_LEN + 1):
        pad = _pad_array_positions(length, xor_key)
        # A length is impossible if the pad bytes it forces contradict known plaintext.
        if any(known_array[pos] not in (None, val) for pos, val in pad.items()):
            continue
        found = _try_length(xor_key, verifier, known_array, length, max_brute)
        if found is not None:
            logger.debug("reconstruct: xorKey=0x%04x verifier=0x%04x -> success (len=%d)", xor_key, verifier, length)
            return found
    logger.debug("reconstruct: xorKey=0x%04x verifier=0x%04x -> failed", xor_key, verifier)
    return None


def _try_length(xor_key: int, verifier: int, known_array: Sequence[int | None], length: int, max_brute: int) -> str | None:
    """Attempt to recover a password of exactly ``length`` bytes (helper for the walk)."""
    known: dict[int, int] = {}
    unknown: list[int] = []
    for pos in range(length):
        array_byte = known_array[pos]
        if array_byte is None:
            unknown.append(pos)
        else:
            known[pos] = _password_byte_from_array(pos, array_byte, xor_key)
    if len(unknown) > max_brute:
        return None  # too many free bytes to brute within budget -- fail honestly upstream
    for combo in itertools.product(range(256), repeat=len(unknown)):
        candidate = bytearray(length)
        for pos, value in known.items():
            candidate[pos] = value
        for pos, value in zip(unknown, combo, strict=True):
            candidate[pos] = value
        text = candidate.decode("latin-1")
        if create_xor_key_method1(text) == xor_key and password_verifier_method1(text) == verifier:
            return text
    return None
