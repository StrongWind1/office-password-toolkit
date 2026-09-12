# SPDX-License-Identifier: Apache-2.0
"""Embedded default passwords.

Microsoft Office auto-encrypts a file that is *protected* but has no user open
password, using a fixed default so the app can round-trip an encrypted stream
that still opens with no prompt. Trying these defaults defeats a large fraction
of "encrypted" files with no cracking at all.

Both defaults are spec-confirmed verbatim in [MS-OFFCRYPTO] Section 2.4.2.3
(see ``constants.DEFAULT_PASSWORD_EXCEL`` / ``DEFAULT_PASSWORD_POWERPOINT``).

Verifying a default against a specific file requires the document-open verifier
and is added with the ``crypto`` layer; this module owns the authoritative list.
"""

from __future__ import annotations

from office_password_toolkit.constants import DEFAULT_PASSWORDS


def default_passwords() -> tuple[str, ...]:
    """Return the ordered auto-try list (empty string, then the two defaults)."""
    return DEFAULT_PASSWORDS
