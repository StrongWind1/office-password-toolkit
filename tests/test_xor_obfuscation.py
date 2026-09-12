"""Self-tests for the legacy XOR-obfuscation primitives ([MS-OFFCRYPTO] Section 2.3.7).

Vectors are the worked examples cross-checked in the analysis notes (Section 7.1):
the 16-bit verifier, the 16-bit XorKey, the 32-bit Word verifier, and the full
16-byte obfuscation arrays for known passwords. The body transform has no published
numeric vector, so it is covered by a determinism + inverse round-trip test.
"""

from __future__ import annotations

import pytest

from office_password_toolkit.crypto.xor import (
    create_xor_array_method1,
    create_xor_key_method1,
    password_verifier_method1,
    password_verifier_method2,
    xor_decode_method1,
    xor_encode_method1,
)

# (password, verifier16, xorkey16, verifier32)
VECTORS = [
    ("a", 0xCE88, 0x9D77, 0x9D77CE88),
    ("abc", 0xCC1A, 0x514A, 0x514ACC1A),
    ("test", 0xCBEB, 0x1FC6, 0x1FC6CBEB),
    ("password", 0x83AF, 0x147A, 0x147A83AF),
    ("VelvetSweatshop", 0x9A0A, 0xB359, 0xB3599A0A),
]

ARRAYS = {
    "abc": bytes.fromhex("95999475DA5778 57DA7465A87A2F2577".replace(" ", "")),
    "VelvetSweatshop": bytes.fromhex("876B9AE21EE3 0562 1E69 9660 986E 9404".replace(" ", "")),
}


@pytest.mark.parametrize(("password", "verif16", "key16", "verif32"), VECTORS)
def test_verifier_and_key_vectors(password, verif16, key16, verif32):
    assert password_verifier_method1(password) == verif16
    assert create_xor_key_method1(password) == key16
    assert password_verifier_method2(password) == verif32


def test_method2_packs_key_and_verifier():
    # High 16 bits = XorKey, low 16 bits = Method 1 verifier.
    v = password_verifier_method2("abc")
    assert v >> 16 == create_xor_key_method1("abc")
    assert v & 0xFFFF == password_verifier_method1("abc")


@pytest.mark.parametrize(("password", "expected"), ARRAYS.items())
def test_obfuscation_array_vectors(password, expected):
    assert create_xor_array_method1(password) == expected


def test_obfuscation_array_is_16_bytes():
    for password, _v, _k, _v32 in VECTORS:
        assert len(create_xor_array_method1(password)) == 16


def test_decode_encode_round_trip():
    # No published numeric decode vector exists, so verify the transform is a
    # true inverse: decode(encode(x)) == x for an arbitrary body and offset.
    array = create_xor_array_method1("VelvetSweatshop")
    plaintext = bytes(range(256)) + b"the quick brown fox"
    for offset in (0, 1, 7, 15, 33):
        encoded = xor_encode_method1(plaintext, array, offset)
        assert encoded != plaintext
        assert xor_decode_method1(encoded, array, offset) == plaintext


def test_decode_is_deterministic():
    array = create_xor_array_method1("abc")
    data = b"\x00\x01\x02\x03\xff\xaa"
    assert xor_decode_method1(data, array) == xor_decode_method1(data, array)


def test_bad_array_width_rejected():
    with pytest.raises(ValueError, match="16 bytes"):
        xor_decode_method1(b"abc", b"\x00" * 15)


def test_empty_password_rejected_for_key():
    with pytest.raises(ValueError, match="length"):
        create_xor_key_method1("")
