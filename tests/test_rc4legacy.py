"""Self-tests for the legacy RC4 document-open KDFs.

Both vectors use password "hashcat" and come verbatim from the hashcat module
self-tests (modes 9700 and 9800), cross-checked against [MS-OFFCRYPTO] Section 2.3.6
and Section 2.3.5 in the source analysis docs.
"""

from __future__ import annotations

import hashlib
import struct

from office_password_toolkit.crypto.rc4legacy import (
    Rc4Scheme,
    parse_rc4_cryptoapi_header,
    rc4_crypt,
    rc4_cryptoapi_derive_key,
    rc4_cryptoapi_hash_line,
    rc4_cryptoapi_verify,
    rc4_md5_derive_key,
    rc4_md5_hash_line,
    rc4_md5_verify,
    rc4_scheme,
)

# --- hashcat mode 9700 self-test vector (module_09700.c), password "hashcat" ---
_MD5_SALT = bytes.fromhex("55045061647456688860411218030058")
_MD5_ENC_VERIFIER = bytes.fromhex("e7e24d163fbd743992d4b8892bf3f2f7")
_MD5_ENC_VERIFIER_HASH = bytes.fromhex("493410dbc832557d3fe1870ace8397e2")
_MD5_LINE = "$oldoffice$0*55045061647456688860411218030058*e7e24d163fbd743992d4b8892bf3f2f7*493410dbc832557d3fe1870ace8397e2"

# --- hashcat mode 9800 self-test vector (module_09800.c), password "hashcat" ---
_CAPI_SALT = bytes.fromhex("83328705222323020515404251156288")
_CAPI_ENC_VERIFIER = bytes.fromhex("2855956a165ff6511bc7f4cd77b9e101")
_CAPI_ENC_VERIFIER_HASH = bytes.fromhex("941861655e73a09c40f7b1e9dfd0c256ed285acd")
_CAPI_LINE = "$oldoffice$3*83328705222323020515404251156288*2855956a165ff6511bc7f4cd77b9e101*941861655e73a09c40f7b1e9dfd0c256ed285acd"


def test_md5_verify_correct_password():
    assert rc4_md5_verify("hashcat", _MD5_SALT, _MD5_ENC_VERIFIER, _MD5_ENC_VERIFIER_HASH) is True


def test_md5_wrong_password_fails():
    assert rc4_md5_verify("Password1", _MD5_SALT, _MD5_ENC_VERIFIER, _MD5_ENC_VERIFIER_HASH) is False


def test_md5_intermediate_t1():
    # t1 = MD5(t0 || salt repeated 16x)[:5] must equal the 9710/9720 seed.
    pw = "hashcat".encode("utf-16-le")
    t0 = hashlib.md5(pw, usedforsecurity=False).digest()[:5]
    t1 = hashlib.md5((t0 + _MD5_SALT) * 16, usedforsecurity=False).digest()[:5]
    assert t1.hex() == "91b2e062b9"


def test_md5_recovered_verifier_is_all_0x41():
    key = rc4_md5_derive_key("hashcat", _MD5_SALT, 0)
    decrypted = rc4_crypt(key, _MD5_ENC_VERIFIER + _MD5_ENC_VERIFIER_HASH)
    assert decrypted[:16] == b"\x41" * 16


def test_md5_hash_line_roundtrip():
    assert rc4_md5_hash_line(0, _MD5_SALT, _MD5_ENC_VERIFIER, _MD5_ENC_VERIFIER_HASH) == _MD5_LINE


def test_cryptoapi_verify_correct_password():
    assert rc4_cryptoapi_verify("hashcat", _CAPI_SALT, 40, _CAPI_ENC_VERIFIER, _CAPI_ENC_VERIFIER_HASH) is True


def test_cryptoapi_wrong_password_fails():
    assert rc4_cryptoapi_verify("Password1", _CAPI_SALT, 40, _CAPI_ENC_VERIFIER, _CAPI_ENC_VERIFIER_HASH) is False


def test_cryptoapi_derived_40bit_key():
    # Hfinal[0:5] must equal the mode-9820 appended key b8f63619ca.
    key = rc4_cryptoapi_derive_key("hashcat", _CAPI_SALT, 40, 0)
    assert key[:5].hex() == "b8f63619ca"
    assert key[5:] == b"\x00" * 11


def test_cryptoapi_hash_line_roundtrip():
    assert rc4_cryptoapi_hash_line(3, 40, _CAPI_SALT, _CAPI_ENC_VERIFIER, _CAPI_ENC_VERIFIER_HASH) == _CAPI_LINE


def test_scheme_discriminator():
    assert rc4_scheme(1, 1, 0) == Rc4Scheme.MD5
    assert rc4_scheme(3, 2, 0x04) == Rc4Scheme.CRYPTOAPI


def test_parse_cryptoapi_header_roundtrip():
    # Build a minimal but spec-shaped RC4 CryptoAPI blob and parse it back.
    csp = "Microsoft Base Cryptographic Provider v1.0\x00".encode("utf-16-le")
    header = struct.pack("<IIiiIIII", 0x04, 0, 0x6801, 0x8004, 40, 1, 0, 0) + csp
    verifier = struct.pack("<I", 16) + _CAPI_SALT + _CAPI_ENC_VERIFIER + struct.pack("<I", 20) + _CAPI_ENC_VERIFIER_HASH
    blob = struct.pack("<HHII", 3, 2, 0x04, len(header)) + header + verifier
    parsed = parse_rc4_cryptoapi_header(blob)
    assert parsed["key_size"] == 40
    assert parsed["salt"] == _CAPI_SALT
    assert parsed["encrypted_verifier"] == _CAPI_ENC_VERIFIER
    assert parsed["encrypted_verifier_hash"] == _CAPI_ENC_VERIFIER_HASH
    assert parsed["scheme"] == Rc4Scheme.CRYPTOAPI
    assert parsed["alg_id"] == 0x6801
    assert parsed["alg_id_hash"] == 0x8004
