# SPDX-License-Identifier: Apache-2.0
"""Project-wide constants: exit codes, container magic bytes, and default passwords.

Import rules: this module imports only from the standard library.
"""

from __future__ import annotations

from typing import Final

# --- Process exit codes ----------------------------------------------------
EXIT_OK: Final = 0  # success
EXIT_ERROR: Final = 1  # general error
EXIT_UNSUPPORTED: Final = 2  # recognised container, but the gate/scheme is not handled
EXIT_NOT_ENCRYPTED: Final = 3  # file carries no password/protection gate
EXIT_CRACK_REQUIRED: Final = 4  # hashes emitted, no plaintext produced -- cracking required
EXIT_UNRECOVERABLE: Final = 5  # not password-recoverable (digital signature / IRM)
EXIT_REFUSED: Final = 6  # refused for safety (would overwrite the input or an existing output)
EXIT_NO_HASH: Final = 7  # gate(s) present but none produce an extractable hash (e.g., no-password protection)

# --- Container magic signatures --------------------------------------------
# OLE / Compound File Binary ([MS-CFB]) -- legacy .doc/.xls/.ppt, and the CFB
# wrapper around an encrypted OOXML package (\EncryptionInfo + \EncryptedPackage).
MAGIC_OLE_CFB: Final = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"
# ZIP local file header -- OPC/OOXML (.docx/.xlsx/.pptx) and ODF (.odt/.ods/.odp).
MAGIC_ZIP: Final = b"PK\x03\x04"
# OneNote revision store ([MS-ONESTORE]) header GUID (first 16 bytes).
MAGIC_ONENOTE: Final = b"\xe4\x52\x5c\x7b\x8c\xd8\xa7\x4d\xae\xb1\x53\x78\xd0\x29\x96\xd3"
# Outlook PST/OST ([MS-PST]) -- "!BDN" sentinel at offset 0.
MAGIC_PST: Final = b"!BDN"
# Access Jet/ACE database -- the engine-name string at header offset 0x04
# ("Standard Jet DB" for .mdb, "Standard ACE DB" for .accdb). Offset 0 is the
# JetFormat header \x00\x01\x00\x00, which is not distinctive on its own.
MAGIC_ACCESS_JET: Final = b"Standard Jet DB"
MAGIC_ACCESS_ACE: Final = b"Standard ACE DB"
ACCESS_SIGNATURE_OFFSET: Final = 0x04
# Access workgroup (.mdw) files -- "Jet System DB" at offset 0x04.
MAGIC_ACCESS_MDW: Final = b"Jet System DB"
# MSISAM database (Microsoft Money 2000+) -- "MSISAM Database" at offset 0x04.
MAGIC_MSISAM: Final = b"MSISAM Database"

# --- Embedded default passwords ([MS-OFFCRYPTO] Section 2.4.2.3) ------------
# Excel auto-encrypts a workbook that is protected but has no user open password
# under this fixed default, so it round-trips while opening with no prompt.
# Spec-confirmed verbatim: [MS-OFFCRYPTO] Section 2.4.2.3; [MS-XLS] Section 2.4.191 <100>;
# [MS-XLSB] Section 2.4.308 <25>.
DEFAULT_PASSWORD_EXCEL: Final = "VelvetSweatshop"
# PowerPoint (2003 / 2007 / 2007 SP1; 2007 SP2 dropped it) uses this fixed default
# when a modify password is set but no open password.
# Spec-confirmed verbatim: [MS-OFFCRYPTO] Section 2.4.2.3 (byte string), note <26>.
DEFAULT_PASSWORD_POWERPOINT: Final = "/01Hannes Ruescher/01"

# Ordered auto-try list: empty string first, then the two documented defaults.
# A large fraction of "encrypted" Office files open on one of these with no cracking.
DEFAULT_PASSWORDS: Final[tuple[str, ...]] = (
    "",
    DEFAULT_PASSWORD_EXCEL,
    DEFAULT_PASSWORD_POWERPOINT,
)
