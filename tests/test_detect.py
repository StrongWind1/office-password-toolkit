"""Tests for magic-byte container detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from office_password_toolkit.constants import MAGIC_OLE_CFB, MAGIC_ZIP
from office_password_toolkit.detect import detect
from office_password_toolkit.models import ContainerKind

if TYPE_CHECKING:
    from pathlib import Path


def test_detects_ole_cfb(tmp_path: Path):
    f = tmp_path / "legacy.doc"
    f.write_bytes(MAGIC_OLE_CFB + b"\x00" * 32)
    assert detect(f).container == ContainerKind.OLE_CFB


def test_detects_ooxml_zip(tmp_path: Path):
    f = tmp_path / "modern.docx"
    f.write_bytes(MAGIC_ZIP + b"random zip bytes")
    assert detect(f).container == ContainerKind.OOXML_ZIP


def test_detects_odf_by_mimetype(tmp_path: Path):
    f = tmp_path / "doc.odt"
    f.write_bytes(MAGIC_ZIP + b"..mimetypeapplication/vnd.oasis.opendocument.text")
    assert detect(f).container == ContainerKind.ODF_ZIP


def test_unknown_container(tmp_path: Path):
    f = tmp_path / "random.bin"
    f.write_bytes(b"not an office file")
    assert detect(f).container == ContainerKind.UNKNOWN
