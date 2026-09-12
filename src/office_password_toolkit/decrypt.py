# SPDX-License-Identifier: Apache-2.0
"""Decryption: write a plaintext copy given the document-open password."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from office_password_toolkit.detect import detect
from office_password_toolkit.formats import handler_for

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


def decrypt_file(path: Path, out: Path, password: str) -> None:
    """Detect ``path`` and decrypt it to ``out`` with ``password``.

    Raises :class:`LookupError` if the container is unrecognised, or
    :class:`NotImplementedError` if its handler has no decryptor yet.
    """
    logger.debug("decrypt_file: %s -> %s", path, out)
    result = detect(path)
    logger.debug("decrypt_file: container=%s", result.container.value)
    handler = handler_for(result.container)
    if handler is None:
        logger.debug("decrypt_file: no handler for %s", result.container.value)
        msg = f"unrecognised container for {path!s} ({result.container.value})"
        raise LookupError(msg)
    logger.debug("decrypt_file: dispatching to %s", type(handler).__name__)
    handler.decrypt(path, out, password)
