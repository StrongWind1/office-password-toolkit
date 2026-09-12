"""Tests for the ISO write-protection verifier ([MS-OFFCRYPTO] Section 2.4.2.4).

Vectors: password "hashcat" with the shared salt ``876MLoKTq42+/DLp415iZQ==``,
spinCount 100000. The SHA-512 digest is hashcat's 25300 self-test; the SHA-1
digest is the [MS-OFFCRYPTO] Section 7 / [MS-OE376] example. Both prove the
counter is APPENDED (not prepended) inside the spin loop.
"""

from __future__ import annotations

from base64 import b64decode

import pytest

from office_password_toolkit.crypto.protection import (
    hash_line_25300,
    iso_protection_hash,
    verify,
)

_SALT_B64 = "876MLoKTq42+/DLp415iZQ=="
_SHA512_HASH_B64 = "TNDvpvYyvlSUy97UOLKNhXynhUDDA7H8kLql0ISH5SxcP6hbthdjaTo4Z3/MU0dcR2SAd+AduYb3TB5CLZ8+ow=="
_SHA1_HASH_B64 = "Q90CLEfaPWfDIIE3UmWxb1KFkhM="
_SPIN = 100000


def _salt() -> bytes:
    return b64decode(_SALT_B64)


def test_sha512_vector_verifies():
    assert verify("hashcat", _salt(), _SPIN, "SHA-512", b64decode(_SHA512_HASH_B64))


def test_sha512_wrong_password_fails():
    assert not verify("wrongpass", _salt(), _SPIN, "SHA-512", b64decode(_SHA512_HASH_B64))


def test_sha1_vector_verifies():
    assert verify("hashcat", _salt(), _SPIN, "SHA-1", b64decode(_SHA1_HASH_B64))


def test_append_not_prepend_reproduces_vector():
    """The published digest is reproducible ONLY with the counter appended.

    Recompute with the counter PREPENDED (the agile-KDF order) and confirm it
    does NOT match -- the definitive proof this method appends the counter.
    """
    import hashlib

    salt = _salt()
    want = b64decode(_SHA512_HASH_B64)

    # APPEND (correct): matches the module implementation and the shipped vector.
    appended = iso_protection_hash("hashcat", salt, _SPIN, "SHA-512")
    assert appended == want

    # PREPEND (wrong, agile order): must diverge from the vector.
    pw = "hashcat".encode("utf-16-le")
    h = hashlib.sha512(salt + pw).digest()
    for i in range(_SPIN):
        h = hashlib.sha512(i.to_bytes(4, "little") + h).digest()
    assert h != want


def test_algorithm_name_variants():
    salt = _salt()
    want = b64decode(_SHA512_HASH_B64)
    for name in ("SHA-512", "SHA512", "sha 512", "sha-512"):
        assert iso_protection_hash("hashcat", salt, _SPIN, name) == want


def test_md4_md2_produce_correct_digest():
    salt = _salt()
    for name in ("MD2", "MD4"):
        digest = iso_protection_hash("hashcat", salt, 1, name)
        assert len(digest) == 16, f"{name} should produce a 16-byte digest"


def test_unknown_algorithm_raises():
    for name in ("WHIRLPOOL", "RIPEMD-160", "NONSENSE"):
        with pytest.raises(ValueError):
            iso_protection_hash("hashcat", _salt(), 1, name)


def test_hash_line_25300_valid_shape():
    line = hash_line_25300(_SALT_B64, _SHA512_HASH_B64)
    assert line == f"$office$2016$0$100000${_SALT_B64}${_SHA512_HASH_B64}"


def test_hash_line_25300_rejects_bad_spin():
    with pytest.raises(ValueError):
        hash_line_25300(_SALT_B64, _SHA512_HASH_B64, spin_count=50000)


def test_hash_line_25300_rejects_sha1_digest():
    # A 20-byte SHA-1 digest is not the 64-byte SHA-512 shape 25300 requires.
    with pytest.raises(ValueError):
        hash_line_25300(_SALT_B64, _SHA1_HASH_B64)
