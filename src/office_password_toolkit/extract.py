# SPDX-License-Identifier: Apache-2.0
"""Hash extraction: turn a file into crackable ``$office$``/``$oldoffice$``/``$odf$`` lines.

Returns ALL extractable hash lines a file carries -- not just the document-open
password, but also ISO protection verifiers (25300), VBA project SHA-1 (110),
XOR-obfuscation verifiers, and PST CRC-32 lines -- so a single ``extract`` call
surfaces everything a cracker or auditor would want to see.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from office_password_toolkit.detect import detect
from office_password_toolkit.formats import handler_for

if TYPE_CHECKING:
    from pathlib import Path

    from office_password_toolkit.models import ExtractedHash

logger = logging.getLogger(__name__)


def extract_hashes(path: Path) -> list[ExtractedHash]:
    """Detect ``path`` and return every crackable hash line its handler can extract.

    Raises :class:`LookupError` if the container is unrecognised, or
    :class:`~office_password_toolkit.formats.base.HandlerNotImplementedError`
    if its handler has no extractor yet.
    """
    logger.debug("extract_hashes: %s", path)
    result = detect(path)
    logger.debug("extract_hashes: container=%s", result.container.value)
    handler = handler_for(result.container)
    if handler is None:
        logger.debug("extract_hashes: no handler for %s", result.container.value)
        msg = f"unrecognised container for {path!s} ({result.container.value})"
        raise LookupError(msg)
    hashes = handler.extract(path)
    logger.debug("extract_hashes: %s returned %d hashes", type(handler).__name__, len(hashes))
    return hashes
