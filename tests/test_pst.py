"""Tests for the PST CRC-32 password verifier and NDB body cipher."""

from __future__ import annotations

import zlib

from office_password_toolkit.crypto.pst import (
    PID_TAG_PST_PASSWORD,
    crc_collision,
    cyclic_decode,
    describe_password_strip,
    password_crc,
    permute_decode,
    pst_crc32,
)


def _bitwise_reflected_crc(data: bytes, seed: int = 0) -> int:
    # Independent bit-at-a-time reflected CRC-32 (poly 0xEDB88320, init seed,
    # no xorout) to cross-check the table-driven pst_crc32.
    crc = seed & 0xFFFFFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (0xEDB88320 ^ (crc >> 1)) if (crc & 1) else (crc >> 1)
    return crc & 0xFFFFFFFF


def test_crc_matches_independent_bitwise():
    for sample in (b"", b"123456789", b"hashcat", bytes(range(256))):
        assert pst_crc32(sample) == _bitwise_reflected_crc(sample)


def test_crc_is_not_zlib():
    # [MS-PST] Section 5.3 seeds with 0 and does not invert, unlike zlib.crc32.
    assert pst_crc32(b"hashcat") != zlib.crc32(b"hashcat")
    assert pst_crc32(b"123456789") == 0x2DFD2D88


def test_crc_of_zeros_is_zero():
    # Seed-0, no-xorout CRC is linear: the all-zero message hashes to 0.
    assert pst_crc32(b"\x00\x00\x00\x00") == 0


def test_password_crc_is_crc32():
    assert password_crc(b"hashcat") == pst_crc32(b"hashcat")


def test_permute_round_trip():
    payload = bytes(range(256)) + b"encoded NDB body block"
    assert permute_decode(permute_decode(payload, encode=True)) == payload


def test_permute_encode_decode_are_inverse_tables():
    # Every byte must survive an encode then decode unchanged (mpbbI == mpbbR^-1).
    everything = bytes(range(256))
    assert permute_decode(permute_decode(everything, encode=True)) == everything


def test_cyclic_is_self_inverse():
    payload = bytes(range(256)) + b"cyclic block"
    for key in (0x00000000, 0x12345678, 0xDEADBEEF, 0xFFFFFFFF):
        encoded = cyclic_decode(payload, key)
        assert cyclic_decode(encoded, key) == payload


def test_cyclic_key_changes_output():
    payload = b"the quick brown fox"
    # Keys whose 16-bit mixers (key ^ (key >> 16)) differ must diverge.
    assert cyclic_decode(payload, 0x00000001) != cyclic_decode(payload, 0x00000002)


def test_crc_collision_hits_target():
    for target in (0x00000000, 0x5A0E0134, 0xDEADBEEF, 0xFFFFFFFF, password_crc(b"hashcat")):
        forged = crc_collision(target)
        assert len(forged) == 4
        assert pst_crc32(forged) == target


def test_strip_plan_targets_password_property():
    plan = describe_password_strip()
    assert plan.property_tag == PID_TAG_PST_PASSWORD == 0x67FF0003
    assert plan.node_id == 0x0021
    assert plan.new_value == 0
