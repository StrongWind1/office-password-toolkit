# SPDX-License-Identifier: Apache-2.0
"""MSISAM encryption: password verification, hash extraction, and page decryption.

MSISAM is the encryption layer used by Microsoft Money 2002+ and some Jet 4.0
databases configured with the MSISAM encryption provider. The algorithm is:

1. Password uppercased, encoded as UTF-16LE, null-padded to 0x28 (40) bytes.
2. Hashed with MD5 (default) or SHA-1 (flag 0x20 at offset 0x298), truncated to 16 bytes.
3. Per-page RC4 key = ``digest[0:16] + salt[0x72:0x76]`` (20 bytes), with the page
   number mixed into the last 4 bytes for per-page variation.
4. Password verification: RC4-decrypt 4 bytes at ``0x2E9 + adjustment`` with
   key ``digest + salt[0x72:0x7A]`` (24 bytes); compare to ``salt[0x72:0x76]``.

The ``adjustment`` for Money 2003+ is the byte at decrypted offset 0x72; for
Money 2002 and earlier it is 0.

Only pages 0 through 14 (0x0E) are encrypted; higher pages are cleartext.

Ported from Jackcess ``MSISAMCryptCodecHandler.java`` and thewd-hub
``moneyCrk.cpp``. Verified against ``money2008-pwd.mny`` (password ``TEST12345``).
"""

from __future__ import annotations

import hashlib
import struct
from dataclasses import dataclass

# --- Constants ----------------------------------------------------------------

_SALT_OFFSET: int = 0x72
_SALT_LEN_FULL: int = 8
_SALT_LEN_CHECK: int = 4
_CRYPT_CHECK_START: int = 0x2E9
_CRYPT_CHECK_LEN: int = 4
_FLAGS_OFFSET: int = 0x298
_FLAG_NEW_ENCRYPTION: int = 0x06
_FLAG_USE_SHA1: int = 0x20
_FLAG_MONEY_2003: int = 0x08
_PASSWORD_BUF_SIZE: int = 0x28
_DIGEST_LEN: int = 16
_MAX_ENCRYPTED_PAGE: int = 0x0E
_PAGE_SIZE: int = 0x1000
_RC4_STATE_SIZE: int = 256
_RC4_KEY_LEN: int = 4

# RC4 fixed key for header obfuscation (same as Jet 4).
_HEADER_RC4_KEY: bytes = b"\xc7\xda\x39\x6b"
_HEADER_RC4_START: int = 0x18
_HEADER_RC4_LEN: int = 0x80


# --- Data types ---------------------------------------------------------------


@dataclass(frozen=True)
class MsisamParams:
    """Extracted MSISAM encryption parameters for verification and decryption."""

    use_sha1: bool
    salt_full: bytes
    salt_check: bytes
    crypt_check: bytes
    adjustment: int


# --- RC4 implementation -------------------------------------------------------


def _rc4(key: bytes, data: bytes) -> bytes:
    """RC4 encrypt/decrypt."""
    state = list(range(_RC4_STATE_SIZE))
    j = 0
    for i in range(_RC4_STATE_SIZE):
        j = (j + state[i] + key[i % len(key)]) % _RC4_STATE_SIZE
        state[i], state[j] = state[j], state[i]
    out = bytearray(len(data))
    i = j = 0
    for idx, byte in enumerate(data):
        i = (i + 1) % _RC4_STATE_SIZE
        j = (j + state[i]) % _RC4_STATE_SIZE
        state[i], state[j] = state[j], state[i]
        out[idx] = byte ^ state[(state[i] + state[j]) % _RC4_STATE_SIZE]
    return bytes(out)


# --- Parameter extraction -----------------------------------------------------


def is_msisam_encrypted(first_page: bytes) -> bool:
    """Return True if the file has the MSISAM new-encryption flag at 0x298."""
    if len(first_page) <= _FLAGS_OFFSET:
        return False
    return bool(first_page[_FLAGS_OFFSET] & _FLAG_NEW_ENCRYPTION)


def extract_params(first_page: bytes) -> MsisamParams | None:
    """Extract MSISAM encryption parameters from the first page.

    The header region (0x18..0x98) must be RC4-decrypted first to read the salt.
    """
    if len(first_page) < _PAGE_SIZE:
        return None
    if not is_msisam_encrypted(first_page):
        return None

    flags = first_page[_FLAGS_OFFSET]
    use_sha1 = bool(flags & _FLAG_USE_SHA1)
    is_money_2003 = bool(flags & _FLAG_MONEY_2003)

    header_region = _rc4(_HEADER_RC4_KEY, first_page[_HEADER_RC4_START : _HEADER_RC4_START + _HEADER_RC4_LEN])
    salt_offset_in_region = _SALT_OFFSET - _HEADER_RC4_START
    salt_full = bytes(header_region[salt_offset_in_region : salt_offset_in_region + _SALT_LEN_FULL])
    salt_check = salt_full[:_SALT_LEN_CHECK]

    adjustment = header_region[salt_offset_in_region] if is_money_2003 else 0
    crypt_check_offset = _CRYPT_CHECK_START + adjustment
    if crypt_check_offset + _CRYPT_CHECK_LEN > len(first_page):
        return None
    crypt_check = bytes(first_page[crypt_check_offset : crypt_check_offset + _CRYPT_CHECK_LEN])

    return MsisamParams(use_sha1=use_sha1, salt_full=salt_full, salt_check=salt_check, crypt_check=crypt_check, adjustment=adjustment)


# --- Password hashing and verification ----------------------------------------


def _password_digest(password: str, *, use_sha1: bool) -> bytes:
    """Compute the 16-byte digest of an MSISAM password."""
    pw_buf = bytearray(_PASSWORD_BUF_SIZE)
    if password:
        encoded = password.upper().encode("utf-16-le")
        pw_buf[: min(len(encoded), _PASSWORD_BUF_SIZE)] = encoded[:_PASSWORD_BUF_SIZE]

    algo = hashlib.sha1 if use_sha1 else hashlib.md5
    return algo(bytes(pw_buf)).digest()[:_DIGEST_LEN]


def verify_password(params: MsisamParams, password: str) -> bool:
    """Verify a candidate password against the MSISAM crypt check."""
    digest = _password_digest(password, use_sha1=params.use_sha1)
    rc4_key = digest + params.salt_full
    decrypted = _rc4(rc4_key, params.crypt_check)
    return decrypted == params.salt_check


# --- Hash extraction ----------------------------------------------------------


def msisam_hash_line(params: MsisamParams) -> str:
    """Emit a custom ``$msisam$`` hash line for offline cracking.

    Format: ``$msisam$<algo>$<salt_hex>$<crypt_check_hex>$<adjustment>``

    * ``algo``: ``1`` for SHA-1, ``0`` for MD5
    * ``salt_hex``: 8-byte salt from offset 0x72 (hex-encoded)
    * ``crypt_check_hex``: 4-byte verification block (hex-encoded)
    * ``adjustment``: integer offset adjustment for Money 2003+
    """
    algo = 1 if params.use_sha1 else 0
    return f"$msisam${algo}${params.salt_full.hex()}${params.crypt_check.hex()}${params.adjustment}"


# --- Page decryption ----------------------------------------------------------


def _page_rc4_key(digest: bytes, salt_check: bytes, page_number: int) -> bytes:
    """Compute the per-page RC4 key: digest[0:16] + (salt XOR page_number)."""
    page_bytes = struct.pack("<I", page_number)
    mixed_salt = bytes(a ^ b for a, b in zip(salt_check, page_bytes, strict=True))
    return digest + mixed_salt


def decrypt_page(params: MsisamParams, password: str, page_number: int, page_data: bytes) -> bytes:
    """RC4-decrypt one MSISAM page. Pages above 0x0E are cleartext (returned as-is)."""
    if page_number > _MAX_ENCRYPTED_PAGE:
        return page_data
    digest = _password_digest(password, use_sha1=params.use_sha1)
    key = _page_rc4_key(digest, params.salt_check, page_number)
    return _rc4(key, page_data)


def decrypt_file(data: bytes, password: str) -> bytes:
    """Decrypt an entire MSISAM file given the correct password.

    Page 0 (header) is partially encrypted; pages 1-14 are fully encrypted;
    pages 15+ are cleartext. Returns the full decrypted file.
    """
    params = extract_params(data)
    if params is None:
        msg = "Not an MSISAM-encrypted file"
        raise ValueError(msg)

    if not verify_password(params, password):
        msg = "Incorrect password"
        raise ValueError(msg)

    digest = _password_digest(password, use_sha1=params.use_sha1)
    result = bytearray(data)

    for page_num in range(1, min(_MAX_ENCRYPTED_PAGE + 1, len(data) // _PAGE_SIZE)):
        offset = page_num * _PAGE_SIZE
        page = data[offset : offset + _PAGE_SIZE]
        if len(page) < _PAGE_SIZE:
            break
        key = _page_rc4_key(digest, params.salt_check, page_num)
        result[offset : offset + _PAGE_SIZE] = _rc4(key, page)

    return bytes(result)
