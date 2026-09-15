"""Tests for new CLI features: batch info, --json, --quiet, --no-hash, --debug, advanced subcommands, directory input, status:scheme output."""

from __future__ import annotations

import json
import shutil
from typing import TYPE_CHECKING

from typer.testing import CliRunner

from office_password_toolkit.cli.app import app
from office_password_toolkit.constants import MAGIC_OLE_CFB, MAGIC_ZIP

if TYPE_CHECKING:
    from pathlib import Path

runner = CliRunner()

# --- Corpus paths (relative to repo root, resolved at call site) -----------
_ENCRYPTED_DOCX = "tests/corpus/encrypted/docx-open-agile-2013.docx"
_ENCRYPTED_XLSX = "tests/corpus/encrypted/m-xlsx-open-2013.xlsx"
_PROTECTED_XLSX = "tests/corpus/protected/m-xlsx-sheet-2013.xlsx"
_SIGNED_XLSX = "tests/corpus/protected/hello-world-signed.xlsx"


# ==========================================================================
# info command
# ==========================================================================


def test_info_single_file():
    """info on a single encrypted file: exit 0, stdout has hash, stderr has human-readable detail."""
    result = runner.invoke(app, ["info", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    assert "$office-open$" in result.stdout
    assert "Word document (encrypted)" in result.stderr
    assert "Document-open password" in result.stderr


def test_info_multiple_files():
    """info with 2 files: hash lines on stdout, table + stats on stderr."""
    result = runner.invoke(app, ["info", _ENCRYPTED_DOCX, _PROTECTED_XLSX])
    assert result.exit_code == 0

    stdout_lines = result.stdout.strip().splitlines()
    assert len(stdout_lines) == 2

    # Multi-file stderr: compact table lines + stats block.
    assert "encrypted" in result.stderr
    assert "protected" in result.stderr
    assert "files scanned" in result.stderr


def test_info_directory(tmp_path: Path):
    """info on a directory recursively finds office files inside it."""
    # Copy two corpus files into a temp directory.
    src_a = _PROTECTED_XLSX
    src_b = _SIGNED_XLSX
    shutil.copy(src_a, tmp_path / "sheet.xlsx")
    shutil.copy(src_b, tmp_path / "signed.xlsx")

    result = runner.invoke(app, ["info", "--no-hash", str(tmp_path)])
    assert result.exit_code == 0

    # Both files should appear in stderr (sorted by name).
    assert "sheet.xlsx" in result.stderr
    assert "signed.xlsx" in result.stderr


def test_info_json():
    """info --json: stderr is valid JSON with files/gates structure."""
    result = runner.invoke(app, ["info", "--json", _ENCRYPTED_DOCX])
    assert result.exit_code == 0

    # stdout still carries the hash line.
    assert "$office-open$" in result.stdout

    # stderr should be parseable JSON.
    payload = json.loads(result.stderr)
    assert "files" in payload
    assert len(payload["files"]) == 1

    entry = payload["files"][0]
    assert "path" in entry
    assert "container" in entry
    assert "gates" in entry
    assert isinstance(entry["gates"], list)
    assert len(entry["gates"]) >= 1
    assert entry["gates"][0]["status"] == "encrypted"


def test_info_quiet():
    """info -q: stderr is empty (hash lines only on stdout)."""
    result = runner.invoke(app, ["info", "-q", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    assert "$office-open$" in result.stdout
    assert result.stderr == ""


def test_info_no_hash():
    """info --no-hash: stdout is empty (human-readable detail on stderr)."""
    result = runner.invoke(app, ["info", "--no-hash", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    assert result.stdout == ""
    assert "encrypted" in result.stderr


def test_info_format_hashcat():
    """info --format hashcat: hash uses $office$*2013* format, not unified $office$*sha512*."""
    result = runner.invoke(app, ["info", "--format", "hashcat", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    hash_line = result.stdout.strip()
    # Hashcat format starts with $office$*2013* (year-based).
    assert "$office$*2013*" in hash_line
    # It should NOT contain the unified scheme identifiers.
    assert "$office$*sha512*" not in hash_line


def test_info_nonexistent_file():
    """info on a missing file: non-zero exit code."""
    result = runner.invoke(app, ["info", "/tmp/definitely_nonexistent_opt_test_file.docx"])
    assert result.exit_code != 0


# ==========================================================================
# advanced subcommands
# ==========================================================================


def test_advanced_help():
    """advanced --help shows all 8 subcommands."""
    result = runner.invoke(app, ["advanced", "--help"])
    assert result.exit_code == 0
    expected_subcommands = ["extract", "decode", "collide", "bypass", "strip", "decrypt", "verify", "detail"]
    for sub in expected_subcommands:
        assert sub in result.stdout or sub in result.stderr, f"subcommand {sub!r} not found in advanced --help output"


def test_advanced_detail():
    """advanced detail on an encrypted file: stdout has tab-delimited summary, stderr has gate breakdown."""
    result = runner.invoke(app, ["advanced", "detail", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    # stdout: tab-delimited summary line (path, container, extension, state).
    parts = result.stdout.strip().split("\t")
    assert len(parts) == 4
    assert parts[1] == "ole-cfb"
    assert parts[3] == "encrypted"


def test_advanced_extract():
    """advanced extract on an encrypted file: stdout carries hash line."""
    result = runner.invoke(app, ["advanced", "extract", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    assert "$office$*2013*" in result.stdout


def test_advanced_strip(tmp_path: Path):
    """advanced strip writes output file with --force."""
    src = tmp_path / "input.xlsx"
    shutil.copy(_PROTECTED_XLSX, src)
    result = runner.invoke(app, ["advanced", "strip", str(src), "--force"])
    assert result.exit_code == 0
    # stdout carries the produced output path.
    produced = result.stdout.strip()
    assert "unlocked" in produced


def test_advanced_verify():
    """advanced verify on a valid unencrypted office file reports 'valid Office document'."""
    result = runner.invoke(app, ["advanced", "verify", _PROTECTED_XLSX])
    assert result.exit_code == 0
    assert "valid Office document" in result.stdout


# ==========================================================================
# debug mode
# ==========================================================================


def test_debug_mode():
    """--debug info: stderr contains 'debug mode enabled' and container/gate details."""
    result = runner.invoke(app, ["--debug", "info", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    assert "debug mode enabled" in result.stderr
    assert "container=" in result.stderr
    assert "gates found:" in result.stderr


# ==========================================================================
# status:scheme format
# ==========================================================================


def test_status_scheme_encrypted():
    """Encrypted file shows 'encrypted' in stderr detail."""
    result = runner.invoke(app, ["info", _ENCRYPTED_DOCX])
    assert result.exit_code == 0
    assert "(encrypted)" in result.stderr


def test_status_scheme_open(tmp_path: Path):
    """Unprotected file shows 'No protection.' in stderr detail."""
    f = tmp_path / "bare.doc"
    f.write_bytes(MAGIC_OLE_CFB + b"\x00" * 32)
    result = runner.invoke(app, ["info", "--no-hash", str(f)])
    assert result.exit_code == 0
    assert "No protection." in result.stderr
