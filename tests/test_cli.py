"""CLI smoke tests via typer's runner."""

from __future__ import annotations

from typing import TYPE_CHECKING

from typer.testing import CliRunner

from office_password_toolkit.cli.app import app
from office_password_toolkit.constants import MAGIC_OLE_CFB

if TYPE_CHECKING:
    from pathlib import Path

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "office-password-toolkit" in result.stdout


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    # Top-level commands: info, unlock, advanced.
    for command in ("info", "unlock", "advanced"):
        assert command in result.stdout


def test_info_command(tmp_path: Path):
    f = tmp_path / "legacy.doc"
    f.write_bytes(MAGIC_OLE_CFB + b"\x00" * 32)
    # The new info command exits 1 when no crackable hash is emitted (EXIT_ERROR).
    result = runner.invoke(app, ["info", str(f)])
    assert result.exit_code == 1


def test_info_no_hash_flag(tmp_path: Path):
    f = tmp_path / "legacy.doc"
    f.write_bytes(MAGIC_OLE_CFB + b"\x00" * 32)
    # With --no-hash, info suppresses hash stdout and exits 0.
    result = runner.invoke(app, ["info", "--no-hash", str(f)])
    assert result.exit_code == 0
