# SPDX-License-Identifier: Apache-2.0
"""Format-handler registry: dispatch a :class:`ContainerKind` to its handler."""

from __future__ import annotations

from typing import TYPE_CHECKING

from office_password_toolkit.formats.access import AccessHandler
from office_password_toolkit.formats.base import FormatHandler
from office_password_toolkit.formats.mdw import MdwHandler
from office_password_toolkit.formats.odf import OdfHandler
from office_password_toolkit.formats.ole import OleHandler
from office_password_toolkit.formats.onenote import OneNoteHandler
from office_password_toolkit.formats.ooxml import OoxmlHandler
from office_password_toolkit.formats.outlook import OutlookHandler

if TYPE_CHECKING:
    from office_password_toolkit.models import ContainerKind

# One instance per container kind, keyed for O(1) dispatch.
_HANDLERS: dict[ContainerKind, FormatHandler] = {
    handler.container: handler
    for handler in (
        OleHandler(),
        OoxmlHandler(),
        OdfHandler(),
        OneNoteHandler(),
        OutlookHandler(),
        AccessHandler(),
        MdwHandler(),
    )
}


def handler_for(container: ContainerKind) -> FormatHandler | None:
    """Return the handler registered for ``container``, or ``None`` if unknown."""
    return _HANDLERS.get(container)


__all__ = ["FormatHandler", "handler_for"]
