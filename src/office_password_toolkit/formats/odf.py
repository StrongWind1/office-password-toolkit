# SPDX-License-Identifier: Apache-2.0
"""OpenDocument handler -- ``.odt`` / ``.ods`` / ``.odp`` (ODF-ZIP container).

An ODF file is a plain PKZIP archive (stdlib :mod:`zipfile`), never OLE/CFB and
never an OPC package. Its crypto parameters are not a binary header: they live as
Base64 XML attributes in ``META-INF/manifest.xml`` (OASIS *OpenDocument v1.2
Part 3: Packages* Section 3.4 "Encryption"; the ODF 1.1 Blowfish profile predates
that split -- ODF 1.1 spec Section 17.3). Encryption is **per stream**: each
significant member (``content.xml``, ``styles.xml`` ...) is raw-DEFLATE
compressed then individually encrypted, while the ZIP directory, ``mimetype``,
member names, and the manifest itself stay in cleartext. One password gates the
whole package -- there is no separate modify/macro password.

This handler covers, per ``analysis/file-formats/opendocument.md`` and
``analysis/password-algorithms/odf-encryption.md``:

* **Open password** (document-open encryption) -- ODF 1.1 (Blowfish CFB, hashcat
  18600), ODF 1.2 (AES-256-CBC, hashcat 18400), and ODF 1.3 "Wholesome Encryption"
  (Argon2id + AES-256-GCM, LibreOffice 24.8+). ODF 1.3 has no hashcat / John mode
  (a memory-hard KDF plus AEAD tag is a GPU gap, :func:`crypto.odf.is_gap`), but it
  is fully decryptable with a known password and :meth:`extract` emits the extended
  ``$odf$*2*...`` line (hashcat_mode ``None``) rather than skipping it.
* **Body protection** (not encryption) -- ``<table:table table:protected="true">``
  in a spreadsheet body -> sheet protection, and ``<text:section
  text:protected="true">`` in a text body -> section protection. Both are a free
  STRIP: the content is plaintext and only a flag enforces the lock.

All crypto lives in :mod:`office_password_toolkit.crypto.odf`; this file is the
container glue -- zip reading, gate enumeration, and the mimetype-first repackage
that :meth:`OdfHandler.decrypt` / :meth:`OdfHandler.bypass` write.
"""

from __future__ import annotations

import dataclasses
import logging
import re
import xml.parsers.expat
import zipfile
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

from typing_extensions import override

from office_password_toolkit.crypto import odf
from office_password_toolkit.formats.base import FormatHandler
from office_password_toolkit.models import ContainerKind, ExtractedHash, Gate, GateType, HashScheme, RecoveryClass

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)

# --- Container constants ---

# Fixed member names inside every ODF-ZIP (OpenDocument Part 3 Section 3). The
# manifest is always cleartext; ``mimetype`` must be the first entry and stored
# uncompressed or the package is invalid.
_MANIFEST_PATH: Final = "META-INF/manifest.xml"
_MIMETYPE_NAME: Final = "mimetype"
_CONTENT_NAME: Final = "content.xml"

# hashcat modes for the two supported ODF profiles ([odf-encryption.md] Section 2).
_MODE_ODF12_AES: Final = 18400  # ODF 1.2: SHA-256 start key + PBKDF2 x100000 + AES-256-CBC
_MODE_ODF11_BLOWFISH: Final = 18600  # ODF 1.1: SHA-1 start key + PBKDF2 x1024 + Blowfish CFB

# Cipher-URI markers used to map an entry to its hashcat mode. The OASIS schema
# lets cipher vary independently, so we key off the meaningful token in the URI
# rather than an exact string (matches crypto.odf's own classification).
_CIPHER_AES_CBC: Final = "aes256-cbc"
_CIPHER_BLOWFISH: Final = "blowfish"

# Exceptions that a malformed-but-well-named package can raise while we read and
# parse it. Detection/enumeration must never crash on bad input, so every public
# method funnels its zip/XML reads through these. ``binascii.Error`` (bad Base64
# in the manifest) is a ``ValueError`` subclass, hence covered by ``ValueError``.
_PARSE_ERRORS = (OSError, zipfile.BadZipFile, KeyError, ValueError, xml.parsers.expat.ExpatError)

# --- Body-protection strip patterns ([opendocument.md] body-protection table) ---
#
# Sheet/section protection is enforced only by a flag plus a Base64 digest that
# guards nothing (the body is plaintext). BYPASS = set the flag false and delete
# the protection-key attributes. Applied to the raw ``content.xml`` bytes; ODF
# writers always double-quote attribute values, so the patterns target that form.
_PROTECTED_TRUE = re.compile(rb'((?:table|text):protected=")true(")')
_PROTECTION_KEY = re.compile(rb'\s+(?:table|text):protection-key(?:-digest-algorithm(?:-2)?)?="[^"]*"')


@dataclass(frozen=True)
class _RepackagePlan:
    """Inputs for a mimetype-first ODF rebuild (bundled to keep call sites small).

    :attr:`replacements` maps a member name to the bytes that replace its stored
    content (decrypted plaintext, or a rewritten ``content.xml``); every other
    member is copied verbatim. :attr:`manifest_override`, when set, replaces
    ``META-INF/manifest.xml`` (used by :meth:`OdfHandler.decrypt` to drop the
    ``<encryption-data>`` blocks).
    """

    replacements: dict[str, bytes]
    manifest_override: bytes | None = None


# --- Zip / manifest helpers ---


def _reject_zip_bomb(archive: zipfile.ZipFile) -> None:
    """Refuse an ODF-ZIP whose members inflate past a sane cap (a zip bomb).

    Sums the central-directory ``file_size`` fields only (no decompression), so a
    hostile compression ratio is caught before any member is read into memory.
    """
    cap = 1024 * 1024 * 1024  # 1 GiB total uncompressed
    total = sum(member.file_size for member in archive.infolist())
    if total > cap:
        msg = f"archive declares {total} uncompressed bytes, over the {cap}-byte cap; refusing (possible zip bomb)"
        raise ValueError(msg)


def _read_member(path: Path, name: str) -> bytes | None:
    """Return the stored bytes of ``name`` inside the ODF-ZIP, or None if absent.

    Never raises on a malformed or missing package -- callers treat None as "not
    present", which for the manifest means "not an ODF file / not encrypted".
    """
    try:
        with zipfile.ZipFile(path) as archive:
            _reject_zip_bomb(archive)
            return archive.read(name)
    except _PARSE_ERRORS:
        return None


def _load_entries(path: Path) -> list[odf.OdfEntry]:
    """Parse the manifest into one :class:`~crypto.odf.OdfEntry` per encrypted member.

    Returns ``[]`` for an unencrypted package, a non-ODF file, or a malformed
    manifest -- the "no open-encryption" answer in every case.
    """
    manifest = _read_member(path, _MANIFEST_PATH)
    if manifest is None:
        return []
    try:
        return odf.parse_manifest(manifest)
    except _PARSE_ERRORS:
        return []


def _primary_entry(entries: list[odf.OdfEntry]) -> odf.OdfEntry:
    """Return the entry a cracker keys off -- ``content.xml`` if present, else the first.

    Every member of a package shares one profile/password, but odf2john and
    hashcat pin on ``content.xml``; we mirror that so the OPEN gate's mode matches.
    """
    for entry in entries:
        if entry.full_path in (_CONTENT_NAME, "/" + _CONTENT_NAME):
            return entry
    return entries[0]


def _hashcat_mode(entry: odf.OdfEntry) -> int | None:
    """Map an encrypted member to its hashcat mode, or None for the ODF 1.3 GAP.

    18400 for AES-256-CBC (ODF 1.2), 18600 for Blowfish CFB (ODF 1.1); Argon2id /
    AES-GCM members return None (no mode exists -- see :func:`crypto.odf.is_gap`).
    """
    if odf.is_gap(entry):
        return None
    cipher = entry.cipher.lower()
    if _CIPHER_AES_CBC in cipher:
        return _MODE_ODF12_AES
    if _CIPHER_BLOWFISH in cipher:
        return _MODE_ODF11_BLOWFISH
    return None


def _profile_note(mode: int | None) -> str:
    """Human-readable profile label for an OPEN-gate note."""
    if mode == _MODE_ODF12_AES:
        return "ODF 1.2 profile: SHA-256 start key + PBKDF2-HMAC-SHA1 + AES-256-CBC"
    if mode == _MODE_ODF11_BLOWFISH:
        return "ODF 1.1 profile: SHA-1 start key + PBKDF2-HMAC-SHA1 + Blowfish CFB (falls fast, ~1024 iters)"
    return "ODF 1.3 profile: SHA-256 start key + Argon2id + AES-256-GCM -- decryptable with the password, no hashcat mode (memory-hard KDF + AEAD)"


class _BodyProtectionScanner:
    """Streaming scan of ``content.xml`` for sheet/section protection flags.

    Driven by :mod:`xml.parsers.expat` start-element callbacks -- no DOM, no
    external-entity resolution. Sets a flag when it sees a ``<table:table>`` or
    ``<text:section>`` carrying ``*:protected="true"`` ([opendocument.md]
    body-protection table).
    """

    def __init__(self) -> None:
        """Initialise both protection flags to absent."""
        self.sheet_protected = False
        self.section_protected = False

    def start_element(self, name: str, attrs: dict[str, str]) -> None:
        """Handle an expat start-element event, matching by local name."""
        local = name.rsplit(":", 1)[-1]
        # Attribute keys are namespace-qualified (e.g. "table:protected"); the
        # local "protected" flag is what carries the lock on either body type.
        protected = next((value for key, value in attrs.items() if key.rsplit(":", 1)[-1] == "protected"), None)
        if protected != "true":
            return
        if local == "table":
            self.sheet_protected = True
        elif local == "section":
            self.section_protected = True


def _scan_body_protection(content: bytes) -> tuple[bool, bool]:
    """Return ``(sheet_protected, section_protected)`` for a plaintext ``content.xml``.

    Returns ``(False, False)`` on malformed XML -- enumeration never crashes.
    """
    scanner = _BodyProtectionScanner()
    parser = xml.parsers.expat.ParserCreate()
    parser.StartElementHandler = scanner.start_element
    try:
        # expat's Parse takes is_final as a positional-only flag; a named local keeps
        # the boolean literal out of the call site (ruff FBT003) without changing behaviour.
        is_final = True
        parser.Parse(content, is_final)
    except xml.parsers.expat.ExpatError:
        return (False, False)
    return (scanner.sheet_protected, scanner.section_protected)


# --- XML rewriters (byte-accurate, no DOM round-trip) ---


class _EncryptionDataSpanFinder:
    """Locate the byte spans of every ``<manifest:encryption-data>`` subtree.

    Uses expat's :attr:`CurrentByteIndex` to record the exact start/end offsets of
    each ``encryption-data`` element so we can splice them out of the original
    manifest bytes -- an XML-aware delete that never disturbs the surrounding
    prefixes, whitespace, or attribute quoting. The element is never nested, so a
    single pending-start marker is enough.
    """

    def __init__(self, parser: xml.parsers.expat.XMLParserType) -> None:
        """Bind to the running ``parser`` (needed for the byte-offset cursor)."""
        self.spans: list[tuple[int, int]] = []
        self._parser = parser
        self._pending_start: int | None = None

    def start_element(self, name: str, attrs: dict[str, str]) -> None:
        """Record the start offset when an ``encryption-data`` element opens."""
        _ = attrs
        if name.rsplit(":", 1)[-1] == "encryption-data":
            self._pending_start = self._parser.CurrentByteIndex

    def end_element(self, name: str) -> None:
        """Close the span at the end tag, capturing the full ``</...>`` sequence."""
        if name.rsplit(":", 1)[-1] == "encryption-data" and self._pending_start is not None:
            # CurrentByteIndex at end points at the "<" of the closing tag; add the
            # closing-tag width to cover "</manifest:encryption-data>".
            end = self._parser.CurrentByteIndex + len(f"</{name}>")
            self.spans.append((self._pending_start, end))
            self._pending_start = None


def _strip_encryption_data(manifest: bytes) -> bytes:
    """Return the manifest with every ``<manifest:encryption-data>`` block removed.

    Marks each member as stored-in-clear so a decrypted package round-trips as an
    ordinary ODF file. The ``manifest:size`` (plaintext length) attributes are left
    in place -- readers ignore them once the encryption block is gone.
    """
    parser = xml.parsers.expat.ParserCreate()
    finder = _EncryptionDataSpanFinder(parser)
    parser.StartElementHandler = finder.start_element
    parser.EndElementHandler = finder.end_element
    # expat's is_final flag is positional-only; pass it via a named local (ruff FBT003).
    is_final = True
    parser.Parse(manifest, is_final)

    # Splice the spans out back-to-front so earlier offsets stay valid.
    result = manifest
    for start, end in sorted(finder.spans, reverse=True):
        result = result[:start] + result[end:]
    return result


def _strip_body_protection(content: bytes) -> bytes:
    """Return ``content.xml`` with sheet/section protection lifted (BYPASS).

    Sets ``*:protected="false"`` and deletes the ``*:protection-key`` /
    ``*:protection-key-digest-algorithm`` attributes on every locked
    ``<table:table>`` / ``<text:section>`` ([opendocument.md]). The body was never
    encrypted, so this is instant and needs no password.
    """
    without_flag = _PROTECTED_TRUE.sub(rb"\1false\2", content)
    return _PROTECTION_KEY.sub(b"", without_flag)


# --- Repackaging ---


def _repackage(src: Path, out: Path, plan: _RepackagePlan) -> None:
    """Write ``src`` to ``out`` as a valid ODF-ZIP applying ``plan``'s edits.

    Enforces the two ODF packaging invariants ([opendocument.md] Tools section):
    ``mimetype`` is written first and STORED (uncompressed); every other member is
    DEFLATE-compressed. The input is opened read-only and never modified -- the
    output is a separate file. Members named in :attr:`_RepackagePlan.replacements`
    (and the manifest, when overridden) get their new bytes; the rest are copied.
    """
    with zipfile.ZipFile(src) as archive:
        _reject_zip_bomb(archive)
        names = archive.namelist()
        infos = archive.infolist()

        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as writer:
            # mimetype first + stored, or the package is not a valid ODF file.
            if _MIMETYPE_NAME in names:
                stored = zipfile.ZipInfo(_MIMETYPE_NAME)
                stored.compress_type = zipfile.ZIP_STORED
                writer.writestr(stored, archive.read(_MIMETYPE_NAME))

            for info in infos:
                name = info.filename
                if name == _MIMETYPE_NAME:
                    continue  # already emitted first
                override = plan.manifest_override if name == _MANIFEST_PATH else None
                data = override if override is not None else plan.replacements.get(name, archive.read(name))
                # Directory entries carry a trailing slash and no payload; writestr
                # re-creates them so the package structure is preserved.
                writer.writestr(name, data)


class OdfHandler(FormatHandler):
    """Handler for the OpenDocument ZIP container (``.odt`` / ``.ods`` / ``.odp``)."""

    container = ContainerKind.ODF_ZIP

    @override
    def is_encrypted(self, path: Path) -> bool:
        """Report document-open encryption: True iff the manifest has an encryption block.

        The manifest is cleartext, so this is a cheap read -- no key needed. Body
        protection (sheet/section) is not encryption and never sets this True.
        """
        return bool(_load_entries(path))

    @override
    def gates(self, path: Path) -> list[Gate]:
        """Enumerate the open-encryption gate and any plaintext body-protection gates.

        The OPEN gate (recovery CRACK, scheme ODF) is emitted whenever the manifest
        carries encryption, with the profile's hashcat mode (18400 / 18600) or a
        GAP note for ODF 1.3. Sheet/section protection is detectable only when the
        body is *not* encrypted -- a locked-but-encrypted body stays hidden until
        the package is decrypted.
        """
        gates: list[Gate] = []
        entries = _load_entries(path)
        logger.debug("gates: %d encrypted entries", len(entries))

        if entries:
            primary = _primary_entry(entries)
            mode = _hashcat_mode(primary)
            gates.append(
                Gate(
                    gate=GateType.OPEN,
                    recovery=RecoveryClass.CRACK,
                    scheme=HashScheme.ODF,
                    hashcat_mode=mode,
                    where=f"{_MANIFEST_PATH} <manifest:encryption-data> ({primary.full_path})",
                    note=_profile_note(mode),
                ),
            )

        # Body protection lives in cleartext content.xml; skip when it is encrypted.
        encrypted_names = {entry.full_path for entry in entries}
        if _CONTENT_NAME not in encrypted_names and ("/" + _CONTENT_NAME) not in encrypted_names:
            content = _read_member(path, _CONTENT_NAME)
            if content is not None:
                sheet, section = _scan_body_protection(content)
                if sheet:
                    gates.append(Gate(gate=GateType.PROTECT_SHEET, recovery=RecoveryClass.STRIP, where='content.xml <table:table table:protected="true">', note="ODF sheet protection -- body is plaintext; strip the flag"))
                if section:
                    gates.append(Gate(gate=GateType.SECTION, recovery=RecoveryClass.STRIP, where='content.xml <text:section text:protected="true">', note="ODF section protection -- body is plaintext; strip the flag"))

        return gates

    @override
    def extract(self, path: Path) -> list[ExtractedHash]:
        """Emit an ``$odf$*...`` hash line for every encrypted member.

        ODF 1.1 / 1.2 members yield the odf2john / hashcat 18600 / 18400 line
        (``hashcat_mode`` set). ODF 1.3 members (Argon2id + AES-GCM) yield the
        extended ``$odf$*2*...`` line with the trailing kdf / gcm_tag / start_key /
        m_cost / t_cost / lanes tokens and ``hashcat_mode=None`` -- there is no GPU
        mode, but the package still produces a labelled record instead of nothing.
        Only a cipher with no code path at all is skipped. Body protection carries no
        crackable hash and produces no line.
        """
        hashes: list[ExtractedHash] = []
        entries = _load_entries(path)

        for entry in entries:
            # The whole stored member is needed: ODF 1.3 splits IV || ciphertext ||
            # tag, and the GCM tag authenticates the full stream (no 1024 cap).
            ciphertext = _read_member(path, entry.full_path)
            if ciphertext is None:
                continue
            filled = dataclasses.replace(entry, ciphertext=ciphertext)
            try:
                line = odf.odf_hash_line(filled)
                opt_line = odf.unified_odf_line(filled)
            except odf.OdfUnsupportedError:
                # A cipher outside the three profiles -- nothing we can emit.
                continue
            hashes.append(ExtractedHash(scheme=HashScheme.ODF, hashcat_mode=_hashcat_mode(entry), value=line, gate=GateType.OPEN, opt_value=opt_line))

        return hashes

    @override
    def bypass(self, path: Path, out: Path, *, remove_signatures: bool = False) -> None:
        """Write a NEW package with sheet/section protection stripped (free BYPASS).

        Rewrites ``content.xml`` to clear ``*:protected`` and delete the
        ``*:protection-key`` attributes, then repackages mimetype-first. Does NOT
        touch open-encryption: an encrypted ``content.xml`` is opaque, so the file
        is repackaged unchanged in that case. The input is never modified.
        ``remove_signatures`` is accepted for interface parity but ignored -- the
        ODF handler enumerates no digital-signature gate.
        """
        _ = remove_signatures  # ODF documentsignatures are not a gate this handler models
        entries = _load_entries(path)
        encrypted_names = {entry.full_path for entry in entries}

        replacements: dict[str, bytes] = {}
        # Only a plaintext content.xml can be de-protected; skip when encrypted.
        if _CONTENT_NAME not in encrypted_names and ("/" + _CONTENT_NAME) not in encrypted_names:
            content = _read_member(path, _CONTENT_NAME)
            if content is not None:
                stripped = _strip_body_protection(content)
                if stripped != content:
                    logger.debug("bypass: stripped body protection from %s", _CONTENT_NAME)
                    replacements[_CONTENT_NAME] = stripped

        logger.debug("bypass: repackaging to %s (%d replacements)", out, len(replacements))
        _repackage(path, out, _RepackagePlan(replacements=replacements))

    @override
    def decrypt(self, path: Path, out: Path, password: str) -> None:
        """Decrypt every encrypted member with ``password`` and write a plaintext ODF.

        Confirms the password per member (a wrong password raises ``ValueError``
        from :func:`crypto.odf.decrypt_entry` -- a checksum miss for ODF 1.1 / 1.2 or
        a GCM tag miss for ODF 1.3), decrypts each member to its DEFLATE-inflated
        plaintext, drops the ``<encryption-data>`` blocks from the manifest, and
        repackages mimetype-first. All three profiles (Blowfish CFB, AES-256-CBC,
        Argon2id + AES-256-GCM) are handled. The input is opened read-only; the
        output is a separate, ordinary ODF file. Raises
        :class:`~crypto.odf.OdfUnsupportedError` only for a cipher with no code path.
        """
        entries = _load_entries(path)
        if not entries:
            msg = f"{path} is not an encrypted ODF package (no <manifest:encryption-data>)"
            raise ValueError(msg)

        # Confirm the password against the canonical content.xml, not the first
        # member: LibreOffice writes small Basic-macro members whose /1K checksum
        # does not match even under the correct key, so gating the whole decrypt on
        # such a member would spuriously reject a good password.
        primary = _primary_entry(entries)
        logger.debug("decrypt: verifying password against %s", primary.full_path)
        primary_ciphertext = _read_member(path, primary.full_path)
        if primary_ciphertext is None or not odf.verify(primary, password, primary_ciphertext):
            logger.debug("decrypt: password rejected")
            msg = f"incorrect password for {path}"
            raise ValueError(msg)
        logger.debug("decrypt: password accepted, decrypting %d members", len(entries))

        replacements: dict[str, bytes] = {}
        for entry in entries:
            ciphertext = _read_member(path, entry.full_path)
            if ciphertext is None:
                msg = f"encrypted member {entry.full_path!r} named in the manifest is missing from the package"
                raise ValueError(msg)
            try:
                replacements[entry.full_path] = odf.decrypt_entry(entry, password, ciphertext)
            except ValueError:
                # The password is already confirmed via content.xml; a per-member
                # checksum miss is the small-member quirk documented on decrypt_entry,
                # so decrypt this member best-effort (the key is correct).
                replacements[entry.full_path] = odf.decrypt_entry(entry, password, ciphertext, verify=False)

        manifest = _read_member(path, _MANIFEST_PATH)
        manifest_override = _strip_encryption_data(manifest) if manifest is not None else None
        logger.debug("decrypt: writing decrypted package to %s (%d members)", out, len(replacements))
        _repackage(path, out, _RepackagePlan(replacements=replacements, manifest_override=manifest_override))
