"""Tests for the VBA project-password codec and verifier ([MS-OVBA] Section 2.4)."""

from __future__ import annotations

import hashlib

from office_password_toolkit.crypto import vba

# All-zero CLSID forced when DPB stores a password hash ([MS-OVBA] Section 2.3.1.2).
_ZERO_CLSID = "{00000000-0000-0000-0000-000000000000}"


def test_project_key_matches_spec_examples():
    # Section 3.1.6 example CLSID sums (braces + hyphens included) to 0xDF.
    assert vba.project_key("{917DED54-440B-4FD1-A5C1-74ACF261E600}") == 0xDF
    # All-zero CLSID of the hash case sums to 0xAC.
    assert vba.project_key(_ZERO_CLSID) == 0xAC


def test_vector_a_no_password_dpb():
    # [MS-OVBA] Section 3.1.6 printed no-password DPB decodes to a single 0x00.
    assert vba.decode_data_encryption("0E0CD1ECDFF4E7F5E7F5E7") == b"\x00"


def test_vector_a_cmg_and_gc():
    # Sibling CMG (no protection bits) and GC (visible) from the same worked example.
    assert vba.decode_data_encryption("0705D8E3D8EDDBF1DBF1DBF1DBF1") == bytes(4)
    assert vba.decode_data_encryption("1517CAF1D6F9D7F9D706") == b"\xff"


def test_password_hash_against_hand_computed_sha1():
    # SHA1(mbcs("macro") || 11223344) computed independently here.
    key = bytes.fromhex("11223344")
    expected = hashlib.sha1(b"macro" + key).hexdigest()
    assert vba.password_hash("macro", key).hex() == expected
    # And the value pinned by the spec-derived Vector B.
    assert expected == "9113756963e99e6821d78ae7643278285ff3cf55"


def test_vector_b_full_roundtrip():
    # Build the hash-case DPB exactly as Vector B, then recover the crack line.
    key = bytes.fromhex("11223344")
    digest = vba.password_hash("macro", key)
    struct = vba.build_password_hash_structure(key, digest)
    assert struct.hex() == "ffffffff112233449113756963e99e6821d78ae7643278285ff3cf5500"

    dpb = vba.encode_data_encryption(struct, 0xAB, 0xAC)
    # The exact DPB string derived in the analysis (Seed=0xAB, ProjKey=0xAC, filler 0x00).
    assert dpb == "ABA907551A721A72E58E1B720BA11E90F33273CEBFD8361EBFE81C9567CBE16B5639865DDB"

    # decode -> parse -> hashcat -m 110 line round-trips to the original salt and digest.
    assert vba.decode_data_encryption(dpb) == struct
    line = vba.extract_vba_hash(dpb)
    assert line == "9113756963e99e6821d78ae7643278285ff3cf55:11223344"


def test_encode_decode_nulls_roundtrip_with_zero_bytes():
    # Exercise Encode/Decode Nulls (Section 2.4.4.2/3) with 0x00 bytes in Key and hash.
    key = bytes.fromhex("00112200")
    digest = bytes.fromhex("00" * 3 + "aabbcc" + "00" + "ddeeff11223344556677889900")
    assert len(digest) == 20
    struct = vba.build_password_hash_structure(key, digest)
    parsed = vba.parse_password_hash_structure(struct)
    assert parsed == (key, digest)


def test_extract_returns_none_for_cleartext_password():
    # A plaintext-password DPB is a decode, not a crack: no hash line.
    proj_key = vba.project_key(_ZERO_CLSID)
    dpb = vba.encode_data_encryption(b"secret\x00", 0x0A, proj_key)
    assert vba.extract_vba_hash(dpb) is None
    assert vba.decode_data_encryption(dpb) == b"secret\x00"


def test_unprotected_state_decodes_to_clear_values():
    lines = dict(line.split("=", 1) for line in vba.unprotected_project_state().splitlines())
    assert vba.decode_data_encryption(lines["CMG"].strip('"')) == bytes(4)
    assert vba.decode_data_encryption(lines["DPB"].strip('"')) == b"\x00"
    assert vba.decode_data_encryption(lines["GC"].strip('"')) == b"\xff"
