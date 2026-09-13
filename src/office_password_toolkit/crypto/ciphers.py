# SPDX-License-Identifier: Apache-2.0
r"""Centralised cipher operations for every format handler.

All third-party cipher library imports (``cryptography``) are contained in this
single module. Protocol-specific code (KDFs, verifiers, parsers) imports cipher
primitives from here rather than reaching into ``cryptography`` directly, so a
library import-path change only touches this file.

RC4 is pure Python because ``cryptography`` restricts key sizes to a whitelist
that does not cover all sizes the [MS-OFFCRYPTO] CryptoAPI spec allows (e.g.
48-bit / 6-byte keys). This is the single canonical implementation, replacing
four former copies in ``rc4legacy``, ``msisam``, ``uls``, and ``formats/access``.

DESX has no native library support and is implemented manually per
[MS-OFFCRYPTO] Section 2.3.4.10: single-DES ECB with pre/post-whitening XOR
layers, wrapped in manual CBC chaining.
"""

from __future__ import annotations

import logging
from typing import Final

# --- All ``cryptography`` imports are confined to this module ----------------
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.decrepit.ciphers.algorithms import RC2 as _RC2
from cryptography.hazmat.decrepit.ciphers.algorithms import Blowfish as _Blowfish
from cryptography.hazmat.decrepit.ciphers.algorithms import TripleDES as _TripleDES
from cryptography.hazmat.decrepit.ciphers.modes import CFB as _CFB
from cryptography.hazmat.primitives.ciphers import Cipher as _Cipher
from cryptography.hazmat.primitives.ciphers import algorithms as _alg
from cryptography.hazmat.primitives.ciphers import modes as _modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM as _AESGCM

__all__ = [
    "InvalidTag",
    "aes_cbc_decrypt",
    "aes_cbc_encrypt",
    "aes_ecb_decrypt",
    "aes_ecb_encrypt_block",
    "aes_gcm_decrypt",
    "blowfish_cfb_decrypt",
    "cbc_decrypt",
    "cbc_encrypt",
    "desx_cbc_decrypt",
    "desx_cbc_encrypt",
    "rc2_cbc_decrypt",
    "rc2_cbc_encrypt",
    "rc4",
    "tripledes_cbc_decrypt",
    "tripledes_cbc_encrypt",
    "tripledes_ecb_decrypt",
    "tripledes_ecb_encrypt",
]

logger = logging.getLogger(__name__)

# DES key lengths for 3DES key expansion.
_DES_KEY_LEN: Final = 8  # single DES key
_TWO_KEY_LEN: Final = 16  # two-key 3DES (EDE2)

# DESX block size (DES operates on 8-byte blocks).
_DESX_BLOCK: Final = 8


# --- RC4 (pure Python) -------------------------------------------------------


def rc4(key: bytes, data: bytes) -> bytes:
    """RC4 stream cipher (KSA + PRGA). Symmetric: encrypt and decrypt are the same call.

    Pure-Python implementation that accepts any key length from 1 to 256 bytes,
    unlike ``cryptography`` which restricts RC4 to a whitelist of key sizes.
    Required by [MS-OFFCRYPTO] CryptoAPI which allows 40-128 bit keys in 8-bit
    steps, including 48-bit (6-byte) keys the library rejects. Verified against
    RFC 6229 test vectors (40/56/128/256-bit keys at offsets 0-4096).
    """
    # KSA (Key Scheduling Algorithm)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) & 0xFF
        s[i], s[j] = s[j], s[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    out = bytearray(len(data))
    i = j = 0
    for idx in range(len(data)):
        i = (i + 1) & 0xFF
        j = (j + s[i]) & 0xFF
        s[i], s[j] = s[j], s[i]
        out[idx] = data[idx] ^ s[(s[i] + s[j]) & 0xFF]
    return bytes(out)


# --- AES ----------------------------------------------------------------------


def aes_cbc_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """AES-CBC decrypt. Key: 16/24/32 bytes, IV: 16 bytes."""
    decryptor = _Cipher(_alg.AES(key), _modes.CBC(iv)).decryptor()
    return decryptor.update(data) + decryptor.finalize()


def aes_cbc_encrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """AES-CBC encrypt. Key: 16/24/32 bytes, IV: 16 bytes."""
    encryptor = _Cipher(_alg.AES(key), _modes.CBC(iv)).encryptor()
    return encryptor.update(data) + encryptor.finalize()


def aes_ecb_decrypt(key: bytes, data: bytes) -> bytes:
    """AES-ECB decrypt. Per [MS-OFFCRYPTO] Section 2.3.4.9 (standard scheme)."""
    decryptor = _Cipher(_alg.AES(key), _modes.ECB()).decryptor()
    return decryptor.update(data) + decryptor.finalize()


def aes_ecb_encrypt_block(key: bytes, block: bytes) -> bytes:
    """AES-ECB encrypt a single 16-byte block. Per [MS-OFFCRYPTO] Section 2.3.4.9."""
    encryptor = _Cipher(_alg.AES(key), _modes.ECB()).encryptor()
    return encryptor.update(block) + encryptor.finalize()


def aes_gcm_decrypt(key: bytes, nonce: bytes, ct_and_tag: bytes, aad: bytes | None) -> bytes:
    """AES-GCM authenticated decrypt. Raises :class:`InvalidTag` on wrong key/tampered data.

    Used by ODF 1.3 "Wholesome Encryption" (Argon2id + AES-256-GCM). The
    ``ct_and_tag`` input is ciphertext with the 16-byte auth tag appended, which
    is the format ``cryptography``'s AESGCM expects.
    """
    return _AESGCM(key).decrypt(nonce, ct_and_tag, aad)


# --- Blowfish -----------------------------------------------------------------


def blowfish_cfb_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """Blowfish CFB-64 decrypt. Key: 16 bytes, IV: 8 bytes.

    Full 8-byte-feedback CFB (CFB-64) as used by ODF 1.1. ``cryptography``'s
    :class:`CFB` mode is full-block feedback, matching the 64-bit Blowfish block.
    """
    decryptor = _Cipher(_Blowfish(key), _CFB(iv)).decryptor()
    return decryptor.update(data) + decryptor.finalize()


# --- Triple DES ---------------------------------------------------------------


def _expand_des_key(key: bytes) -> bytes:
    """Expand a DES/2-key-3DES key to the 24-byte form TripleDES requires.

    8-byte key (single DES) → key * 3 (runs DES three times with the same key).
    16-byte key (two-key 3DES / EDE2) → key + key[:8] (K1=K3).
    24-byte key (full 3DES) → unchanged.
    """
    if len(key) == _DES_KEY_LEN:
        return key * 3
    if len(key) == _TWO_KEY_LEN:
        return key + key[:_DES_KEY_LEN]
    return key


def tripledes_cbc_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """Triple-DES CBC decrypt. Key: 8/16/24 bytes (expanded internally), IV: 8 bytes."""
    decryptor = _Cipher(_TripleDES(_expand_des_key(key)), _modes.CBC(iv)).decryptor()
    return decryptor.update(data) + decryptor.finalize()


def tripledes_cbc_encrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """Triple-DES CBC encrypt. Key: 8/16/24 bytes (expanded internally), IV: 8 bytes."""
    encryptor = _Cipher(_TripleDES(_expand_des_key(key)), _modes.CBC(iv)).encryptor()
    return encryptor.update(data) + encryptor.finalize()


def tripledes_ecb_decrypt(key: bytes, data: bytes) -> bytes:
    """Triple-DES ECB decrypt. Key: 8/16/24 bytes (expanded internally).

    Replaces pycryptodome ``DES3.new(key, DES3.MODE_ECB).decrypt(data)``.
    """
    decryptor = _Cipher(_TripleDES(_expand_des_key(key)), _modes.ECB()).decryptor()
    return decryptor.update(data) + decryptor.finalize()


def tripledes_ecb_encrypt(key: bytes, data: bytes) -> bytes:
    """Triple-DES ECB encrypt. Key: 8/16/24 bytes (expanded internally)."""
    encryptor = _Cipher(_TripleDES(_expand_des_key(key)), _modes.ECB()).encryptor()
    return encryptor.update(data) + encryptor.finalize()


# --- RC2 ----------------------------------------------------------------------


def rc2_cbc_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """RC2 CBC decrypt. Variable key length."""
    decryptor = _Cipher(_RC2(key), _modes.CBC(iv)).decryptor()
    return decryptor.update(data) + decryptor.finalize()


def rc2_cbc_encrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """RC2 CBC encrypt. Variable key length."""
    encryptor = _Cipher(_RC2(key), _modes.CBC(iv)).encryptor()
    return encryptor.update(data) + encryptor.finalize()


# --- DESX (manual construction) -----------------------------------------------


def desx_cbc_decrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    r"""DESX-CBC decrypt: K3 \xor DES_K1^{-1}(K2 \xor ciphertext).

    DES-XEX3-CBC per [DRAFT-DESX] draft-ietf-ipsec-ciph-desx-00 Section 2.2,
    referenced by [MS-OFFCRYPTO] Section 2.3.4.10. The 24-byte key is split in
    Windows CNG order (DES key first, not the draft's XOR-key-first order):
    K1 (8 bytes, DES key), K2 (8 bytes, pre-whitening XOR), K3 (8 bytes,
    post-whitening XOR). CBC chaining XORs the previous ciphertext block into
    the plaintext after each block's DESX decrypt. A new Cipher object is
    created per block because no library provides native DESX; the whitening
    must wrap each individual ECB call.
    """
    des_key = key[:8]
    pre_whiten = key[8:16]
    post_whiten = key[16:24]
    plaintext = bytearray()
    prev = iv
    for offset in range(0, len(data), _DESX_BLOCK):
        ct_block = data[offset : offset + _DESX_BLOCK]
        pre = bytes(a ^ b for a, b in zip(ct_block, post_whiten, strict=True))
        decryptor = _Cipher(_TripleDES(des_key * 3), _modes.ECB()).decryptor()
        mid = decryptor.update(pre) + decryptor.finalize()
        pt_block = bytes(a ^ b for a, b in zip(mid, pre_whiten, strict=True))
        pt_block = bytes(a ^ b for a, b in zip(pt_block, prev, strict=True))
        plaintext += pt_block
        prev = ct_block
    return bytes(plaintext)


def desx_cbc_encrypt(key: bytes, iv: bytes, data: bytes) -> bytes:
    """DESX-CBC encrypt (inverse of :func:`desx_cbc_decrypt`). Same per-block Cipher approach.

    DES-XEX3-CBC per [DRAFT-DESX] draft-ietf-ipsec-ciph-desx-00 Section 2.2.
    """
    des_key = key[:8]
    pre_whiten = key[8:16]
    post_whiten = key[16:24]
    ciphertext = bytearray()
    prev = iv
    for offset in range(0, len(data), _DESX_BLOCK):
        pt_block = data[offset : offset + _DESX_BLOCK]
        pre = bytes(a ^ b for a, b in zip(pt_block, prev, strict=True))
        pre = bytes(a ^ b for a, b in zip(pre, pre_whiten, strict=True))
        encryptor = _Cipher(_TripleDES(des_key * 3), _modes.ECB()).encryptor()
        mid = encryptor.update(pre) + encryptor.finalize()
        ct_block = bytes(a ^ b for a, b in zip(mid, post_whiten, strict=True))
        ciphertext += ct_block
        prev = ct_block
    return bytes(ciphertext)


# --- String-based agile cipher dispatchers ------------------------------------


def cbc_decrypt(cipher_algorithm: str, key: bytes, iv: bytes, data: bytes) -> bytes:
    """Decrypt with the named agile cipher in CBC mode ([MS-OFFCRYPTO] Section 2.3.4.13).

    Routes the ``cipherAlgorithm`` XML attribute to the concrete cipher function.
    """
    name = cipher_algorithm.upper()
    if name == "AES":
        return aes_cbc_decrypt(key, iv, data)
    if name == "DESX":
        return desx_cbc_decrypt(key, iv, data)
    if name in ("3DES", "3DES_112", "DES"):
        return tripledes_cbc_decrypt(key, iv, data)
    if name == "RC2":
        return rc2_cbc_decrypt(key, iv, data)
    msg = f"unsupported cipherAlgorithm {cipher_algorithm!r}"
    raise ValueError(msg)


def cbc_encrypt(cipher_algorithm: str, key: bytes, iv: bytes, data: bytes) -> bytes:
    """Encrypt with the named agile cipher in CBC mode ([MS-OFFCRYPTO] Section 2.3.4.13)."""
    name = cipher_algorithm.upper()
    if name == "AES":
        return aes_cbc_encrypt(key, iv, data)
    if name == "DESX":
        return desx_cbc_encrypt(key, iv, data)
    if name in ("3DES", "3DES_112", "DES"):
        return tripledes_cbc_encrypt(key, iv, data)
    if name == "RC2":
        return rc2_cbc_encrypt(key, iv, data)
    msg = f"unsupported cipherAlgorithm {cipher_algorithm!r}"
    raise ValueError(msg)
