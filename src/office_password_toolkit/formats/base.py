# SPDX-License-Identifier: Apache-2.0
"""Format-handler base class.

Each container kind gets a :class:`FormatHandler` subclass that knows how to
enumerate its gates, extract crackable hashes, and apply bypasses. Handlers are
registered in :mod:`office_password_toolkit.formats` and dispatched by
:class:`~office_password_toolkit.models.ContainerKind`.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from pathlib import Path

    from office_password_toolkit.models import ContainerKind, ExtractedHash, Gate


class HandlerNotImplementedError(NotImplementedError):
    """Raised when a handler has not implemented an operation for its container."""

    def __init__(self, operation: str, container: str) -> None:
        """Build the error for ``operation`` on ``container``."""
        super().__init__(f"{operation} is not yet implemented for container {container!r}")


class FormatHandler(ABC):
    """Base class for a per-container handler.

    Subclasses set :attr:`container` and override the operations they support.
    The default implementations raise :class:`HandlerNotImplementedError` so an
    unfinished handler fails loudly rather than silently returning nothing.
    """

    container: ClassVar[ContainerKind]

    def is_encrypted(self, path: Path) -> bool:
        """Report whether ``path`` carries document-open encryption (real ciphertext).

        A cheap, direct check used by :func:`~office_password_toolkit.detect.detect`
        to choose the decrypt-vs-bypass branch without enumerating every gate. The
        default raises so an unfinished handler is detected and falls back rather
        than silently reporting ``False``.
        """
        _ = path
        operation = "encryption detection"
        raise HandlerNotImplementedError(operation, self.container.value)

    def gates(self, path: Path) -> list[Gate]:
        """Enumerate every permission/password gate present in ``path``."""
        _ = path
        operation = "gate enumeration"
        raise HandlerNotImplementedError(operation, self.container.value)

    def extract(self, path: Path) -> list[ExtractedHash]:
        """Extract crackable hash lines (``$office$*...`` etc.) from ``path``."""
        _ = path
        operation = "hash extraction"
        raise HandlerNotImplementedError(operation, self.container.value)

    def bypass(self, path: Path, out: Path, *, remove_signatures: bool = False) -> None:
        """Write a copy of ``path`` to ``out`` with removable protection stripped.

        When ``remove_signatures`` is set, any digital signature is deleted too --
        an opt-in, destructive action that drops the integrity/authenticity claim
        and cannot be undone (a signature carries no recoverable secret).
        """
        _ = (path, out, remove_signatures)
        operation = "bypass"
        raise HandlerNotImplementedError(operation, self.container.value)

    def decrypt(self, path: Path, out: Path, password: str) -> None:
        """Decrypt ``path`` to ``out`` using the document-open ``password``."""
        _ = (path, out, password)
        operation = "decryption"
        raise HandlerNotImplementedError(operation, self.container.value)
