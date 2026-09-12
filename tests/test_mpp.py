"""Tests for the MPP Props parser and password decode (crypto/mpp.py)."""

from __future__ import annotations

import struct

import pytest

from office_password_toolkit.crypto.mpp import (
    PROPS_KEY_ENCRYPTION_CODE,
    PROPS_KEY_PASSWORD_DATA,
    PROPS_KEY_PASSWORD_FLAG,
    PROPS_KEY_WRITE_PASSWORD_DATA,
    _PASSWORD_BLOCK_SIZE,
    _PASSWORD_MASK,
    decode_mpp9_password,
    decode_mpp9_write_password,
    has_open_password,
    has_write_reservation,
    parse_props,
    password_flag,
)


def _build_props_stream(items: list[tuple[int, bytes]]) -> bytes:
    """Build a synthetic Props9-format binary stream from (key, value) pairs."""
    header = bytearray(16)
    struct.pack_into("<H", header, 12, len(items))
    body = bytearray()
    for key, value in items:
        body += struct.pack("<iiI", len(value), key, 0)
        body += value
        if len(value) % 2 != 0:
            body += b"\x00"
    return bytes(header) + bytes(body)


def _build_password_block(password: str, code: int) -> bytes:
    """Plant a password into a 64-byte block using the XOR+permutation scheme."""
    mask = (0xFF - code) & 0xFF if code != 0 else 0
    block = bytearray(_PASSWORD_BLOCK_SIZE)
    for i, ch in enumerate(password):
        if i >= len(_PASSWORD_MASK):
            break
        block[_PASSWORD_MASK[i]] = ord(ch)
    for i in range(_PASSWORD_BLOCK_SIZE):
        block[i] ^= mask
    return bytes(block)


def test_parse_props_empty():
    assert parse_props(b"") == {}
    assert parse_props(b"\x00" * 15) == {}


def test_parse_props_single_item():
    data = _build_props_stream([(0x1234, b"hello")])
    props = parse_props(data)
    assert props[0x1234] == b"hello"


def test_parse_props_multiple_items():
    data = _build_props_stream([(0x01, b"ab"), (0x02, b"cde"), (0x03, b"f")])
    props = parse_props(data)
    assert props[0x01] == b"ab"
    assert props[0x02] == b"cde"
    assert props[0x03] == b"f"


def test_parse_props_alignment_padding():
    data = _build_props_stream([(0xAA, b"x")])
    props = parse_props(data)
    assert props[0xAA] == b"x"


def test_password_flag_not_set():
    props = parse_props(_build_props_stream([]))
    assert password_flag(props) == 0
    assert not has_open_password(props)
    assert not has_write_reservation(props)


def test_password_flag_open_only():
    data = _build_props_stream([(PROPS_KEY_PASSWORD_FLAG, b"\x01")])
    props = parse_props(data)
    assert has_open_password(props)
    assert not has_write_reservation(props)


def test_password_flag_write_only():
    data = _build_props_stream([(PROPS_KEY_PASSWORD_FLAG, b"\x02")])
    props = parse_props(data)
    assert not has_open_password(props)
    assert has_write_reservation(props)


def test_password_flag_both():
    data = _build_props_stream([(PROPS_KEY_PASSWORD_FLAG, b"\x03")])
    props = parse_props(data)
    assert has_open_password(props)
    assert has_write_reservation(props)


def test_decode_mpp9_password_round_trip():
    password = "Secret1"
    code = 0x42
    block = _build_password_block(password, code)
    items = [
        (PROPS_KEY_PASSWORD_FLAG, b"\x01"),
        (PROPS_KEY_PASSWORD_DATA, block),
        (PROPS_KEY_ENCRYPTION_CODE, bytes([code])),
    ]
    props = parse_props(_build_props_stream(items))
    assert decode_mpp9_password(props) == password


def test_decode_mpp9_password_no_encryption_code():
    password = "open"
    block = _build_password_block(password, 0)
    items = [
        (PROPS_KEY_PASSWORD_FLAG, b"\x01"),
        (PROPS_KEY_PASSWORD_DATA, block),
    ]
    props = parse_props(_build_props_stream(items))
    assert decode_mpp9_password(props) == password


def test_decode_mpp9_password_empty_when_no_flag():
    block = _build_password_block("Secret1", 0x42)
    items = [
        (PROPS_KEY_PASSWORD_FLAG, b"\x00"),
        (PROPS_KEY_PASSWORD_DATA, block),
        (PROPS_KEY_ENCRYPTION_CODE, b"\x42"),
    ]
    props = parse_props(_build_props_stream(items))
    assert decode_mpp9_password(props) is None


def test_decode_mpp9_password_missing_block():
    items = [
        (PROPS_KEY_PASSWORD_FLAG, b"\x01"),
        (PROPS_KEY_ENCRYPTION_CODE, b"\x42"),
    ]
    props = parse_props(_build_props_stream(items))
    assert decode_mpp9_password(props) is None


def test_decode_mpp9_write_password():
    password = "WriteP"
    code = 0x10
    block = _build_password_block(password, code)
    items = [
        (PROPS_KEY_PASSWORD_FLAG, b"\x02"),
        (PROPS_KEY_WRITE_PASSWORD_DATA, block),
        (PROPS_KEY_ENCRYPTION_CODE, bytes([code])),
    ]
    props = parse_props(_build_props_stream(items))
    assert decode_mpp9_write_password(props) == password


def test_decode_mpp9_long_password():
    password = "1234567890ABCDEF"
    code = 0xFF
    block = _build_password_block(password, code)
    items = [
        (PROPS_KEY_PASSWORD_FLAG, b"\x01"),
        (PROPS_KEY_PASSWORD_DATA, block),
        (PROPS_KEY_ENCRYPTION_CODE, bytes([code])),
    ]
    props = parse_props(_build_props_stream(items))
    assert decode_mpp9_password(props) == password


def test_signed_key_parsing():
    key = -0x01  # should be stored as signed i32, parsed as unsigned 0xFFFFFFFF
    data = _build_props_stream([(key, b"val")])
    props = parse_props(data)
    assert 0xFFFFFFFF in props
