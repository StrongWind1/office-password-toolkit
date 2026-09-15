# SPDX-License-Identifier: Apache-2.0
"""office-password-toolkit CLI -- typer entry point.

3-command architecture:

    info     -- show protection gates + emit crackable hashes (multi-file, multi-dir)
    unlock   -- try everything cheapest-first to recover file(s) (multi-file)
    advanced -- expert single-file tools:
                  extract   emit raw hash lines
                  decode    reverse keyless obfuscation
                  collide   mint a tiny-verifier password
                  bypass    strip non-encrypting gates (signatures preserved)
                  strip     strip ALL non-encrypting gates (signatures included)
                  decrypt   decrypt with a known/guessed password
                  verify    check a file's integrity after recovery
                  detail    verbose per-gate breakdown (the old ``info`` output)

stdout carries only machine-parseable output (hash lines, produced paths) for
piping; all human-facing status, diagnostics, and errors go to stderr via rich.
Exit codes are defined in :mod:`office_password_toolkit.constants`.
"""

from __future__ import annotations

import json
import logging
import os
import re
import shutil
import sys
import tempfile
import time
import zipfile
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Annotated, Final

import olefile
import typer
from rich.console import Console

from office_password_toolkit import __version__
from office_password_toolkit.bypass import bypass_file
from office_password_toolkit.constants import (
    EXIT_CRACK_REQUIRED,
    EXIT_ERROR,
    EXIT_NO_HASH,
    EXIT_NOT_ENCRYPTED,
    EXIT_OK,
    EXIT_REFUSED,
    EXIT_UNRECOVERABLE,
    EXIT_UNSUPPORTED,
)
from office_password_toolkit.crypto import pst as pst_crypto
from office_password_toolkit.crypto.uls import parse_mdw
from office_password_toolkit.decrypt import decrypt_file
from office_password_toolkit.defaults import default_passwords
from office_password_toolkit.detect import classify_container
from office_password_toolkit.detect import detect as detect_file
from office_password_toolkit.extract import extract_hashes
from office_password_toolkit.formats import handler_for
from office_password_toolkit.formats.access import AccessEngine, decode_jet_password, read_header
from office_password_toolkit.models import (
    ContainerKind,
    GateType,
    HashScheme,
    Product,
    RecoveryClass,
    Status,
    gate_scheme_tag,
    gate_status,
)

if TYPE_CHECKING:
    from office_password_toolkit.formats.base import FormatHandler
    from office_password_toolkit.models import DetectResult, ExtractedHash, Gate

# --- Module logger -----------------------------------------------------------
# The ``opt`` logger is the single channel for debug-mode diagnostics.  The
# ``--debug`` / ``-d`` global flag flips it to DEBUG; without it, no messages
# propagate (NullHandler default).
logger = logging.getLogger("opt")

# --- Rich consoles -----------------------------------------------------------
# Everything human-facing lands on stderr so that stdout stays clean for piping.
# When stderr is not a TTY (piped to a file or another process), disable ALL
# ANSI formatting — colors, bold, dim, etc. — so output is clean ASCII for
# machine consumption. When it IS a TTY, let Rich render full formatting.
# The NO_COLOR env var is also respected per https://no-color.org/ spec.
_is_tty = sys.stderr.isatty()
_err = Console(stderr=True, no_color=not _is_tty, highlight=_is_tty, markup=_is_tty)

# --- Typer applications ------------------------------------------------------
app = typer.Typer(
    name="opt",
    help="Detect, extract, bypass, and decrypt passwords/protection in Office and OpenDocument files.",
    add_completion=False,
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)

# The ``advanced`` group houses expert single-file tools that the ``info`` and
# ``unlock`` commands orchestrate internally.  Power users invoke them directly.
advanced_app = typer.Typer(
    name="advanced",
    help="Expert tools: extract, decode, collide, bypass, strip, decrypt, verify, detail.",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)
app.add_typer(advanced_app, name="advanced")

# --- Reusable type aliases for typer arguments/options -----------------------
# Multi-file argument: accepts files AND directories (recursively scanned).
_InputFiles = Annotated[
    list[Path],
    typer.Argument(exists=True, help="Office / OpenDocument files or directories (recursive)"),
]
# Single-file argument: the ``advanced`` subcommands operate on one file at a time.
_InputFile = Annotated[
    Path,
    typer.Argument(exists=True, dir_okay=False, readable=True, help="Office / OpenDocument file"),
]
_Wordlist = Annotated[
    Path | None,
    typer.Option("--wordlist", "--password-file", exists=True, dir_okay=False, readable=True, help="File of candidate passwords, one per line"),
]
_Password = Annotated[str | None, typer.Option("-p", "--password", help="Document-open password to try")]
_Force = Annotated[bool, typer.Option("--force", help="Overwrite the output if it already exists")]

# --- Constants ---------------------------------------------------------------
# Recognized Office/ODF extensions for directory recursion.  Files passed
# individually are not extension-checked -- the user knows what they passed.
_OFFICE_EXTENSIONS: frozenset[str] = frozenset(
    {
        # Word
        ".doc",
        ".docx",
        ".docm",
        ".dotx",
        ".dotm",
        ".dot",
        ".wbk",
        # Excel
        ".xls",
        ".xlsx",
        ".xlsm",
        ".xlsb",
        ".xltx",
        ".xltm",
        ".xlam",
        ".xlt",
        ".xlm",
        ".xla",
        ".xll",
        ".xlw",
        # PowerPoint
        ".ppt",
        ".pptx",
        ".pptm",
        ".potx",
        ".potm",
        ".ppsx",
        ".ppsm",
        ".pot",
        ".pps",
        ".ppa",
        ".ppam",
        ".sldx",
        ".sldm",
        # OpenDocument
        ".odt",
        ".ods",
        ".odp",
        ".odg",
        ".odf",
        # OneNote
        ".one",
        ".onetoc2",
        ".onepkg",
        # Outlook
        ".pst",
        ".ost",
        ".nst",
        ".msg",
        ".oft",
        # Access
        ".mdb",
        ".accdb",
        ".mde",
        ".accde",
        ".mdw",
        ".mda",
        ".accdr",
        # Money (MSISAM Jet databases)
        ".mny",
        # Visio
        ".vsdx",
        ".vsdm",
        ".vsd",
        ".vss",
        ".vst",
        ".vsw",
        ".vstx",
        ".vstm",
        ".vssx",
        ".vssm",
        # Publisher / InfoPath / Project
        ".pub",
        ".xsn",
        ".mpp",
        ".mpt",
    }
)

# Sort key for the ``status:scheme`` tags -- encrypted first (most urgent),
# then removable, trivial, info, blocked, and finally the bare ``open`` status.
_STATUS_ORDER: dict[Status, int] = {
    Status.ENCRYPTED: 0,
    Status.REMOVABLE: 1,
    Status.TRIVIAL: 2,
    Status.INFO: 3,
    Status.BLOCKED: 4,
    Status.OPEN: 5,
}

# Gate types whose occurrence count is shown in the tag, e.g. ``sheets(3)``.
# All other gate types appear at most once per file regardless of how many
# underlying records exist.
_COUNTABLE_GATES: frozenset[GateType] = frozenset(
    {
        GateType.PROTECT_SHEET,
        GateType.ALLOW_EDIT_RANGES,
    }
)


# --- Human-readable output (info/unlock commands) ----------------------------

_PRODUCT_DESCRIPTIONS: Final[dict[Product, str]] = {
    Product.WORD: "Word document",
    Product.EXCEL: "Excel workbook",
    Product.POWERPOINT: "PowerPoint presentation",
    Product.ONENOTE: "OneNote notebook",
    Product.OUTLOOK: "Outlook data file",
    Product.ACCESS: "Access database",
    Product.VISIO: "Visio drawing",
    Product.PROJECT: "Project file",
    Product.PUBLISHER: "Publisher document",
    Product.INFOPATH: "InfoPath form",
    Product.OPENDOCUMENT: "OpenDocument file",
    Product.UNKNOWN: "Office file",
}

_SCHEME_HUMAN_NAMES: Final[dict[HashScheme, str]] = {
    HashScheme.OFFICE_2007: "AES-128/SHA-1",
    HashScheme.OFFICE_2010: "AES-128/SHA-1",
    HashScheme.OFFICE_2013: "AES-256/SHA-512",
    HashScheme.OLDOFFICE_RC4_MD5: "RC4/MD5",
    HashScheme.OLDOFFICE_RC4_SHA1: "RC4/SHA-1",
    HashScheme.OFFICE_SHEETPROT: "SHA-512",
    HashScheme.ODF: "ODF",
    HashScheme.VBA_SHA1: "SHA-1",
    HashScheme.MSISAM: "MSISAM",
}

_STRIPPABLE_RECOVERIES: Final[frozenset[RecoveryClass]] = frozenset(
    {
        RecoveryClass.DEFAULT,
        RecoveryClass.READ,
        RecoveryClass.DECODE,
        RecoveryClass.BYPASS,
        RecoveryClass.STRIP,
        RecoveryClass.COLLIDE,
    }
)

_GATE_HUMAN_DESCRIPTIONS: Final[dict[GateType, tuple[str, str]]] = {
    GateType.PROTECT_SHEET: ("sheet protected", "sheets protected"),
    GateType.ALLOW_EDIT_RANGES: ("range password", "range passwords"),
    GateType.PROTECT_WORKBOOK: ("Workbook structure locked", "Workbook structure locked"),
    GateType.RESTRICT_EDIT: ("Editing restriction", "Editing restrictions"),
    GateType.SHARED_REVISIONS: ("Shared-revisions lock", "Shared-revisions lock"),
    GateType.SECTION: ("Section protection", "Section protection"),
    GateType.VBA_PROJECT: ("VBA project lock", "VBA project lock"),
    GateType.MODIFY: ("Modify password", "Modify password"),
    GateType.SIGNATURE: ("Digital signature", "Digital signatures"),
    GateType.IRM: ("Rights management (IRM)", "Rights management (IRM)"),
    GateType.MAIL_BODY: ("Mail body cipher", "Mail body cipher"),
}


@dataclass(frozen=True)
class _FileResult:
    """Structured result from processing one file."""

    path: Path
    product: Product
    container: ContainerKind
    encrypted: bool
    gates: list[Gate]
    hash_line: str | None
    error: str | None = None


@dataclass
class _InfoStats:
    """Accumulator for info command batch statistics."""

    total: int = 0
    elapsed: float = 0.0
    by_product: dict[str, int] = field(default_factory=dict)
    encrypted: int = 0
    protected: int = 0
    no_protection: int = 0
    not_recoverable: int = 0
    hashes_extracted: int = 0
    hashcat_modes: dict[int, int] = field(default_factory=dict)
    errors: int = 0

    def record(self, result: _FileResult) -> None:
        """Record one file's result into the accumulator."""
        self.total += 1
        prod = _PRODUCT_DESCRIPTIONS.get(result.product, result.product.value)
        self.by_product[prod] = self.by_product.get(prod, 0) + 1
        if result.error:
            self.errors += 1
            return
        status = _file_status_word(result.gates)
        if status == "encrypted":
            self.encrypted += 1
        elif status == "protected":
            self.protected += 1
        elif status == "not recoverable":
            self.not_recoverable += 1
        else:
            self.no_protection += 1
        if result.hash_line:
            self.hashes_extracted += 1
            for gate in result.gates:
                if gate.hashcat_mode is not None:
                    self.hashcat_modes[gate.hashcat_mode] = self.hashcat_modes.get(gate.hashcat_mode, 0) + 1

    def format(self) -> str:
        """Format the stats block as an aligned table for stderr."""
        parts: list[str] = []
        time_str = f"{self.elapsed:.1f}s" if self.elapsed < 60 else f"{int(self.elapsed // 60)}m {int(self.elapsed % 60)}s"  # noqa: PLR2004
        parts.append(f"{self.total} files scanned in {time_str}")
        products = sorted(self.by_product.items(), key=lambda kv: -kv[1])
        if products:
            pad = max(len(name) for name, _ in products)
            for name, count in products:
                parts.append(f"  {name:<{pad}}  {count:>5}")
        parts.append("")
        rows: list[tuple[str, int]] = []
        if self.encrypted:
            rows.append(("encrypted — password required", self.encrypted))
        if self.protected:
            rows.append(("protected — removable with opt unlock", self.protected))
        if self.not_recoverable:
            rows.append(("not recoverable", self.not_recoverable))
        if self.no_protection:
            rows.append(("no protection", self.no_protection))
        if rows:
            pad = max(len(label) for label, _ in rows)
            for label, count in rows:
                parts.append(f"  {label:<{pad}}  {count:>5}")
        if self.hashes_extracted:
            parts.append("")
            parts.append(f"  {self.hashes_extracted} hash{'es' if self.hashes_extracted != 1 else ''} extracted")
            for mode, count in sorted(self.hashcat_modes.items()):
                parts.append(f"    hashcat -m {mode:<5}  {count:>5}")
        if self.errors:
            parts.append(f"  {self.errors} error{'s' if self.errors != 1 else ''}")
        return "\n".join(parts)


@dataclass
class _UnlockStats:
    """Accumulator for unlock command batch statistics."""

    total: int = 0
    elapsed: float = 0.0
    by_product: dict[str, int] = field(default_factory=dict)
    decrypted: int = 0
    decrypted_default: int = 0
    protection_stripped: int = 0
    skipped_no_protection: int = 0
    skipped_not_recoverable: int = 0
    still_encrypted: int = 0
    files_written: int = 0
    hashcat_modes: dict[int, int] = field(default_factory=dict)
    errors: int = 0

    def record_product(self, product: Product) -> None:
        """Record the product type for one file."""
        self.total += 1
        prod = _PRODUCT_DESCRIPTIONS.get(product, product.value)
        self.by_product[prod] = self.by_product.get(prod, 0) + 1

    def format(self) -> str:
        """Format the stats block for stderr."""
        parts: list[str] = []
        time_str = f"{self.elapsed:.1f}s" if self.elapsed < 60 else f"{int(self.elapsed // 60)}m {int(self.elapsed % 60)}s"  # noqa: PLR2004
        parts.append(f"{self.total} files processed in {time_str}")
        products = sorted(self.by_product.items(), key=lambda kv: -kv[1])
        if products:
            pad = max(len(name) for name, _ in products)
            for name, count in products:
                parts.append(f"  {name:<{pad}}  {count:>5}")
        parts.append("")
        rows: list[tuple[str, int]] = []
        if self.decrypted:
            label = "decrypted"
            if self.decrypted_default:
                non_default = self.decrypted - self.decrypted_default
                detail_parts: list[str] = []
                if self.decrypted_default:
                    detail_parts.append(f"{self.decrypted_default} default password")
                if non_default:
                    detail_parts.append(f"{non_default} provided")
                label = f"decrypted ({', '.join(detail_parts)})"
            rows.append((label, self.decrypted))
        if self.protection_stripped:
            rows.append(("protection stripped", self.protection_stripped))
        if self.skipped_no_protection:
            rows.append(("no protection — skipped", self.skipped_no_protection))
        if self.skipped_not_recoverable:
            rows.append(("not recoverable — skipped", self.skipped_not_recoverable))
        if self.still_encrypted:
            rows.append(("still encrypted — hash emitted", self.still_encrypted))
        if self.files_written:
            rows.append(("files written", self.files_written))
        if rows:
            pad = max(len(label) for label, _ in rows)
            for label, count in rows:
                parts.append(f"  {label:<{pad}}  {count:>5}")
        if self.errors:
            parts.append(f"  {self.errors} error{'s' if self.errors != 1 else ''}")
        return "\n".join(parts)


# --- Gate description functions -----------------------------------------------


def _product_description(product: Product, *, encrypted: bool = False) -> str:
    """Return 'Excel workbook', 'Word document', etc."""
    if product is Product.UNKNOWN and encrypted:
        return "encrypted Office document"
    return _PRODUCT_DESCRIPTIONS.get(product, "Office file")


def _file_header(path: Path, product: Product, *, encrypted: bool = False) -> str:
    """Format the file header line: 'budget.xlsx — Excel workbook'."""
    desc = _product_description(product, encrypted=encrypted)
    suffix = " (encrypted)" if encrypted and product is not Product.UNKNOWN else ""
    return f"{path.name} — {desc}{suffix}"


def _file_status_word(gates: list[Gate]) -> str:
    """Classify a file's gates into a user-facing status word."""
    if not gates:
        return "no protection"
    has_encrypted = any(g.recovery in (RecoveryClass.CRACK, RecoveryClass.KEYSPACE, RecoveryClass.DECRYPT) and g.gate not in (GateType.SIGNATURE, GateType.IRM) for g in gates)
    if has_encrypted:
        return "encrypted"
    has_blocked = any((g.gate is GateType.IRM or g.recovery is RecoveryClass.NONE) and g.gate is not GateType.SIGNATURE for g in gates)
    has_strippable = any(g.recovery in _STRIPPABLE_RECOVERIES for g in gates)
    if has_strippable:
        return "protected"
    if has_blocked:
        return "not recoverable"
    return "protected"


def _describe_open_gate(gate: Gate) -> str:
    """Describe a document-open encryption gate in human terms."""
    scheme_name = _SCHEME_HUMAN_NAMES.get(gate.scheme, "") if gate.scheme else ""
    qualifier = f" ({scheme_name})" if scheme_name else ""
    return f"Document-open password{qualifier}"


def _describe_protection_gates(gates: list[Gate]) -> list[str]:
    """Group non-OPEN gates by type and produce human-readable description lines."""
    by_type: dict[GateType, list[Gate]] = {}
    for g in gates:
        if g.gate is GateType.OPEN:
            continue
        by_type.setdefault(g.gate, []).append(g)

    lines: list[str] = []
    for gate_type, group in by_type.items():
        count = len(group)
        singular, plural = _GATE_HUMAN_DESCRIPTIONS.get(gate_type, (gate_type.value, gate_type.value))

        if gate_type in (GateType.PROTECT_SHEET, GateType.ALLOW_EDIT_RANGES):
            with_hash = [g for g in group if g.scheme is not None]
            without_hash = count - len(with_hash)
            desc = f"1 {singular}" if count == 1 else f"{count} {plural}"
            if with_hash and without_hash and count > 1:
                scheme_name = _SCHEME_HUMAN_NAMES.get(with_hash[0].scheme, "hash") if with_hash[0].scheme else "hash"
                desc += f" ({len(with_hash)} with {scheme_name} hashes, {without_hash} without password)"
            elif with_hash and count > 1:
                scheme_name = _SCHEME_HUMAN_NAMES.get(with_hash[0].scheme, "hash") if with_hash[0].scheme else "hash"
                desc += f" ({scheme_name} hashes)"
            elif without_hash and count > 1:
                desc += " (no password)"
            elif with_hash:
                scheme_name = _SCHEME_HUMAN_NAMES.get(with_hash[0].scheme, "hash") if with_hash[0].scheme else "hash"
                desc += f" ({scheme_name} hash)"
            else:
                desc += " (no password)"
        else:
            desc = singular
            if group[0].scheme is not None:
                scheme_name = _SCHEME_HUMAN_NAMES.get(group[0].scheme, "")
                if scheme_name:
                    desc += f" ({scheme_name})"

        all_strippable = all(g.recovery in _STRIPPABLE_RECOVERIES for g in group)
        all_blocked = all(g.recovery is RecoveryClass.NONE for g in group)
        if all_blocked:
            desc += " — not recoverable"
        elif all_strippable:
            desc += " — strippable"

        lines.append(desc)
    return lines


def _action_hint(gates: list[Gate], path: Path) -> str:
    """Produce the action hint for single-file info output."""
    open_gates = [g for g in gates if g.gate is GateType.OPEN]
    if open_gates:
        gate = open_gates[0]
        mode_str = f"hashcat -m {gate.hashcat_mode}" if gate.hashcat_mode else "hashcat"
        return f"Crack with {mode_str}, or: opt unlock -p <password>"
    return f"Run: opt unlock {path.name}"


def _gate_summary_compact(gates: list[Gate]) -> str:
    """Produce a one-line summary of gates for multi-file table output."""
    open_gates = [g for g in gates if g.gate is GateType.OPEN]
    if open_gates:
        gate = open_gates[0]
        scheme_name = _SCHEME_HUMAN_NAMES.get(gate.scheme, "") if gate.scheme else ""
        return f"document-open password ({scheme_name})" if scheme_name else "document-open password"

    by_type: dict[GateType, list[Gate]] = {}
    for g in gates:
        by_type.setdefault(g.gate, []).append(g)

    parts: list[str] = []
    all_strippable = all(g.recovery in _STRIPPABLE_RECOVERIES for g in gates)
    for gate_type, group in by_type.items():
        singular, plural = _GATE_HUMAN_DESCRIPTIONS.get(gate_type, (gate_type.value, gate_type.value))
        count = len(group)
        if gate_type in (GateType.PROTECT_SHEET, GateType.ALLOW_EDIT_RANGES):
            parts.append(f"{count} {plural}" if count > 1 else f"1 {singular}")
        else:
            parts.append(singular.lower())
    summary = ", ".join(parts)
    if all_strippable:
        summary += " (strippable)"
    return summary


# ==========================================================================
# Input resolution
# ==========================================================================
def _resolve_inputs(paths: list[Path]) -> list[Path]:
    """Resolve a mix of files, directories, and globs into individual Office files.

    For directories: two-pass filter. First, files with a recognized Office
    extension are included (fast, no I/O). Second, files WITHOUT an Office
    extension are checked by magic bytes so renamed Office files (e.g. a
    ``.pdf`` that is actually an OLE compound file) are still found. Files
    whose extension says Office but whose magic bytes say otherwise (e.g. a
    ``.doc`` that is really a PDF) are caught later during detection.

    For explicitly named files: included as-is (the user chose them — detection
    and any "not an Office file" message happen downstream).

    The returned list is sorted by filename for deterministic batch output.
    """
    resolved: list[Path] = []
    for p in paths:
        if p.is_dir():
            for child in sorted(p.rglob("*")):
                if not child.is_file():
                    continue
                if child.suffix.lower() in _OFFICE_EXTENSIONS:
                    resolved.append(child)
                elif classify_container(child) is not ContainerKind.UNKNOWN:
                    logger.debug("directory scan: non-Office extension but valid magic: %s", child)
                    resolved.append(child)
        elif p.is_file():
            resolved.append(p)
        else:
            _err.print(f"[yellow]Skipping {p}: not a file or directory[/]")
            logger.debug("skipping non-file non-directory: %s", p)
    resolved.sort(key=lambda x: x.name)
    return resolved


# ==========================================================================
# Output formatting -- ``status:scheme`` one-liners
# ==========================================================================
def _format_status_tag(status: Status, scheme: str, count: int | None = None) -> str:
    """Format a single ``status:scheme`` tag with an optional count.

    Examples: ``encrypted:agile-sha512``, ``removable:sheets(3)``, ``open``.
    The bare ``open`` status has no colon or scheme -- it stands alone.
    """
    if status is Status.OPEN:
        return "open"
    suffix = f"({count})" if count is not None and count > 1 else ""
    return f"{status.value}:{scheme}{suffix}"


def _build_tags(gates: list[Gate]) -> list[str]:
    """Build the ordered list of ``status:scheme`` tags from a file's gate list.

    Countable gates (sheets, ranges) are grouped and counted; all other gate
    types appear at most once.  Tags are sorted by severity: ``encrypted`` first,
    then ``removable``, ``trivial``, ``info``, ``blocked``.
    """
    if not gates:
        return ["open"]

    # Accumulate unique (status, scheme) pairs, counting only countable gates.
    tag_counts: dict[tuple[Status, str], int] = {}
    tag_order: dict[tuple[Status, str], int] = {}

    for gate in gates:
        status = gate_status(gate)
        scheme = gate_scheme_tag(gate)
        key = (status, scheme)

        # Record the first-seen position for stable ordering within a status.
        if key not in tag_order:
            tag_order[key] = len(tag_order)

        if gate.gate in _COUNTABLE_GATES:
            # Countable gates: increment the counter for each occurrence.
            tag_counts[key] = tag_counts.get(key, 0) + 1
        else:
            # Non-countable gates: mark present (1) but never increment beyond that.
            tag_counts.setdefault(key, 1)

    # Sort by status severity, then by first-seen order within the same status.
    sorted_keys = sorted(
        tag_counts,
        key=lambda k: (_STATUS_ORDER.get(k[0], 99), tag_order.get(k, 99)),
    )

    tags: list[str] = []
    for key in sorted_keys:
        status, scheme = key
        count = tag_counts[key]
        # Only show the parenthesized count when it is greater than 1.
        show_count = count if count > 1 else None
        tags.append(_format_status_tag(status, scheme, show_count))
    return tags


def _build_json_gates(gates: list[Gate]) -> list[dict[str, str | int]]:
    """Build the JSON-serializable gate list for a single file.

    Same grouping/counting logic as ``_build_tags``, but returns a list of dicts
    with ``status``, ``scheme``, and optionally ``count`` keys.
    """
    if not gates:
        return []

    # Same accumulation as _build_tags but keyed by (status, scheme, gate_type)
    # so the JSON can carry the gate type if needed in the future.
    seen: dict[tuple[Status, str], int] = {}
    order_keys: dict[tuple[Status, str], int] = {}

    for gate in gates:
        status = gate_status(gate)
        scheme = gate_scheme_tag(gate)
        key = (status, scheme)

        if key not in order_keys:
            order_keys[key] = len(order_keys)

        if gate.gate in _COUNTABLE_GATES:
            seen[key] = seen.get(key, 0) + 1
        else:
            seen.setdefault(key, 1)

    sorted_keys = sorted(
        seen,
        key=lambda k: (_STATUS_ORDER.get(k[0], 99), order_keys.get(k, 99)),
    )

    result: list[dict[str, str | int]] = []
    for key in sorted_keys:
        status, scheme = key
        count = seen[key]
        entry: dict[str, str | int] = {"status": status.value, "scheme": scheme}
        if count > 1:
            entry["count"] = count
        result.append(entry)
    return result


# ==========================================================================
# Shared helpers
# ==========================================================================
def _derive_output(path: Path, tag: str) -> Path:
    """Return ``<stem>.<tag><ext>`` next to ``path`` (e.g. ``secret.unlocked.docx``)."""
    return path.with_name(f"{path.stem}.{tag}{path.suffix}")


def _guard_output(inp: Path, out: Path, *, force: bool) -> None:
    """Enforce the one safety rule: the input is never modified.

    Also refuse to silently overwrite an existing output unless ``--force``.
    """
    same_file = out.exists() and inp.exists() and out.samefile(inp)
    if inp.resolve() == out.resolve() or same_file:
        _err.print("[red]Refusing:[/] output path is the input; the input is never modified.")
        raise typer.Exit(code=EXIT_REFUSED)
    if out.exists() and not force:
        _err.print(f"[red]Refusing:[/] {out} already exists (pass --force to overwrite).")
        raise typer.Exit(code=EXIT_REFUSED)


def _candidate_passwords(password: str | None, wordlist: Path | None) -> list[str]:
    """Build the ordered auto-try list: built-in defaults, then ``-p``, then wordlist lines.

    The built-in defaults (empty string, ``VelvetSweatshop``,
    ``/01Hannes Ruescher/01``) are always tried first and silently -- they
    defeat a large fraction of "encrypted" files with no cracking.
    """
    candidates: list[str] = list(default_passwords())
    n_defaults = len(candidates)
    if password is not None:
        candidates.append(password)
    if wordlist is not None:
        candidates.extend(wordlist.read_text(encoding="utf-8", errors="replace").splitlines())
    logger.debug("candidates: %d total (%d defaults, user=%s, wordlist=%s)", len(candidates), n_defaults, "yes" if password is not None else "no", str(wordlist) if wordlist is not None else "none")
    return candidates


def _decrypt_with_candidates(path: Path, out: Path, candidates: list[str]) -> bool:
    """Try each candidate password in order; return ``True`` on the first that decrypts.

    Stops at the first success (short-circuit).  On ``ValueError`` the candidate
    is wrong and the next one is tried; all other exceptions propagate.
    """
    total = len(candidates)
    for i, candidate in enumerate(candidates):
        logger.debug("trying candidate %d/%d", i + 1, total)
        try:
            decrypt_file(path, out, candidate)
        except ValueError:
            continue
        else:
            logger.debug("candidate %d/%d: decrypt succeeded", i + 1, total)
            return True
    logger.debug("all %d candidates failed", total)
    return False


def _get_gates(path: Path) -> list[Gate]:
    """Enumerate all gates for ``path``, returning an empty list on any failure.

    This is the safe wrapper around ``handler.gates()`` that never raises --
    used by the ``info`` and ``unlock`` commands where a gate-enumeration failure
    should degrade gracefully, not crash the batch.
    """
    try:
        result = detect_file(path)
        handler = handler_for(result.container)
        if handler is None:
            logger.debug("no handler for container %s", result.container.value)
            return []
        return handler.gates(path)
    except Exception as exc:
        logger.debug("gate enumeration failed for %s: %s", path, exc)
        return []


def _extract_hashes_safe(path: Path) -> list[ExtractedHash]:
    """Extract hashes for ``path``, returning an empty list on any failure.

    The safe wrapper around ``extract_hashes()`` for batch contexts where a
    single file's extraction failure must not abort the run.
    """
    try:
        return extract_hashes(path)
    except Exception as exc:
        logger.debug("hash extraction failed for %s: %s", path, exc)
        return []


def _emit_hashes(path: Path) -> None:
    """Print every crackable hash line for ``path`` to stdout.

    Filters out fast-verifier schemes (XOR/PST) since those are handled by
    ``decode`` / ``collide``, not by GPU cracking.
    """
    hashes = _extract_hashes_safe(path)
    if not hashes:
        _err.print("[yellow]No crackable hash found.[/]")
        return
    for extracted in hashes:
        typer.echo(extracted.value)


def _is_unrecoverable(path: Path) -> bool:
    """Return ``True`` if the file's protection has no password secret to recover.

    Currently this checks for IRM/RMS, where the content key is held off-file
    by an enterprise certificate or Rights Management server.
    """
    gates = _get_gates(path)
    return any(gate.gate is GateType.IRM and gate.recovery is RecoveryClass.NONE for gate in gates)


# ==========================================================================
# Root callback -- global options (--version, --debug)
# ==========================================================================
def _version_callback(*, value: bool) -> None:
    """Print the version and exit when ``--version`` is given."""
    if value:
        typer.echo(f"office-password-toolkit {__version__}")
        raise typer.Exit


@app.callback()
def _root(
    *,
    _version: Annotated[
        bool,
        typer.Option("--version", callback=_version_callback, is_eager=True, help="Show version and exit."),
    ] = False,
    debug: Annotated[
        bool,
        typer.Option("--debug", "-d", help="Enable debug output on stderr (container, handler, streams, encryption details)."),
    ] = False,
) -> None:
    """office-password-toolkit -- detect, extract, bypass, and decrypt Office file passwords."""
    if debug:
        # Wire the ``opt`` logger to stderr so debug messages appear alongside
        # the rich status output, never contaminating stdout hash lines.
        logging.basicConfig(
            level=logging.DEBUG,
            format="  [%(module)s] %(message)s",
            force=True,
        )
        logger.setLevel(logging.DEBUG)
        logger.debug("debug mode enabled")


# ==========================================================================
# info command -- helpers
# ==========================================================================
def _log_detect_result(result: DetectResult) -> None:
    """Log the detection result at DEBUG level."""
    logger.debug(
        "container=%s  encrypted=%s  extension=%s  product=%s",
        result.container.value,
        result.encrypted,
        result.extension,
        result.product.value,
    )


def _log_gates(gates: list[Gate]) -> None:
    """Log each gate at DEBUG level."""
    logger.debug("gates found: %d", len(gates))
    for g in gates:
        logger.debug(
            "  gate=%s  recovery=%s  scheme=%s  hashcat=%s  where=%s",
            g.gate.value,
            g.recovery.value,
            g.scheme.value if g.scheme else "-",
            g.hashcat_mode,
            g.where or "-",
        )


def _pick_hash_line(path: Path, *, use_unified: bool) -> str | None:
    """Extract the primary crackable hash line for ``path``.

    Returns the formatted hash string or ``None`` when no crackable hash exists.
    Filters out fast-verifier schemes (XOR/PST) since those are decode/collide
    targets, not GPU crack targets.
    """
    hashes = _extract_hashes_safe(path)
    if not hashes:
        return None
    # Pick the first hash (document-open encryption, the primary crack target).
    h = hashes[0]
    if use_unified and h.opt_value is not None:
        return h.opt_value
    # Fallback to hashcat format (always available).
    return h.value


def _info_emit_json(
    file_result: _FileResult,
    *,
    use_unified: bool,
    json_records: list[dict[str, object]],
) -> None:
    """Append a JSON record for one file (flushed in bulk by the caller)."""
    record: dict[str, object] = {
        "path": str(file_result.path),
        "container": file_result.container.value,
        "product": file_result.product.value,
        "gates": _build_json_gates(file_result.gates),
    }
    if file_result.hash_line is not None:
        record["hash"] = file_result.hash_line
        record["hash_format"] = "unified" if use_unified else "hashcat"
    json_records.append(record)


def _info_print_single(file_result: _FileResult) -> None:
    """Print detailed single-file info output to stderr."""
    _err.print(f"[bold]{_file_header(file_result.path, file_result.product, encrypted=file_result.encrypted)}[/]")
    if file_result.error:
        _err.print(f"  [red]Error: {file_result.error}[/]")
        return
    if not file_result.gates:
        _err.print("  No protection.")
        return
    open_gates = [g for g in file_result.gates if g.gate is GateType.OPEN]
    for og in open_gates:
        _err.print(f"  {_describe_open_gate(og)}")
    for line in _describe_protection_gates(file_result.gates):
        _err.print(f"  {line}")
    _err.print(f"  {_action_hint(file_result.gates, file_result.path)}")


def _info_print_table_line(file_result: _FileResult, pad_to: int) -> None:
    """Print one compact table line for multi-file info output to stderr."""
    status_word = _file_status_word(file_result.gates)
    if file_result.error:
        summary = f"error: {file_result.error}"
    elif not file_result.gates:
        summary = ""
    else:
        open_gates = [g for g in file_result.gates if g.gate is GateType.OPEN]
        summary = _describe_open_gate(open_gates[0]) if open_gates else _gate_summary_compact(file_result.gates)
    padded = file_result.path.name.ljust(pad_to)
    status_padded = status_word.ljust(16)
    _err.print(f"{padded}  {status_padded}{summary}")


def _info_emit_results(
    results: list[_FileResult],
    *,
    stats: _InfoStats,
    single_file: bool,
    no_hash: bool,
    quiet: bool,
    json_output: bool,
    max_name_len: int,
) -> None:
    """Emit per-file output (stderr + stdout hash lines) and accumulate stats."""
    for file_result in results:
        if file_result.container is ContainerKind.UNKNOWN and not file_result.error:
            if single_file:
                _err.print(f"{file_result.path.name} — not a recognized Office file, skipping.")
            continue
        stats.record(file_result)
        if not quiet and not json_output:
            if single_file:
                _info_print_single(file_result)
            else:
                _info_print_table_line(file_result, max_name_len)
        # Hash line to stdout AFTER the stderr status so they group visually.
        if not no_hash:
            typer.echo(file_result.hash_line if file_result.hash_line is not None else "")


# ==========================================================================
# info command -- parallel worker
# ==========================================================================
def _info_one_file(args: tuple[Path, bool]) -> _FileResult:
    """Process one file in a worker process: detect, enumerate gates, extract hash.

    Returns a ``_FileResult`` with structured data so the main process can
    format and accumulate stats.  Defined at module level (not a closure) so
    ``ProcessPoolExecutor`` can pickle it with ``forkserver``.
    """
    path, use_unified = args
    try:
        result = detect_file(path)
        gates = _get_gates(path)
        hash_line = _pick_hash_line(path, use_unified=use_unified)
    except Exception as exc:
        return _FileResult(path=path, product=Product.UNKNOWN, container=ContainerKind.UNKNOWN, encrypted=False, gates=[], hash_line=None, error=str(exc))
    return _FileResult(path=path, product=result.product, container=result.container, encrypted=result.encrypted, gates=gates, hash_line=hash_line)


# ==========================================================================
# info command
# ==========================================================================
@app.command()
def info(
    paths: _InputFiles,
    *,
    format_: Annotated[
        str,
        typer.Option("--format", help="Output format: 'hashcat' (hashcat hash lines), 'unified' (self-describing hash lines), or 'json' (structured JSON to stderr)."),
    ] = "unified",
    no_hash: Annotated[bool, typer.Option("--no-hash", help="Suppress stdout hash output.")] = False,
    json_output: Annotated[bool, typer.Option("--json", help="Output structured JSON to stderr instead of one-liners.")] = False,
    quiet: Annotated[bool, typer.Option("-q", "--quiet", help="Suppress stderr output (hash lines only, same as 2>/dev/null).")] = False,
    jobs: Annotated[int, typer.Option("-j", "--jobs", help="Worker processes for parallel file processing (default: CPU count, 1 = sequential).")] = 0,
) -> None:
    """Show protection gates on Office files and emit crackable hashes.

    stdout: crackable hash lines (one per file, blank line if none) -- pipe to hashcat.
    stderr: human-readable protection summary per file.

    Accepts individual files, directories (recursively finds Office files), and
    shell glob patterns.

    Examples:
      opt info secret.xlsx                  Show protection details
      opt info *.docx | hashcat -m 37000   Batch extract + crack
      opt info *.xlsx 2>/dev/null           Hashes only (for scripting)
      opt info folder/                      Recurse into directory
      opt info --format json secret.xlsx    Full JSON output
    """
    files = _resolve_inputs(paths)
    if not files:
        _err.print("[red]No Office files found in the given paths.[/]")
        raise typer.Exit(code=EXIT_ERROR)

    if format_.lower() == "json":
        json_output = True

    use_unified = format_.lower() in ("unified", "json")
    start_time = time.monotonic()
    single_file = len(files) == 1
    max_name_len = min(max(len(f.name) for f in files), 60)

    json_records: list[dict[str, object]] = []
    stats = _InfoStats()
    results: list[_FileResult] = []

    workers = jobs if jobs > 0 else (os.cpu_count() or 4)
    debug_active = logger.isEnabledFor(logging.DEBUG)
    use_parallel = workers > 1 and not debug_active and not json_output and len(files) > 1

    if use_parallel:
        chunksize = max(1, len(files) // (workers * 4))
        work_args = [(p, use_unified) for p in files]
        with ProcessPoolExecutor(max_workers=workers) as executor:
            results = list(executor.map(_info_one_file, work_args, chunksize=chunksize))
    else:
        for path in files:
            logger.debug("processing: %s", path)
            try:
                result = detect_file(path)
                _log_detect_result(result)
                gates = _get_gates(path)
                _log_gates(gates)
                hash_line = _pick_hash_line(path, use_unified=use_unified) if not no_hash else None
                file_result = _FileResult(path=path, product=result.product, container=result.container, encrypted=result.encrypted, gates=gates, hash_line=hash_line)
            except Exception as exc:
                logger.debug("error processing %s: %s", path, exc)
                file_result = _FileResult(path=path, product=Product.UNKNOWN, container=ContainerKind.UNKNOWN, encrypted=False, gates=[], hash_line=None, error=str(exc))
            results.append(file_result)
            if json_output:
                _info_emit_json(file_result, use_unified=use_unified, json_records=json_records)

    _info_emit_results(results, stats=stats, single_file=single_file, no_hash=no_hash, quiet=quiet, json_output=json_output, max_name_len=max_name_len)

    if not quiet and not json_output and not single_file:
        stats.elapsed = time.monotonic() - start_time
        _err.print(f"\n{stats.format()}")

    if json_output and not quiet:
        sys.stderr.write(json.dumps({"files": json_records}, indent=2) + "\n")


# ==========================================================================
# unlock command -- recovery ladder helpers
# ==========================================================================
def _unlock_decode(path: Path, result: DetectResult, *, force: bool, tmp_dir: Path | None = None) -> Path | None:
    """Step 1: decode keyless obfuscation if applicable.

    Handles: Outlook PST/OST body cipher, Access Jet .mdb password recovery,
    and Access MDW workgroup account password recovery.  Returns the decoded
    output path on success, ``None`` when the step does not apply.

    When ``tmp_dir`` is given, intermediates are written there instead of next
    to the input (used by ``unlock`` to keep intermediates temporary).
    """
    if result.container is ContainerKind.ACCESS:
        return _unlock_decode_access(path)
    if result.container is ContainerKind.ACCESS_MDW:
        return _unlock_decode_mdw(path)
    if result.container is not ContainerKind.PST:
        return None
    pst_handler = handler_for(result.container)
    decode_fn = getattr(pst_handler, "decode_body", None)
    if decode_fn is None:
        return None
    decode_target = (tmp_dir / f"decoded{path.suffix}") if tmp_dir else _derive_output(path, "unlocked")
    try:
        if not tmp_dir:
            _guard_output(path, decode_target, force=force)
        decode_fn(path, decode_target)
    except (NotImplementedError, LookupError, ValueError, SystemExit):
        logger.debug("PST decode step did not apply or failed for %s", path)
        return None
    logger.debug("decoded %s -> %s", path, decode_target)
    return decode_target


def _unlock_decode_access(path: Path) -> Path | None:
    """Recover a Jet .mdb password instantly (DECODE class) and print it."""
    header = read_header(path)
    if header is None:
        return None
    decode = decode_jet_password(header)
    if decode.recovered:
        _err.print(f"[green]Database password recovered:[/] [bold]{decode.recovered!r}[/]")
    return None


def _unlock_decode_mdw(path: Path) -> Path | None:
    """Recover all ULS account passwords from a .mdw workgroup file."""
    data = path.read_bytes()
    result = parse_mdw(data)
    if result is None:
        return None
    for acc in result.accounts:
        if acc.is_group or not acc.password:
            continue
        pid_info = f" PID={acc.pid!r}" if acc.pid else ""
        _err.print(f"[green]ULS account {acc.name!r}:[/] password=[bold]{acc.password!r}[/]{pid_info}")
    if result.workgroup and result.workgroup.workgroup_id.strip():
        wg = result.workgroup
        _err.print(f"[green]Workgroup:[/] WID={wg.workgroup_id!r} Name={wg.owner_name!r} Org={wg.organisation!r}")
    return None


def _unlock_decrypt(
    source: Path,
    password: str | None,
    wordlist: Path | None,
    *,
    force: bool,
    tmp_dir: Path | None = None,
) -> tuple[Path | None, int]:
    """Step 2: decrypt open-encryption with defaults then user-supplied candidates.

    Returns ``(produced_path, exit_code)``.  ``produced_path`` is the decrypted
    file on success, ``None`` when the file is not encrypted.  ``exit_code`` is
    ``EXIT_OK`` on success or skip, or a terminal code (``EXIT_CRACK_REQUIRED``,
    ``EXIT_UNRECOVERABLE``) when the step fails -- the caller decides whether to
    abort or continue with the next file.

    When ``tmp_dir`` is given, the decrypted file is written there instead of
    next to the input (used by ``unlock`` to keep intermediates temporary).
    """
    decrypt_result = detect_file(source)
    if not decrypt_result.encrypted:
        logger.debug("not encrypted, skipping decrypt step")
        return None, EXIT_OK

    if _is_unrecoverable(source):
        logger.debug("IRM/RMS detected, skipping decrypt step")
        return None, EXIT_UNRECOVERABLE

    decrypt_target = (tmp_dir / f"decrypted{source.suffix}") if tmp_dir else _derive_output(source, "unlocked")
    try:
        if not tmp_dir:
            _guard_output(source, decrypt_target, force=force)
        opened = _decrypt_with_candidates(source, decrypt_target, _candidate_passwords(password, wordlist))
    except (NotImplementedError, LookupError, SystemExit) as exc:
        logger.debug("decrypt unavailable: %s", exc)
        opened = False

    if opened:
        logger.debug("decrypted %s -> %s", source, decrypt_target)
        return decrypt_target, EXIT_OK

    if not tmp_dir:
        _emit_hashes(source)
    return None, EXIT_CRACK_REQUIRED


def _unlock_collide(source: Path) -> None:
    """Step 3: print any collidable (tiny) verifiers the file carries.

    These are 16-bit / 32-bit / CRC-32 verifiers where minting a satisfying
    password is instant (no cracking required).  The ``unlock`` command reports
    them; the actual collision is done by ``opt advanced collide``.
    """
    gates = _get_gates(source)
    collidable = [g for g in gates if g.recovery is RecoveryClass.COLLIDE]
    logger.debug("unlock collide: %d collidable gates out of %d total", len(collidable), len(gates))
    for gate in collidable:
        _err.print(f"[cyan]{gate.display_name}[/]: [bold]collide[/] [dim]-- {gate.note}[/]")


def _unlock_one_file(
    path: Path,
    *,
    out: Path | None,
    password: str | None,
    wordlist: Path | None,
    remove_signatures: bool,
    force: bool,
    stats: _UnlockStats,
) -> int:
    """Process one file through the recovery ladder, returning the exit code."""
    result = detect_file(path)
    gates = _get_gates(path)
    stats.record_product(result.product)
    logger.debug("unlock: processing %s", path)

    _err.print(f"\n[bold]{_file_header(path, result.product, encrypted=result.encrypted)}[/]")

    if not gates and not result.encrypted:
        _err.print("  No protection, nothing to do.")
        stats.skipped_no_protection += 1
        return EXIT_OK

    if _is_unrecoverable(path):
        _err.print("  [yellow]Rights management (IRM) — not recoverable.[/]")
        stats.skipped_not_recoverable += 1
        return EXIT_OK

    found_parts: list[str] = []
    open_gates = [g for g in gates if g.gate is GateType.OPEN]
    if open_gates:
        found_parts.append(_describe_open_gate(open_gates[0]))
    found_parts.extend(_describe_protection_gates(gates))
    if found_parts:
        joined = ", ".join(found_parts)
        _err.print(f"  Found: {joined[0].lower()}{joined[1:]}")

    exit_code = EXIT_OK
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        source: Path = path
        was_decrypted = False
        members_stripped = 0

        decoded = _unlock_decode(path, result, force=force, tmp_dir=tmp)
        if decoded is not None:
            source = decoded

        decrypted, decrypt_exit = _unlock_decrypt(source, password, wordlist, force=force, tmp_dir=tmp)
        if decrypt_exit != EXIT_OK:
            exit_code = decrypt_exit
        if decrypted is not None:
            source = decrypted
            was_decrypted = True

        _unlock_collide(source)

        final_out = _unlock_produce_output(path, source, out=out, remove_signatures=remove_signatures, force=force)
        if isinstance(final_out, Path):
            members_stripped = _count_stripped(path, source, final_out)
        else:
            members_stripped = 0
            final_out = None

        _unlock_report(path, gates, open_gates, stats, was_decrypted=was_decrypted, members_stripped=members_stripped, final_out=final_out)

    return exit_code


def _unlock_produce_output(
    original: Path,
    source: Path,
    *,
    out: Path | None,
    remove_signatures: bool,
    force: bool,
) -> Path | None:
    """Write the final ``.unlocked`` output from bypass or copy."""
    current_gates = _get_gates(source)
    if current_gates:
        target = out if out is not None else _derive_output(original, "unlocked")
        try:
            _guard_output(original, target, force=force)
            changed = bypass_file(source, target, remove_signatures=remove_signatures)
        except (NotImplementedError, LookupError, SystemExit) as exc:
            logger.debug("bypass failed for %s: %s", source, exc)
            return None
        if not changed:
            target.unlink(missing_ok=True)
            return None
        return target
    if source != original:
        target = out if out is not None else _derive_output(original, "unlocked")
        _guard_output(original, target, force=force)
        shutil.copy2(source, target)
        return target
    return None


def _count_stripped(original: Path, source: Path, final_out: Path) -> int:
    """Return the number of members stripped by comparing source vs output gates."""
    source_gates = _get_gates(source) if source != original else _get_gates(original)
    final_gates = _get_gates(final_out)
    return max(0, len(source_gates) - len(final_gates))


def _unlock_report(
    path: Path,
    gates: list[Gate],
    open_gates: list[Gate],
    stats: _UnlockStats,
    *,
    was_decrypted: bool,
    members_stripped: int,
    final_out: Path | None,
) -> None:
    """Print the per-file narrative and update stats."""
    if was_decrypted and members_stripped:
        _err.print(f"  Decrypted, stripped protection from {members_stripped} member{'s' if members_stripped != 1 else ''}")
        stats.decrypted += 1
        stats.protection_stripped += 1
    elif was_decrypted:
        _err.print("  Decrypted")
        stats.decrypted += 1
    elif members_stripped:
        _err.print(f"  Stripped protection from {members_stripped} member{'s' if members_stripped != 1 else ''}")
        stats.protection_stripped += 1

    if final_out is not None:
        remaining = _get_gates(final_out)
        status_desc = "no protection remaining" if not remaining else f"{len(remaining)} gate{'s' if len(remaining) != 1 else ''} remaining"
        _err.print(f"  [green]Wrote:[/] {final_out} ({status_desc})")
        stats.files_written += 1
    elif open_gates and not was_decrypted:
        _err.print("  [yellow]Cannot decrypt without password[/]")
        stats.still_encrypted += 1
        for gate in gates:
            if gate.hashcat_mode is not None:
                _err.print(f"  Hash for cracking (hashcat -m {gate.hashcat_mode}):")
                stats.hashcat_modes[gate.hashcat_mode] = stats.hashcat_modes.get(gate.hashcat_mode, 0) + 1
                break
        for h in _extract_hashes_safe(path):
            typer.echo(h.opt_value or h.value)


# ==========================================================================
# unlock command
# ==========================================================================
@app.command()
def unlock(
    paths: _InputFiles,
    *,
    out: Annotated[
        Path | None,
        typer.Option("-o", "--output", dir_okay=False, help="Output path (only valid with a single input file)"),
    ] = None,
    password: _Password = None,
    wordlist: _Wordlist = None,
    remove_signatures: Annotated[
        bool,
        typer.Option("--remove-signatures", help="Also delete digital signatures in the bypass step (destructive, cannot be undone)."),
    ] = False,
    force: _Force = False,
) -> None:
    """Try everything cheapest-first to recover Office file(s).

    Walks the recovery ladder per file: decode, decrypt, collide, bypass.
    Each step degrades gracefully when it does not apply.  Produces a single
    ``.unlocked`` output file per input when any step succeeds.

    Examples:
      opt unlock secret.xlsx                       Auto-recover
      opt unlock secret.xlsx -p "hunter2"          Try a known password
      opt unlock *.docx --wordlist passwords.txt   Batch with wordlist
      opt unlock folder/ --force                   Recurse + overwrite
    """
    files = _resolve_inputs(paths)
    if not files:
        _err.print("[red]No Office files found in the given paths.[/]")
        raise typer.Exit(code=EXIT_ERROR)

    if out is not None and len(files) > 1:
        _err.print("[red]--output/-o can only be used with a single input file.[/]")
        raise typer.Exit(code=EXIT_REFUSED)

    start_time = time.monotonic()
    stats = _UnlockStats()
    worst_exit = EXIT_OK

    for path in files:
        file_exit = _unlock_one_file(path, out=out, password=password, wordlist=wordlist, remove_signatures=remove_signatures, force=force, stats=stats)
        worst_exit = max(worst_exit, file_exit)

    if len(files) > 1:
        stats.elapsed = time.monotonic() - start_time
        _err.print(f"\n{stats.format()}")

    if worst_exit != EXIT_OK:
        raise typer.Exit(code=worst_exit)


# ==========================================================================
# advanced subcommand group
# ==========================================================================


# --- advanced extract --------------------------------------------------------
@advanced_app.command(name="extract")
def adv_extract(
    path: _InputFile,
    *,
    format_: Annotated[
        str,
        typer.Option("--format", help="Hash line format: 'hashcat' (default, for piping) or 'opt' (self-describing 4-family lines)."),
    ] = "hashcat",
    hashcat_only: Annotated[
        bool,
        typer.Option("--hashcat-only", help="Emit only lines that current hashcat HEAD can ingest."),
    ] = False,
) -> None:
    """Emit crackable hash lines for every password gate the file carries.

    Default (--format hashcat): hashcat-compatible lines ($office$*2013*...,
    $oldoffice$*..., $odf$*..., hashcat 110 for VBA).
    --format opt: self-describing 4-family lines ($office$*sha512*aes256*cbc*...).
    XOR and PST verifiers are handled by ``decode`` / ``collide``, not here.
    Exit 0 if any hash is emitted, 3 if no gate exists, 7 if gates exist but
    none produce a hash.
    """
    try:
        hashes = extract_hashes(path)
    except (NotImplementedError, LookupError, ValueError) as exc:
        _err.print(f"[yellow]{exc}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED) from exc

    if hashcat_only:
        hashes = [h for h in hashes if h.hashcat_mode is not None]
    use_opt = format_.lower() == "opt"
    if use_opt:
        hashes = [h for h in hashes if h.opt_value is not None]

    if not hashes:
        # Distinguish "no gates at all" from "gates present but no extractable hash".
        result = detect_file(path)
        handler = handler_for(result.container)
        has_gates = handler is not None and bool(handler.gates(path))
        if has_gates:
            _err.print("[yellow]Protection gates present but no crackable hash (try decode / collide / bypass).[/]")
            raise typer.Exit(code=EXIT_NO_HASH)
        _err.print("[yellow]No crackable hash found.[/]")
        raise typer.Exit(code=EXIT_NOT_ENCRYPTED)

    for extracted in hashes:
        typer.echo(extracted.opt_value if use_opt else extracted.value)


# --- advanced decode ---------------------------------------------------------
def _decode_pst(path: Path, handler: FormatHandler, out: Path | None, *, force: bool) -> None:
    """Decode the PST body cipher and write the plaintext store.

    The body cipher is keyless (NDB_CRYPT_PERMUTE or NDB_CRYPT_CYCLIC) -- no
    password is needed.  The CRC-32 advisory password is a separate gate.
    """
    target = out if out is not None else _derive_output(path, "unlocked")
    _guard_output(path, target, force=force)
    decode_fn = getattr(handler, "decode_body", None)
    if decode_fn is None:
        _err.print("[yellow]No decode_body method on this handler[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED)
    try:
        decode_fn(path, target)
    except (NotImplementedError, LookupError) as exc:
        _err.print(f"[yellow]{exc}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED) from exc
    _err.print(f"[green]Decoded ->[/] {target}")
    typer.echo(str(target))


def _decode_access(path: Path) -> None:
    """Recover the Jet .mdb cleartext password and print it.

    Jet 3 and 4 store the "database password" as a fixed/date-key XOR of the
    plaintext in the header -- it is recovered instantly, no cracking involved.
    ACE .accdb uses real agile encryption and requires ``decrypt`` instead.
    """
    header = read_header(path)
    if header is None or header.engine not in (AccessEngine.JET3, AccessEngine.JET4):
        _err.print("[yellow]Not a Jet .mdb file (ACE .accdb uses real encryption -- try decrypt).[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED)
    decode_result = decode_jet_password(header)
    if decode_result.recovered:
        _err.print(f"[green]Jet database password recovered:[/] {decode_result.recovered!r}")
        typer.echo(decode_result.recovered)
    else:
        _err.print(f"[yellow]{decode_result.note}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED)


def _decode_ole(path: Path, out: Path | None, *, force: bool) -> None:
    """Decode an XOR-obfuscated .xls/.doc via the decrypt path with an empty password.

    The XOR "encryption" in [MS-OFFCRYPTO] Section 2.3.6.2 uses a key derived
    from a 16-bit password verifier.  An empty password (or any collision) is
    all that is needed.
    """
    target = out if out is not None else _derive_output(path, "unlocked")
    _guard_output(path, target, force=force)
    try:
        decrypt_file(path, target, "")
    except ValueError:
        _err.print("[yellow]Could not decode: the file may need a password (try decrypt -p <password>).[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED) from None
    except (NotImplementedError, LookupError) as exc:
        _err.print(f"[yellow]{exc}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED) from exc
    _err.print(f"[green]Decoded ->[/] {target}")
    typer.echo(str(target))


@advanced_app.command(name="decode")
def adv_decode(
    path: _InputFile,
    out: Annotated[
        Path | None,
        typer.Argument(dir_okay=False, help="Output path (default: <stem>.unlocked<ext>)"),
    ] = None,
    *,
    force: _Force = False,
) -> None:
    """Reverse keyless obfuscation -- no password needed.

    Handles XOR-obfuscated .xls/.doc (array from known plaintext or stored
    XorKey), Outlook PST/OST body cipher (NDB_CRYPT_PERMUTE / NDB_CRYPT_CYCLIC),
    and Access Jet .mdb password decode (recovers cleartext from the header).
    The input is never modified.  For Jet .mdb, the recovered password is printed
    to stdout instead of writing a file (the database body is already plaintext).
    """
    result = detect_file(path)
    handler = handler_for(result.container)
    if handler is None:
        _err.print(f"[yellow]No handler for {result.container.value}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED)

    # Dispatch to the container-specific decode logic.
    if result.container is ContainerKind.PST and hasattr(handler, "decode_body"):
        _decode_pst(path, handler, out, force=force)
    elif result.container is ContainerKind.ACCESS:
        _decode_access(path)
    elif result.container is ContainerKind.OLE_CFB:
        _decode_ole(path, out, force=force)
    else:
        _err.print(f"[yellow]No decode path for {result.container.value} files.[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED)


# --- advanced collide --------------------------------------------------------
def _collide_pst(handler: FormatHandler, path: Path) -> bool:
    """Collide PST CRC-32 verifiers; return whether any were found.

    Reads the CRC from the OPEN gate's note (the gate embeds the hex value)
    and mints a 4-byte preimage. Uses gates(), not extract().
    """
    try:
        gates = handler.gates(path)
    except (NotImplementedError, LookupError, ValueError):
        return False
    found = False
    for gate in gates:
        if gate.gate is not GateType.OPEN or gate.recovery is not RecoveryClass.STRIP:
            continue
        match = re.search(r"0x([0-9a-fA-F]{8})", gate.note)
        if match is None:
            continue
        crc_int = int(match.group(1), 16)
        collided = pst_crypto.crc_collision(crc_int)
        _err.print(f"[green]PST CRC-32 collided:[/] {collided.hex()}")
        typer.echo(collided.hex())
        found = True
    return found


def _collide_ole(handler: FormatHandler, path: Path) -> bool:
    """Report collidable OLE verifiers (16/32-bit); return whether any were found.

    Legacy .xls 16-bit protection verifiers (sheet, workbook, modify, range,
    revisions) and .doc 32-bit restrict-editing verifier are collidable.
    """
    try:
        gates = handler.gates(path)
    except (NotImplementedError, LookupError, ValueError):
        return False
    found = False
    for gate in gates:
        if gate.recovery is RecoveryClass.COLLIDE and gate.note:
            _err.print(f"[cyan]{gate.display_name}[/]: {gate.note}")
            found = True
    return found


@advanced_app.command(name="collide")
def adv_collide(path: _InputFile) -> None:
    """Mint a password that satisfies a tiny verifier -- instant, read-only.

    Handles: Outlook PST advisory CRC-32 (mints a 4-byte preimage), legacy .xls
    16-bit protection verifiers (sheet / workbook / modify / range / revisions),
    and .doc 32-bit restrict-editing verifier.  Prints each collided password to
    stdout.  The original password is not recovered -- only a value with the same
    checksum.
    """
    result = detect_file(path)
    handler = handler_for(result.container)
    if handler is None:
        _err.print(f"[yellow]No handler for {result.container.value}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED)

    # Dispatch to container-specific collision logic.
    found = _collide_pst(handler, path) if result.container is ContainerKind.PST else _collide_ole(handler, path) if result.container is ContainerKind.OLE_CFB else False
    if not found:
        _err.print("[yellow]No collidable verifier found in this file.[/]")
        raise typer.Exit(code=EXIT_NO_HASH)


# --- advanced bypass ---------------------------------------------------------
@advanced_app.command(name="bypass")
def adv_bypass(
    path: _InputFile,
    out: Annotated[
        Path | None,
        typer.Argument(dir_okay=False, help="Output path (default: <stem>.unlocked<ext>)"),
    ] = None,
    *,
    remove_signatures: Annotated[
        bool,
        typer.Option("--remove-signatures", help="Also delete any digital signature (destructive, cannot be undone)."),
    ] = False,
    force: _Force = False,
) -> None:
    """Strip/clear ALL non-encrypting gates in one pass into a NEW file.

    Never touches the input.  Clears modify / write-reservation, sheet / workbook /
    document / range / revisions protection, VBA project lock, PST advisory
    password, and ODF body protection.  Digital signatures are left intact unless
    ``--remove-signatures`` is given (opt-in, destructive: it drops the signature's
    integrity/authenticity claim).  Does not attempt open-encryption -- that is
    ``decrypt``.
    """
    target = out if out is not None else _derive_output(path, "unlocked")
    _guard_output(path, target, force=force)
    try:
        changed = bypass_file(path, target, remove_signatures=remove_signatures)
    except (NotImplementedError, LookupError, ValueError) as exc:
        _err.print(f"[yellow]{exc}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED) from exc
    if not changed:
        target.unlink(missing_ok=True)
        _err.print("[yellow]No protection to strip.[/]")
        raise typer.Exit(code=EXIT_OK)
    _err.print(f"[green]Bypassed ->[/] {target}")
    typer.echo(str(target))


# --- advanced strip ----------------------------------------------------------
@advanced_app.command(name="strip")
def adv_strip(
    path: _InputFile,
    out: Annotated[
        Path | None,
        typer.Argument(dir_okay=False, help="Output path (default: <stem>.unlocked<ext>)"),
    ] = None,
    *,
    force: _Force = False,
) -> None:
    """Strip ALL non-encrypting protection INCLUDING digital signatures.

    The most aggressive non-encrypting recovery: every protection gate that can
    be removed without the password is removed, including the digital signature
    integrity claim.  Equivalent to ``bypass --remove-signatures``, but with an
    explicit name for scripts that want the nuclear option.  The input is never
    modified.
    """
    target = out if out is not None else _derive_output(path, "unlocked")
    _guard_output(path, target, force=force)
    try:
        # remove_signatures=True is the key difference from bypass.
        bypass_file(path, target, remove_signatures=True)
    except (NotImplementedError, LookupError, ValueError) as exc:
        _err.print(f"[yellow]{exc}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED) from exc
    _err.print(f"[green]Stripped ->[/] {target}")
    typer.echo(str(target))


# --- advanced decrypt --------------------------------------------------------
@advanced_app.command(name="decrypt")
def adv_decrypt(
    path: _InputFile,
    out: Annotated[
        Path | None,
        typer.Argument(dir_okay=False, help="Output path (default: <stem>.unlocked<ext>)"),
    ] = None,
    *,
    password: _Password = None,
    wordlist: _Wordlist = None,
    force: _Force = False,
) -> None:
    """Decrypt real document-open encryption into a NEW plaintext file.

    The built-in defaults (empty string, ``VelvetSweatshop``,
    ``/01Hannes Ruescher/01``) are tried first and silently, then any
    ``-p``/``--password``, then each ``--wordlist`` entry, stopping on the first
    that opens the file.  On success, run ``opt info`` and ``opt advanced bypass``
    on the output, which may still carry inner protection.
    """
    target = out if out is not None else _derive_output(path, "unlocked")
    _guard_output(path, target, force=force)

    # Bail early on IRM/RMS -- the content key is held off-file.
    if _is_unrecoverable(path):
        _err.print("[yellow]Rights-managed (IRM/RMS): the content key is held off-file; not recoverable.[/]")
        raise typer.Exit(code=EXIT_UNRECOVERABLE)

    # Bail if the file is not encrypted -- bypass is the right tool then.
    if not detect_file(path).encrypted:
        _err.print("[yellow]Not encrypted: there is no document-open password to decrypt (try `opt advanced bypass`).[/]")
        raise typer.Exit(code=EXIT_NOT_ENCRYPTED)

    candidates = _candidate_passwords(password, wordlist)
    try:
        opened = _decrypt_with_candidates(path, target, candidates)
    except (NotImplementedError, LookupError) as exc:
        _err.print(f"[yellow]{exc}[/]")
        raise typer.Exit(code=EXIT_UNSUPPORTED) from exc

    if not opened:
        _err.print("[yellow]No candidate password decrypted the file; cracking is required.[/]")
        raise typer.Exit(code=EXIT_CRACK_REQUIRED)

    _err.print(f"[green]Decrypted ->[/] {target}. Next: run `opt info {target}` and `opt advanced bypass {target}`.")
    typer.echo(str(target))


# --- advanced verify ---------------------------------------------------------
def _verify_ole_integrity(path: Path) -> str | None:
    """Try opening ``path`` as an OLE/CFB compound file and return an error string on failure.

    Returns ``None`` when the file opens cleanly, or a description of the
    corruption when it does not.
    """
    try:
        ole = olefile.OleFileIO(path)
        ole.close()
    except Exception as exc:
        return f"corrupt OLE container: {exc}"
    return None


def _verify_zip_integrity(path: Path) -> str | None:
    """Try opening ``path`` as a ZIP archive and check its internal structure.

    For OOXML packages, also checks that ``[Content_Types].xml`` is present
    and parseable.  Returns ``None`` on success, or an error description on
    failure.
    """
    try:
        with zipfile.ZipFile(path, "r") as zf:
            # Run the CRC integrity check on all members.
            bad = zf.testzip()
            if bad is not None:
                return f"corrupt ZIP: CRC mismatch in member {bad}"
            error = _check_zip_manifest(zf)
            if error is not None:
                return error
    except zipfile.BadZipFile as exc:
        return f"corrupt ZIP: {exc}"
    except Exception as exc:
        return f"not a valid ZIP archive: {exc}"
    return None


def _check_zip_manifest(zf: zipfile.ZipFile) -> str | None:
    """Verify the internal manifest of an opened OOXML or ODF ZIP archive.

    Returns ``None`` on success, or an error description on failure.
    """
    names = zf.namelist()
    if "[Content_Types].xml" in names:
        try:
            ct_data = zf.read("[Content_Types].xml")
            if not ct_data or b"<Types" not in ct_data:
                return "corrupt OOXML: [Content_Types].xml is empty or malformed"
        except Exception as exc:
            return f"corrupt OOXML: cannot read [Content_Types].xml: {exc}"
    elif any(n.startswith("mimetype") for n in names):
        try:
            zf.read("mimetype")
        except Exception as exc:
            return f"corrupt ODF: cannot read mimetype member: {exc}"
    return None


def _verify_password_against_file(path: Path, password: str) -> bool:
    """Try to decrypt ``path`` with ``password`` into a temporary file.

    Returns ``True`` when decryption succeeds (the password is correct),
    ``False`` otherwise.  The temporary output is discarded immediately.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_out = Path(tmpdir) / f"verify{path.suffix}"
        try:
            decrypt_file(path, tmp_out, password)
        except (ValueError, NotImplementedError, LookupError, OSError):
            return False
        else:
            return True


def _verify_container_integrity(path: Path, container: ContainerKind) -> str | None:
    """Check structural integrity of the container at ``path``.

    Returns ``None`` when the container opens cleanly, or a human-readable
    error string describing the corruption.  For PST, Access, and OneNote
    containers, detection itself validates the header -- a corrupt header
    would have produced ``ContainerKind.UNKNOWN`` already.
    """
    if container in (ContainerKind.OOXML_ZIP, ContainerKind.ODF_ZIP):
        return _verify_zip_integrity(path)
    if container is ContainerKind.OLE_CFB:
        return _verify_ole_integrity(path)
    return None


def _verify_encrypted_with_password(path: Path, password: str | None) -> None:
    """Handle the "file is still encrypted" branch of verify.

    When a password is given, tests it against the file.  Always raises
    ``typer.Exit`` (encrypted files never reach the "valid" path) except
    when the password test succeeds -- in that case it returns normally so
    the caller can ``return`` after printing.
    """
    if password is None:
        _err.print(f"[yellow]still encrypted:[/] {path}")
        typer.echo("still encrypted")
        raise typer.Exit(code=EXIT_CRACK_REQUIRED)

    valid = _verify_password_against_file(path, password)
    if valid:
        _err.print(f"[green]still encrypted:[/] {path} -- password is correct (decryption succeeded)")
        typer.echo("still encrypted: password valid")
    else:
        _err.print(f"[yellow]still encrypted:[/] {path} -- password is incorrect or unsupported")
        typer.echo("still encrypted: password invalid")
        raise typer.Exit(code=EXIT_CRACK_REQUIRED)


@advanced_app.command(name="verify")
def adv_verify(
    path: _InputFile,
    *,
    password: _Password = None,
) -> None:
    """Verify a file's integrity after decryption or bypass.

    Opens the file with olefile (OLE/CFB) or zipfile (OOXML/ODF) to confirm
    the container is structurally valid, checks whether the content is still
    encrypted, enumerates any remaining protection gates, and reports the
    overall file status.

    When ``-p`` / ``--password`` is given and the file is still encrypted,
    verifies the password against the file (decrypts to a temporary file
    without writing permanent output).

    Reported statuses:
      valid Office document  -- container opens cleanly, not encrypted
      corrupt/truncated      -- container fails integrity checks
      still encrypted        -- document-open encryption is present
      not an Office file     -- not a recognized Office container

    Examples:
      opt advanced verify secret.unlocked.xlsx           Post-unlock check
      opt advanced verify secret.xlsx -p "hunter2"        Verify a password
    """
    result = detect_file(path)

    # Check 1: recognized container?
    if result.container is ContainerKind.UNKNOWN:
        _err.print(f"[red]not an Office file:[/] {path}")
        typer.echo("not an Office file")
        raise typer.Exit(code=EXIT_UNSUPPORTED)

    # Check 2: structural integrity -- try opening the container.
    integrity_error = _verify_container_integrity(path, result.container)
    if integrity_error is not None:
        _err.print(f"[red]corrupt/truncated:[/] {path}: {integrity_error}")
        typer.echo("corrupt/truncated")
        raise typer.Exit(code=EXIT_ERROR)

    # Check 3: still encrypted?
    if result.encrypted:
        _verify_encrypted_with_password(path, password)
        return

    # Check 4: for decrypted ZIP-based files, verify the inner content is valid
    # (a failed decrypt can produce a ZIP with garbage XML inside).
    if result.container in (ContainerKind.OOXML_ZIP, ContainerKind.ODF_ZIP):
        inner_error = _verify_zip_integrity(path)
        if inner_error is not None:
            _err.print(f"[red]corrupt/truncated:[/] {path}: decrypted content is damaged: {inner_error}")
            typer.echo("corrupt/truncated")
            raise typer.Exit(code=EXIT_ERROR)

    # Check 5: any remaining protection gates?
    gates = _get_gates(path)
    if gates:
        tags = _build_tags(gates)
        _err.print(f"[green]valid Office document[/] ({result.container.value}): {path} -- {len(gates)} protection gate(s) remaining: {'  '.join(tags)}")
    else:
        _err.print(f"[green]valid Office document[/] ({result.container.value}): {path} -- no encryption, no protection gates")
    typer.echo("valid Office document")


# --- advanced detail ---------------------------------------------------------
@advanced_app.command(name="detail")
def adv_detail(path: _InputFile) -> None:
    """Show detailed per-gate breakdown for a single file.

    Prints the container, encryption state, and every gate with its recovery
    class, hashcat mode, location within the file, and notes.  This is the
    verbose version of ``opt info`` -- the expert's starting point for deciding
    which advanced subcommand to run.

    The machine-readable summary line goes to stdout; the per-gate breakdown
    (recovery action, hashcat -m mode, location, notes) goes to stderr.
    """
    result = detect_file(path)
    state = "encrypted" if result.encrypted else "not encrypted"
    # Machine-readable summary to stdout (tab-delimited for easy parsing).
    typer.echo(f"{result.path}\t{result.container.value}\t{result.extension or '(none)'}\t{state}")

    handler = handler_for(result.container)
    if handler is None:
        _err.print(f"[yellow]gates: no handler for {result.container.value}[/]")
        return

    try:
        gates = handler.gates(path)
    except (NotImplementedError, LookupError, ValueError):
        _err.print(f"[yellow]gates: not yet enumerated for {result.container.value}[/]")
        return

    if not gates:
        _err.print("[green]gates: none present[/]")
        return

    # Print each gate with full detail to stderr.
    for gate in gates:
        mode = f" [dim](hashcat -m {gate.hashcat_mode})[/]" if gate.hashcat_mode is not None else ""
        where = f" [dim]@ {gate.where}[/]" if gate.where else ""
        note = f" [dim]-- {gate.note}[/]" if gate.note else ""
        _err.print(f"[cyan]{gate.display_name}[/]: [bold]{gate.recovery.value}[/]{mode}{where}{note}")


# ==========================================================================
# Entry point
# ==========================================================================
def main() -> None:
    """Console-script entry point (``office-password-toolkit`` / ``opt``)."""
    app()
