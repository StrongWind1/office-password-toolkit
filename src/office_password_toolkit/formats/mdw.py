# SPDX-License-Identifier: Apache-2.0
"""MDW handler -- Jet workgroup information files (``.mdw`` / ``.mda``).

Workgroup files store User-Level Security accounts, passwords, PIDs, and the
workgroup identity (WID, owner name, organisation).  All user passwords are
3DES-EDE2-ECB encrypted with hardcoded keys and are instantly recoverable
(DECODE class).  The workgroup identity is encrypted with a separate 3DES key,
and PIDs use a custom obfuscation scheme.

Gate mapping:

* Every user account with a non-blank password -> **DECODE**.  The 3DES keys
  are fixed and hardcoded in ``msjet40.dll``; recovery is instant.
* Workgroup identity (WID/Name/Organisation) -> **DECODE**.  Separate 3DES key.
* Personal IDs (PIDs) -> **DECODE**.  Custom XOR/rotate/split obfuscation.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, ClassVar

from typing_extensions import override

from office_password_toolkit.crypto.uls import MdwFile, is_mdw, parse_mdw
from office_password_toolkit.formats.base import FormatHandler
from office_password_toolkit.models import ContainerKind, ExtractedHash, Gate, GateType, RecoveryClass

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


class MdwHandler(FormatHandler):
    """Handler for Jet workgroup information files."""

    container: ClassVar[ContainerKind] = ContainerKind.ACCESS_MDW

    @override
    def is_encrypted(self, path: Path) -> bool:
        """MDW files are never document-open encrypted; passwords are per-account."""
        return False

    @override
    def gates(self, path: Path) -> list[Gate]:
        """Enumerate all password-protected accounts in the workgroup file."""
        result = _parse_file(path)
        if result is None:
            return []

        gates: list[Gate] = []
        for acc in result.accounts:
            if acc.is_group or not acc.password:
                continue
            gates.append(
                Gate(
                    gate=GateType.OPEN,
                    recovery=RecoveryClass.DECODE,
                    note=f"ULS account {acc.name!r}: password={acc.password!r}",
                )
            )
        return gates

    @override
    def extract(self, path: Path) -> list[ExtractedHash]:
        """No crackable hashes -- passwords are directly decoded (DECODE class)."""
        return []


def _parse_file(path: Path) -> MdwFile | None:
    """Read and parse a .mdw file, returning the decoded structure."""
    try:
        data = path.read_bytes()
    except OSError:
        logger.debug("Cannot read MDW file: %s", path)
        return None
    if not is_mdw(data):
        return None
    return parse_mdw(data)
