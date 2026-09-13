# SPDX-License-Identifier: Apache-2.0
r"""ECMA-376 document-open encryption: Standard (2007) and Agile (2010/2013+).

This module is the heart of the toolkit's slow-hash support. It parses the
``\EncryptionInfo`` stream of an encrypted Office Open XML document, emits the
``$office$*...`` hash line consumed by hashcat/John, verifies a candidate
password against the stored verifier, and -- once the password is known --
decrypts the ``\EncryptedPackage`` stream back to the original OPC ZIP.

Two schemes live here, distinguished on disk by the version words at the head
of ``\EncryptionInfo`` ([MS-OFFCRYPTO] Section 2.1.4):

* **Standard** (``vMinor == 0x0002``) -- Office 2007. Fixed binary layout,
  AES-ECB, a bespoke SHA-1 key-derivation spun 50000 times. hashcat mode 9400,
  hash-line proxy ``2007``. See [MS-OFFCRYPTO] Section 2.3.4.5-2.3.4.9.
* **Agile** (``vMajor == vMinor == 0x0004``) -- Office 2010 and later. An XML
  descriptor names every parameter; AES-CBC, a spin-loop KDF finalised with an
  8-byte block key per protected field. hashcat modes 9500 (SHA-1/AES-128,
  proxy ``2010``) and 9600 (SHA-512/AES-256, proxy ``2013``). See
  [MS-OFFCRYPTO] Section 2.3.4.10-2.3.4.15.

Design notes for the reader who knows Python but not the format:

* Every integer inside the container is little-endian.
* Passwords are hashed as UTF-16LE with no BOM and no terminating NUL -- the
  single most common implementation mistake ([MS-OFFCRYPTO] Section 2.3.4.7 /
  2.3.4.11).
* The document-open KDF *prepends* the 4-byte iterator inside the spin loop and
  finishes with a trailing block key. This is the opposite of the ISO
  worksheet-protection KDF (Section 2.4.2.4), which appends the iterator and has
  no block key; getting prepend-vs-append wrong silently breaks everything.
"""

from __future__ import annotations

import base64
import hashlib
import logging
import re
from dataclasses import dataclass
from enum import StrEnum
from typing import Final

from office_password_toolkit.crypto import ciphers, hashes

logger = logging.getLogger(__name__)

# --- On-disk discriminators ([MS-OFFCRYPTO] Section 2.1.4 / 2.3.4.5 / 2.3.4.10) ---
_VERSION_MINOR_STANDARD: Final = 0x0002  # standard (and legacy CryptoAPI) encryption
_VERSION_MINOR_EXTENSIBLE: Final = 0x0003  # extensible / IRM -- not password-recoverable
_VERSION_MINOR_AGILE: Final = 0x0004  # agile encryption

# --- EncryptionHeader constants ([MS-OFFCRYPTO] Section 2.3.1 / 2.3.2) ---
_FLAG_AES: Final = 0x20  # EncryptionHeaderFlags fAES bit -- set only for ECMA-376 AES
_ALGID_RC4: Final = 0x00006801  # CryptoAPI RC4 -- a *different* scheme, rejected here
# AlgID -> AES key length in bits, used when KeySize is absent/zero.
_ALGID_KEY_BITS: Final[dict[int, int]] = {
    0x0000660E: 128,
    0x0000660F: 192,
    0x00006610: 256,
}

# --- KDF constants ---
_STANDARD_SPIN_COUNT: Final = 50000  # fixed iteration count ([MS-OFFCRYPTO] Section 2.3.4.7)
_SHA1_SIZE: Final = 20  # SHA-1 digest length in bytes
_HMAC_BLOCK: Final = 64  # ipad/opad buffer length ([MS-OFFCRYPTO] Section 2.3.4.7)
_IPAD: Final = 0x36  # inner-pad byte for the key-expansion step
_OPAD: Final = 0x5C  # outer-pad byte for the key-expansion step
_KDF_PAD_BYTE: Final = 0x36  # right-pad byte when Hfinal is shorter than keyBits/8

# --- Cipher constants ---
_AES_BLOCK: Final = 16  # AES block size in bytes; also the standard-scheme block/IV size
_SEGMENT_SIZE: Final = 4096  # agile bulk-data CBC segment length ([MS-OFFCRYPTO] Section 2.3.4.15)
_STREAM_SIZE_PREFIX: Final = 8  # \EncryptedPackage 8-byte LE plaintext-length prefix
_CHAINING_CBC: Final = "ChainingModeCBC"  # the only agile chaining mode implemented here

# --- Supported hashcat key sizes (proxy selection in office_hash_line) ---
_KEY_BITS_128: Final = 128  # AES-128 key length in bits (9500 agile SHA-1)
_KEY_BITS_256: Final = 256  # AES-256 key length in bits (9600 agile SHA-512)

# --- Agile block keys ([MS-OFFCRYPTO] Section 2.3.4.13) ---
# Appended after the spun hash before the finalisation hash so that the three
# derived keys (verifier input, verifier hash, intermediate) never collide.
_BLOCK_KEY_VERIFIER_INPUT: Final = b"\xfe\xa7\xd2\x76\x3b\x4b\x9e\x79"  # derives the encryptedVerifierHashInput key
_BLOCK_KEY_VERIFIER_VALUE: Final = b"\xd7\xaa\x0f\x6d\x30\x61\x34\x4e"  # derives the encryptedVerifierHashValue key
_BLOCK_KEY_INTERMEDIATE: Final = b"\x14\x6e\x0b\xe7\xab\xac\xd0\xd6"  # derives the intermediate key for bulk decryption

# --- Hash-name normalisation ---
# Map the spec's ASCII algorithm strings (agile) to hashlib names. Keys are
# uppercased with hyphens stripped so "SHA-512", "SHA512" and "sha512" all match.
_HASH_ALIASES: Final[dict[str, str]] = {
    "SHA1": "sha1",
    "SHA256": "sha256",
    "SHA384": "sha384",
    "SHA512": "sha512",
    "MD5": "md5",
    "MD4": "md4",
    "MD2": "md2",
}

# Attribute extractor for the agile XML descriptor. We deliberately avoid a full
# XML parser: the descriptor is a flat set of attributes, base64 or decimal, and
# regex extraction cannot be fooled by external entities or a billion-laughs
# expansion in an attacker-controlled \EncryptionInfo stream.
_ATTR_RE: Final = re.compile(r'([\w:.\-]+)\s*=\s*"([^"]*)"')


class EncryptionKind(StrEnum):
    r"""Which ECMA-376 document-open scheme an ``\EncryptionInfo`` stream uses."""

    STANDARD = "standard"  # Office 2007, fixed binary layout, AES-ECB (hashcat 9400)
    AGILE = "agile"  # Office 2010+, XML descriptor, AES-CBC (hashcat 9500/9600)


@dataclass(frozen=True)
class EncryptionInfo:
    r"""Normalised parse of an ``\EncryptionInfo`` stream for either scheme.

    The shared fields (``salt`` through ``enc_verifier_hash``) are all a handler
    needs to emit a hash line or verify a password. The ``key_data_*`` /
    ``enc_key_value`` fields are populated only for the agile scheme and only
    matter when decrypting the bulk ``\EncryptedPackage`` stream.
    """

    kind: EncryptionKind
    version_major: int  # EncryptionVersionInfo.vMajor
    version_minor: int  # EncryptionVersionInfo.vMinor
    salt: bytes  # PasswordKeyEncryptor / EncryptionVerifier salt (KDF salt and CBC IV)
    key_bits: int  # derived-key length in bits (128/192/256)
    spin_count: int  # KDF iterations (50000 fixed for standard; free for agile)
    hash_algorithm: str  # e.g. "SHA-1", "SHA512"
    cipher_algorithm: str  # e.g. "AES"
    cipher_chaining: str  # e.g. "ChainingModeCBC" (agile) or "ChainingModeECB" (standard)
    block_size: int  # cipher block size in bytes (also the IV length)
    hash_size: int  # verifier hash length in bytes (20 for SHA-1, 64 for SHA-512)
    enc_verifier: bytes  # encrypted random verifier (hashcat "encVerifier")
    enc_verifier_hash: bytes  # encrypted hash of the verifier (hashcat "encVerifierHash")
    # --- Agile-only: material for decrypting the bulk package (None for standard) ---
    enc_key_value: bytes | None = None  # encrypted intermediate/bulk key
    key_data_salt: bytes | None = None  # <keyData> saltValue (bulk segment IV seed)
    key_data_hash_algorithm: str | None = None  # <keyData> hashAlgorithm
    key_data_cipher_algorithm: str | None = None  # <keyData> cipherAlgorithm
    key_data_cipher_chaining: str | None = None  # <keyData> cipherChaining
    key_data_key_bits: int | None = None  # <keyData> keyBits (intermediate-key length)
    key_data_block_size: int | None = None  # <keyData> blockSize
    key_data_hash_size: int | None = None  # <keyData> hashSize

    @property
    def salt_size(self) -> int:
        """Salt length in bytes -- the ``saltSize`` token in the hash line."""
        return len(self.salt)


# --- Low-level primitives -------------------------------------------------


def _hashlib_name(spec_name: str) -> str:
    """Resolve a spec algorithm string (e.g. ``"SHA-512"``) to a hashlib name.

    Returns the hashlib-compatible name for SHA-1/256/384/512 and MD5. Also accepts
    MD4 and MD2 (handled by ``hashes.digest()``'s pure-Python fallback).
    Raises ``ValueError`` for unknown names.
    """
    key = spec_name.strip().upper().replace("-", "")
    name = _HASH_ALIASES.get(key)
    if name is None:
        msg = f"unknown hash algorithm {spec_name!r}"
        raise ValueError(msg)
    # MD4/MD2 are handled by hashes.digest()'s pure-Python fallback; skip the hashlib probe.
    if name in ("md4", "md2"):
        return name
    try:
        hashlib.new(name, usedforsecurity=False)
    except (ValueError, TypeError) as exc:
        msg = f"hash algorithm {spec_name!r} is not available in this OpenSSL build"
        raise ValueError(msg) from exc
    return name


def _fit(data: bytes, size: int) -> bytes:
    """Fit ``data`` to exactly ``size`` bytes per [MS-OFFCRYPTO] Section 2.3.4.12.

    Truncate if too long; right-pad with ``0x36`` if too short. Used to shape a
    salt/hash into an IV of the cipher's block size. For AES the salt is already
    16 bytes, so this is a no-op there.
    """
    if len(data) >= size:
        return data[:size]
    return data + bytes([_KDF_PAD_BYTE]) * (size - len(data))


# --- Key derivation -------------------------------------------------------


def _derive_key_standard(password: str, salt: bytes, key_bits: int) -> bytes:
    """Derive the AES key for standard encryption ([MS-OFFCRYPTO] Section 2.3.4.7).

    ``H0 = SHA1(salt || pw)``; spin ``Hn = SHA1(LE32(i) || Hn-1)`` 50000 times;
    ``Hfinal = SHA1(Hspin || LE32(0))``; then an ipad/opad expansion whose first
    ``keyBits/8`` bytes are the key. Note the iterator and block number are fed
    little-endian and the salt is hashed *before* the password.
    """
    pw = password.encode("utf-16-le")  # UTF-16LE, no BOM, no NUL
    h = hashes.digest("sha1", salt + pw)  # H0
    for i in range(_STANDARD_SPIN_COUNT):
        h = hashes.digest("sha1", i.to_bytes(4, "little") + h)  # LE32(i) prepended
    h_final = hashes.digest("sha1", h + (0).to_bytes(4, "little"))  # append block number 0
    # ipad/opad key expansion: XOR the 20-byte Hfinal into 64-byte pad buffers.
    inner = bytes((_IPAD ^ h_final[i]) if i < _SHA1_SIZE else _IPAD for i in range(_HMAC_BLOCK))
    outer = bytes((_OPAD ^ h_final[i]) if i < _SHA1_SIZE else _OPAD for i in range(_HMAC_BLOCK))
    expanded = hashes.digest("sha1", inner) + hashes.digest("sha1", outer)  # X1 || X2 (40 bytes)
    return expanded[: key_bits // 8]


def _iterate_agile_hash(password: str, salt: bytes, hashlib_name: str, spin_count: int) -> bytes:
    """Run the agile spin loop, returning ``H_{spinCount-1}`` ([MS-OFFCRYPTO] Section 2.3.4.11).

    ``H0 = H(salt || pw)``; then ``Hn = H(LE32(i) || Hn-1)`` for ``spin_count``
    iterations. This spin is the entire cost of the KDF and depends only on the
    password and salt, so a caller derives it once and reuses it for every block
    key (verifier input, verifier value, and the intermediate/bulk key).
    """
    pw = password.encode("utf-16-le")  # UTF-16LE, no BOM, no NUL
    h = hashes.digest(hashlib_name, salt + pw)  # H0
    for i in range(spin_count):
        h = hashes.digest(hashlib_name, i.to_bytes(4, "little") + h)  # LE32(i) prepended
    return h


def _finalize_agile_key(iterated: bytes, block_key: bytes, hashlib_name: str, key_bits: int) -> bytes:
    """Finish one agile key from the spun hash and an 8-byte block key ([MS-OFFCRYPTO] Section 2.3.4.11).

    ``Hfinal = H(Hspin || blockKey)``; take the first ``keyBits/8`` bytes,
    right-padding with ``0x36`` when the digest is shorter than the key.
    """
    h = hashes.digest(hashlib_name, iterated + block_key)  # append the 8-byte block key
    key_len = key_bits // 8
    if len(h) >= key_len:
        return h[:key_len]
    return h + bytes([_KDF_PAD_BYTE]) * (key_len - len(h))


# --- Verification ---------------------------------------------------------


def _verify_standard(info: EncryptionInfo, password: str) -> bool:
    """Verify a password against a standard-encryption verifier.

    Uses the encrypt-and-compare form ([MS-OFFCRYPTO] Section 2.3.4.9 optimised):
    decrypt the verifier, hash it, re-encrypt the first 16 bytes of that hash and
    compare against the first ciphertext block. Comparing one block (128 bits) is
    what hashcat does and is ample against false positives; it also means only the
    first 16 bytes of ``enc_verifier_hash`` are needed, matching the 20-byte value
    the hash line carries.
    """
    key = _derive_key_standard(password, info.salt, info.key_bits)
    verifier = ciphers.aes_ecb_decrypt(key, info.enc_verifier)  # 16-byte Verifier
    calc = hashes.digest("sha1", verifier)  # SHA1(Verifier), 20 bytes
    reencrypted = ciphers.aes_ecb_encrypt_block(key, calc[:_AES_BLOCK])
    return reencrypted == info.enc_verifier_hash[:_AES_BLOCK]


def _verify_agile(info: EncryptionInfo, password: str) -> bool:
    """Verify a password against an agile-encryption verifier.

    Spins the password hash once, then derives the two verifier keys (input and
    value) from their block keys, CBC-decrypts the verifier (IV = salt), hashes
    it, and re-encrypts the first block of that hash to compare against the stored
    ciphertext's first block ([MS-OFFCRYPTO] Section 2.3.4.13). The single-block
    compare matches hashcat and works whether ``enc_verifier_hash`` is the full
    field or the 32-byte prefix the hash line carries.
    """
    cipher = info.cipher_algorithm
    hashlib_name = _hashlib_name(info.hash_algorithm)
    iterated = _iterate_agile_hash(password, info.salt, hashlib_name, info.spin_count)
    key_input = _finalize_agile_key(iterated, _BLOCK_KEY_VERIFIER_INPUT, hashlib_name, info.key_bits)
    key_value = _finalize_agile_key(iterated, _BLOCK_KEY_VERIFIER_VALUE, hashlib_name, info.key_bits)
    iv = _fit(info.salt, info.block_size)
    block = info.block_size
    verifier = ciphers.cbc_decrypt(cipher, key_input, iv, info.enc_verifier)
    computed = hashes.digest(hashlib_name, verifier)
    reencrypted = ciphers.cbc_encrypt(cipher, key_value, iv, computed[:block])
    return reencrypted[:block] == info.enc_verifier_hash[:block]


def verify_password(info: EncryptionInfo, password: str) -> bool:
    """Return ``True`` if ``password`` unlocks the document described by ``info``."""
    result = _verify_standard(info, password) if info.kind is EncryptionKind.STANDARD else _verify_agile(info, password)
    logger.debug("verify: %s (%s)", "pass" if result else "fail", info.kind.value)
    return result


# --- Parsing --------------------------------------------------------------


def _element_attributes(xml_text: str, local_name: str) -> dict[str, str]:
    """Return the attributes of the first ``<local_name .../>`` element as a dict.

    Namespace prefixes (e.g. ``p:encryptedKey``) are matched and ignored. See the
    module note on why a regex is used instead of a full XML parser.
    """
    pattern = re.compile(r"<(?:[\w.]+:)?" + re.escape(local_name) + r"\b([^>]*?)/?>", re.DOTALL)
    match = pattern.search(xml_text)
    if match is None:
        msg = rf"agile \EncryptionInfo XML is missing the <{local_name}> element"
        raise ValueError(msg)
    return dict(_ATTR_RE.findall(match.group(1)))


def _password_encrypted_key(xml_text: str) -> dict[str, str]:
    r"""Return the PasswordKeyEncryptor's ``<p:encryptedKey>`` attributes.

    An agile ``<encryption>`` descriptor may carry several ``<keyEncryptor>``
    children (a certificate encryptor can precede the password one). Only the
    password encryptor carries ``spinCount`` + ``saltValue``, so we select the
    ``encryptedKey`` that has them rather than the first of any namespace prefix --
    otherwise a certificate-first file would break a password-recoverable document.
    Raises ``ValueError`` when no password encryptor exists (certificate-only files
    are not password-recoverable).
    """
    for attrs_text in re.findall(r"<(?:[\w.]+:)?encryptedKey\b([^>]*?)/?>", xml_text, re.DOTALL):
        attrs: dict[str, str] = dict(_ATTR_RE.findall(attrs_text))
        if "spinCount" in attrs and "saltValue" in attrs:
            return attrs
    msg = r"agile \EncryptionInfo has no password keyEncryptor (certificate-only; not password-recoverable)"
    raise ValueError(msg)


def _parse_standard(blob: bytes, version_major: int, version_minor: int) -> EncryptionInfo:
    r"""Parse a standard-encryption ``\EncryptionInfo`` stream (Section 2.3.4.5).

    Rejects the structurally similar CryptoAPI RC4 scheme (Section 2.3.5): those
    streams share the header layout but clear the ``fAES`` flag / carry the RC4
    ``AlgID``, and are handled by a different module.
    """
    header_size = int.from_bytes(blob[8:12], "little")
    header = blob[12 : 12 + header_size]
    header_flags = int.from_bytes(header[0:4], "little")
    alg_id = int.from_bytes(header[8:12], "little")
    key_size_bits = int.from_bytes(header[16:20], "little")
    if alg_id == _ALGID_RC4 or not header_flags & _FLAG_AES:
        msg = r"\EncryptionInfo is CryptoAPI RC4, not ECMA-376 standard encryption"
        raise ValueError(msg)
    # EncryptionVerifier immediately follows the header (Section 2.3.3).
    cursor = 12 + header_size
    salt_size = int.from_bytes(blob[cursor : cursor + 4], "little")
    cursor += 4
    salt = blob[cursor : cursor + salt_size]
    cursor += salt_size
    enc_verifier = blob[cursor : cursor + _AES_BLOCK]
    cursor += _AES_BLOCK
    verifier_hash_size = int.from_bytes(blob[cursor : cursor + 4], "little")
    cursor += 4
    enc_verifier_hash = blob[cursor : cursor + 2 * _AES_BLOCK]  # 32 bytes on disk
    key_bits = key_size_bits or _ALGID_KEY_BITS.get(alg_id, _KEY_BITS_128)
    logger.debug("standard: keyBits=%d salt=%s", key_bits, salt.hex())
    return EncryptionInfo(
        kind=EncryptionKind.STANDARD,
        version_major=version_major,
        version_minor=version_minor,
        salt=salt,
        key_bits=key_bits,
        spin_count=_STANDARD_SPIN_COUNT,
        hash_algorithm="SHA-1",
        cipher_algorithm="AES",
        cipher_chaining="ChainingModeECB",
        block_size=_AES_BLOCK,
        hash_size=verifier_hash_size,
        enc_verifier=enc_verifier,
        enc_verifier_hash=enc_verifier_hash,
    )


def _parse_agile(blob: bytes, version_major: int, version_minor: int) -> EncryptionInfo:
    r"""Parse an agile-encryption ``\EncryptionInfo`` stream (Section 2.3.4.10).

    The 8-byte binary header is followed by a UTF-8 ``<encryption>`` descriptor.
    We pull the ``<keyData>`` (bulk cipher) and ``<p:encryptedKey>``
    (PasswordKeyEncryptor) attributes; the latter is the element the cracker
    attacks.
    """
    xml_text = blob[8:].rstrip(b"\x00").decode("utf-8")
    key_data = _element_attributes(xml_text, "keyData")
    enc_key = _password_encrypted_key(xml_text)
    logger.debug(
        "agile: hash=%s cipher=%s keyBits=%s spinCount=%s salt=%s",
        enc_key["hashAlgorithm"],
        enc_key["cipherAlgorithm"],
        enc_key["keyBits"],
        enc_key["spinCount"],
        base64.b64decode(enc_key["saltValue"]).hex(),
    )
    return EncryptionInfo(
        kind=EncryptionKind.AGILE,
        version_major=version_major,
        version_minor=version_minor,
        salt=base64.b64decode(enc_key["saltValue"]),
        key_bits=int(enc_key["keyBits"]),
        spin_count=int(enc_key["spinCount"]),
        hash_algorithm=enc_key["hashAlgorithm"],
        cipher_algorithm=enc_key["cipherAlgorithm"],
        cipher_chaining=enc_key["cipherChaining"],
        block_size=int(enc_key["blockSize"]),
        hash_size=int(enc_key["hashSize"]),
        enc_verifier=base64.b64decode(enc_key["encryptedVerifierHashInput"]),
        enc_verifier_hash=base64.b64decode(enc_key["encryptedVerifierHashValue"]),
        enc_key_value=base64.b64decode(enc_key["encryptedKeyValue"]),
        key_data_salt=base64.b64decode(key_data["saltValue"]),
        key_data_hash_algorithm=key_data["hashAlgorithm"],
        key_data_cipher_algorithm=key_data["cipherAlgorithm"],
        key_data_cipher_chaining=key_data["cipherChaining"],
        key_data_key_bits=int(key_data["keyBits"]),
        key_data_block_size=int(key_data["blockSize"]),
        key_data_hash_size=int(key_data["hashSize"]),
    )


def parse_encryption_info(blob: bytes) -> EncryptionInfo:
    r"""Parse the raw ``\EncryptionInfo`` stream bytes into an ``EncryptionInfo``.

    The version words at offset 0 select the scheme ([MS-OFFCRYPTO] Section
    2.1.4): ``vMinor == 4`` is agile, ``vMinor == 2`` is standard. Anything else
    -- extensible/IRM (``vMinor == 3``) or a CryptoAPI RC4 stream -- raises
    ``ValueError`` for the caller to route elsewhere.
    """
    if len(blob) < _STREAM_SIZE_PREFIX:
        msg = r"\EncryptionInfo stream is too short to contain a version header"
        raise ValueError(msg)
    version_major = int.from_bytes(blob[0:2], "little")
    version_minor = int.from_bytes(blob[2:4], "little")
    logger.debug("EncryptionInfo: vMajor=%d vMinor=%d", version_major, version_minor)
    if version_minor == _VERSION_MINOR_AGILE:
        return _parse_agile(blob, version_major, version_minor)
    if version_minor == _VERSION_MINOR_STANDARD:
        return _parse_standard(blob, version_major, version_minor)
    if version_minor == _VERSION_MINOR_EXTENSIBLE:
        msg = r"\EncryptionInfo is extensible/IRM encryption -- not password-recoverable"
        raise ValueError(msg)
    msg = f"unrecognised \\EncryptionInfo version {version_major}.{version_minor}"
    raise ValueError(msg)


# --- Hash-line emission ---------------------------------------------------


def office_hash_line(info: EncryptionInfo) -> str:
    """Emit the hashcat/John ``$office$*...`` line for ``info``.

    Standard -> ``2007`` (mode 9400). Agile SHA-1/AES-128 -> ``2010`` (9500);
    agile SHA-512/AES-256 -> ``2013`` (9600). Any other agile tuple has no
    hashcat mode and raises ``ValueError``. The verifier-hash token carries the
    first 20 bytes (standard) or 32 bytes (agile) of the field, matching what the
    parsers expect.
    """
    salt_hex = info.salt.hex()
    verifier_hex = info.enc_verifier.hex()
    if info.kind is EncryptionKind.STANDARD:
        verifier_hash_hex = info.enc_verifier_hash[:_SHA1_SIZE].hex()
        return f"$office$*2007*{info.hash_size}*{info.key_bits}*{info.salt_size}*{salt_hex}*{verifier_hex}*{verifier_hash_hex}"
    # Agile: pick the version proxy from the (hash, keyBits) tuple hashcat encodes.
    hashlib_name = _hashlib_name(info.hash_algorithm)
    if hashlib_name == "sha1" and info.key_bits == _KEY_BITS_128:
        version = "2010"
    elif hashlib_name == "sha512" and info.key_bits == _KEY_BITS_256:
        version = "2013"
    else:
        msg = f"no hashcat mode for agile tuple hash={info.hash_algorithm!r} keyBits={info.key_bits}"
        raise ValueError(msg)
    verifier_hash_hex = info.enc_verifier_hash[: 2 * _AES_BLOCK].hex()  # first 32 bytes / 64 hex
    return f"$office$*{version}*{info.spin_count}*{info.key_bits}*{info.salt_size}*{salt_hex}*{verifier_hex}*{verifier_hash_hex}"


def unified_office_line(info: EncryptionInfo) -> str:
    r"""Emit the self-describing ``$office$*...`` line for any ECMA-376 scheme.

    Grammar (docs/reference/hash-formats.md):
    ``$office$*<hashfunc>*<cipher>*<mode>*<iters>*<salt>*<encverifier>*<encverifierhash>``

    Covers standard (AES-ECB, fixed SHA-1 50k), agile (any hash x cipher x chaining x spin),
    and every non-default tuple — no ValueError, no mode table, no year numbers. The
    ``(hashfunc, cipher, mode, iters)`` tuple identifies the scheme unambiguously, so a
    cracker routes to the right kernel without a year proxy.

    The verifier-hash field carries the meaningful prefix: 20 B for standard (SHA-1 width),
    32 B for agile (first two cipher blocks, matching hashcat's own line cap).
    """
    hash_token = _unified_hash_token(info.hash_algorithm)
    cipher_token = _unified_cipher_token(info.cipher_algorithm, info.key_bits)
    mode_token = _unified_mode_token(info.cipher_chaining, info.kind)
    salt_hex = info.salt.hex()
    verifier_hex = info.enc_verifier.hex()
    hash_prefix = _SHA1_SIZE if info.kind is EncryptionKind.STANDARD else 2 * _AES_BLOCK
    verifier_hash_hex = info.enc_verifier_hash[:hash_prefix].hex()
    return f"$office$*{hash_token}*{cipher_token}*{mode_token}*{info.spin_count}*{salt_hex}*{verifier_hex}*{verifier_hash_hex}"


def _unified_hash_token(spec_name: str) -> str:
    """Map a spec hash algorithm string to the lowercase token for the unified ``$office$`` line."""
    squashed = "".join(ch for ch in spec_name.upper() if ch.isalnum())
    return {
        "SHA1": "sha1",
        "SHA256": "sha256",
        "SHA384": "sha384",
        "SHA512": "sha512",
        "MD5": "md5",
        "MD4": "md4",
        "MD2": "md2",
    }.get(squashed, spec_name.lower().replace("-", ""))


_3DES_2KEY_MAX: Final = 128  # 3DES at <=128-bit key length is the 2-key (112-bit) variant

# Maps spec cipher names to unified hash-line tokens for ciphers whose token is
# fixed (not parameterised by key size, unlike AES/RC4 which include the bit width).
_CIPHER_FIXED_TOKENS: Final[dict[str, str]] = {
    "RC2": "rc2",
    "DES": "des",
    "DESX": "desx",
    "3DES_112": "3des112",
}


def _unified_cipher_token(cipher_algorithm: str, key_bits: int) -> str:
    """Map a spec cipher algorithm + key size to the unified cipher token (e.g. ``aes256``, ``rc4-40``)."""
    name = cipher_algorithm.upper()
    if name in ("AES", "RC4"):
        sep = "" if name == "AES" else "-"
        return f"{name.lower()}{sep}{key_bits}"
    fixed = _CIPHER_FIXED_TOKENS.get(name)
    if fixed is not None:
        return fixed
    if name in ("3DES", "TRIPLEDES"):
        return "3des112" if key_bits <= _3DES_2KEY_MAX else "3des"
    return cipher_algorithm.lower()


def _unified_mode_token(cipher_chaining: str, kind: EncryptionKind) -> str:
    """Map the cipher chaining mode to ``ecb``/``cbc``/``cfb``/``stream``."""
    if kind is EncryptionKind.STANDARD:
        return "ecb"
    chain = cipher_chaining.replace("ChainingMode", "").upper()
    if chain == "CBC":
        return "cbc"
    if chain == "CFB":
        return "cfb"
    return chain.lower()


# --- Package decryption ---------------------------------------------------


def _decrypt_package_standard(info: EncryptionInfo, password: str, encrypted_package: bytes) -> bytes:
    r"""Decrypt a standard-scheme ``\EncryptedPackage`` (Section 2.3.4.4/2.3.4.9)."""
    key = _derive_key_standard(password, info.salt, info.key_bits)
    declared_size = int.from_bytes(encrypted_package[:_STREAM_SIZE_PREFIX], "little")
    plaintext = ciphers.aes_ecb_decrypt(key, encrypted_package[_STREAM_SIZE_PREFIX:])
    return plaintext[:declared_size]


def _decrypt_package_agile(info: EncryptionInfo, password: str, encrypted_package: bytes) -> bytes:
    r"""Decrypt an agile-scheme ``\EncryptedPackage`` (Section 2.3.4.14/2.3.4.15).

    Unwraps ``encryptedKeyValue`` with the intermediate block key to recover the
    bulk key, then CBC-decrypts the payload in 4096-byte segments whose per-segment
    IV is ``H(keyDataSalt || LE32(segmentIndex))`` fit to the block size.
    """
    if info.enc_key_value is None or info.key_data_salt is None:
        msg = r"agile \EncryptionInfo is missing the bulk-key material"
        raise ValueError(msg)
    cipher = info.cipher_algorithm
    hashlib_name = _hashlib_name(info.hash_algorithm)
    iterated = _iterate_agile_hash(password, info.salt, hashlib_name, info.spin_count)
    wrap_key = _finalize_agile_key(iterated, _BLOCK_KEY_INTERMEDIATE, hashlib_name, info.key_bits)
    bulk_key = ciphers.cbc_decrypt(cipher, wrap_key, _fit(info.salt, info.block_size), info.enc_key_value)
    key_data_cipher = info.key_data_cipher_algorithm or cipher
    key_data_hash = _hashlib_name(info.key_data_hash_algorithm or info.hash_algorithm)
    block_size = info.key_data_block_size or info.block_size
    declared_size = int.from_bytes(encrypted_package[:_STREAM_SIZE_PREFIX], "little")
    data = encrypted_package[_STREAM_SIZE_PREFIX:]
    plaintext = bytearray()
    for segment, offset in enumerate(range(0, len(data), _SEGMENT_SIZE)):
        chunk = data[offset : offset + _SEGMENT_SIZE]
        segment_iv = _fit(hashes.digest(key_data_hash, info.key_data_salt + segment.to_bytes(4, "little")), block_size)
        plaintext += ciphers.cbc_decrypt(key_data_cipher, bulk_key, segment_iv, chunk)
    return bytes(plaintext[:declared_size])


def decrypt_package(info: EncryptionInfo, password: str, encrypted_package: bytes) -> bytes:
    r"""Decrypt ``\EncryptedPackage`` to the original OPC ZIP bytes.

    Verifies the password first and raises ``ValueError`` if it is wrong, so a
    caller never mistakes AES garbage for a real package.
    """
    logger.debug("decrypt_package: kind=%s keyBits=%d", info.kind.value, info.key_bits)
    if not verify_password(info, password):
        msg = "incorrect password: verifier check failed"
        raise ValueError(msg)
    if info.kind is EncryptionKind.STANDARD:
        return _decrypt_package_standard(info, password, encrypted_package)
    return _decrypt_package_agile(info, password, encrypted_package)
