# SPDX-License-Identifier: Apache-2.0
"""Core data models: container/format/gate enumerations and result records.

These types are the shared vocabulary between the format handlers (which detect
gates and produce hashes) and the CLI (which renders them). Each enumeration
maps to a concept documented in the ``../office`` analysis corpus.

Import rules: this module imports only from the standard library.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Final


class Status(StrEnum):
    """CLI output status — tells the user what a gate means for THEM.

    These map directly to the ``status:scheme`` output format documented in
    ``docs/design/cli-output.md``. Each gate is assigned a status based on its
    recovery class, giving the user an immediate, actionable classification.
    """

    ENCRYPTED = "encrypted"  # you need the password to read this file
    REMOVABLE = "removable"  # this gate can be removed without the password
    TRIVIAL = "trivial"  # instantly reversible, no password needed
    INFO = "info"  # something to know about, not a password gate
    BLOCKED = "blocked"  # not recoverable (needs certificate or server key)
    OPEN = "open"  # no protection at all


class Product(StrEnum):
    """The Office application that created/owns the file, detected from internal streams.

    Distinct from ContainerKind: Word .doc and Excel .xls are both OLE_CFB, but
    they are different products with different gate sets. Detection reads internal
    streams (WordDocument, Workbook, PowerPoint Document) or OPC content types.
    """

    WORD = "Word"
    EXCEL = "Excel"
    POWERPOINT = "PowerPoint"
    ONENOTE = "OneNote"
    OUTLOOK = "Outlook"
    ACCESS = "Access"
    VISIO = "Visio"
    PROJECT = "Project"
    PUBLISHER = "Publisher"
    INFOPATH = "InfoPath"
    OPENDOCUMENT = "OpenDocument"
    UNKNOWN = "Unknown"


class ContainerKind(StrEnum):
    """The physical container format a file uses on disk, independent of the Office application.

    Detection keys off magic bytes at offset 0 (or 0x04 for Access), never the file
    extension -- an encrypted ``.docx`` is physically OLE/CFB, not a ZIP.
    """

    OLE_CFB = "ole-cfb"  # [MS-CFB] compound file: legacy .doc/.xls/.ppt + encrypted-OOXML wrapper
    OOXML_ZIP = "ooxml-zip"  # OPC/ZIP package: .docx/.xlsx/.pptx/.xlsb
    ODF_ZIP = "odf-zip"  # OpenDocument ZIP: .odt/.ods/.odp
    ONENOTE = "onenote"  # [MS-ONESTORE] revision store: .one/.onetoc2
    PST = "pst"  # [MS-PST] node database: .pst/.ost
    ACCESS = "access"  # Jet/ACE database: .mdb/.accdb (out-of-corpus)
    ACCESS_MDW = "access-mdw"  # Jet workgroup: .mdw/.mda (User-Level Security)
    UNKNOWN = "unknown"


class GateType(StrEnum):
    """A distinct password/permission mechanism a file can carry."""

    OPEN = "open"  # document-open encryption password (the only real crack target)
    MODIFY = "modify"  # modify / write-reservation password
    PROTECT_SHEET = "protect-sheet"  # worksheet protection
    PROTECT_WORKBOOK = "protect-workbook"  # workbook structure/windows protection
    RESTRICT_EDIT = "restrict-edit"  # Word document / editing-restriction protection
    ALLOW_EDIT_RANGES = "allow-edit-ranges"  # Excel range passwords
    SHARED_REVISIONS = "shared-revisions"  # shared-workbook revision-history lock
    SECTION = "section"  # ODF text-section (.odt) / table (.ods) protection
    VBA_PROJECT = "vba-project"  # VBA macro project lock
    SIGNATURE = "signature"  # digital signature (not password-recoverable)
    IRM = "irm"  # information rights management (not password-recoverable)
    MAIL_BODY = "mail-body"  # Outlook NDB body cipher (keyless obfuscation)


class RecoveryClass(StrEnum):
    """The fastest way a gate is defeated.

    This is the recovery-action vocabulary from ``docs/reference/gates.md``,
    ordered cheapest-first -- the ``unlock`` command walks it top to bottom. Only
    ``KEYSPACE`` / ``CRACK`` cost real work; every other action is free.
    """

    DEFAULT = "default"  # open with a built-in fixed password Office set automatically
    READ = "read"  # the password is stored as plain text -- just read it out
    DECODE = "decode"  # reverse a keyless scramble; recover the content with no password
    BYPASS = "bypass"  # flip the protection flag off (on -> off); content was never encrypted
    STRIP = "strip"  # delete the whole record/element that carries the protection
    COLLIDE = "collide"  # tiny verifier (16/32-bit / CRC-32) -- mint any satisfying password
    DECRYPT = "decrypt"  # derive the key from a known password/default and decrypt real ciphertext
    KEYSPACE = "keyspace"  # brute the small cipher key directly (2^40), faster than the password
    CRACK = "crack"  # real encryption: extract the hash and hand it to hashcat
    NONE = "none"  # no password secret exists (signatures, IRM/RMS, enterprise EDP)


class HashScheme(StrEnum):
    """The hash-line format a gate extracts to (hashcat/John naming).

    Each member maps to a ``$prefix$`` signature and, when one exists, a hashcat ``-m``
    mode. Members below the ``---`` comment have no shipped hashcat mode -- they are
    extractable verifiers the toolkit surfaces beyond what office2john covers.
    """

    OFFICE_2007 = "office-2007"  # $office$*2007 -> hashcat 9400
    OFFICE_2010 = "office-2010"  # $office$*2010 -> hashcat 9500
    OFFICE_2013 = "office-2013"  # $office$*2013 -> hashcat 9600 (also OneNote, .accdb 2010+)
    OLDOFFICE_RC4_MD5 = "oldoffice-rc4-md5"  # $oldoffice$0/1 -> hashcat 9700
    OLDOFFICE_RC4_SHA1 = "oldoffice-rc4-sha1"  # $oldoffice$3/4 -> hashcat 9800
    OFFICE_SHEETPROT = "office-sheetprot"  # $office$2016 -> hashcat 25300
    ODF = "odf"  # $odf$ -> hashcat 18400/18600
    VBA_SHA1 = "vba-sha1"  # sha1($pass.$salt) -> hashcat 110
    # --- no hashcat mode (custom format) ---
    MSISAM = "msisam"  # $msisam$ (MD5/SHA-1 + RC4, Money 2002+) -- no hashcat mode


# Friendly, human-facing gate names (the "simple name" column of
# ``docs/reference/gates.md``). The CLI renders these; the ``GateType`` value is
# the stable machine token. Single source of truth so the docs and ``opt info``
# never drift apart.
GATE_DISPLAY_NAMES: Final[dict[GateType, str]] = {
    GateType.OPEN: "Open password",
    GateType.MODIFY: "Modify password",
    GateType.PROTECT_SHEET: "Sheet protection",
    GateType.PROTECT_WORKBOOK: "Workbook protection",
    GateType.RESTRICT_EDIT: "Restrict editing",
    GateType.ALLOW_EDIT_RANGES: "Range passwords",
    GateType.SHARED_REVISIONS: "Shared-revisions lock",
    GateType.SECTION: "Section protection",
    GateType.VBA_PROJECT: "Macro project lock (VBA)",
    GateType.SIGNATURE: "Digital signature",
    GateType.IRM: "Rights management (IRM)",
    GateType.MAIL_BODY: "Mail body cipher",
}


@dataclass(frozen=True)
class Gate:
    """A single permission/password gate discovered in a file.

    Produced by a format handler's ``gates()`` method and consumed by the CLI to render
    the triage. The ``recovery`` field drives the ``unlock`` command's cheapest-first
    action order, and ``scheme`` / ``hashcat_mode`` drive ``extract``.
    """

    gate: GateType
    recovery: RecoveryClass
    scheme: HashScheme | None = None  # the hash scheme, when the gate is a crackable hash
    hashcat_mode: int | None = None  # the hashcat -m mode, when one exists
    where: str = ""  # human-readable location (stream/record/XML element)
    note: str = ""  # extra context (e.g. "try VelvetSweatshop first")

    @property
    def display_name(self) -> str:
        """The friendly gate name from ``docs/reference/gates.md`` (for CLI output)."""
        return GATE_DISPLAY_NAMES.get(self.gate, self.gate.value)


@dataclass(frozen=True)
class ExtractedHash:
    """A crackable hash line pulled from a file, ready for hashcat/John.

    Two line representations coexist: ``value`` is the hashcat-compatible line
    (``$office$*2013*...`` / ``$oldoffice$...`` / ``$odf$*0*0*...``) emitted by
    default; ``opt_value`` is the self-describing 4-family line (``$office$*sha512*
    aes256*cbc*...`` / ``$protect$*...`` / ``$odf$*sha256*pbkdf2*...`` / ``$vba$*...``)
    emitted by ``--format opt``. The ``opt_value`` is ``None`` for verifiers that are
    not slow hashes (XOR, PST CRC) — those are handled by ``opt decode`` /
    ``opt collide`` instead.
    """

    scheme: HashScheme
    hashcat_mode: int | None
    value: str  # hashcat-compatible line (``$office$*2013*...`` etc.)
    gate: GateType = GateType.OPEN
    opt_value: str | None = None  # self-describing line (``$office$*sha512*aes256*cbc*...`` etc.)


@dataclass(frozen=True)
class DetectResult:
    """The outcome of triaging a single file.

    Returned by :func:`~office_password_toolkit.detect.detect` and printed by the
    CLI ``info`` command. ``encrypted`` reflects document-open encryption only (keyed
    ciphertext); protection-only files report ``False`` here and surface their gates
    through the handler's ``gates()`` method instead.
    """

    path: str
    container: ContainerKind
    extension: str
    encrypted: bool
    gates: list[Gate] = field(default_factory=list)
    product: Product = Product.UNKNOWN


# --- Status/scheme mapping for CLI output -----------------------------------

# Maps RecoveryClass → Status for the ``status:scheme`` CLI output format.
_RECOVERY_TO_STATUS: Final[dict[RecoveryClass, Status]] = {
    RecoveryClass.DEFAULT: Status.TRIVIAL,
    RecoveryClass.READ: Status.TRIVIAL,
    RecoveryClass.DECODE: Status.TRIVIAL,
    RecoveryClass.BYPASS: Status.REMOVABLE,
    RecoveryClass.STRIP: Status.REMOVABLE,
    RecoveryClass.COLLIDE: Status.REMOVABLE,
    RecoveryClass.DECRYPT: Status.ENCRYPTED,
    RecoveryClass.KEYSPACE: Status.ENCRYPTED,
    RecoveryClass.CRACK: Status.ENCRYPTED,
    RecoveryClass.NONE: Status.BLOCKED,
}

# Maps GateType → base scheme name for gates that aren't hash-based.
_GATE_TO_SCHEME: Final[dict[GateType, str]] = {
    GateType.SIGNATURE: "signed",
    GateType.IRM: "rights-managed",
    GateType.MAIL_BODY: "pst-encoded",
}

# Maps HashScheme → short scheme name for the CLI status:scheme output.
_SCHEME_TO_TAG: Final[dict[HashScheme, str]] = {
    HashScheme.OFFICE_2007: "standard",
    HashScheme.OFFICE_2010: "agile-sha1",
    HashScheme.OFFICE_2013: "agile-sha512",
    HashScheme.OLDOFFICE_RC4_MD5: "rc4-md5",
    HashScheme.OLDOFFICE_RC4_SHA1: "rc4-sha1",
    HashScheme.OFFICE_SHEETPROT: "iso-sha512",
    HashScheme.ODF: "odf",
    HashScheme.VBA_SHA1: "macros",
}

# Maps GateType → short scheme name for protection gates without a HashScheme.
_GATE_SCHEME_NAMES: Final[dict[GateType, str]] = {
    GateType.PROTECT_SHEET: "sheets",
    GateType.PROTECT_WORKBOOK: "workbook",
    GateType.RESTRICT_EDIT: "restricted",
    GateType.ALLOW_EDIT_RANGES: "ranges",
    GateType.SHARED_REVISIONS: "revisions",
    GateType.MODIFY: "write",
    GateType.SECTION: "section",
}


def gate_status(gate: Gate) -> Status:
    """Map a gate to its CLI output status (encrypted/removable/trivial/info/blocked)."""
    # IRM and signatures are always info/blocked regardless of recovery class.
    if gate.gate is GateType.IRM:
        return Status.BLOCKED
    if gate.gate in (GateType.SIGNATURE, GateType.MAIL_BODY):
        return Status.INFO
    return _RECOVERY_TO_STATUS.get(gate.recovery, Status.INFO)


def gate_scheme_tag(gate: Gate) -> str:
    """Map a gate to its CLI output scheme tag (e.g., 'agile-sha512', 'sheets', 'signed')."""
    # Non-password gates have fixed scheme names.
    if gate.gate in _GATE_TO_SCHEME:
        return _GATE_TO_SCHEME[gate.gate]
    # Hash-based gates use the HashScheme mapping.
    if gate.scheme is not None and gate.scheme in _SCHEME_TO_TAG:
        return _SCHEME_TO_TAG[gate.scheme]
    # Protection gates without a specific hash scheme use the gate type name.
    if gate.gate in _GATE_SCHEME_NAMES:
        return _GATE_SCHEME_NAMES[gate.gate]
    # Fallback: the gate type value itself.
    return gate.gate.value
