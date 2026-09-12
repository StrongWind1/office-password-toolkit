# SPDX-License-Identifier: Apache-2.0
"""Container/format detection and top-level triage.

Detection is magic-byte first (the extension is advisory and often wrong for
encrypted files, which are re-wrapped in an OLE/CFB container while keeping the
outer extension). Per-gate enumeration is delegated to the format handlers in
:mod:`office_password_toolkit.formats`.

Product detection (Word vs Excel vs PowerPoint, etc.) is layered on top of the
container classification: it reads internal streams (OLE) or OPC content-type
prefixes (OOXML) to determine which Office application owns the file, falling
back to file extension when the container cannot be opened (e.g. encrypted or
corrupted).
"""

from __future__ import annotations

import logging
import struct
import zipfile
from typing import TYPE_CHECKING, Final

import olefile

from office_password_toolkit.constants import (
    ACCESS_SIGNATURE_OFFSET,
    MAGIC_ACCESS_ACE,
    MAGIC_ACCESS_JET,
    MAGIC_ACCESS_MDW,
    MAGIC_MSISAM,
    MAGIC_OLE_CFB,
    MAGIC_ONENOTE,
    MAGIC_PST,
    MAGIC_ZIP,
)
from office_password_toolkit.formats import handler_for
from office_password_toolkit.formats.base import HandlerNotImplementedError
from office_password_toolkit.models import ContainerKind, DetectResult, Product

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)

# How many head bytes to read for container disambiguation. The OLE/CFB, ZIP,
# OneNote, and PST magics all sit at offset 0, but the ODF marker below does not
# finish until ~offset 72 in a real package (a 30-byte ZIP local-file header, the
# 8-byte "mimetype" member name, then the stored mimetype string). 512 bytes
# clears that comfortably even when the local header carries an extra field.
_HEADER_READ: Final = 512

# ODF ZIP packages begin with an uncompressed "mimetype" member; OOXML packages
# carry "[Content_Types].xml". Both share the ZIP local-file-header magic, so the
# member name distinguishes them.
_ODF_MARKER = b"mimetypeapplication/vnd.oasis.opendocument"

# An encrypted OOXML package is wrapped back into an OLE/CFB container carrying
# this stream (see [MS-OFFCRYPTO] Section 2.3.4). Its presence is the cheapest,
# most reliable "this file is encrypted" signal for the modern formats.
_ENCRYPTION_INFO_STREAM = "EncryptionInfo"

# --- OLE/CFB stream names that identify the owning product --------------------
# These are top-level streams whose presence is authoritative. The names come
# from the binary format specs: [MS-DOC] (WordDocument), [MS-XLS] (Workbook,
# Book for BIFF5), [MS-PPT] (PowerPoint Document), and the Visio VSD format
# (VisioDocument).
_OLE_STREAM_WORD: Final = "WordDocument"  # [MS-DOC] Section 2.1.1
_OLE_STREAM_WORKBOOK: Final = "Workbook"  # [MS-XLS] Section 2.1.7.20 (BIFF8)
_OLE_STREAM_BOOK: Final = "Book"  # [MS-XLS] BIFF5 variant
_OLE_STREAM_POWERPOINT: Final = "PowerPoint Document"  # [MS-PPT] Section 2.1.1
_OLE_STREAM_VISIO: Final = "VisioDocument"  # Visio binary (.vsd)

# --- Extension-to-Product fallback maps ---------------------------------------
# Used when internal stream/content-type inspection fails (encrypted, corrupt,
# or ambiguous container). Kept per-container so a .doc inside a ZIP would not
# accidentally match.
_OLE_EXT_TO_PRODUCT: Final[dict[str, Product]] = {
    ".doc": Product.WORD,
    ".dot": Product.WORD,
    ".wbk": Product.WORD,
    ".xls": Product.EXCEL,
    ".xlt": Product.EXCEL,
    ".xla": Product.EXCEL,
    ".ppt": Product.POWERPOINT,
    ".pps": Product.POWERPOINT,
    ".pot": Product.POWERPOINT,
    ".vsd": Product.VISIO,
    ".vss": Product.VISIO,
    ".vst": Product.VISIO,
    ".pub": Product.PUBLISHER,
    ".mpp": Product.PROJECT,
    ".mpt": Product.PROJECT,
    ".msg": Product.OUTLOOK,
    ".oft": Product.OUTLOOK,
}

_OOXML_EXT_TO_PRODUCT: Final[dict[str, Product]] = {
    ".docx": Product.WORD,
    ".docm": Product.WORD,
    ".dotx": Product.WORD,
    ".dotm": Product.WORD,
    ".xlsx": Product.EXCEL,
    ".xlsm": Product.EXCEL,
    ".xlsb": Product.EXCEL,
    ".xltx": Product.EXCEL,
    ".xltm": Product.EXCEL,
    ".xlam": Product.EXCEL,
    ".pptx": Product.POWERPOINT,
    ".pptm": Product.POWERPOINT,
    ".ppsx": Product.POWERPOINT,
    ".ppsm": Product.POWERPOINT,
    ".potx": Product.POWERPOINT,
    ".potm": Product.POWERPOINT,
    ".vsdx": Product.VISIO,
    ".vsdm": Product.VISIO,
    ".vstx": Product.VISIO,
    ".vstm": Product.VISIO,
    ".vssx": Product.VISIO,
    ".vssm": Product.VISIO,
}

_GENERIC_EXT_TO_PRODUCT: Final[dict[str, Product]] = {
    ".xsn": Product.INFOPATH,
    ".onepkg": Product.ONENOTE,
}


def detect(path: Path) -> DetectResult:
    """Triage a single file into a :class:`DetectResult` (container + encrypted + product).

    The returned :attr:`~DetectResult.gates` list is **not populated** by this function
    because gate enumeration is more expensive and not always needed. To enumerate gates,
    call ``handler_for(result.container).gates(path)`` on the result's container, or use
    the CLI ``info`` command which does this automatically.
    """
    header = _read_header(path)
    container = _classify(header)
    encrypted = _is_encrypted(path, container)
    product = detect_product(path, container)
    return DetectResult(
        path=str(path),
        container=container,
        extension=path.suffix.lower(),
        encrypted=encrypted,
        product=product,
    )


def detect_product(path: Path, container: ContainerKind) -> Product:
    """Determine which Office application owns *path* based on internal streams or content types.

    The detection strategy depends on the container kind:

    - **OLE_CFB**: open with olefile and check for well-known top-level stream names
      (WordDocument, Workbook, PowerPoint Document, VisioDocument). Falls back to
      extension if the file cannot be opened or no known stream is found.
    - **OOXML_ZIP**: open as a ZIP, read ``[Content_Types].xml``, and look for OPC
      content-type directory prefixes (``word/``, ``xl/``, ``ppt/``, ``visio/``).
    - **ODF_ZIP**: always :attr:`Product.OPENDOCUMENT`.
    - **ONENOTE**: always :attr:`Product.ONENOTE`.
    - **PST**: always :attr:`Product.OUTLOOK`.
    - **ACCESS**: always :attr:`Product.ACCESS`.
    - **UNKNOWN**: extension fallback only.

    Never raises -- product detection must not crash the pipeline.
    """
    # Containers with a 1:1 product mapping -- no inspection needed.
    direct: dict[ContainerKind, tuple[Product, str]] = {
        ContainerKind.ODF_ZIP: (Product.OPENDOCUMENT, "ODF mimetype entry"),
        ContainerKind.ONENOTE: (Product.ONENOTE, "OneNote magic bytes"),
        ContainerKind.PST: (Product.OUTLOOK, "PST magic bytes"),
        ContainerKind.ACCESS: (Product.ACCESS, "Access engine signature"),
    }
    if container in direct:
        product, source = direct[container]
        logger.debug("Product detected: %s (from %s)", product, source)
        return product

    # Containers that require internal inspection.
    if container is ContainerKind.OLE_CFB:
        return _product_from_ole(path)
    if container is ContainerKind.OOXML_ZIP:
        return _product_from_ooxml(path)

    # UNKNOWN container -- last-resort extension fallback.
    ext = path.suffix.lower()
    product = _GENERIC_EXT_TO_PRODUCT.get(ext, Product.UNKNOWN)
    if product is not Product.UNKNOWN:
        logger.debug("Product detected: %s (from %s extension)", product, ext)
    return product


# --- OLE/CFB product inspection -----------------------------------------------


def _product_from_ole(path: Path) -> Product:
    """Inspect OLE/CFB streams to determine product, falling back to extension."""
    try:
        if not olefile.isOleFile(str(path)):
            return _product_from_ole_extension(path)
        with olefile.OleFileIO(str(path)) as ole:
            # Flatten the directory listing to a set of top-level stream names
            # for O(1) lookups.  olefile.listdir() returns lists of path segments;
            # we only need the first (top-level) segment.
            top_streams: set[str] = {entry[0] for entry in ole.listdir() if entry}
            return _match_ole_stream(top_streams, path)
    except (OSError, ValueError, struct.error, RuntimeError):
        # Encrypted or corrupted CFB -- fall back to extension.
        logger.debug("OLE open failed for %s, falling back to extension", path)
        return _product_from_ole_extension(path)


def _match_ole_stream(top_streams: set[str], path: Path) -> Product:
    """Match OLE top-level streams to a product, most-specific first."""
    if _OLE_STREAM_WORD in top_streams:
        logger.debug("Product detected: %s (from %s stream)", Product.WORD, _OLE_STREAM_WORD)
        return Product.WORD
    if _OLE_STREAM_WORKBOOK in top_streams or _OLE_STREAM_BOOK in top_streams:
        stream = _OLE_STREAM_WORKBOOK if _OLE_STREAM_WORKBOOK in top_streams else _OLE_STREAM_BOOK
        logger.debug("Product detected: %s (from %s stream)", Product.EXCEL, stream)
        return Product.EXCEL
    if _OLE_STREAM_POWERPOINT in top_streams:
        logger.debug("Product detected: %s (from %s stream)", Product.POWERPOINT, _OLE_STREAM_POWERPOINT)
        return Product.POWERPOINT
    if _OLE_STREAM_VISIO in top_streams:
        logger.debug("Product detected: %s (from %s stream)", Product.VISIO, _OLE_STREAM_VISIO)
        return Product.VISIO

    # No well-known stream found (might be Publisher, Project, or an encrypted
    # OOXML wrapper that only contains EncryptionInfo + EncryptedPackage) --
    # fall back to extension.
    return _product_from_ole_extension(path)


def _product_from_ole_extension(path: Path) -> Product:
    """Extension-based fallback for OLE/CFB files without a recognized stream.

    Checks both legacy OLE extensions and OOXML extensions because encrypted
    OOXML files (.docx, .xlsx, .pptx, etc.) are re-wrapped in OLE/CFB containers
    while retaining their original extension.
    """
    ext = path.suffix.lower()
    product = _OLE_EXT_TO_PRODUCT.get(ext, Product.UNKNOWN)
    if product is Product.UNKNOWN:
        product = _OOXML_EXT_TO_PRODUCT.get(ext, Product.UNKNOWN)
    if product is not Product.UNKNOWN:
        logger.debug("Product detected: %s (from %s extension, OLE fallback)", product, ext)
    return product


# --- OOXML/ZIP product inspection ---------------------------------------------


def _product_from_ooxml(path: Path) -> Product:
    """Read [Content_Types].xml from an OOXML ZIP to determine the product."""
    try:
        with zipfile.ZipFile(str(path), "r") as zf:
            try:
                content_types = zf.read("[Content_Types].xml").decode("utf-8", errors="replace")
            except KeyError:
                # No [Content_Types].xml -- unusual but possible in a damaged package.
                logger.debug("[Content_Types].xml missing in %s, falling back to extension", path)
                return _product_from_ooxml_extension(path)
            return _match_ooxml_content_types(content_types, path)
    except (zipfile.BadZipFile, OSError, ValueError):
        # Encrypted or corrupted ZIP -- fall back to extension.
        logger.debug("ZIP open failed for %s, falling back to extension", path)
        return _product_from_ooxml_extension(path)


def _match_ooxml_content_types(content_types: str, path: Path) -> Product:
    """Match OPC content-type directory prefixes to a product."""
    # The PartName attributes in [Content_Types].xml use forward-slash paths
    # like /word/document.xml, /xl/workbook.xml, /ppt/presentation.xml.
    # A substring check on the lowercase content is fast and sufficient.
    ct_lower = content_types.lower()
    if "word/" in ct_lower or "/word/" in ct_lower:
        logger.debug("Product detected: %s (from %s)", Product.WORD, "word/ in [Content_Types].xml")
        return Product.WORD
    if "xl/" in ct_lower or "/xl/" in ct_lower:
        logger.debug("Product detected: %s (from %s)", Product.EXCEL, "xl/ in [Content_Types].xml")
        return Product.EXCEL
    if "ppt/" in ct_lower or "/ppt/" in ct_lower:
        logger.debug("Product detected: %s (from %s)", Product.POWERPOINT, "ppt/ in [Content_Types].xml")
        return Product.POWERPOINT
    if "visio/" in ct_lower or "/visio/" in ct_lower:
        logger.debug("Product detected: %s (from %s)", Product.VISIO, "visio/ in [Content_Types].xml")
        return Product.VISIO

    # Ambiguous OOXML package -- fall back to extension.
    return _product_from_ooxml_extension(path)


def _product_from_ooxml_extension(path: Path) -> Product:
    """Extension-based fallback for OOXML ZIP files without a recognized content-type prefix."""
    ext = path.suffix.lower()
    product = _OOXML_EXT_TO_PRODUCT.get(ext, Product.UNKNOWN)
    if product is not Product.UNKNOWN:
        logger.debug("Product detected: %s (from %s extension, OOXML fallback)", product, ext)
    return product


# --- Existing detection infrastructure (unchanged) ----------------------------


def _read_header(path: Path) -> bytes:
    """Read the first header bytes, tolerating short files."""
    with path.open("rb") as handle:
        return handle.read(_HEADER_READ)


def _classify(header: bytes) -> ContainerKind:
    """Map raw header bytes to a :class:`ContainerKind`.

    Priority order matters: OLE/CFB is checked first because an encrypted OOXML
    document (``.docx``/``.xlsx``) is physically an OLE container wrapping the
    ``EncryptionInfo`` + ``EncryptedPackage`` streams ([MS-OFFCRYPTO] Section 2.3.4).
    Access is last because its engine-name string at offset 0x04 is less distinctive
    than the offset-0 magics.
    """
    if header.startswith(MAGIC_OLE_CFB):
        return ContainerKind.OLE_CFB
    if header.startswith(MAGIC_ONENOTE):
        return ContainerKind.ONENOTE
    if header.startswith(MAGIC_PST):
        return ContainerKind.PST
    if header.startswith(MAGIC_ZIP):
        # ODF stores the mimetype as the first member; OOXML does not.
        return ContainerKind.ODF_ZIP if _ODF_MARKER in header else ContainerKind.OOXML_ZIP
    # Access .mdb/.accdb/.mdw: the engine-name string sits at offset 0x04 (offset
    # 0 is the non-distinctive JetFormat header), so it is matched last.
    sig_15 = header[ACCESS_SIGNATURE_OFFSET : ACCESS_SIGNATURE_OFFSET + len(MAGIC_ACCESS_JET)]
    if sig_15 in (MAGIC_ACCESS_JET, MAGIC_ACCESS_ACE, MAGIC_MSISAM):
        return ContainerKind.ACCESS
    sig_13 = header[ACCESS_SIGNATURE_OFFSET : ACCESS_SIGNATURE_OFFSET + len(MAGIC_ACCESS_MDW)]
    return ContainerKind.ACCESS_MDW if sig_13 == MAGIC_ACCESS_MDW else ContainerKind.UNKNOWN


def _is_encrypted(path: Path, container: ContainerKind) -> bool:
    """Report whether the file carries document-open encryption (real ciphertext).

    Delegated to the container's format handler when it implements the check
    (legacy FilePass/FIB, ODF manifest, OneNote/PST, etc.). Until a handler does,
    this falls back to the authoritative modern signal: the OLE/CFB
    ``EncryptionInfo`` stream that wraps an encrypted OOXML package.
    """
    handler = handler_for(container)
    if handler is not None:
        try:
            return handler.is_encrypted(path)
        except HandlerNotImplementedError:
            pass  # fall through to the generic EncryptionInfo probe below
    if container is not ContainerKind.OLE_CFB:
        return False
    if not olefile.isOleFile(str(path)):
        return False
    try:
        with olefile.OleFileIO(str(path)) as ole:
            return any(e[0].lower() == _ENCRYPTION_INFO_STREAM.lower() for e in ole.listdir() if e)
    except (OSError, ValueError, struct.error):
        # A truncated or malformed CFB is treated as "not encrypted" rather than
        # raising -- detection must never crash on adversarial input.
        return False
