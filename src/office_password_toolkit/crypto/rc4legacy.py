# SPDX-License-Identifier: Apache-2.0
"""Legacy binary-document RC4 "password to open" schemes for OLE2 Office files.

This module reproduces the two pre-OOXML RC4 document-open key derivations that
live in the Compound File Binary container ([MS-CFB]) of Word/Excel/PowerPoint
97-2003 files:

* **RC4 + MD5, 40-bit** -- Office 97/2000 ("Office Binary Document RC4
  Encryption", [MS-OFFCRYPTO] Section 2.3.6). hashcat modes 9700/9710/9720,
  hash tag ``$oldoffice$0`` (Word ``.doc``) / ``$oldoffice$1`` (Excel ``.xls``).
* **RC4 CryptoAPI + SHA-1** -- Office XP/2003 ("Office Binary Document RC4
  CryptoAPI Encryption", [MS-OFFCRYPTO] Section 2.3.5). hashcat modes
  9800/9810/9820, hash tag ``$oldoffice$3`` (40-bit key) / ``$oldoffice$4``
  (128-bit key).

Both derive an RC4 key from the UTF-16LE password and a 16-byte salt, then
decrypt a 16-byte verifier plus its stored hash to confirm a candidate. Neither
KDF is iterated (there is no spin count), which is what makes these formats
cheap per candidate -- the 40-bit variants additionally have only a 2^40 key
space, so the document key can be brute-forced directly without the password.

Design notes:

* Passwords are encoded UTF-16LE with no BOM and no NUL terminator, as every
  Microsoft Office scheme requires.
* All container integers are little-endian.
* The 40-bit RC4 scheme truncates hashes to 5 bytes twice; the CryptoAPI scheme
  truncates ``Hfinal`` once and zero-pads a 40-bit key up to 16 bytes.
* MD5 and SHA-1 are called with ``usedforsecurity=False``. These are the legacy
  primitives the on-disk format mandates; we are reproducing a broken scheme to
  audit it, not protecting anything -- and the flag keeps the hashes available
  even on FIPS-restricted interpreters.
"""

from __future__ import annotations

import logging
import struct
from dataclasses import dataclass
from enum import StrEnum
from typing import Final

from office_password_toolkit.crypto.ciphers import rc4 as rc4_crypt
from office_password_toolkit.crypto.hashes import digest as _digest

logger = logging.getLogger(__name__)

# --- Shared constants ---

# Every hashcat "$oldoffice$" line begins with this 11-byte ASCII signature.
_SIGNATURE: Final = "$oldoffice$"

# Passwords are hashed as UTF-16LE (no BOM, no NUL) for all MS Office schemes.
_PW_ENCODING: Final = "utf-16-le"

# Salt is a fixed 16-byte array in both schemes ([MS-OFFCRYPTO] Section 2.3.6.1 / Section 2.3.3).
_SALT_LEN: Final = 16
# The RC4 key schedule is always seeded with 16 bytes (128-bit schedule).
_RC4_KEY_LEN: Final = 16
# Both schemes encrypt a random 16-byte Verifier.
_VERIFIER_LEN: Final = 16
# MD5 verifier hash is 16 bytes; the CryptoAPI SHA-1 verifier hash is 20 bytes.
_MD5_HASH_LEN: Final = 16
_SHA1_HASH_LEN: Final = 20

# In-place stream encryption re-keys every 512 bytes with an incrementing block
# number ([MS-OFFCRYPTO] Section 2.3.6 / Section 2.3.5; the verifier uses block 0).
_INPLACE_BLOCK_SIZE: Final = 512

# --- RC4 + MD5 (Office 97/2000) constants ---

# H0 and H1 are both truncated to their first 5 bytes = 40 bits ([MS-OFFCRYPTO] Section 2.3.6.2).
_MD5_TRUNC_LEN: Final = 5
# The 21-byte block (t0 || salt) is replicated 16 times into a 336-byte buffer.
_MD5_BLOCK_REPEAT: Final = 16
# Accepted version digits for the MD5 scheme: 0 = Word doc, 1 = Excel xls.
_MD5_VERSION_DIGITS: Final = frozenset({0, 1})

# --- RC4 CryptoAPI + SHA-1 (Office XP/2003) constants ---

# Algorithm identifiers stored in the EncryptionHeader ([MS-OFFCRYPTO] Section 2.3.2).
_ALG_ID_RC4: Final = 0x0000_6801  # AlgID: RC4 stream cipher.
_ALG_ID_HASH_SHA1: Final = 0x0000_8004  # AlgIDHash: SHA-1.

# EncryptionHeaderFlags bits ([MS-OFFCRYPTO] Section 2.3.1).
_FLAG_FCRYPTOAPI: Final = 0x04  # Set for the CryptoAPI RC4/AES families.
_FLAG_FAES: Final = 0x20  # Set only by the AES standard/agile schemes, never by RC4.

# The two RC4 key sizes hashcat can represent, and their "$oldoffice$" version digit.
_KEYSIZE_40: Final = 40  # -> $oldoffice$3
_KEYSIZE_128: Final = 128  # -> $oldoffice$4
# Per [MS-OFFCRYPTO] Section 2.3.5, the spec allows key sizes 40-128 in 8-bit
# steps. The $oldoffice$ digit: 3 = 40-bit (zero-padded to 128-bit RC4 key),
# 4 = any size > 40-bit (key is Hfinal[:keyBits/8], no padding).
_CRYPTOAPI_VERSION_BY_KEYSIZE: Final = {_KEYSIZE_40: 3, _KEYSIZE_128: 4}
# 40-bit keys are Hfinal[0:5] padded with 11 zero bytes up to the 16-byte schedule.
_KEY40_REAL_BYTES: Final = 5
_KEY40_ZERO_PAD: Final = _RC4_KEY_LEN - _KEY40_REAL_BYTES

# EncryptionVersionInfo words that select each scheme ([MS-OFFCRYPTO] Section 2.3.5.1 / Section 2.3.6.1).
_MD5_VERSION_WORDS: Final = (1, 1)  # (vMajor, vMinor) for the 40-bit RC4+MD5 scheme.
_CRYPTOAPI_VMINOR: Final = 2
_CRYPTOAPI_VMAJORS: Final = frozenset({2, 3, 4})


class Rc4Scheme(StrEnum):
    """The two legacy RC4 document-open families this module implements."""

    MD5 = "rc4-md5"  # Office 97/2000, MD5 KDF, 40-bit key (Section 2.3.6).
    CRYPTOAPI = "rc4-cryptoapi"  # Office XP/2003, SHA-1 KDF, 40- or 128-bit key (Section 2.3.5).


# --- RC4 + MD5, 40-bit (Office 97/2000, $oldoffice$0 / $oldoffice$1) ---


def rc4_md5_derive_key(password: str, salt: bytes, block: int = 0) -> bytes:
    """Derive the 128-bit RC4 key for the 40-bit MD5 scheme ([MS-OFFCRYPTO] Section 2.3.6.2).

    Steps, password -> 16-byte RC4 key:

    1. ``t0 = MD5(UTF-16LE(password))[:5]`` -- keep the first 40 bits of H0.
    2. Replicate the 21-byte block ``t0 || salt`` 16 times into a 336-byte buffer
       and hash it: ``t1 = MD5(buffer)[:5]`` -- the first 40 bits of H1.
    3. ``Hfinal = MD5(t1 || LE32(block))``. The block number is PREPENDED-free
       here -- it is appended after ``t1`` as a 4-byte little-endian counter and
       is 0 for the verifier.
    4. The RC4 key is ``Hfinal[:16]``.

    Args:
        password: The document-open password (plain text).
        salt: The 16-byte KDF salt from the encryption header.
        block: 32-bit block number; 0 for the verifier, incrementing per
            512-byte body block during in-place stream decryption.

    Returns:
        The 16-byte RC4 key for the requested block.

    """
    pw_bytes = password.encode(_PW_ENCODING)
    # H0 -> first 40 bits. Everything past byte 5 is discarded (the 40-bit cap).
    t0 = _digest("md5", pw_bytes)[:_MD5_TRUNC_LEN]
    # 21-byte (t0 || salt) block repeated 16 times = 336 bytes. Note: t0 first, salt second.
    intermediate = (t0 + salt) * _MD5_BLOCK_REPEAT
    t1 = _digest("md5", intermediate)[:_MD5_TRUNC_LEN]
    # Append the little-endian block number, then hash the 9-byte input.
    block_le = struct.pack("<I", block)
    hfinal = _digest("md5", t1 + block_le)
    return hfinal[:_RC4_KEY_LEN]


def rc4_md5_verify(password: str, salt: bytes, enc_verifier: bytes, enc_verifier_hash: bytes) -> bool:
    """Return ``True`` iff ``password`` opens a 40-bit RC4+MD5 document ([MS-OFFCRYPTO] Section 2.3.6.4).

    Derives the block-0 key, RC4-decrypts the concatenated verifier and verifier
    hash in one continuous keystream (the cipher state is NOT reset between the
    two fields), then checks ``MD5(Verifier) == storedHash`` over all 16 bytes.
    """
    key = rc4_md5_derive_key(password, salt, 0)
    # One RC4 call over verifier(16) || verifierHash(16): the keystream is continuous.
    decrypted = rc4_crypt(key, enc_verifier + enc_verifier_hash)
    verifier = decrypted[:_VERIFIER_LEN]
    stored_hash = decrypted[_VERIFIER_LEN : _VERIFIER_LEN + _MD5_HASH_LEN]
    result = _digest("md5", verifier) == stored_hash
    logger.debug("rc4-md5 verify: %s", "pass" if result else "fail")
    return result


def rc4_md5_hash_line(version_digit: int, salt: bytes, enc_verifier: bytes, enc_verifier_hash: bytes) -> str:
    """Format the hashcat 9700 (``$oldoffice$0`` / ``$oldoffice$1``) hash line.

    Grammar (rc4-md5 Section 7)::

        $oldoffice$<ver>*<salt>*<encryptedVerifier>*<encryptedVerifierHash>

    ``ver`` is 0 for Word ``.doc`` and 1 for Excel ``.xls``; the crypto is
    identical, the digit is informational metadata only. Salt, verifier, and
    verifier hash are each emitted as 32 lowercase hex characters (16 bytes).
    """
    if version_digit not in _MD5_VERSION_DIGITS:
        msg = f"rc4-md5 version digit must be 0 or 1, got {version_digit}"
        raise ValueError(msg)
    return f"{_SIGNATURE}{version_digit}*{salt.hex()}*{enc_verifier.hex()}*{enc_verifier_hash.hex()}"


# --- RC4 CryptoAPI + SHA-1 (Office XP/2003, $oldoffice$3 / $oldoffice$4) ---


def rc4_cryptoapi_derive_key(password: str, salt: bytes, key_bits: int, block: int = 0) -> bytes:
    """Derive the RC4 key for the CryptoAPI SHA-1 scheme ([MS-OFFCRYPTO] Section 2.3.5.2).

    Steps, password -> RC4 key:

    1. ``H0 = SHA1(salt || UTF-16LE(password))`` -- the salt PREFIXES the password.
    2. ``Hfinal = SHA1(H0 || LE32(block))``; block 0 for the verifier.
    3. Take the first ``key_bits/8`` bytes of ``Hfinal`` as key material.
    4. 40-bit special case: pad the 5 real bytes with 11 zero bytes to form a
       128-bit RC4 key. For 128-bit the key is ``Hfinal[:16]`` (``Hfinal[16:20]``
       is discarded). Other key sizes return exactly ``key_bits/8`` bytes.

    Args:
        password: The document-open password (plain text).
        salt: The 16-byte salt from the EncryptionVerifier.
        key_bits: RC4 key length in bits (40 or 128 for hashcat; the spec allows
            40..128 in 8-bit steps).
        block: 32-bit little-endian block number; 0 for the verifier.

    Returns:
        The RC4 key: 16 bytes for the 40-bit (zero-padded) and 128-bit cases.

    """
    pw_bytes = password.encode(_PW_ENCODING)
    # Salt prefixes the password -- getting this order wrong silently breaks everything.
    h0 = _digest("sha1", salt + pw_bytes)
    block_le = struct.pack("<I", block)
    hfinal = _digest("sha1", h0 + block_le)
    key_bytes = key_bits // 8
    if key_bits == _KEYSIZE_40:
        # "first 40 bits of Hfinal and 88 bits set to zero, creating a 128-bit key."
        return hfinal[:_KEY40_REAL_BYTES] + bytes(_KEY40_ZERO_PAD)
    return hfinal[:key_bytes]


def rc4_cryptoapi_verify(password: str, salt: bytes, key_bits: int, enc_verifier: bytes, enc_verifier_hash: bytes) -> bool:
    """Return ``True`` iff ``password`` opens a CryptoAPI SHA-1 document ([MS-OFFCRYPTO] Section 2.3.5.6).

    Derives the block-0 key, RC4-decrypts ``EncryptedVerifier`` (16 bytes) then
    continues the same keystream over ``EncryptedVerifierHash`` (20 bytes), and
    checks ``SHA1(Verifier) == storedHash`` over the full 20 bytes (hashcat only
    compares the first 16; the full compare removes any false-positive risk).
    """
    key = rc4_cryptoapi_derive_key(password, salt, key_bits, 0)
    # Continuous keystream across the 16-byte verifier and the 20-byte hash.
    decrypted = rc4_crypt(key, enc_verifier + enc_verifier_hash)
    verifier = decrypted[:_VERIFIER_LEN]
    stored_hash = decrypted[_VERIFIER_LEN : _VERIFIER_LEN + _SHA1_HASH_LEN]
    result = _digest("sha1", verifier) == stored_hash
    logger.debug("rc4-cryptoapi verify: %s (keyBits=%d)", "pass" if result else "fail", key_bits)
    return result


def rc4_cryptoapi_hash_line(version_digit: int, key_size_bits: int, salt: bytes, enc_verifier: bytes, enc_verifier_hash: bytes) -> str:
    """Format the hashcat 9800 (``$oldoffice$3`` / ``$oldoffice$4``) hash line.

    Grammar (rc4-cryptoapi-sha1 Section 7)::

        $oldoffice$<ver>*<salt>*<encryptedVerifier>*<encryptedVerifierHash>

    The RC4 KeySize is NOT a separate token -- it is carried by the version
    digit: ``3`` = 40-bit key, ``4`` = 128-bit key. ``key_size_bits`` is therefore
    validated to agree with ``version_digit`` (3 <-> 40, 4 <-> 128) so the emitted
    line encodes the correct key size. Salt (16 B) and verifier (16 B) are 32 hex
    chars; the verifier hash is 40 hex chars (20 B). (Mode 9820's optional sixth
    ``:<seed>`` field is a collider artefact and is appended by the caller, not
    the extractor.)

    Raises:
        ValueError: If ``version_digit`` is not 3 or 4, or the digit disagrees
            with the key size (3 for 40-bit, 4 for >40-bit).

    """
    # [MS-OFFCRYPTO] Section 2.3.5 allows key sizes 40-128 in 8-bit steps.
    # Digit 3 = 40-bit (zero-padded), digit 4 = any size > 40-bit.
    if not (_KEYSIZE_40 <= key_size_bits <= _KEYSIZE_128 and key_size_bits % 8 == 0):
        msg = f"rc4-cryptoapi key size must be 40-128 bits (8-bit aligned), got {key_size_bits}"
        raise ValueError(msg)
    expected = 3 if key_size_bits == _KEYSIZE_40 else 4
    if version_digit != expected:
        msg = f"version digit {version_digit} does not match {key_size_bits}-bit key (expected {expected})"
        raise ValueError(msg)
    return f"{_SIGNATURE}{version_digit}*{salt.hex()}*{enc_verifier.hex()}*{enc_verifier_hash.hex()}"


def unified_rc4_office_line(scheme: Rc4Scheme, salt: bytes, key_bits: int, enc_verifier: bytes, enc_verifier_hash: bytes) -> str:
    """Emit the self-describing ``$office$*...`` line for a legacy RC4 document-open scheme.

    Grammar (docs/reference/hash-formats.md): same ``$office$`` prefix as ECMA-376,
    with ``hashfunc`` = ``md5`` (97/2000) or ``sha1`` (XP/2003), ``cipher`` = ``rc4-{keybits}``,
    ``mode`` = ``stream``, ``iters`` = ``0`` (un-iterated). The ``(hashfunc, cipher, mode, iters)``
    tuple distinguishes the two legacy schemes from each other and from the modern ones
    without any version digit or year number.
    """
    hash_token = "md5" if scheme is Rc4Scheme.MD5 else "sha1"
    cipher_token = f"rc4-{key_bits}"
    return f"$office$*{hash_token}*{cipher_token}*stream*0*{salt.hex()}*{enc_verifier.hex()}*{enc_verifier_hash.hex()}"


# --- Header parsing and scheme discrimination ---


def rc4_scheme(version_major: int, version_minor: int, flags: int) -> Rc4Scheme:
    """Classify an ``EncryptionVersionInfo`` word pair as one of the two RC4 schemes.

    Discrimination ([MS-OFFCRYPTO] Section 2.3.5.1 / Section 2.3.6.1):

    * ``(vMajor, vMinor) == (1, 1)`` -> RC4 + MD5 (Section 2.3.6).
    * ``vMinor == 2`` and ``vMajor in {2, 3, 4}`` -> RC4 CryptoAPI (Section 2.3.5),
      *unless* the ``fAES`` flag is set, which marks the AES standard/agile
      schemes that share the same version words.

    Args:
        version_major: ``EncryptionVersionInfo.vMajor`` (little-endian u16).
        version_minor: ``EncryptionVersionInfo.vMinor`` (little-endian u16).
        flags: ``EncryptionHeaderFlags`` (u32); ``fAES`` disqualifies CryptoAPI RC4.

    Returns:
        The matching :class:`Rc4Scheme`.

    Raises:
        ValueError: If the version words (with the flags) match neither RC4 scheme.

    """
    if (version_major, version_minor) == _MD5_VERSION_WORDS:
        return Rc4Scheme.MD5
    if version_minor == _CRYPTOAPI_VMINOR and version_major in _CRYPTOAPI_VMAJORS:
        if flags & _FLAG_FAES:
            # Same version words, but fAES set means AES standard/agile, not RC4.
            msg = f"version ({version_major}, {version_minor}) with fAES set is an AES scheme, not RC4 CryptoAPI"
            raise ValueError(msg)
        return Rc4Scheme.CRYPTOAPI
    msg = f"version ({version_major}, {version_minor}) matches no legacy RC4 scheme"
    raise ValueError(msg)


def parse_rc4_cryptoapi_header(blob: bytes) -> dict[str, int | bytes | str]:
    """Parse an RC4 CryptoAPI encryption blob into its fields ([MS-OFFCRYPTO] Section 2.3.5.1).

    On-disk layout (all integers little-endian)::

        EncryptionVersionInfo : vMajor(u16), vMinor(u16)
        Flags                 : u32  (an outer copy of EncryptionHeader.Flags)
        EncryptionHeaderSize  : u32
        EncryptionHeader      : Flags(u32), SizeExtra(u32), AlgID(i32),
                                AlgIDHash(i32), KeySize(u32), ProviderType(u32),
                                Reserved1(u32), Reserved2(u32),
                                CSPName(UTF-16LE, NUL-terminated)
        EncryptionVerifier    : SaltSize(u32), Salt(16), EncryptedVerifier(16),
                                VerifierHashSize(u32), EncryptedVerifierHash(20)

    Args:
        blob: The encryption blob starting at ``EncryptionVersionInfo``.

    Returns:
        A dict with the decoded header and verifier fields. ``key_size`` is in
        bits; ``salt``, ``encrypted_verifier``, and ``encrypted_verifier_hash``
        are raw bytes; ``scheme`` is the :class:`Rc4Scheme` value.

    Raises:
        ValueError: If the blob is too short or the version words are not a
            CryptoAPI RC4 pair.

    """
    # EncryptionVersionInfo + outer Flags + EncryptionHeaderSize = 12 bytes minimum.
    header_prefix = 12
    if len(blob) < header_prefix:
        msg = f"blob too short for RC4 CryptoAPI header: {len(blob)} bytes"
        raise ValueError(msg)

    v_major, v_minor, outer_flags, header_size = struct.unpack_from("<HHII", blob, 0)
    # This raises if the version words are not a CryptoAPI RC4 pair.
    scheme = rc4_scheme(v_major, v_minor, outer_flags)

    header_start = header_prefix
    header_end = header_start + header_size
    if len(blob) < header_end:
        msg = f"blob too short for EncryptionHeader ({header_size} bytes declared)"
        raise ValueError(msg)
    header = blob[header_start:header_end]

    # EncryptionHeader fixed fields ([MS-OFFCRYPTO] Section 2.3.2), then CSPName.
    inner_flags, size_extra, alg_id, alg_id_hash, key_size, provider_type, reserved1, reserved2 = struct.unpack_from("<IIiiIIII", header, 0)
    csp_name = header[32:].decode(_PW_ENCODING, errors="replace").rstrip("\x00")

    # EncryptionVerifier ([MS-OFFCRYPTO] Section 2.3.3) follows the header.
    verifier = blob[header_end:]
    salt_size, salt, enc_verifier = struct.unpack_from(f"<I{_SALT_LEN}s{_VERIFIER_LEN}s", verifier, 0)
    verifier_hash_size = struct.unpack_from("<I", verifier, 4 + _SALT_LEN + _VERIFIER_LEN)[0]
    vh_offset = 4 + _SALT_LEN + _VERIFIER_LEN + 4
    enc_verifier_hash = verifier[vh_offset : vh_offset + verifier_hash_size]

    result: dict[str, int | bytes | str] = {
        "version_major": v_major,
        "version_minor": v_minor,
        "flags": outer_flags,
        "header_size": header_size,
        "header_flags": inner_flags,
        "size_extra": size_extra,
        "alg_id": alg_id,
        "alg_id_hash": alg_id_hash,
        "key_size": key_size,
        "provider_type": provider_type,
        "reserved1": reserved1,
        "reserved2": reserved2,
        "csp_name": csp_name,
        "salt_size": salt_size,
        "salt": salt,
        "encrypted_verifier": enc_verifier,
        "verifier_hash_size": verifier_hash_size,
        "encrypted_verifier_hash": enc_verifier_hash,
        "scheme": scheme,
    }
    logger.debug("CryptoAPI header: algID=0x%04x keySize=%d salt=%s csp=%s", alg_id, key_size, salt.hex(), csp_name)
    return result


# --- In-place document body decryption (stretch goal) ---


@dataclass(frozen=True)
class Rc4StreamParams:
    """How to walk an in-place-encrypted legacy RC4 stream ([MS-OFFCRYPTO] Section 2.3.5 / Section 2.3.6).

    Bundled so ``decrypt_stream`` stays a small ``(password, salt, ciphertext,
    params)`` call. The defaults describe the common Word/Excel body: MD5 scheme,
    512-byte re-keyed blocks, starting at block 0. ``key_bits`` is consulted only
    for the CryptoAPI scheme (the MD5 scheme is always 40-bit effective).
    """

    scheme: Rc4Scheme = Rc4Scheme.MD5
    key_bits: int = _KEYSIZE_128
    block_size: int = _INPLACE_BLOCK_SIZE
    first_block: int = 0


def decrypt_stream(password: str, salt: bytes, ciphertext: bytes, params: Rc4StreamParams | None = None) -> bytes:
    """Decrypt an in-place-encrypted legacy stream, re-keying per block ([MS-OFFCRYPTO] Section 2.3.6 / Section 2.3.5).

    Both legacy RC4 schemes encrypt document streams "in place" in fixed-size
    blocks (512 bytes): the RC4 key is re-derived for every block using an
    incrementing block number, and the RC4 keystream restarts at each block
    boundary. This walks ``ciphertext`` in ``params.block_size`` chunks starting
    at ``params.first_block`` and decrypts each with its own key.

    ``ciphertext`` is assumed to begin on a block boundary (block index
    ``params.first_block``). For the verifier path use the dedicated ``*_verify``
    helpers instead; this is for recovering document body bytes once the
    password/key is known.

    Args:
        password: The recovered document-open password.
        salt: The 16-byte KDF salt.
        ciphertext: The encrypted stream bytes, starting on a block boundary.
        params: How to walk the stream (scheme, key size, block size, first
            block); defaults to the MD5 / 512-byte / block-0 profile.

    Returns:
        The decrypted stream bytes.

    """
    params = params or Rc4StreamParams()
    scheme = Rc4Scheme(params.scheme)
    logger.debug("decrypt_stream: scheme=%s keyBits=%d blocks=%d", scheme.value, params.key_bits, (len(ciphertext) + params.block_size - 1) // params.block_size)
    out = bytearray()
    for offset in range(0, len(ciphertext), params.block_size):
        block_no = params.first_block + offset // params.block_size
        chunk = ciphertext[offset : offset + params.block_size]
        # Each block gets its own key; the MD5 scheme ignores key_bits (always 40-bit effective).
        key = rc4_md5_derive_key(password, salt, block_no) if scheme is Rc4Scheme.MD5 else rc4_cryptoapi_derive_key(password, salt, params.key_bits, block_no)
        out += rc4_crypt(key, chunk)
    return bytes(out)
