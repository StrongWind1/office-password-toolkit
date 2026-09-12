"""Tests for the embedded default-password list."""

from __future__ import annotations

from office_password_toolkit.constants import DEFAULT_PASSWORD_EXCEL, DEFAULT_PASSWORD_POWERPOINT
from office_password_toolkit.defaults import default_passwords


def test_default_passwords_are_ordered_and_spec_confirmed():
    passwords = default_passwords()
    # Empty string is tried first (the "protected, no open password" case).
    assert passwords[0] == ""
    # The two documented defaults are present, verbatim from [MS-OFFCRYPTO] 2.4.2.3.
    assert DEFAULT_PASSWORD_EXCEL == "VelvetSweatshop"
    assert DEFAULT_PASSWORD_POWERPOINT == "/01Hannes Ruescher/01"
    assert DEFAULT_PASSWORD_EXCEL in passwords
    assert DEFAULT_PASSWORD_POWERPOINT in passwords
