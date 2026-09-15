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
import sys
import tempfile
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import TYPE_CHECKING, Annotated

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
from office_password_toolkit.detect import detect as detect_file
from office_password_toolkit.extract import extract_hashes
from office_password_toolkit.formats import handler_for
from office_password_toolkit.formats.access import AccessEngine, decode_jet_password, read_header
from office_password_toolkit.models import (
    ContainerKind,
    GateType,
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


# ==========================================================================
# Input resolution
# ==========================================================================
def _resolve_inputs(paths: list[Path]) -> list[Path]:
    """Resolve a mix of files, directories, and globs into individual Office files.

    For directories: recursively find files with recognized Office extensions.
    For files: use as-is (no extension filter -- the user chose them explicitly).
    The returned list is sorted by filename for deterministic batch output.
    """
    resolved: list[Path] = []
    for p in paths:
        if p.is_dir():
            for child in sorted(p.rglob("*")):
                if child.is_file():
                    logger.debug("directory scan: found %s", child)
                    resolved.append(child)
        elif p.is_file():
            resolved.append(p)
        else:
            # Should rarely happen (typer validates exists=True), but be safe.
            _err.print(f"[yellow]Skipping {p}: not a file or directory[/]")
            logger.debug("skipping non-file non-directory: %s", p)
    # Sort by name for deterministic output order across batch runs.
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


def format_file_line(filename: str, gates: list[Gate], pad_to: int = 0) -> str:
    """Format the one-liner ``status:scheme`` output for a single file.

    Returns a string like ``secret.xlsx  encrypted:agile-sha512  removable:sheets(3)``.
    When ``pad_to`` is set (for multi-file batch output), the filename column is
    left-padded to that width so the tags align vertically.
    """
    tags = _build_tags(gates)
    padded_name = filename.ljust(pad_to)
    return f"{padded_name}  {'  '.join(tags)}"


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
    """Return ``<stem>.<tag><ext>`` next to ``path`` (e.g. ``secret.decrypted.docx``)."""
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


def _info_emit_status(
    path: Path,
    result: DetectResult,
    gates: list[Gate],
    hash_line: str | None,
    *,
    use_unified: bool,
    json_records: list[dict[str, object]],
    json_output: bool,
    quiet: bool,
    pad_to: int,
) -> None:
    """Emit the per-file status to stderr (JSON record or one-liner).

    When ``json_output`` is set, appends a record to ``json_records`` (flushed
    in bulk by the caller).  Otherwise prints the ``format_file_line`` one-liner.
    """
    if json_output:
        record: dict[str, object] = {
            "path": str(path),
            "container": result.container.value,
            "product": result.product.value,
            "gates": _build_json_gates(gates),
        }
        if hash_line is not None:
            record["hash"] = hash_line
            record["hash_format"] = "unified" if use_unified else "hashcat"
        json_records.append(record)
    elif not quiet:
        line = format_file_line(path.name, gates, pad_to=pad_to)
        _err.print(line)


# ==========================================================================
# info command -- parallel worker
# ==========================================================================
def _info_one_file(args: tuple[Path, bool, int]) -> tuple[str, str | None]:
    """Process one file in a worker process: detect, enumerate gates, extract hash.

    Returns ``(status_line, hash_line_or_None)`` — pre-formatted strings so the
    main process only needs to print them in order.  Defined at module level (not
    a closure) so ``ProcessPoolExecutor`` can pickle it with ``forkserver``.
    """
    path, use_unified, pad_to = args
    try:
        gates = _get_gates(path)
        hash_line = _pick_hash_line(path, use_unified=use_unified)
        status = format_file_line(path.name, gates, pad_to=pad_to)
    except Exception:
        status = format_file_line(path.name, [], pad_to=pad_to)
        hash_line = None
    return status, hash_line


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
    stderr: status:scheme one-liner per file (or JSON with --json / --format json).

    Accepts individual files, directories (recursively finds Office files), and
    shell glob patterns.  Exit 0 if at least one hash was emitted.

    Status key:
      encrypted:   You need the password to read this file
      removable:   Can be removed without the password (opt unlock)
      trivial:     Instantly reversible, no password needed (opt unlock)
      info:        Not a password gate -- just informational
      blocked:     Not recoverable (needs certificate or server key)
      open         No protection at all

    Examples:
      opt info secret.xlsx                  Show gates + hash
      opt info *.docx | hashcat -m 37000   Batch extract + crack
      opt info *.xlsx 2>/dev/null           Hashes only (for scripting)
      opt info folder/                      Recurse into directory
      opt info --format json secret.xlsx    Full JSON output
    """
    files = _resolve_inputs(paths)
    if not files:
        _err.print("[red]No Office files found in the given paths.[/]")
        raise typer.Exit(code=EXIT_ERROR)

    # --format json implies --json (structured JSON output on stderr).
    if format_.lower() == "json":
        json_output = True

    # Compute the longest filename for aligned column output.
    max_name_len = max(len(f.name) for f in files)

    any_hash_emitted = False
    json_records: list[dict[str, object]] = []  # Populated only when --json.
    use_unified = format_.lower() in ("unified", "json")

    # Decide parallelism: 0 = auto (CPU count), 1 = sequential, N = N workers.
    # Fall back to sequential for --debug (child logging), --json (accumulates
    # records), single files (no parallelism benefit), and --no-hash (trivial).
    workers = jobs if jobs > 0 else (os.cpu_count() or 4)
    debug_active = logger.isEnabledFor(logging.DEBUG)
    use_parallel = workers > 1 and not debug_active and not json_output and len(files) > 1

    if use_parallel:
        chunksize = max(1, len(files) // (workers * 4))
        work_args = [(p, use_unified, max_name_len) for p in files]
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for status, hash_line in executor.map(_info_one_file, work_args, chunksize=chunksize):
                if hash_line is not None:
                    any_hash_emitted = True
                if not no_hash:
                    typer.echo(hash_line if hash_line is not None else "")
                if not quiet:
                    _err.print(status)
    else:
        for path in files:
            logger.debug("processing: %s", path)

            # Detect container and enumerate gates.
            result = detect_file(path)
            _log_detect_result(result)
            gates = _get_gates(path)
            _log_gates(gates)

            # Extract hash line for stdout (unless suppressed).
            hash_line = _pick_hash_line(path, use_unified=use_unified) if not no_hash else None
            if hash_line is not None:
                any_hash_emitted = True

            # Emit hash line to stdout (blank line when no hash, for file-to-line alignment).
            if not no_hash:
                typer.echo(hash_line if hash_line is not None else "")

            # Emit status to stderr (JSON or one-liner).
            _info_emit_status(
                path,
                result,
                gates,
                hash_line,
                use_unified=use_unified,
                json_records=json_records,
                json_output=json_output,
                quiet=quiet,
                pad_to=max_name_len,
            )

    # Flush the JSON blob to stderr if --json was given.
    if json_output and not quiet:
        sys.stderr.write(json.dumps({"files": json_records}, indent=2) + "\n")

    # Exit 0 when at least one hash was emitted; 1 otherwise.
    if not any_hash_emitted and not no_hash:
        raise typer.Exit(code=EXIT_ERROR)


# ==========================================================================
# unlock command -- recovery ladder helpers
# ==========================================================================
def _unlock_decode(path: Path, result: DetectResult, *, force: bool) -> Path | None:
    """Step 1: decode keyless obfuscation if applicable.

    Handles: Outlook PST/OST body cipher, Access Jet .mdb password recovery,
    and Access MDW workgroup account password recovery.  Returns the decoded
    output path on success, ``None`` when the step does not apply.
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
    decode_target = _derive_output(path, "decoded")
    try:
        _guard_output(path, decode_target, force=force)
        decode_fn(path, decode_target)
    except (NotImplementedError, LookupError, ValueError, SystemExit):
        logger.debug("PST decode step did not apply or failed for %s", path)
        return None
    _err.print(f"[green]PST body decoded ->[/] {decode_target}")
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
) -> tuple[Path | None, int]:
    """Step 2: decrypt open-encryption with defaults then user-supplied candidates.

    Returns ``(produced_path, exit_code)``.  ``produced_path`` is the decrypted
    file on success, ``None`` when the file is not encrypted.  ``exit_code`` is
    ``EXIT_OK`` on success or skip, or a terminal code (``EXIT_CRACK_REQUIRED``,
    ``EXIT_UNRECOVERABLE``) when the step fails -- the caller decides whether to
    abort or continue with the next file.
    """
    decrypt_result = detect_file(source)
    if not decrypt_result.encrypted:
        logger.debug("not encrypted, skipping decrypt step")
        return None, EXIT_OK

    # IRM/RMS: the content key is held off-file -- nothing we can do.
    if _is_unrecoverable(source):
        _err.print("[yellow]Rights-managed (IRM/RMS): the content key is held off-file; not recoverable.[/]")
        return None, EXIT_UNRECOVERABLE

    decrypt_target = _derive_output(source, "decrypted")
    try:
        _guard_output(source, decrypt_target, force=force)
        opened = _decrypt_with_candidates(source, decrypt_target, _candidate_passwords(password, wordlist))
    except (NotImplementedError, LookupError, SystemExit) as exc:
        _err.print(f"[yellow]decrypt unavailable: {exc}[/]")
        opened = False

    if opened:
        _err.print(f"[green]Decrypted ->[/] {decrypt_target}")
        return decrypt_target, EXIT_OK

    # Could not decrypt -- emit hashes for cracking and signal the caller.
    _err.print("[yellow]Cannot produce plaintext; emitting hashes for cracking.[/]")
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


def _unlock_bypass(
    source: Path,
    out: Path | None,
    *,
    remove_signatures: bool,
    force: bool,
) -> Path | None:
    """Step 4: strip all non-encrypting gates.

    Clears modify / write-reservation, sheet / workbook / document / range /
    revisions protection, the VBA project lock, PST advisory password, and ODF
    body protection.  Signatures are left unless ``remove_signatures`` is set.
    Returns the produced path on success, ``None`` on failure.
    """
    bypass_target = out if out is not None else _derive_output(source, "bypassed")
    logger.debug("unlock bypass: source=%s remove_signatures=%s", source, remove_signatures)
    try:
        _guard_output(source, bypass_target, force=force)
        changed = bypass_file(source, bypass_target, remove_signatures=remove_signatures)
    except (NotImplementedError, LookupError, SystemExit) as exc:
        _err.print(f"[yellow]bypass unavailable: {exc}[/]")
        logger.debug("bypass failed for %s: %s", source, exc)
        return None
    if not changed:
        logger.debug("unlock bypass: handler rewrote 0 members, removing no-op output")
        bypass_target.unlink(missing_ok=True)
        return None
    _err.print(f"[green]Bypassed ->[/] {bypass_target}")
    return bypass_target


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

    Orchestrates the full recovery ladder per file:
    info -> decode -> decrypt -> collide -> bypass -> info.  Each step degrades
    gracefully when it does not apply or the handler is unfinished.  Supports
    multiple files and directories (each file processed independently).

    ``-o`` / ``--output`` is only valid with a single input file.

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

    # --output only makes sense with a single file.
    if out is not None and len(files) > 1:
        _err.print("[red]--output/-o can only be used with a single input file.[/]")
        raise typer.Exit(code=EXIT_REFUSED)

    # Track the worst exit code across all files so the process signals
    # partial failure to the caller (e.g. some files needed cracking).
    worst_exit = EXIT_OK

    for path in files:
        _err.print(f"\n[bold]--- {path.name} ---[/]")
        logger.debug("unlock: processing %s", path)

        # Step 0: triage -- show the file's gates before doing anything.
        result = detect_file(path)
        gates = _get_gates(path)
        line = format_file_line(path.name, gates)
        _err.print(line)

        # Step 1: decode keyless obfuscation (PST body cipher, etc.).
        produced = _unlock_decode(path, result, force=force)
        source = produced if produced is not None else path

        # Step 2: decrypt open-encryption with defaults / password / wordlist.
        decrypted, decrypt_exit = _unlock_decrypt(source, password, wordlist, force=force)
        if decrypt_exit != EXIT_OK:
            # Record the failure but continue to subsequent steps -- collide
            # and bypass may still clear non-encrypting protection.
            worst_exit = max(worst_exit, decrypt_exit)
        if decrypted is not None:
            produced = decrypted
            source = decrypted

        # Step 3: report collidable (tiny) verifiers.
        _unlock_collide(source)

        # Step 4: strip non-encrypting protection (skip when nothing to strip).
        current_gates = _get_gates(source)
        if current_gates:
            bypassed = _unlock_bypass(source, out, remove_signatures=remove_signatures, force=force)
        else:
            logger.debug("unlock bypass: no gates on %s, skipping", source)
            bypassed = None
        if bypassed is not None:
            produced = bypassed

        # Final triage: show the gates of whatever file was produced.
        if produced is not None:
            _err.print("[bold]Final triage:[/]")
            final_gates = _get_gates(produced)
            final_line = format_file_line(produced.name, final_gates)
            _err.print(final_line)

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
    target = out if out is not None else _derive_output(path, "decoded")
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
    target = out if out is not None else _derive_output(path, "decoded")
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
        typer.Argument(dir_okay=False, help="Decoded output path (default: <stem>.decoded<ext>)"),
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
        typer.Argument(dir_okay=False, help="Unprotected output path (default: <stem>.bypassed<ext>)"),
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
    target = out if out is not None else _derive_output(path, "bypassed")
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
        typer.Argument(dir_okay=False, help="Stripped output path (default: <stem>.stripped<ext>)"),
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
    target = out if out is not None else _derive_output(path, "stripped")
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
        typer.Argument(dir_okay=False, help="Decrypted output path (default: <stem>.decrypted<ext>)"),
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
    target = out if out is not None else _derive_output(path, "decrypted")
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
      opt advanced verify secret.decrypted.xlsx           Post-decrypt check
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
