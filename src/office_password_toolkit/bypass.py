# SPDX-License-Identifier: Apache-2.0
"""Bypass: write a copy with removable protection stripped (no cracking)."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from office_password_toolkit.detect import detect
from office_password_toolkit.formats import handler_for

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


def bypass_file(path: Path, out: Path, *, remove_signatures: bool = False) -> int:
    """Write ``path`` to ``out`` with strip/collide-able protection removed.

    Returns the number of members/streams/elements actually rewritten. A return
    of ``0`` means the file was copied faithfully with no protection changes.

    When ``remove_signatures`` is set, digital signatures are deleted too -- an
    opt-in action that invalidates the signature and cannot be undone (signatures
    carry no recoverable secret, so they are left intact by default).

    Raises :class:`LookupError` if the container is unrecognised, or
    :class:`~office_password_toolkit.formats.base.HandlerNotImplementedError`
    if its handler has no bypass yet.
    """
    logger.debug("bypass_file: %s -> %s (remove_signatures=%s)", path, out, remove_signatures)
    result = detect(path)
    logger.debug("bypass_file: container=%s", result.container.value)
    handler = handler_for(result.container)
    if handler is None:
        logger.debug("bypass_file: no handler for %s", result.container.value)
        msg = f"unrecognised container for {path!s} ({result.container.value})"
        raise LookupError(msg)
    logger.debug("bypass_file: dispatching to %s", type(handler).__name__)
    return handler.bypass(path, out, remove_signatures=remove_signatures)
