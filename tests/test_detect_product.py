# SPDX-License-Identifier: Apache-2.0
"""Tests for product detection (detect_product and its integration with detect).

Each test exercises detect_product() or detect() against a real corpus file
(preferred) or a minimal synthetic file when no corpus specimen exists.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

import pytest

from office_password_toolkit.detect import detect, detect_product
from office_password_toolkit.models import ContainerKind, Product

# Corpus root relative to this file.
CORPUS: Final = Path(__file__).parent / "corpus"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _corpus(relpath: str) -> Path:
    """Return a corpus file path, raising FileNotFoundError if missing."""
    p = CORPUS / relpath
    if not p.exists():
        msg = f"corpus file not found: {p}"
        raise FileNotFoundError(msg)
    return p


def _has_corpus(relpath: str) -> bool:
    return (CORPUS / relpath).exists()


# ---------------------------------------------------------------------------
# 1. .xls (OLE/CFB) -> Product.EXCEL
# ---------------------------------------------------------------------------


class TestDetectProductExcelXls:
    """A .xls file should detect as Product.EXCEL via the Workbook/Book stream."""

    RELPATH: Final = "protected/47034.xls"

    @pytest.mark.skipif(
        not _has_corpus("protected/47034.xls"),
        reason="corpus file protected/47034.xls not available",
    )
    def test_detect_product_excel_xls(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.OLE_CFB)
        assert result is Product.EXCEL


# ---------------------------------------------------------------------------
# 2. .doc (OLE/CFB) -> Product.WORD
# ---------------------------------------------------------------------------


class TestDetectProductWordDoc:
    """A .doc file should detect as Product.WORD via the WordDocument stream."""

    RELPATH: Final = "encrypted/doc-open-rc4-2003.doc"

    @pytest.mark.skipif(
        not _has_corpus("encrypted/doc-open-rc4-2003.doc"),
        reason="corpus file encrypted/doc-open-rc4-2003.doc not available",
    )
    def test_detect_product_word_doc(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.OLE_CFB)
        assert result is Product.WORD


# ---------------------------------------------------------------------------
# 3. .ppt (OLE/CFB) -> Product.POWERPOINT
# ---------------------------------------------------------------------------


class TestDetectProductPpt:
    """A .ppt file should detect as Product.POWERPOINT via the 'PowerPoint Document' stream."""

    RELPATH: Final = "encrypted/cryptoapi-proc2356.ppt"

    @pytest.mark.skipif(
        not _has_corpus("encrypted/cryptoapi-proc2356.ppt"),
        reason="corpus file encrypted/cryptoapi-proc2356.ppt not available",
    )
    def test_detect_product_ppt(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.OLE_CFB)
        assert result is Product.POWERPOINT


# ---------------------------------------------------------------------------
# 4. .xlsx (OPC/ZIP) -> Product.EXCEL
# ---------------------------------------------------------------------------


class TestDetectProductXlsx:
    """A .xlsx file (unencrypted OPC/ZIP) should detect as Product.EXCEL via [Content_Types].xml."""

    RELPATH: Final = "protected/47889.xlsx"

    @pytest.mark.skipif(
        not _has_corpus("protected/47889.xlsx"),
        reason="corpus file protected/47889.xlsx not available",
    )
    def test_detect_product_xlsx(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.OOXML_ZIP)
        assert result is Product.EXCEL


# ---------------------------------------------------------------------------
# 5. .docx (OPC/ZIP) -> Product.WORD
# ---------------------------------------------------------------------------


class TestDetectProductDocx:
    """A .docx file (unencrypted OPC/ZIP) should detect as Product.WORD via [Content_Types].xml."""

    RELPATH: Final = "protected/docx-modify-2016.docx"

    @pytest.mark.skipif(
        not _has_corpus("protected/docx-modify-2016.docx"),
        reason="corpus file protected/docx-modify-2016.docx not available",
    )
    def test_detect_product_docx(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.OOXML_ZIP)
        assert result is Product.WORD


# ---------------------------------------------------------------------------
# 6. .pptx (OPC/ZIP) -> Product.POWERPOINT
# ---------------------------------------------------------------------------


class TestDetectProductPptx:
    """A .pptx file (unencrypted OPC/ZIP) should detect as Product.POWERPOINT via [Content_Types].xml."""

    RELPATH: Final = "protected/hello-world-signed.pptx"

    @pytest.mark.skipif(
        not _has_corpus("protected/hello-world-signed.pptx"),
        reason="corpus file protected/hello-world-signed.pptx not available",
    )
    def test_detect_product_pptx(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.OOXML_ZIP)
        assert result is Product.POWERPOINT


# ---------------------------------------------------------------------------
# 7. Encrypted .xlsx (OLE/CFB wrapper) -> Product.EXCEL via extension fallback
# ---------------------------------------------------------------------------


class TestDetectProductEncryptedXlsx:
    """An encrypted .xlsx is an OLE/CFB container with EncryptionInfo + EncryptedPackage.

    No Workbook/Book stream exists, so product detection falls through to the
    extension map (_OLE_EXT_TO_PRODUCT -> _OOXML_EXT_TO_PRODUCT) and resolves
    from the .xlsx suffix.
    """

    RELPATH: Final = "encrypted/m-xlsx-open-2013.xlsx"

    @pytest.mark.skipif(
        not _has_corpus("encrypted/m-xlsx-open-2013.xlsx"),
        reason="corpus file encrypted/m-xlsx-open-2013.xlsx not available",
    )
    def test_detect_product_encrypted_xlsx(self) -> None:
        path = _corpus(self.RELPATH)
        # The physical container is OLE/CFB (encrypted OOXML wrapper).
        result = detect_product(path, ContainerKind.OLE_CFB)
        assert result is Product.EXCEL


# ---------------------------------------------------------------------------
# 8. .odt (ODF/ZIP) -> Product.OPENDOCUMENT
# ---------------------------------------------------------------------------


class TestDetectProductOdf:
    """An .odt file should detect as Product.OPENDOCUMENT (direct mapping from ODF_ZIP)."""

    RELPATH: Final = "encrypted/odt-enc-test.odt"

    @pytest.mark.skipif(
        not _has_corpus("encrypted/odt-enc-test.odt"),
        reason="corpus file encrypted/odt-enc-test.odt not available",
    )
    def test_detect_product_odf(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.ODF_ZIP)
        assert result is Product.OPENDOCUMENT


# ---------------------------------------------------------------------------
# 9. .pst -> Product.OUTLOOK
# ---------------------------------------------------------------------------


class TestDetectProductPst:
    """A .pst file should detect as Product.OUTLOOK (direct mapping from PST container)."""

    RELPATH: Final = "protected/pst-backup-2013.pst"

    @pytest.mark.skipif(
        not _has_corpus("protected/pst-backup-2013.pst"),
        reason="corpus file protected/pst-backup-2013.pst not available",
    )
    def test_detect_product_pst(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.PST)
        assert result is Product.OUTLOOK


# ---------------------------------------------------------------------------
# 10. .one -> Product.ONENOTE
# ---------------------------------------------------------------------------


class TestDetectProductOneNote:
    """A .one file should detect as Product.ONENOTE (direct mapping from ONENOTE container)."""

    RELPATH: Final = "encrypted/onenote-section-pw-2013.one"

    @pytest.mark.skipif(
        not _has_corpus("encrypted/onenote-section-pw-2013.one"),
        reason="corpus file encrypted/onenote-section-pw-2013.one not available",
    )
    def test_detect_product_onenote(self) -> None:
        path = _corpus(self.RELPATH)
        result = detect_product(path, ContainerKind.ONENOTE)
        assert result is Product.ONENOTE


# ---------------------------------------------------------------------------
# 11. .mdb / .accdb -> Product.ACCESS
# ---------------------------------------------------------------------------


class TestDetectProductAccess:
    """An Access database should detect as Product.ACCESS (direct mapping from ACCESS container)."""

    RELPATH_ACCDB: Final = "encrypted/accdb-enc-2013.accdb"
    RELPATH_MDB: Final = "protected/mdb-vba-hash-2003.mdb"

    @pytest.mark.skipif(
        not _has_corpus("encrypted/accdb-enc-2013.accdb"),
        reason="corpus file encrypted/accdb-enc-2013.accdb not available",
    )
    def test_detect_product_access_accdb(self) -> None:
        path = _corpus(self.RELPATH_ACCDB)
        result = detect_product(path, ContainerKind.ACCESS)
        assert result is Product.ACCESS

    @pytest.mark.skipif(
        not _has_corpus("protected/mdb-vba-hash-2003.mdb"),
        reason="corpus file protected/mdb-vba-hash-2003.mdb not available",
    )
    def test_detect_product_access_mdb(self) -> None:
        path = _corpus(self.RELPATH_MDB)
        result = detect_product(path, ContainerKind.ACCESS)
        assert result is Product.ACCESS


# ---------------------------------------------------------------------------
# 12. detect() result includes product field
# ---------------------------------------------------------------------------


class TestDetectResultIncludesProduct:
    """The full detect() pipeline should populate DetectResult.product."""

    @pytest.mark.skipif(
        not _has_corpus("protected/47034.xls"),
        reason="corpus file protected/47034.xls not available",
    )
    def test_detect_result_includes_product_xls(self) -> None:
        """detect() on a .xls should return a DetectResult with product=Product.EXCEL."""
        path = _corpus("protected/47034.xls")
        result = detect(path)
        assert result.product is Product.EXCEL
        assert result.container is ContainerKind.OLE_CFB

    @pytest.mark.skipif(
        not _has_corpus("protected/docx-modify-2016.docx"),
        reason="corpus file protected/docx-modify-2016.docx not available",
    )
    def test_detect_result_includes_product_docx(self) -> None:
        """detect() on a .docx should return a DetectResult with product=Product.WORD."""
        path = _corpus("protected/docx-modify-2016.docx")
        result = detect(path)
        assert result.product is Product.WORD

    @pytest.mark.skipif(
        not _has_corpus("protected/pst-backup-2013.pst"),
        reason="corpus file protected/pst-backup-2013.pst not available",
    )
    def test_detect_result_includes_product_pst(self) -> None:
        """detect() on a .pst should return a DetectResult with product=Product.OUTLOOK."""
        path = _corpus("protected/pst-backup-2013.pst")
        result = detect(path)
        assert result.product is Product.OUTLOOK

    def test_detect_result_product_defaults_to_unknown(self, tmp_path: Path) -> None:
        """detect() on an unrecognised file should set product=Product.UNKNOWN."""
        f = tmp_path / "random.bin"
        f.write_bytes(b"not an office file at all")
        result = detect(f)
        assert result.product is Product.UNKNOWN
