# SPDX-License-Identifier: Apache-2.0
"""OOXML / OPC handler -- unencrypted ``.docx`` / ``.xlsx`` / ``.pptx`` / ``.xlsb`` packages.

An OPC package is a plain PKZIP archive of XML (or, for ``.xlsb``, binary
BIFF12) parts. This handler owns the *unencrypted* case only: a document-open
*encrypted* OOXML file is not a ZIP on disk -- Office re-wraps the whole package
inside an OLE/CFB container (``EncryptionInfo`` + ``EncryptedPackage`` streams)
that keeps the ``.docx``/``.xlsx``/``.pptx`` extension, and that physical layout is
handled by :class:`~office_password_toolkit.formats.ole.OleHandler`. So here
:meth:`OoxmlHandler.is_encrypted` is *always* ``False`` and :meth:`decrypt` does
not apply; the job of this module is the inner permission gates that ride inside
the plaintext package and the free ways to strip them.

Gates enumerated (see ``docs/reference/gates.md`` and the analysis corpus
``analysis/file-formats/{word,excel,powerpoint}.md`` +
``analysis/password-algorithms/iso-protection-hash.md``):

* Excel ``xl/worksheets/sheetN.xml`` ``<sheetProtection>`` -> Protect Sheet;
  ``<protectedRange>`` -> Allow Edit Ranges; ``xl/chartsheets`` chart sheets.
* Excel ``xl/workbook.xml`` ``<workbookProtection>`` -> Protect Workbook (plus its
  ``revisions*`` half -> Shared-revisions lock) and ``<fileSharing>`` -> Modify.
* ``.xlsb`` binary ``Brt*ProtectionIso`` / ``BrtFileSharingIso`` records: the gate
  is detected by a BIFF12 record walk and the ``IsoPasswordData`` body is parsed for
  a hash line (iso-protection-hash.md Section 3.3 / 10.4).
* Word ``word/settings.xml`` ``<w:writeProtection>`` -> Modify and
  ``<w:documentProtection>`` -> Restrict Editing. The ISO ``*Value`` dialect emits a
  25300 or generalized ``$office-protect$`` line; the legacy ``crypt*`` dialect emits
  an ``$office-protect$*...*crypt*...`` line (crypt-documentprotection.md Section 7).
* PowerPoint ``ppt/presentation.xml`` ``<p:modifyVerifier>`` -> Modify.
* ``*/vbaProject.bin`` (an embedded OLE blob) -> Macro project lock (VBA).
* ``_xmlsignatures/`` parts -> Digital signature.

Every ISO protection carrier ([MS-OFFCRYPTO] Section 2.4.2.4) exposes
``algorithmName``/``saltValue``/``hashValue``/``spinCount`` in the clear. Only the
modern default shape -- SHA-512, spinCount 100000, 16-byte salt -- has a shipped
hashcat mode (25300); every other primitive/spin/salt length is emitted as the
generalized ``$office-protect$`` line (iso-protection-hash.md Section 7) with no
hashcat mode. Because the package body is never encrypted by any of these gates,
the fast path is always STRIP (delete the element), which :meth:`bypass` does on a
fresh copy of the package.

Design notes: parts are read with the stdlib :mod:`zipfile`; the small,
attribute-only protection elements are parsed and rewritten with byte-level
regular expressions (the same approach the crypto layer uses for the agile
descriptor) so :meth:`bypass` preserves every untouched member exactly.
"""

from __future__ import annotations

import io
import logging
import re
import struct
import zipfile
from base64 import b64encode
from dataclasses import dataclass
from html import unescape
from typing import TYPE_CHECKING, Final

import olefile
from typing_extensions import override

from office_password_toolkit.crypto import protection, vba
from office_password_toolkit.crypto.protection import unified_protect_line, unified_protect_line_from_sid
from office_password_toolkit.crypto.vba import unified_vba_line
from office_password_toolkit.formats.base import FormatHandler
from office_password_toolkit.models import (
    ContainerKind,
    ExtractedHash,
    Gate,
    GateType,
    HashScheme,
    RecoveryClass,
)

if TYPE_CHECKING:
    from collections.abc import Iterator
    from pathlib import Path

logger = logging.getLogger(__name__)

# --- hashcat mode / hash-shape constants ---

# hashcat "MS Office 2016 - SheetProtection". Ingests the ISO write-protection
# hash only for the modern Office default shape ([MS-OFFCRYPTO] Section 2.4.2.4;
# iso-protection-hash.md Section 9): SHA-512, spinCount 100000, 16-byte salt.
_MODE_25300: Final = 25300
_SPIN_25300: Final = 100_000
# Canonical (separator-stripped, upper-cased) form of the only crackable primitive.
_SHA512_CANON: Final = "SHA512"
# hashcat "sha1($pass.$salt)" -- reused for the VBA project verifier ([MS-OVBA] Section 2.4.4.4).
_MODE_VBA: Final = 110

# --- VBA PROJECT-stream constants ([MS-OVBA]) ---

# The all-zero CLSID [MS-OVBA] Section 2.3.1.16 forces whenever DPB stores a
# password hash; its byte-sum gives the fixed ProjKey 0xAC used for re-encoding.
_ALL_ZERO_CLSID: Final = "{00000000-0000-0000-0000-000000000000}"
# Any seed works for the Data Encryption wrapper; picking one whose ``seed & 6``
# is zero yields zero filler bytes, i.e. the shortest possible encoding -- which
# guarantees the rewritten (unprotected) PROJECT stream is never longer than the
# original, so it fits back into the fixed-size CFB stream ([MS-OVBA] Section 2.4.3.2).
_VBA_MIN_SEED: Final = 0xA9
# The no-password DPB sentinel payload ([MS-OVBA] Section 2.3.1.16): Length 1, Data 0x00.
_DPB_SENTINEL: Final = b"\x00"

# --- .xlsb BIFF12 record constants ([MS-XLSB] Section 2.1.4 / record enumeration) ---

# Record-type numbers of the ISO strong-password protection records ([MS-XLSB]).
# Detected by a record walk so a plain (unprotected) .xlsb never false-positives;
# the IsoPasswordData body is then parsed into a 25300 / generalized hash line
# (iso-protection-hash.md Section 3.3 / 10.4).
_BRT_FILE_SHARING_ISO: Final = 676  # Section 2.4.672 (write reservation)
_BRT_BOOK_PROTECTION_ISO: Final = 677  # Section 2.4.309 (structure/windows + revisions)
_BRT_SHEET_PROTECTION_ISO: Final = 678  # Section 2.4.784 (worksheet)
_BRT_CS_PROTECTION_ISO: Final = 679  # Section 2.4.343 (chart sheet)
_BRT_RANGE_PROTECTION_ISO: Final = 680  # Section 2.4.756 (edit range)
_BRT_RANGE_PROTECTION_ISO14: Final = 1104  # Section 2.4.757 (edit range, FRT-framed: detection only)

_XLSB_RECORD_GATES: Final[dict[int, tuple[GateType, str]]] = {
    _BRT_FILE_SHARING_ISO: (GateType.MODIFY, "BrtFileSharingIso"),
    _BRT_BOOK_PROTECTION_ISO: (GateType.PROTECT_WORKBOOK, "BrtBookProtectionIso"),
    _BRT_SHEET_PROTECTION_ISO: (GateType.PROTECT_SHEET, "BrtSheetProtectionIso"),
    _BRT_CS_PROTECTION_ISO: (GateType.PROTECT_SHEET, "BrtCsProtectionIso"),
    _BRT_RANGE_PROTECTION_ISO: (GateType.ALLOW_EDIT_RANGES, "BrtRangeProtectionIso"),
    _BRT_RANGE_PROTECTION_ISO14: (GateType.ALLOW_EDIT_RANGES, "BrtRangeProtectionIso14"),
}
# A record type is two bytes iff the low byte's high bit is set; each 7-bit group
# is little-endian ([MS-XLSB] Section 2.1.4).
_BIFF12_CONTINUE: Final = 0x80
_BIFF12_LOW7: Final = 0x7F
_BIFF12_SIZE_MAX_BYTES: Final = 4  # record size is 1..4 bytes

# --- IsoPasswordData body layout ([MS-XLSB] Section 2.5.80 and the carrier records) ---
# ipdPasswordData start offsets for the fixed-prefix records: the byte counts of the
# leading spin-count / Boolean-option fields that precede the password data.
_ISO_OFF_SHEET: Final = 68  # dwSpinCount(4) + 16 Boolean option DWORDs (64) [MS-XLSB] 2.4.784
_ISO_OFF_CS: Final = 12  # dwSpinCount(4) + fLocked(4) + fObjects(4) [MS-XLSB] 2.4.343
_ISO_OFF_BOOK: Final = 10  # dwBookSpinCount(4) + dwRevSpinCount(4) + wFlags(2) [MS-XLSB] 2.4.309
_FILE_SHARING_PREFIX: Final = 6  # dwSpinCount(4) + fReadOnlyRec(2) before stUserName [MS-XLSB] 2.4.672
_XL_U32: Final = 4  # little-endian unsigned 32-bit field width
_XL_NULL_STRING: Final = 0xFFFFFFFF  # XLNullableWideString NULL marker ([MS-XLSB] 2.5.167)
_UNCHECKED_RFX_SIZE: Final = 16  # UncheckedRfX = rwFirst/rwLast/colFirst/colLast, 4 x u32 ([MS-XLSB] 2.5.154)

# --- Excel workbookProtection attribute groups ([MS-OE376] Section 2.1.621) ---

# Structure/windows half of <workbookProtection>: any of these means Protect Workbook.
_WB_STRUCTURE_ATTRS: Final = ("lockStructure", "lockWindows", "workbookAlgorithmName", "workbookHashValue", "workbookSaltValue", "workbookSpinCount", "workbookPassword")
# Revisions half of <workbookProtection>: any of these means the shared-revisions lock.
_WB_REVISION_ATTRS: Final = ("lockRevision", "revisionsAlgorithmName", "revisionsHashValue", "revisionsSaltValue", "revisionsSpinCount", "revisionsPassword")

# --- Friendly notes attached to gates/hashes ---

_NOTE_25300: Final = "ISO SHA-512 verifier -- crackable with hashcat -m 25300, but the body is not encrypted so STRIP is the fast path"
_NOTE_GENERALIZED: Final = "ISO protection verifier; no hashcat mode -- generalized $office-protect$ line (iso-protection-hash.md Section 7); body is not encrypted so STRIP is the fast path"
_NOTE_SIGNATURE: Final = "digital signature carries no password secret; run `opt bypass --remove-signatures` to drop the _xmlsignatures/ parts and the integrity claim"
_NOTE_WORD_LEGACY: Final = "Legacy crypt* documentProtection/writeProtection dialect; no hashcat mode -- $office-protect$*...*crypt*... line (crypt-documentprotection.md Section 7); STRIP is the fast path"
_NOTE_XLSB: Final = "binary BIFF12 ISO protection record; the IsoPasswordData body did not parse, so no hash line (bypass does not rewrite binary parts)"
_NOTE_VBA_HASH: Final = "VBA project locked; SHA-1 verifier -> hashcat -m 110 (or STRIP the DPB lock -- macro source is not encrypted)"
_NOTE_VBA_OTHER: Final = "VBA project locked with a cleartext/obfuscated DPB (no crackable verifier); STRIP the DPB lock"

# --- Regular expressions for the attribute-only protection elements ---

# One name="value" attribute pair (name may carry an XML namespace prefix).
_ATTR_RE: Final = re.compile(r'([\w:.\-]+)\s*=\s*"([^"]*)"')


@dataclass(frozen=True)
class _Material:
    """The four ISO write-protection attributes needed to build a hash line."""

    algorithm_name: str
    salt_b64: str
    hash_b64: str
    spin_count: int


@dataclass(frozen=True)
class _Finding:
    """A discovered gate plus, when one exists, its ready-to-crack hash line."""

    gate: GateType
    recovery: RecoveryClass
    where: str
    scheme: HashScheme | None = None
    hashcat_mode: int | None = None
    hash_line: str | None = None
    note: str = ""
    opt_hash_line: str | None = None


# --- Small XML helpers (regex-based, namespace-agnostic) ---


def _canonical(algorithm_name: str) -> str:
    """Collapse an ``algorithmName`` to bare alphanumerics upper-cased (``SHA-512`` -> ``SHA512``)."""
    return "".join(ch for ch in algorithm_name.upper() if ch.isalnum())


def _decode(data: bytes) -> str | None:
    """Decode a UTF-8 XML part, or ``None`` if it is not valid UTF-8 (never raise)."""
    try:
        return data.decode("utf-8")
    except ValueError:
        # UnicodeDecodeError (a ValueError) -- treat a non-text part as "nothing to scan".
        return None


def _find_tags(xml: str, local_name: str) -> list[str]:
    """Return the raw attribute string of every ``<local_name ...>`` opening tag.

    Matches the element regardless of namespace prefix (``<w:documentProtection>``
    and ``<documentProtection>`` both hit). The trailing ``/`` of a self-closing
    tag lands harmlessly in the captured attribute string.
    """
    pattern = re.compile(r"<(?:[\w.\-]+:)?" + re.escape(local_name) + r"\b([^>]*)>", re.DOTALL)
    return [str(m) for m in pattern.findall(xml)]


def _attrs(attr_string: str) -> dict[str, str]:
    """Parse an attribute string into a ``localname -> value`` dict (prefixes stripped, entities decoded)."""
    return {name.split(":")[-1]: unescape(value) for name, value in _ATTR_RE.findall(attr_string)}


def _iso_key(prefix: str, base: str) -> str:
    """Build the attribute name for a carrier: ``""`` -> ``saltValue``; ``"workbook"`` -> ``workbookSaltValue``."""
    if not prefix:
        return base[0].lower() + base[1:]
    return prefix + base


def _iso_material(attrs: dict[str, str], prefix: str) -> _Material | None:
    """Pull the four ISO attributes for ``prefix`` from ``attrs``, or ``None`` if incomplete.

    ``prefix`` selects the carrier's attribute family: ``""`` for the bare quartet
    (sheet/range/fileSharing/Word-ISO/PowerPoint), ``"workbook"`` for structure and
    ``"revisions"`` for the shared-revisions half of ``<workbookProtection>``.
    """
    algorithm = attrs.get(_iso_key(prefix, "AlgorithmName"))
    salt = attrs.get(_iso_key(prefix, "SaltValue"))
    digest = attrs.get(_iso_key(prefix, "HashValue"))
    spin = attrs.get(_iso_key(prefix, "SpinCount"))
    if not (algorithm and salt and digest and spin):
        return None
    try:
        spin_count = int(spin)
    except ValueError:
        return None
    return _Material(algorithm, salt, digest, spin_count)


def _iso_line(material: _Material) -> str | None:
    """Return the ``$office$2016$0$...`` line for ``material``, or ``None`` (GAP) if it is not the 25300 shape.

    The primitive is checked explicitly: only ``algorithmName = SHA-512`` qualifies.
    :func:`protection.hash_line_25300` enforces the spinCount/salt/digest lengths.
    """
    if _canonical(material.algorithm_name) != _SHA512_CANON:
        return None
    if material.spin_count != _SPIN_25300:
        return None
    try:
        return protection.hash_line_25300(material.salt_b64, material.hash_b64, material.spin_count)
    except ValueError:
        # Salt/hash did not decode to the exact 16/64-byte lengths 25300 requires -> GAP.
        return None


def _iso_gap_note(material: _Material) -> str:
    """Human note explaining why an ISO carrier could not be turned into any crackable line."""
    return f"ISO {material.algorithm_name} verifier (spinCount {material.spin_count}); could not build a hash line (unknown primitive or hash width mismatch)"


def _protection_finding(gate: GateType, where: str, material: _Material | None) -> _Finding:
    """Turn an ISO carrier into a :class:`_Finding`: the 25300 line when it fits, else the generalized line, else a bare gate.

    Every one of these gates is STRIP -- the package body is plaintext, so deleting
    the element lifts the lock (``docs/reference/gates.md`` .xlsx/.docx column). The
    non-25300 lines carry no shipped hashcat mode, so ``hashcat_mode`` is ``None``;
    the ``OFFICE_SHEETPROT`` scheme is reused as the office-protection-verifier
    family label (the enum has no dedicated generalized value and ``models.py`` is
    out of scope here), and the ``$office-protect$`` prefix disambiguates the line.
    """
    if material is None:
        return _Finding(gate, RecoveryClass.STRIP, where)
    opt = unified_protect_line(material.algorithm_name, "iso", material.spin_count, material.salt_b64, material.hash_b64)
    line = _iso_line(material)
    if line is not None:
        return _Finding(gate, RecoveryClass.STRIP, where, HashScheme.OFFICE_SHEETPROT, _MODE_25300, line, _NOTE_25300, opt_hash_line=opt)
    if opt is not None:
        return _Finding(gate, RecoveryClass.STRIP, where, HashScheme.OFFICE_SHEETPROT, None, opt, _NOTE_GENERALIZED, opt_hash_line=opt)
    return _Finding(gate, RecoveryClass.STRIP, where, note=_iso_gap_note(material), opt_hash_line=opt)


def _has_any(attrs: dict[str, str], names: tuple[str, ...]) -> bool:
    """Return whether ``attrs`` carries any attribute in ``names``."""
    return any(name in attrs for name in names)


# --- Per-part scanners ---


def _scan_worksheet(data: bytes, where: str) -> list[_Finding]:
    """Enumerate sheet protection and edit-range gates in a worksheet/chartsheet XML part."""
    xml = _decode(data)
    if xml is None:
        return []
    findings: list[_Finding] = [_protection_finding(GateType.PROTECT_SHEET, f"{where} <sheetProtection>", _iso_material(_attrs(tag), "")) for tag in _find_tags(xml, "sheetProtection")]
    findings.extend(_protection_finding(GateType.ALLOW_EDIT_RANGES, f"{where} <protectedRange>", _iso_material(_attrs(tag), "")) for tag in _find_tags(xml, "protectedRange"))
    return findings


def _scan_workbook(data: bytes) -> list[_Finding]:
    """Enumerate workbook-structure, shared-revisions, and write-reservation gates in ``xl/workbook.xml``."""
    xml = _decode(data)
    if xml is None:
        return []
    findings: list[_Finding] = []
    for tag in _find_tags(xml, "workbookProtection"):
        attrs = _attrs(tag)
        # A single <workbookProtection> can carry the structure half, the revisions
        # half, or both -- report only the halves that are actually present.
        if _has_any(attrs, _WB_STRUCTURE_ATTRS):
            findings.append(_protection_finding(GateType.PROTECT_WORKBOOK, "xl/workbook.xml <workbookProtection>", _iso_material(attrs, "workbook")))
        if _has_any(attrs, _WB_REVISION_ATTRS):
            findings.append(_protection_finding(GateType.SHARED_REVISIONS, "xl/workbook.xml <workbookProtection revisions*>", _iso_material(attrs, "revisions")))
    findings.extend(_protection_finding(GateType.MODIFY, "xl/workbook.xml <fileSharing>", _iso_material(_attrs(tag), "")) for tag in _find_tags(xml, "fileSharing"))
    return findings


def _word_finding(gate: GateType, where: str, attrs: dict[str, str]) -> _Finding:
    """Classify a Word protection element: ISO dialect vs legacy ``crypt*`` dialect vs flag-only.

    The ISO dialect (``algorithmName``/``saltValue``/``hashValue``/``spinCount``) goes
    through :func:`_protection_finding` (25300 or generalized). The legacy crypt*
    dialect (``cryptAlgorithmSid``/``cryptSpinCount``/``salt``/``hash``) is a different
    salt-appended, legacy-derived KDF (crypt-documentprotection.md Section 6.1)
    with no hashcat mode; we emit its ``$office-protect$*...*crypt*...`` extraction line.
    """
    material = _iso_material(attrs, "")
    if material is not None:
        return _protection_finding(gate, where, material)
    sid = attrs.get("cryptAlgorithmSid")
    spin = attrs.get("cryptSpinCount")
    salt = attrs.get("salt")
    digest = attrs.get("hash")
    if sid and spin and salt and digest:
        opt = unified_protect_line_from_sid(int(sid), int(spin), salt, digest)
        return _Finding(gate, RecoveryClass.STRIP, where, HashScheme.OFFICE_SHEETPROT, None, opt, _NOTE_WORD_LEGACY, opt_hash_line=opt)
    if "cryptAlgorithmSid" in attrs or "hash" in attrs:
        return _Finding(gate, RecoveryClass.STRIP, where, note=_NOTE_WORD_LEGACY)
    return _Finding(gate, RecoveryClass.STRIP, where)


def _scan_word(data: bytes) -> list[_Finding]:
    """Enumerate write-protection and document-restriction gates in ``word/settings.xml``."""
    xml = _decode(data)
    if xml is None:
        return []
    findings: list[_Finding] = [_word_finding(GateType.MODIFY, "word/settings.xml <w:writeProtection>", _attrs(tag)) for tag in _find_tags(xml, "writeProtection")]
    findings.extend(_word_finding(GateType.RESTRICT_EDIT, "word/settings.xml <w:documentProtection>", _attrs(tag)) for tag in _find_tags(xml, "documentProtection"))
    return findings


def _scan_powerpoint(data: bytes) -> list[_Finding]:
    """Enumerate the PowerPoint modify-password gate in ``ppt/presentation.xml``."""
    xml = _decode(data)
    if xml is None:
        return []
    return [_protection_finding(GateType.MODIFY, "ppt/presentation.xml <p:modifyVerifier>", _iso_material(_attrs(tag), "")) for tag in _find_tags(xml, "modifyVerifier")]


# --- .xlsb BIFF12 record walk ([MS-XLSB] Section 2.1.4) ---


def _biff12_records(data: bytes) -> Iterator[tuple[int, bytes]]:
    """Yield ``(record_id, body)`` for every record in a BIFF12 part ([MS-XLSB] Section 2.1.4).

    The framing is: a 1- or 2-byte little-endian 7-bit record type, then a 1..4-byte
    little-endian 7-bit size, then that many data bytes. A truncated tail stops the
    walk cleanly (the framing read raises ``IndexError``, which ends the generator).
    """
    pos = 0
    size = len(data)
    try:
        while pos < size:
            first = data[pos]
            pos += 1
            if first & _BIFF12_CONTINUE:
                record_id = (first & _BIFF12_LOW7) | ((data[pos] & _BIFF12_LOW7) << 7)
                pos += 1
            else:
                record_id = first
            length = 0
            for index in range(_BIFF12_SIZE_MAX_BYTES):
                byte = data[pos]
                pos += 1
                length |= (byte & _BIFF12_LOW7) << (7 * index)
                if not byte & _BIFF12_CONTINUE:
                    break
            body = data[pos : pos + length]
            pos += length
            yield int(record_id), body
    except IndexError:
        # Ran off the end of a truncated record stream -- stop after the last whole record.
        return


def _biff12_record_ids(data: bytes) -> set[int]:
    """Return the set of record-type numbers present in a BIFF12 part."""
    return {record_id for record_id, _ in _biff12_records(data)}


# --- IsoPasswordData body parsing ([MS-XLSB] Section 2.5.80) ---


def _read_u32(body: bytes, off: int) -> tuple[int, int]:
    """Read a 4-byte little-endian unsigned int, returning ``(value, new_offset)`` (raises past the end)."""
    end = off + _XL_U32
    if end > len(body):
        msg = "BIFF12 record truncated while reading a 32-bit field"
        raise ValueError(msg)
    return int.from_bytes(body[off:end], "little"), end


def _read_i32(body: bytes, off: int) -> tuple[int, int]:
    """Read a 4-byte little-endian *signed* int (used for the ``crfx`` range count, which allows -1)."""
    end = off + _XL_U32
    if end > len(body):
        msg = "BIFF12 record truncated while reading a signed 32-bit field"
        raise ValueError(msg)
    return int.from_bytes(body[off:end], "little", signed=True), end


def _read_lpbytebuf(body: bytes, off: int) -> tuple[bytes, int]:
    """Read an ``LPByteBuf`` ([MS-XLSB] Section 2.5.91): 4-byte LE length prefix, then that many raw bytes."""
    length, off = _read_u32(body, off)
    end = off + length
    if end > len(body):
        msg = "LPByteBuf length runs past the record end"
        raise ValueError(msg)
    return body[off:end], end


def _read_xlnullable(body: bytes, off: int) -> tuple[str, int]:
    """Read an ``XLNullableWideString`` ([MS-XLSB] Section 2.5.167): 4-byte char count (0xFFFFFFFF = NULL), then UTF-16LE chars."""
    count, off = _read_u32(body, off)
    if count == _XL_NULL_STRING:
        return "", off
    end = off + 2 * count
    if end > len(body):
        msg = "XLNullableWideString runs past the record end"
        raise ValueError(msg)
    return body[off:end].decode("utf-16-le"), end


def _read_iso_password_data(body: bytes, off: int, spin_count: int) -> tuple[_Material, int]:
    """Parse the trailing ``IsoPasswordData`` ([MS-XLSB] Section 2.5.80) at ``off`` into ``(_Material, end_offset)``.

    Member order per the spec: ``rgbHash`` (LPByteBuf), ``rgbSalt`` (LPByteBuf),
    ``szAlgName`` (XLNullableWideString). ``spin_count`` is supplied by the caller
    because ``dwSpinCount`` lives at the front of the carrier record, not here.
    """
    rgb_hash, off = _read_lpbytebuf(body, off)
    rgb_salt, off = _read_lpbytebuf(body, off)
    alg_name, off = _read_xlnullable(body, off)
    material = _Material(alg_name, b64encode(rgb_salt).decode("ascii"), b64encode(rgb_hash).decode("ascii"), spin_count)
    return material, off


def _require_end(body: bytes, end: int) -> None:
    """Require that a parse consumed the record exactly (the spec puts IsoPasswordData last).

    A leftover or overrun means the computed ipdPasswordData offset was wrong for
    this record variant; raising here makes the caller fall back to gate-only rather
    than emit a hash line built from misaligned bytes.
    """
    if end != len(body):
        msg = f"IsoPasswordData ended at {end} but the record body is {len(body)} bytes"
        raise ValueError(msg)


def _has_hash(material: _Material) -> bool:
    """Return whether an IsoPasswordData block actually carries a password hash (rgbHash non-empty)."""
    return material.hash_b64 != ""


def _file_sharing_offset(body: bytes) -> int:
    """Compute the ipdPasswordData offset of a BrtFileSharingIso record ([MS-XLSB] Section 2.4.672).

    Prefix: ``dwSpinCount``(4) + ``fReadOnlyRec``(2) + ``stUserName`` (a variable
    XLNullableWideString), so the offset depends on the stored user-name length.
    """
    _, off = _read_xlnullable(body, _FILE_SHARING_PREFIX)
    return off


def _range_offset(body: bytes) -> int:
    """Compute the ipdPasswordData offset of a BrtRangeProtectionIso record ([MS-XLSB] Section 2.4.756).

    Prefix: ``dwSpinCount``(4) + ``sqRfX`` (an UncheckedSqRfX: a signed 4-byte range
    count then that many 16-byte ranges) + ``RangeProtectionTitleSDRel`` (an
    XLWideString title then a 4-byte security-descriptor size and that many bytes).
    """
    off = _XL_U32  # dwSpinCount
    crfx, off = _read_i32(body, off)  # UncheckedSqRfX.crfx (-1 = null, 0 = empty)
    if crfx > 0:
        off += crfx * _UNCHECKED_RFX_SIZE
    title_chars, off = _read_u32(body, off)  # RangeProtectionTitleSDRel.rgchTitle (XLWideString)
    off += 2 * title_chars
    sd_size, off = _read_u32(body, off)  # dwsdRel: security-descriptor byte size
    off += sd_size  # pSDRel (present only when dwsdRel > 0)
    if off > len(body):
        msg = "BrtRangeProtectionIso prefix runs past the record end"
        raise ValueError(msg)
    return off


def _xlsb_parse(record_id: int, body: bytes) -> list[tuple[GateType, _Material]] | None:
    """Parse a protection record body into ``(gate, material)`` blocks, or ``None`` if the record type is detect-only.

    Returns an empty list when the record parses cleanly but carries no password
    hash (options/flags only). Raises ``ValueError``/``IndexError`` on a malformed
    body, which the caller turns into a gate-only finding.
    """
    if record_id == _BRT_SHEET_PROTECTION_ISO:
        return _xlsb_single_block(body, _ISO_OFF_SHEET, GateType.PROTECT_SHEET)
    if record_id == _BRT_CS_PROTECTION_ISO:
        return _xlsb_single_block(body, _ISO_OFF_CS, GateType.PROTECT_SHEET)
    if record_id == _BRT_FILE_SHARING_ISO:
        return _xlsb_single_block(body, _file_sharing_offset(body), GateType.MODIFY)
    if record_id == _BRT_RANGE_PROTECTION_ISO:
        return _xlsb_single_block(body, _range_offset(body), GateType.ALLOW_EDIT_RANGES)
    if record_id == _BRT_BOOK_PROTECTION_ISO:
        return _xlsb_book_blocks(body)
    # BrtRangeProtectionIso14 (FRT-framed) is detected but not parsed.
    return None


def _xlsb_single_block(body: bytes, off: int, gate: GateType) -> list[tuple[GateType, _Material]]:
    """Parse a record carrying one IsoPasswordData (dwSpinCount at the front, password data at ``off``)."""
    spin_count, _ = _read_u32(body, 0)
    material, end = _read_iso_password_data(body, off, spin_count)
    _require_end(body, end)
    return [(gate, material)] if _has_hash(material) else []


def _xlsb_book_blocks(body: bytes) -> list[tuple[GateType, _Material]]:
    """Parse BrtBookProtectionIso ([MS-XLSB] Section 2.4.309): a structure/windows block then a revisions block.

    The record holds two IsoPasswordData structures back to back -- the workbook
    structure/windows password and the shared-revisions password -- each with its
    own spin count at the front (``dwBookSpinCount``/``dwRevSpinCount``).
    """
    book_spin, _ = _read_u32(body, 0)
    rev_spin, _ = _read_u32(body, _XL_U32)
    book_material, off = _read_iso_password_data(body, _ISO_OFF_BOOK, book_spin)
    rev_material, off = _read_iso_password_data(body, off, rev_spin)
    _require_end(body, off)
    blocks: list[tuple[GateType, _Material]] = []
    if _has_hash(book_material):
        blocks.append((GateType.PROTECT_WORKBOOK, book_material))
    if _has_hash(rev_material):
        blocks.append((GateType.SHARED_REVISIONS, rev_material))
    return blocks


def _xlsb_findings(record_id: int, entry: tuple[GateType, str], body: bytes, where: str) -> list[_Finding]:
    """Turn one protection record into findings: a hash line per password block, else a gate-only finding."""
    gate, record_name = entry
    loc = f"{where} ({record_name})"
    try:
        blocks = _xlsb_parse(record_id, body)
    except (ValueError, IndexError):
        # Unexpected/truncated body: keep the detected gate, emit no hash line.
        return [_Finding(gate, RecoveryClass.STRIP, loc, note=_NOTE_XLSB)]
    if blocks is None:
        # Record type we detect but do not parse (BrtRangeProtectionIso14).
        return [_Finding(gate, RecoveryClass.STRIP, loc, note=_NOTE_XLSB)]
    if not blocks:
        # Parsed cleanly but no password hash present (flags/options only) -- bare gate.
        return [_Finding(gate, RecoveryClass.STRIP, loc)]
    return [_protection_finding(block_gate, loc, material) for block_gate, material in blocks]


def _scan_biff12(data: bytes, where: str) -> list[_Finding]:
    """Detect ISO protection records in a ``.xlsb`` binary part and extract their hash lines."""
    findings: list[_Finding] = []
    for record_id, body in _biff12_records(data):
        entry = _XLSB_RECORD_GATES.get(record_id)
        if entry is not None:
            findings.extend(_xlsb_findings(record_id, entry, body, where))
    return findings


# --- VBA project lock ([MS-OVBA]) ---


def _ini_value(text: str, key: str) -> str | None:
    """Read a quoted ``KEY="value"`` line from the INI-style PROJECT stream, or ``None``."""
    match = re.search(r"(?m)^" + re.escape(key) + r'\s*=\s*"([^"]*)"', text)
    return str(match.group(1)) if match else None


def _vba_locked(cmg: str | None, dpb: str | None) -> bool:
    """Return whether the VBA project is protected.

    Protected when the CMG ProjectProtectionState bitfield ([MS-OVBA] Section 2.3.1.15)
    is non-zero, or when DPB holds anything other than the no-password sentinel
    ([MS-OVBA] Section 2.3.1.16). An unprotected project has CMG = 0 and DPB = 0x00.
    """
    if cmg:
        try:
            if any(vba.decode_data_encryption(cmg)):
                return True
        except (ValueError, IndexError):
            return False
    if dpb:
        try:
            if vba.decode_data_encryption(dpb) != _DPB_SENTINEL:
                return True
        except (ValueError, IndexError):
            return False
    return False


def _project_stream(data: bytes) -> str | None:
    """Open a ``vbaProject.bin`` OLE blob and return its PROJECT stream text, or ``None``."""
    try:
        ole = olefile.OleFileIO(io.BytesIO(data))
    except (OSError, ValueError, struct.error):
        return None
    try:
        if not ole.exists("PROJECT"):
            return None
        return str(ole.openstream("PROJECT").read().decode("latin-1"))
    except (OSError, ValueError, KeyError, struct.error):
        return None
    finally:
        ole.close()


def _scan_vba(data: bytes, where: str) -> list[_Finding]:
    """Enumerate the macro project-lock gate (and its 110 verifier line, when present)."""
    text = _project_stream(data)
    if text is None:
        return []
    cmg = _ini_value(text, "CMG")
    dpb = _ini_value(text, "DPB")
    if not _vba_locked(cmg, dpb):
        return []
    line: str | None = None
    if dpb:
        try:
            line = vba.extract_vba_hash(dpb)
        except (ValueError, IndexError):
            line = None
    if line is not None:
        opt = unified_vba_line(dpb) if dpb else None
        return [_Finding(GateType.VBA_PROJECT, RecoveryClass.STRIP, where, HashScheme.VBA_SHA1, _MODE_VBA, line, _NOTE_VBA_HASH, opt_hash_line=opt)]
    return [_Finding(GateType.VBA_PROJECT, RecoveryClass.STRIP, where, note=_NOTE_VBA_OTHER)]


# --- Package-level scan orchestration ---


def _reject_zip_bomb(package: zipfile.ZipFile) -> None:
    """Refuse an archive whose members inflate past a sane cap (a zip bomb).

    Sums the central-directory ``file_size`` fields only (no decompression), so a
    hostile compression ratio is caught before any member is read into memory.
    Raised as ``ValueError`` so the read-only CLI paths degrade with a note.
    """
    cap = 1024 * 1024 * 1024  # 1 GiB total uncompressed
    total = sum(member.file_size for member in package.infolist())
    if total > cap:
        msg = f"archive declares {total} uncompressed bytes, over the {cap}-byte cap; refusing (possible zip bomb)"
        raise ValueError(msg)


def _scan(path: Path) -> list[_Finding]:
    """Walk every relevant part of the OPC package and collect its gate findings."""
    findings: list[_Finding] = []
    try:
        with zipfile.ZipFile(path) as package:
            _reject_zip_bomb(package)
            names = package.namelist()
            name_set = set(names)
            if "xl/workbook.xml" in name_set:
                findings += _scan_workbook(package.read("xl/workbook.xml"))
            if "ppt/presentation.xml" in name_set:
                findings += _scan_powerpoint(package.read("ppt/presentation.xml"))
            if "word/settings.xml" in name_set:
                findings += _scan_word(package.read("word/settings.xml"))
            for name in names:
                findings += _scan_part(package, name)
            if any(name.startswith("_xmlsignatures/") for name in names):
                findings.append(_Finding(GateType.SIGNATURE, RecoveryClass.NONE, "_xmlsignatures/", note=_NOTE_SIGNATURE))
    except (zipfile.BadZipFile, OSError):
        logger.debug("scan: bad/corrupt ZIP")
        return []
    logger.debug("scan: %d findings from %d members", len(findings), len(names))
    return findings


def _scan_part(package: zipfile.ZipFile, name: str) -> list[_Finding]:
    """Dispatch a single member to the right scanner (worksheet / chartsheet / .xlsb binary / VBA)."""
    base = name.rsplit("/", 1)[-1].lower()
    if base == "vbaproject.bin":
        return _scan_vba(package.read(name), name)
    if name.startswith(("xl/worksheets/", "xl/chartsheets/")):
        if name.endswith(".xml"):
            return _scan_worksheet(package.read(name), name)
        if name.endswith(".bin"):
            return _scan_biff12(package.read(name), name)
    if name == "xl/workbook.bin":
        return _scan_biff12(package.read(name), name)
    return []


# --- Bypass: strip every protection element on a fresh copy of the package ---


def _remove_one(xml: str, local_name: str) -> str:
    """Delete every ``<local_name .../>`` (or paired ``<local_name>...</local_name>``) element."""
    prefix = r"(?:[\w.\-]+:)?"
    escaped = re.escape(local_name)
    # Paired form first (element with children, e.g. <protectedRanges>...); the
    # (?<!/) guard keeps this from swallowing a self-closing tag.
    paired = re.compile(r"<" + prefix + escaped + r"\b[^>]*?(?<!/)>.*?</" + prefix + escaped + r">", re.DOTALL)
    xml = paired.sub("", xml)
    self_closing = re.compile(r"<" + prefix + escaped + r"\b[^>]*/>", re.DOTALL)
    return self_closing.sub("", xml)


def _remove_elements(xml: str, local_names: tuple[str, ...]) -> str:
    """Delete each named element from ``xml`` in turn."""
    for local_name in local_names:
        xml = _remove_one(xml, local_name)
    return xml


def _unprotected_project_lines() -> tuple[str, str, str]:
    """Return minimal-length unprotected ``CMG``/``DPB``/``GC`` values ([MS-OVBA] Section 2.3.1.15-17)."""
    proj_key = vba.project_key(_ALL_ZERO_CLSID)  # 0xAC, the hash-case ProjKey
    cmg = vba.encode_data_encryption(b"\x00\x00\x00\x00", _VBA_MIN_SEED, proj_key)  # no protection bits set
    dpb = vba.encode_data_encryption(_DPB_SENTINEL, _VBA_MIN_SEED, proj_key)  # no-password sentinel
    gc = vba.encode_data_encryption(b"\xff", _VBA_MIN_SEED, proj_key)  # project visible
    return cmg, dpb, gc


def _unprotected_project_text(original: bytes) -> bytes | None:
    """Rewrite a locked PROJECT stream's protection triple to the cleared state, or ``None`` if already open.

    Returns the new stream bytes with the ``CMG``/``DPB``/``GC`` values replaced in
    place. The minimal-length replacements guarantee the result never grows, so the
    caller can pad it back to the CFB stream's fixed size.
    """
    text = original.decode("latin-1")
    if not _vba_locked(_ini_value(text, "CMG"), _ini_value(text, "DPB")):
        return None
    cmg, dpb, gc = _unprotected_project_lines()
    replacement = {"CMG": cmg, "DPB": dpb, "GC": gc}

    def _sub(match: re.Match[str]) -> str:
        key = match.group(1)
        return f'{key}="{replacement[key]}"'

    rewritten = re.sub(r'(?m)^(CMG|DPB|GC)\s*=\s*"[^"]*"', _sub, text)
    return rewritten.encode("latin-1")


def _rewrite_vba_project(data: bytes) -> bytes:
    """Return the ``vbaProject.bin`` blob with its project lock cleared, unchanged if it was never locked.

    The PROJECT stream is rewritten in place inside the CFB. Its size must stay
    constant (olefile only overwrites same-size streams), so the shorter cleared
    triple is padded back to the original length with trailing spaces -- harmless
    whitespace the INI parser ignores.
    """
    buffer = io.BytesIO(data)
    try:
        ole = olefile.OleFileIO(buffer, write_mode=True)
    except (OSError, ValueError, struct.error):
        return data
    result = data
    try:
        if ole.exists("PROJECT"):
            original = ole.openstream("PROJECT").read()
            cleared = _unprotected_project_text(original)
            if cleared is not None and len(cleared) <= len(original):
                padded = cleared + b" " * (len(original) - len(cleared))
                ole.write_stream("PROJECT", padded)
                result = buffer.getvalue()
    except (OSError, ValueError, KeyError, struct.error):
        result = data
    finally:
        ole.close()
    return result


# A package ``_rels/.rels`` digital-signature-origin relationship: a self-closing
# ``<Relationship>`` whose Type URI is the OPC digital-signature origin. Matched on
# raw bytes (the .rels part is ASCII) so encoding never gets in the way. ``\b`` after
# "Relationship" keeps it from matching the ``<Relationships>`` container element.
_SIGNATURE_ORIGIN_REL: Final = re.compile(rb"<Relationship\b[^>]*digital-signature[^>]*/>")


def _drop_signature_origin_rel(data: bytes) -> bytes:
    """Remove the digital-signature-origin relationship from a package ``_rels/.rels`` part.

    Dropping the ``_xmlsignatures/`` parts alone would leave a dangling origin
    relationship pointing at a now-absent part; removing it too makes the package
    validly signature-free (OPC / [ECMA-376] Part 2, digital-signature origin
    relationship). Only that one relationship is removed -- every other package
    relationship is preserved byte-for-byte.
    """
    return _SIGNATURE_ORIGIN_REL.sub(b"", data)


def _strip_member(name: str, data: bytes) -> bytes:
    """Return ``data`` for member ``name`` with any protection element removed (else unchanged)."""
    base = name.rsplit("/", 1)[-1].lower()
    if base == "vbaproject.bin":
        return _rewrite_vba_project(data)
    xml = _decode(data)
    if xml is None:
        return data
    if name == "xl/workbook.xml":
        stripped = _remove_elements(xml, ("workbookProtection", "fileSharing"))
    elif name.startswith(("xl/worksheets/", "xl/chartsheets/")) and name.endswith(".xml"):
        stripped = _remove_elements(xml, ("sheetProtection", "protectedRanges", "protectedRange"))
    elif name == "word/settings.xml":
        stripped = _remove_elements(xml, ("writeProtection", "documentProtection"))
    elif name == "ppt/presentation.xml":
        stripped = _remove_elements(xml, ("modifyVerifier",))
    else:
        return data
    return stripped.encode("utf-8")


class OoxmlHandler(FormatHandler):
    """Handler for the OPC/ZIP (Office Open XML) container.

    Owns the *unencrypted* package: enumerates the inner permission gates (sheet /
    workbook / document / range / revisions protection, write-reservation, VBA lock,
    signatures), extracts the crackable ISO SHA-512 (25300) and VBA (110) lines, and
    strips every non-encrypting gate onto a fresh copy. Document-open encryption is
    never seen here (an encrypted OOXML file is physically OLE/CFB).
    """

    container = ContainerKind.OOXML_ZIP

    @override
    def is_encrypted(self, path: Path) -> bool:
        """Report ``False`` unconditionally: an OPC/ZIP package carries no document-open ciphertext.

        A modern Office file with an open password is re-wrapped as OLE/CFB and is
        classified/handled by the OLE handler, so nothing this handler ever sees is
        document-open encrypted.
        """
        _ = path
        return False

    @override
    def gates(self, path: Path) -> list[Gate]:
        """Enumerate every permission/password gate present in the package."""
        findings = _scan(path)
        logger.debug("gates: %d findings from scan", len(findings))
        return [Gate(finding.gate, finding.recovery, finding.scheme, finding.hashcat_mode, finding.where, finding.note) for finding in findings]

    @override
    def extract(self, path: Path) -> list[ExtractedHash]:
        """Return the crackable hash lines from every protection carrier.

        Emits the ISO SHA-512 (25300) verifier when the shape fits, otherwise the
        generalized ``$office-protect$`` line (SHA-1 / non-100000 spin / non-16-byte
        salt); the legacy ``$office-protect$*...*crypt*`` line; the ``.xlsb`` binary records'
        lines; and the VBA (110) line. Lines with no shipped hashcat mode carry
        ``hashcat_mode = None``. A carrier that exposes no password material (options
        only) keeps its gate but emits no line.
        """
        findings = _scan(path)
        hashes = [ExtractedHash(finding.scheme, finding.hashcat_mode, finding.hash_line, finding.gate, opt_value=finding.opt_hash_line) for finding in findings if finding.hash_line is not None and finding.scheme is not None]
        logger.debug("extract: %d hash lines from %d findings", len(hashes), len(findings))
        return hashes

    @override
    def bypass(self, path: Path, out: Path, *, remove_signatures: bool = False) -> int:
        """Write a NEW package to ``out`` with every non-encrypting gate stripped.

        The input is opened read-only and never modified. Each member is copied
        through with its original metadata; the protection-bearing parts
        (worksheet/workbook/settings/presentation XML and ``vbaProject.bin``) are
        rewritten with their protection removed, everything else passes untouched.

        When ``remove_signatures`` is set, the ``_xmlsignatures/`` parts are dropped
        entirely and the digital-signature-origin relationship is removed from
        ``_rels/.rels`` -- the package comes out validly unsigned. This is opt-in and
        destructive: it invalidates the signature and cannot be undone.

        Note: ``.xlsb`` binary protection records are detected but not rewritten
        (their parts pass through unchanged) -- BIFF12 record surgery is a GAP.
        """
        rewritten = 0
        with zipfile.ZipFile(path) as source, zipfile.ZipFile(out, "w") as target:
            _reject_zip_bomb(source)
            for info in source.infolist():
                if remove_signatures and info.filename.startswith("_xmlsignatures/"):
                    logger.debug("bypass: dropping signature part %s", info.filename)
                    continue
                raw = source.read(info.filename)
                stripped = _strip_member(info.filename, raw)
                if remove_signatures and info.filename == "_rels/.rels":
                    stripped = _drop_signature_origin_rel(stripped)
                if stripped != raw:
                    logger.debug("bypass: stripped protection from %s", info.filename)
                    rewritten += 1
                target.writestr(info, stripped)
        logger.debug("bypass: %d members rewritten to %s", rewritten, out)
        return rewritten

    @override
    def decrypt(self, path: Path, out: Path, password: str) -> None:
        """Not applicable: an OPC/ZIP package is never document-open encrypted.

        Encrypted Office files are physically OLE/CFB and decrypted by the OLE
        handler; this raises rather than pretend to decrypt a plaintext package.
        """
        _ = (path, out, password)
        msg = "OOXML/OPC packages are never document-open encrypted; an encrypted Office file is physically OLE/CFB (use the OLE handler)"
        raise ValueError(msg)
