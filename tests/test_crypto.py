"""Tests for the XOR-obfuscation verifier primitive."""

from __future__ import annotations

from office_password_toolkit.crypto.xor import password_verifier_method1


def test_verifier_is_16_bit():
    assert 0 <= password_verifier_method1("VelvetSweatshop") <= 0xFFFF


def test_verifier_is_deterministic():
    assert password_verifier_method1("hashcat") == password_verifier_method1("hashcat")


def test_verifier_differs_by_password():
    assert password_verifier_method1("hashcat") != password_verifier_method1("wordpass")


def test_empty_password_verifier():
    # Empty password: array is just the length byte 0x00 -> 0 folded, XOR 0xCE4B.
    assert password_verifier_method1("") == 0xCE4B
