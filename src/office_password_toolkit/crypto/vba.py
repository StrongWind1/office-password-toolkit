# SPDX-License-Identifier: Apache-2.0
"""VBA project-protection password codec and verifier ([MS-OVBA]).

This module handles the *VBA project* password -- the "Lock project for viewing"
toggle in the VBE (Alt+F11 -> Tools -> VBAProject Properties -> Protection). It
is **not** the document-open password and protects nothing at the data level:
the macro source is stored compressed-but-unencrypted, so the fastest recovery
is almost always a bypass (see :func:`unprotected_project_state`), then a
cleartext decode, and only as a last resort a crack of the SHA-1 verifier.

Three protection lines in the INI-style ``PROJECT`` stream carry obfuscated
values as double-quoted uppercase-hex strings, all wrapped by the single
reversible "Data Encryption" codec of [MS-OVBA] Section 2.4.3:

* ``CMG=`` ProjectProtectionState  ([MS-OVBA] Section 2.3.1.15) -- 4-byte bitfield.
* ``DPB=`` ProjectPassword         ([MS-OVBA] Section 2.3.1.16) -- plaintext password,
  a 29-byte Password Hash Data Structure, or a no-password sentinel.
* ``GC=``  ProjectVisibilityState  ([MS-OVBA] Section 2.3.1.17) -- 1-byte flag.

The de-obfuscation wrapper is deterministic and keyed only by public values, so
anyone can invert it. The one genuine cryptographic primitive is the hash-case
``DPB`` verifier, ``SHA1(mbcs(password) || Key)`` ([MS-OVBA] Section 2.4.4.4) --
a single-pass salted SHA-1 that maps exactly onto hashcat mode ``110``
(``sha1($pass.$salt)``) with the 4-byte ``Key`` as the salt.

Encoding note: unlike the UTF-16LE used by [MS-OFFCRYPTO] document passwords, the
VBA project password is hashed as MBCS bytes in the ``PROJECTCODEPAGE`` code page
([MS-OVBA] Section 2.4.4.4 / Section 2.3.4.2.1.5) -- Windows-1252 on Western
installs. There is no UTF-16 anywhere in this scheme.
"""

from __future__ import annotations

import hashlib
import logging
from typing import Final

logger = logging.getLogger(__name__)

# --- Wrapper constants ([MS-OVBA] Section 2.4.3) ---

# The Data Encryption wrapper version; Version = Seed XOR VersionEnc MUST be 2.
_VERSION: Final = 0x02

# The all-zero CLSID that [MS-OVBA] Section 2.3.1.2/Section 2.3.1.16 force whenever
# DPB stores a password hash: "{00000000-0000-0000-0000-000000000000}". Its ASCII
# byte-sum (1*0x7B + 32*0x30 + 4*0x2D + 1*0x7D = 1964 = 0x07AC) has low byte 0xAC.
_ALL_ZERO_CLSID: Final = "{00000000-0000-0000-0000-000000000000}"

# Default MBCS code page for the password bytes ([MS-OVBA] Section 2.3.4.2.1.5).
# Western installs use Windows-1252; East-Asian installs use a DBCS code page.
_DEFAULT_CODEPAGE: Final = "cp1252"

# --- Password Hash Data Structure constants ([MS-OVBA] Section 2.4.4.1) ---

_HASH_STRUCT_LEN: Final = 29  # 1 Reserved + 3 grbit + 4 Key + 20 hash + 1 term.
_RESERVED: Final = 0xFF  # Struct byte 0; MUST be 0xFF, ignored on read.
_TERMINATOR: Final = 0x00  # Struct byte 28; MUST be 0x00.
_KEY_LEN: Final = 4  # The 4-byte Key acts as the salt.
_HASH_LEN: Final = 20  # SHA-1 digest length ([RFC3174]).


# --- ProjKey checksum ([MS-OVBA] Section 2.4.3.1) ---


def project_key(proj_id: str) -> int:
    """Return ProjKey: the low byte of the sum of the ProjectId CLSID bytes.

    Per [MS-OVBA] Section 2.4.3.1 the wrapper's ProjKey is a byte-sum checksum of
    the ``ID=`` CLSID text *including the braces and the four hyphens* -- the exact
    characters between the quotes. Empirically pinned by the spec's own Section 3.1.6
    example ``{917DED54-440B-4FD1-A5C1-74ACF261E600}`` -> ``0xDF``. When ``DPB``
    holds a password hash the CLSID is forced to all zeros, giving the fixed
    constant ``0xAC``.
    """
    total = 0
    for char_byte in proj_id.encode("ascii"):
        total = (total + char_byte) & 0xFF
    return total


# --- Data Encryption codec ([MS-OVBA] Section 2.4.3.2 / Section 2.4.3.3) ---


def decode_data_encryption(hex_str: str) -> bytes:
    """Decode a Data Encryption wrapper (a ``DPB``/``CMG``/``GC`` hex value) to its payload.

    Implements the decryption of [MS-OVBA] Section 2.4.3.3. The seeded, self-chaining
    XOR stream is fully invertible from public values: ``Seed`` is the first byte,
    ``Version`` is the constant 2, and ``ProjKey`` is recovered as ``Seed XOR
    ProjKeyEnc`` -- so no external key is needed to read the payload. The returned
    bytes are the decrypted ``Data`` field, i.e. the raw payload:

    * a 4-byte protection bitfield for ``CMG``,
    * a 1-byte visibility flag for ``GC``,
    * a null-terminated MBCS password, a 29-byte Password Hash Data Structure, or
      the single ``0x00`` no-password sentinel for ``DPB``.
    """
    enc = bytes.fromhex(hex_str)
    logger.debug("decode: %d hex chars (%d bytes)", len(hex_str), len(enc))

    # [MS-OVBA] Section 2.4.3.3: seed the running state from the three header bytes.
    seed = enc[0]
    version_enc = enc[1]
    proj_key_enc = enc[2]
    proj_key = seed ^ proj_key_enc

    # The rolling feedback registers. UnencByte1/EncByte1/EncByte2 track the last
    # decrypted byte and the two most recent encrypted bytes respectively.
    unenc_byte1 = proj_key
    enc_byte1 = proj_key_enc
    enc_byte2 = version_enc

    # IgnoredLength = (Seed AND 6) / 2 filler bytes follow, then a 4-byte length,
    # then the payload. Every byte uses the same feedback: D = E XOR (EncByte2 + UnencByte1).
    idx = 3

    def _next() -> int:
        """Decrypt the next byte using the rolling XOR feedback state."""
        nonlocal idx, enc_byte1, enc_byte2, unenc_byte1
        enc_val = enc[idx]
        idx += 1
        dec_val = enc_val ^ ((enc_byte2 + unenc_byte1) & 0xFF)
        enc_byte2 = enc_byte1
        enc_byte1 = enc_val
        unenc_byte1 = dec_val
        return dec_val

    ignored_len = (seed & 6) // 2
    for _ in range(ignored_len):
        _next()  # Consume and discard the filler bytes.

    # DataLengthEnc is a little-endian uint32.
    length = 0
    for k in range(4):
        length += _next() * (256**k)

    return bytes(_next() for _ in range(length))


def encode_data_encryption(plaintext: bytes, seed: int, proj_key: int) -> str:
    """Encode ``plaintext`` into a Data Encryption wrapper hex string (inverse of decode).

    Implements [MS-OVBA] Section 2.4.3.2. Emits ``Seed``, ``VersionEnc`` (= Seed XOR 2),
    ``ProjKeyEnc`` (= Seed XOR ProjKey), the ``(Seed AND 6)/2`` filler bytes (set to
    ``0x00`` here), the little-endian 4-byte length, and the encrypted payload. Used
    to build unprotected/no-password states and to round-trip test the decoder.
    """
    seed &= 0xFF
    proj_key &= 0xFF
    version_enc = seed ^ _VERSION
    proj_key_enc = seed ^ proj_key

    out = bytearray([seed, version_enc, proj_key_enc])

    # Same rolling state as the decoder, seeded identically ([MS-OVBA] Section 2.4.3.2).
    unenc_byte1 = proj_key
    enc_byte1 = proj_key_enc
    enc_byte2 = version_enc

    def _emit(plain: int) -> None:
        """Encrypt one byte and append it to the output buffer."""
        nonlocal enc_byte1, enc_byte2, unenc_byte1
        enc_val = plain ^ ((enc_byte2 + unenc_byte1) & 0xFF)
        out.append(enc_val)
        enc_byte2 = enc_byte1
        enc_byte1 = enc_val
        unenc_byte1 = plain

    ignored_len = (seed & 6) // 2
    for _ in range(ignored_len):
        _emit(0x00)  # Filler content is discarded on decode; zeros keep it deterministic.

    length = len(plaintext)
    for k in range(4):
        _emit((length >> (8 * k)) & 0xFF)  # DataLength, little-endian.

    for byte in plaintext:
        _emit(byte)

    return out.hex().upper()


# --- Encode / Decode Nulls ([MS-OVBA] Section 2.4.4.2 / Section 2.4.4.3) ---


def _encode_nulls(key: bytes, password_hash: bytes) -> bytes:
    """Pack ``Key`` + ``PasswordHash`` into the 24-bit grbit + no-null byte layout.

    Per [MS-OVBA] Section 2.4.4.2: each source byte that is ``0x00`` is stored as
    ``0x01`` with its companion grbit bit cleared; any other byte is stored verbatim
    with the grbit bit set. The bits pack GrbitKey (4 bits, Key byte 0 first) then
    GrbitHashNull (20 bits, hash byte 0 first) MSB-first into a 24-bit field.

    Returns the three grbit bytes followed by KeyNoNulls (4) and PasswordHashNoNulls
    (20) -- i.e. struct bytes 1..27. When neither Key nor hash contains a ``0x00``
    the grbit field is simply ``FF FF FF``.
    """
    grbit = 0
    no_nulls = bytearray()
    # Key bits occupy the top 4, hash bits the next 20 (Section 2.4.4.1 packing).
    for byte in key + password_hash:
        grbit <<= 1
        if byte == 0x00:
            no_nulls.append(0x01)  # Null placeholder; grbit bit stays 0.
        else:
            grbit |= 1
            no_nulls.append(byte)
    return grbit.to_bytes(3, "big") + bytes(no_nulls)


def _decode_nulls(grbit_and_nonulls: bytes) -> tuple[bytes, bytes]:
    """Restore ``Key`` and ``PasswordHash`` from the grbit + no-null layout.

    Inverse of :func:`_encode_nulls` ([MS-OVBA] Section 2.4.4.3): reads the 24-bit
    big-endian grbit field, then for each of the 24 positions substitutes ``0x00``
    when the bit is 0 or takes the next no-null byte when it is 1.
    """
    grbit = int.from_bytes(grbit_and_nonulls[:3], "big")
    # KeyNoNulls (4) and PasswordHashNoNulls (20) are stored at fixed positions with
    # any 0x00 written as 0x01 -- they are NOT a compacted stream. Each byte position
    # maps to one grbit bit: bit 0 restores 0x00, bit 1 keeps the stored byte.
    body = grbit_and_nonulls[3:]
    restored = bytes(body[pos] if (grbit >> (23 - pos)) & 1 else 0x00 for pos in range(24))
    return restored[:_KEY_LEN], restored[_KEY_LEN:]


# --- Password verifier ([MS-OVBA] Section 2.4.4.4) ---


def password_hash(password: str, key: bytes, codepage: str = _DEFAULT_CODEPAGE) -> bytes:
    """Return ``SHA1(mbcs(password) || Key)`` -- the 20-byte VBA password hash.

    Implements [MS-OVBA] Section 2.4.4.4: the password is encoded as MBCS bytes in
    the ``PROJECTCODEPAGE`` code page (Windows-1252 by default), the 4-byte ``Key``
    is appended as a salt, and a single SHA-1 pass ([RFC3174]) produces the digest.
    This is exactly the primitive hashcat mode 110 (``sha1($pass.$salt)``) computes.

    The raw digest is returned; the Section 2.4.4.2 Encode-Nulls transform is applied
    only when this hash is *stored* in the Password Hash Data Structure (see
    :func:`build_password_hash_structure`), never to the hash input -- applying it to
    the digest would break hashcat -m 110 compatibility.
    """
    # [MS-OVBA] Section 2.4.4.4 mandates SHA-1; usedforsecurity=False records that the
    # format -- not this code -- chose the primitive (satisfies ruff S324 honestly).
    return hashlib.new("sha1", password.encode(codepage) + key, usedforsecurity=False).digest()


def build_password_hash_structure(key: bytes, password_hash_bytes: bytes) -> bytes:
    """Assemble the 29-byte Password Hash Data Structure ([MS-OVBA] Section 2.4.4.1).

    Layout: ``Reserved`` (0xFF), 3 grbit bytes, ``KeyNoNulls`` (4), ``PasswordHashNoNulls``
    (20), ``Terminator`` (0x00). The Key and hash are passed through Encode Nulls
    (Section 2.4.4.2) before packing. This is the payload that Data Encryption wraps to
    produce a hash-case ``DPB`` value.
    """
    if len(key) != _KEY_LEN:
        msg = f"Key must be {_KEY_LEN} bytes, got {len(key)}"
        raise ValueError(msg)
    if len(password_hash_bytes) != _HASH_LEN:
        msg = f"PasswordHash must be {_HASH_LEN} bytes, got {len(password_hash_bytes)}"
        raise ValueError(msg)
    return bytes([_RESERVED]) + _encode_nulls(key, password_hash_bytes) + bytes([_TERMINATOR])


def parse_password_hash_structure(struct: bytes) -> tuple[bytes, bytes] | None:
    """Return ``(Key, PasswordHash)`` from a 29-byte hash struct, or ``None`` if it is not one.

    Validates the [MS-OVBA] Section 2.4.4.1 framing (length 29, Reserved 0xFF,
    Terminator 0x00) and runs Decode Nulls (Section 2.4.4.3) to recover the raw
    4-byte salt and 20-byte SHA-1 digest.
    """
    if len(struct) != _HASH_STRUCT_LEN or struct[0] != _RESERVED or struct[-1] != _TERMINATOR:
        return None
    return _decode_nulls(struct[1:-1])


# --- Extraction ([MS-OVBA] Section 2.4.4.5, hashcat -m 110 line) ---


def extract_vba_hash(dpb_value: str) -> str | None:
    """Emit the hashcat mode-110 line for a hash-case ``DPB``, or ``None`` otherwise.

    Decodes the ``DPB`` wrapper and, if the payload is a Password Hash Data Structure
    ([MS-OVBA] Section 2.4.4.1), returns ``"<sha1hex>:<keyhex>"`` for
    ``hashcat -m 110 --hex-salt``. Returns ``None`` when the ``DPB`` instead holds a
    cleartext password or the no-password sentinel -- those cases are a decode, not a
    crack, and must be reported separately. The project CLSID is not needed: the
    payload's ``ProjKey`` is carried in the wrapper itself.
    """
    payload = decode_data_encryption(dpb_value)
    parsed = parse_password_hash_structure(payload)
    if parsed is None:
        logger.debug("hash: no hash (cleartext or no-password)")
        return None
    key, digest = parsed
    logger.debug("hash: SHA-1 extracted, key=%s", key.hex())
    return f"{digest.hex()}:{key.hex()}"


def unified_vba_line(dpb_value: str) -> str | None:
    """Emit the self-describing ``$vba$*sha1*<hash>*<salt>`` line, or ``None`` if not a hash case.

    Grammar (docs/reference/hash-formats.md):
    ``$vba$*<hashfunc>*<hash_hex>*<salt_hex>``

    SHA-1 is the only hash the VBA spec mandates ([MS-OVBA] Section 2.4.4.4). The 4-byte
    ``Key`` is the salt, appended after the MBCS password bytes before the single SHA-1 pass.
    Returns ``None`` when the ``DPB`` holds a cleartext password or the no-password sentinel.
    """
    payload = decode_data_encryption(dpb_value)
    parsed = parse_password_hash_structure(payload)
    if parsed is None:
        return None
    key, digest = parsed
    return f"$vba$*sha1*{digest.hex()}*{key.hex()}"


# --- Bypass helper ([MS-OVBA] Section 2.3.1.15-17) ---


def unprotected_project_state() -> str:
    """Return ``CMG``/``DPB``/``GC`` PROJECT-stream lines representing an unprotected project.

    Because the macro source is stored unencrypted, clearing the protection triple
    lets the VBE open the project without any password. This returns the three lines
    for the "clear" state:

    * ``CMG`` -> 4-byte bitfield ``00000000`` (no ``fUserProtected``/``fHostProtected``/``fVBEProtected`` bit set),
    * ``DPB`` -> the no-password sentinel (``Length=1``, ``Data=0x00``, [MS-OVBA] Section 2.3.1.16),
    * ``GC``  -> visibility flag ``0xFF`` (project visible, [MS-OVBA] Section 2.3.1.17).

    The values are encoded with the all-zero-CLSID ProjKey (``0xAC``), matching the
    hash-case convention. For a bypass on a specific target that keeps its real
    CLSID, re-encode each payload with ``encode_data_encryption(payload, seed,
    project_key(real_id))``, or simply copy a known-unprotected triple / rename the
    ``DPB`` key so the parser fails open.
    """
    proj_key = project_key(_ALL_ZERO_CLSID)
    seed = 0xAB  # Any value works; fixed for deterministic output.
    cmg = encode_data_encryption(b"\x00\x00\x00\x00", seed, proj_key)
    dpb = encode_data_encryption(b"\x00", seed, proj_key)
    gc = encode_data_encryption(b"\xff", seed, proj_key)
    return f'CMG="{cmg}"\nDPB="{dpb}"\nGC="{gc}"'
