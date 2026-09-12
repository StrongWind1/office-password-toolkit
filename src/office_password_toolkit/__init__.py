# SPDX-License-Identifier: Apache-2.0
"""office-password-toolkit -- detect, extract, bypass, and decrypt Office/ODF passwords.

Quick start::

    import office_password_toolkit as opt

    result = opt.detect("secret.xlsx")
    hashes = opt.extract_hashes("secret.xlsx")
"""

from __future__ import annotations

from importlib.metadata import version

from office_password_toolkit.bypass import bypass_file
from office_password_toolkit.decrypt import decrypt_file
from office_password_toolkit.defaults import default_passwords
from office_password_toolkit.detect import detect
from office_password_toolkit.extract import extract_hashes
from office_password_toolkit.formats import handler_for
from office_password_toolkit.models import (
    ContainerKind,
    DetectResult,
    ExtractedHash,
    Gate,
    GateType,
    HashScheme,
    Product,
    RecoveryClass,
    Status,
    gate_scheme_tag,
    gate_status,
)

# Single source of truth for the version: the installed package metadata, which
# hatchling populates from the [project] version in pyproject.toml.
__version__ = version("office-password-toolkit")

__all__ = [
    "ContainerKind",
    "DetectResult",
    "ExtractedHash",
    "Gate",
    "GateType",
    "HashScheme",
    "Product",
    "RecoveryClass",
    "Status",
    "__version__",
    "bypass_file",
    "decrypt_file",
    "default_passwords",
    "detect",
    "extract_hashes",
    "gate_scheme_tag",
    "gate_status",
    "handler_for",
]
