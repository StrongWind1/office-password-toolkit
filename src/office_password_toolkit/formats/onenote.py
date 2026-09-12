# SPDX-License-Identifier: Apache-2.0
r"""OneNote handler -- password-protected ``.one`` / ``.onetoc2`` sections.

A OneNote *revision store* is a proprietary binary container ([MS-ONESTORE]),
not an OLE/CFB file and not a ZIP. When a section is password-protected the
application does not invent a new crypto stack: it reuses an [MS-OFFCRYPTO]
``EncryptionInfo`` blob -- the very same structure a ``.docx``/``.xlsx`` carries
in its ``\EncryptionInfo`` stream. The blob is referenced by an
``ObjectDataEncryptionKeyV2FNDX`` node ([MS-ONESTORE] Section 2.5.19) and is
framed on disk by two 64-bit sentinels: header ``0xFB6BA385DAD1A067`` and footer
``0x2649294F8E198B3C``. Everything between them (``cb - 16`` bytes) is the raw
``EncryptionInfo`` the spec deliberately marks "MUST be ignored".

Crucially the framed blob can be *any* of the three [MS-OFFCRYPTO] document-open
schemes, decided per-file by the leading version words -- it is NOT always agile
([MS-ONESTORE]/onenote.md analysis notes):

* **Agile** (``vMajor == vMinor == 4``): ECMA-376 agile, AES-CBC + SHA-1/SHA-512.
  Parsed by :mod:`~office_password_toolkit.crypto.ecma376`; emits
  ``$office$*2013`` (hashcat 9600, SHA-512/AES-256) or ``$office$*2010`` (9500,
  SHA-1/AES-128). A non-hashcat agile tuple falls back to the generalized
  ``$office-agile$`` line.
* **Standard** (``vMinor == 2`` with ``fAES`` set): ECMA-376 standard, AES-ECB +
  SHA-1 x50000. Parsed by ``ecma376``; emits ``$office$*2007`` (hashcat 9400).
* **RC4 CryptoAPI** (``vMinor == 2`` with ``fCryptoAPI`` set and ``fAES`` clear,
  ``AlgID == 0x6801``): SHA-1 + RC4, no iteration. Parsed by
  :mod:`~office_password_toolkit.crypto.rc4legacy`; emits ``$oldoffice$3``/``4``
  (hashcat 9800).

Because both key derivation and hashing already live (and are self-verified) in
``ecma376``/``rc4legacy``, this file never touches a KDF, hash, or cipher. It
only locates the framed blob, reads the version words, and routes to the right
primitive so the emitted line is byte-for-byte identical to what the OLE handler
produces for the same descriptor. OneNote is CRACK-only: there is no clean
``\EncryptedPackage`` container to rebuild, so bypass and decrypt fail honestly.

Import rules: crypto + models + base + stdlib only -- no sibling handler, no
:mod:`~office_password_toolkit.detect`.
"""

from __future__ import annotations

import logging
import struct
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, cast

from typing_extensions import override

from office_password_toolkit.crypto import ecma376, rc4legacy
from office_password_toolkit.formats.base import FormatHandler, HandlerNotImplementedError
from office_password_toolkit.models import ContainerKind, ExtractedHash, Gate, GateType, HashScheme, RecoveryClass

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)

# --- On-disk markers ------------------------------------------------------

# [MS-ONESTORE] Section 2.3.1: every revision store (.one/.onetoc2) opens with a
# 16-byte header GUID {7B5C52E4-D888-4DA7-AEB1-5378D02996D3}, stored in the
# little-endian GUID byte order below. office2john keys off only the first six
# bytes (e4525c7b8cd8); we match the full GUID to avoid false positives.
_ONENOTE_MAGIC: Final = b"\xe4\x52\x5c\x7b\x8c\xd8\xa7\x4d\xae\xb1\x53\x78\xd0\x29\x96\xd3"

# [MS-ONESTORE] Section 2.5.19 (ObjectDataEncryptionKeyV2FNDX): the encryption
# blob is framed by two 64-bit sentinels stored little-endian (they are read as a
# ToUInt64, confirmed by the OfficeDev/Interop-TestSuites captures R615/R617).
# Header = 0xFB6BA385DAD1A067, Footer = 0x2649294F8E198B3C; the interior has a
# 16-byte preamble (4-byte type, 4-byte total length, 4-byte EncryptionInfo offset,
# 4-byte EncryptionInfo size) followed by the [MS-OFFCRYPTO] EncryptionInfo blob.
_BLOB_HEADER_MAGIC: Final = (0xFB6BA385DAD1A067).to_bytes(8, "little")
_BLOB_FOOTER_MAGIC: Final = (0x2649294F8E198B3C).to_bytes(8, "little")
_BLOB_PREAMBLE_SIZE: Final = 16

# office2john's shortcut carves the agile ``<encryption>`` XML directly (no
# framing). We keep that as a fallback so a store that only exposes the bare XML
# still works; the carve bounds the element tag-to-tag for the ecma376 parser.
_ENCRYPTION_OPEN: Final = b"<encryption"
_ENCRYPTION_CLOSE: Final = b"</encryption>"

# Synthetic ``\EncryptionInfo`` prefix reconstructed around a bare carved XML so
# the fallback blob looks exactly like a real agile stream to ecma376:
# vMajor=0x0004, vMinor=0x0004 (agile) and EncryptionInfoFlags = 0x40 (fAgile).
# See [MS-OFFCRYPTO] Section 2.3.4.10.
_AGILE_STREAM_HEADER: Final = b"\x04\x00\x04\x00\x40\x00\x00\x00"

# --- Scheme discriminators ([MS-OFFCRYPTO] Section 2.1.4 / 2.3.1) ---------

# EncryptionVersionInfo.vMinor selects the family: 4 = agile, 2 = standard AES OR
# RC4 CryptoAPI (the fAES/fCryptoAPI flags separate the two Section-2 cases).
_VMINOR_AGILE: Final = 0x0004
_VMINOR_STANDARD_OR_RC4: Final = 0x0002

# EncryptionInfoFlags bits ([MS-OFFCRYPTO] Section 2.3.1). fAES marks AES
# standard/agile; fCryptoAPI (without fAES) marks the legacy RC4 CryptoAPI scheme.
_FLAG_AES: Final = 0x20
_FLAG_CRYPTOAPI: Final = 0x04

# --- hashcat modes for each routed scheme ---------------------------------
_MODE_AGILE_2013: Final = 9600  # agile SHA-512 / AES-256 -> $office$*2013
_MODE_AGILE_2010: Final = 9500  # agile SHA-1 / AES-128 -> $office$*2010
_MODE_STANDARD_2007: Final = 9400  # standard AES-ECB / SHA-1 -> $office$*2007
_MODE_RC4_CRYPTOAPI: Final = 9800  # RC4 CryptoAPI SHA-1 -> $oldoffice$3/4

# Agile tuple discriminators used to pick the hashcat proxy (mirrors ecma376).
_KEY_BITS_128: Final = 128
_KEY_BITS_256: Final = 256
_RC4_DEFAULT_KEY_BITS: Final = 40  # KeySize == 0 means 40-bit ([MS-OFFCRYPTO] Section 2.3.5.1)
_RC4_DIGIT_40: Final = 3  # $oldoffice$3 -- 40-bit RC4 key
_RC4_DIGIT_128: Final = 4  # $oldoffice$4 -- 128-bit RC4 key


@dataclass(frozen=True)
class _OneNoteHash:
    """A routed OneNote encryptor: its scheme, hashcat mode, line, and location.

    Bundled so the carve/route step is done once and both :meth:`OneNoteHandler.gates`
    and :meth:`OneNoteHandler.extract` read from the same value instead of routing
    twice. ``hashcat_mode`` is ``None`` for an agile tuple no single mode ingests.
    """

    scheme: HashScheme
    hashcat_mode: int | None
    value: str
    where: str
    note: str
    opt_value: str = ""


# --- Scheme routing -------------------------------------------------------


def _agile_hash(info: ecma376.EncryptionInfo) -> _OneNoteHash:
    """Route a parsed agile descriptor to its hash line ([MS-OFFCRYPTO] Section 2.3.4.10).

    SHA-512/AES-256 is the OneNote 2013+ default (hashcat 9600); SHA-1/AES-128 is
    the 2010 tuple (9500). Any other agile tuple has no hashcat mode, so it falls
    back to the generalized ``$office-agile$`` line, which a conforming cracker can
    still ingest.
    """
    algo = info.hash_algorithm.upper().replace("-", "")
    where = "ObjectDataEncryptionKeyV2FNDX blob -> agile <encryption> descriptor"
    opt_line = ecma376.unified_office_line(info)
    if algo == "SHA512" and info.key_bits == _KEY_BITS_256:
        return _OneNoteHash(HashScheme.OFFICE_2013, _MODE_AGILE_2013, ecma376.office_hash_line(info), where, "OneNote 2013+ agile SHA-512/AES-256; crack with hashcat 9600", opt_value=opt_line)
    if algo == "SHA1" and info.key_bits == _KEY_BITS_128:
        return _OneNoteHash(HashScheme.OFFICE_2010, _MODE_AGILE_2010, ecma376.office_hash_line(info), where, "agile SHA-1/AES-128; crack with hashcat 9500", opt_value=opt_line)
    return _OneNoteHash(HashScheme.OFFICE_2013, None, opt_line, where, "non-standard agile tuple; unified $office$ line, no hashcat mode", opt_value=opt_line)


def _standard_hash(info: ecma376.EncryptionInfo) -> _OneNoteHash:
    """Route a parsed standard descriptor to its ``$office$*2007`` line (hashcat 9400)."""
    where = "ObjectDataEncryptionKeyV2FNDX blob -> standard EncryptionInfo"
    return _OneNoteHash(HashScheme.OFFICE_2007, _MODE_STANDARD_2007, ecma376.office_hash_line(info), where, "ECMA-376 standard SHA-1/AES-ECB; crack with hashcat 9400", opt_value=ecma376.unified_office_line(info))


def _rc4_hash(blob: bytes) -> _OneNoteHash:
    """Route an RC4 CryptoAPI blob to its ``$oldoffice$3``/``4`` line ([MS-OFFCRYPTO] Section 2.3.5).

    ``rc4legacy`` owns the header layout and the KeySize -> version-digit mapping;
    a KeySize of 0 means 40-bit per the spec. The line is byte-identical to what
    the OLE handler emits for the same descriptor (hashcat 9800).
    """
    header = rc4legacy.parse_rc4_cryptoapi_header(blob)
    key_bits = cast("int", header["key_size"]) or _RC4_DEFAULT_KEY_BITS
    salt = cast("bytes", header["salt"])
    enc_v = cast("bytes", header["encrypted_verifier"])
    enc_vh = cast("bytes", header["encrypted_verifier_hash"])
    digit = _RC4_DIGIT_128 if key_bits == _KEY_BITS_128 else _RC4_DIGIT_40
    line = rc4legacy.rc4_cryptoapi_hash_line(digit, key_bits, salt, enc_v, enc_vh)
    opt_line = rc4legacy.unified_rc4_office_line(rc4legacy.Rc4Scheme.CRYPTOAPI, salt, key_bits, enc_v, enc_vh)
    where = "ObjectDataEncryptionKeyV2FNDX blob -> RC4 CryptoAPI EncryptionInfo"
    return _OneNoteHash(HashScheme.OLDOFFICE_RC4_SHA1, _MODE_RC4_CRYPTOAPI, line, where, "legacy RC4 CryptoAPI SHA-1 (fast hash); crack with hashcat 9800", opt_value=opt_line)


def _classify(blob: bytes) -> _OneNoteHash:
    """Route a carved ``EncryptionInfo`` blob by its version words + flags.

    The leading two u16 words are ``vMajor``/``vMinor``; ``vMinor == 4`` is agile,
    ``vMinor == 2`` is either standard AES or RC4 CryptoAPI (both share the version
    words -- the ``fAES``/``fCryptoAPI`` bits in EncryptionInfoFlags at offset 4
    separate them, [MS-OFFCRYPTO] Section 2.3.1). Raises ``ValueError`` for any
    scheme this toolkit cannot turn into a hash line.
    """
    if len(blob) < len(_AGILE_STREAM_HEADER):
        msg = "OneNote EncryptionInfo blob is too short to carry a version header"
        raise ValueError(msg)
    version_minor = int.from_bytes(blob[2:4], "little")
    if version_minor == _VMINOR_AGILE:
        return _agile_hash(ecma376.parse_encryption_info(blob))
    if version_minor == _VMINOR_STANDARD_OR_RC4:
        flags = int.from_bytes(blob[4:8], "little")
        if flags & _FLAG_AES:
            return _standard_hash(ecma376.parse_encryption_info(blob))
        if flags & _FLAG_CRYPTOAPI:
            return _rc4_hash(blob)
    version_major = int.from_bytes(blob[0:2], "little")
    msg = f"OneNote EncryptionInfo version ({version_major}, {version_minor}) is not a recoverable open-encryption scheme"
    raise ValueError(msg)


class OneNoteHandler(FormatHandler):
    """Handler for the OneNote revision-store container ([MS-ONESTORE])."""

    container = ContainerKind.ONENOTE

    @override
    def is_encrypted(self, path: Path) -> bool:
        """Report whether ``path`` is a password-protected OneNote section.

        True iff the store carries an ``EncryptionInfo`` blob (the payload is real
        ciphertext keyed off the password). A plaintext ``.one`` starts with the
        same header GUID but has no blob, so it reads False.
        """
        data = self._read_store(path)
        if data is None:
            return False
        return self._carve_encryption_info(data) is not None

    @override
    def gates(self, path: Path) -> list[Gate]:
        """Enumerate the gates present -- only the Open-password gate exists here.

        OneNote has no modify/section/VBA flag to strip; the single mechanism is
        the document-open encryption. The scheme/mode are read from the carved
        blob's version words, so agile (9600/9500), standard (9400), and RC4
        CryptoAPI (9800) sections each report their true target rather than a
        hard-coded 9600.
        """
        data = self._read_store(path)
        if data is None:
            return []
        blob = self._carve_encryption_info(data)
        if blob is None:
            logger.debug("gates: no encryption blob")
            return []
        try:
            routed = _classify(blob)
        except (ValueError, struct.error):
            logger.debug("gates: unrecognized EncryptionInfo scheme")
            return [Gate(gate=GateType.OPEN, recovery=RecoveryClass.CRACK, where="ObjectDataEncryptionKeyV2FNDX encryption blob", note="encrypted OneNote section with an unrecognized EncryptionInfo scheme")]
        logger.debug("gates: scheme=%s mode=%s", routed.scheme, routed.hashcat_mode)
        return [
            Gate(
                gate=GateType.OPEN,
                recovery=RecoveryClass.CRACK,
                scheme=routed.scheme,
                hashcat_mode=routed.hashcat_mode,
                where=routed.where,
                note=routed.note,
            ),
        ]

    @override
    def extract(self, path: Path) -> list[ExtractedHash]:
        r"""Carve the encryption blob and emit its hash line for the routed scheme.

        The carved ``EncryptionInfo`` is routed by its version words to
        :mod:`~office_password_toolkit.crypto.ecma376` (agile/standard) or
        :mod:`~office_password_toolkit.crypto.rc4legacy` (RC4 CryptoAPI), so the
        emitted line matches what the OLE handler produces for the same descriptor.
        Returns an empty list for a plaintext store or an unsupported scheme.
        """
        data = self._read_store(path)
        if data is None:
            return []
        blob = self._carve_encryption_info(data)
        if blob is None:
            return []
        try:
            routed = _classify(blob)
        except (ValueError, struct.error):
            return []
        return [
            ExtractedHash(
                scheme=routed.scheme,
                hashcat_mode=routed.hashcat_mode,
                value=routed.value,
                gate=GateType.OPEN,
                opt_value=routed.opt_value or None,
            ),
        ]

    @override
    def bypass(self, path: Path, out: Path, *, remove_signatures: bool = False) -> None:
        """Reject bypass -- OneNote carries no strippable, keyless protection.

        The only gate is real document-open encryption, which cannot be flipped
        off. There is nothing to strip (and no digital-signature gate), so this
        raises rather than silently copying the file.
        """
        _ = (path, out, remove_signatures)
        operation = "OneNote sections have no bypassable gates — the only protection is section-open encryption which requires the password"
        raise HandlerNotImplementedError(operation, self.container.value)

    def verify_password(self, path: Path, password: str) -> bool:
        """Check whether ``password`` opens the encrypted OneNote section.

        Carves the EncryptionInfo blob, routes by version words, and delegates
        to the appropriate verifier (ecma376 for agile/standard, rc4legacy for
        RC4 CryptoAPI). Returns False for plaintext stores or on any parse error.
        """
        data = self._read_store(path)
        if data is None:
            return False
        blob = self._carve_encryption_info(data)
        if blob is None:
            return False
        try:
            return self._verify_blob(blob, password)
        except (ValueError, struct.error):
            return False

    def _verify_blob(self, blob: bytes, password: str) -> bool:
        """Route a carved blob to the correct password verifier."""
        version_minor = int.from_bytes(blob[2:4], "little")
        if version_minor == _VMINOR_AGILE:
            return ecma376.verify_password(ecma376.parse_encryption_info(blob), password)
        if version_minor == _VMINOR_STANDARD_OR_RC4:
            flags = int.from_bytes(blob[4:8], "little")
            if flags & _FLAG_AES:
                return ecma376.verify_password(ecma376.parse_encryption_info(blob), password)
            if flags & _FLAG_CRYPTOAPI:
                header = rc4legacy.parse_rc4_cryptoapi_header(blob)
                key_bits = cast("int", header["key_size"]) or _RC4_DEFAULT_KEY_BITS
                return rc4legacy.rc4_cryptoapi_verify(password, cast("bytes", header["salt"]), key_bits, cast("bytes", header["encrypted_verifier"]), cast("bytes", header["encrypted_verifier_hash"]))
        return False

    @override
    def decrypt(self, path: Path, out: Path, password: str) -> None:
        """Reject in-place decryption -- OneNote is CRACK-only (GAP P4.1).

        The section's object-space payload is genuine ciphertext with no clean
        container to rebuild into a valid plaintext ``.one``. Implementing this
        requires parsing the [MS-ONESTORE] revision-store layout, identifying
        encrypted object data regions, decrypting them with the derived key, and
        reassembling a valid ``.one`` file (~300-500 lines). Recovery is currently
        limited to carving the hash (:meth:`extract`) and cracking it externally.

        When a password is supplied, we at least verify it against the carved
        EncryptionInfo verifier so the user knows whether their password is correct
        before spending GPU time on hashcat.
        """
        _ = out
        if password and self.verify_password(path, password):
            logger.debug("decrypt: password verified but ONESTORE decryption not implemented")
            operation = f"OneNote password '{password}' is CORRECT but section decryption is not yet implemented (GAP P4.1) -- the ONESTORE object-space layout requires reverse-engineering to rebuild a valid .one"
        else:
            operation = "OneNote decryption not yet implemented -- extract the hash with opt info and crack with hashcat"
        raise HandlerNotImplementedError(operation, self.container.value)

    # --- Internal helpers -------------------------------------------------

    def _read_store(self, path: Path) -> bytes | None:
        """Read the store bytes, returning None unless it is a OneNote container.

        Detection/enumeration must never crash on malformed input, so read errors
        collapse to None (treated as "not an encrypted OneNote file").
        """
        try:
            data = path.read_bytes()
        except OSError:
            return None
        if not data.startswith(_ONENOTE_MAGIC):
            return None
        return data

    def _carve_encryption_info(self, data: bytes) -> bytes | None:
        r"""Carve the raw ``EncryptionInfo`` blob from a store, or None if plaintext.

        Preferred path: the ObjectDataEncryptionKeyV2FNDX blob framed by the two
        64-bit sentinels ([MS-ONESTORE] Section 2.5.19). The interior (everything
        between them) is the [MS-OFFCRYPTO] ``EncryptionInfo`` for whichever of the
        three schemes the section uses -- standard/agile are text-or-binary, RC4 is
        binary, so the framed carve is what supports all three.

        Fallback: office2john's bare ``<encryption>`` XML carve (agile only), wrapped
        in a synthetic agile stream header so the shared parser can read it. This
        keeps a store that exposes only the XML working.
        """
        start = data.find(_BLOB_HEADER_MAGIC)
        if start != -1:
            interior = start + len(_BLOB_HEADER_MAGIC)
            end = data.find(_BLOB_FOOTER_MAGIC, interior)
            if end != -1:
                raw = data[interior:end]
                # Skip the 16-byte OneNote preamble ([MS-ONESTORE] §2.5.19):
                # the EncryptionInfo starts after [type:4][len:4][offset:4][size:4].
                if len(raw) > _BLOB_PREAMBLE_SIZE:
                    return raw[_BLOB_PREAMBLE_SIZE:]
                return raw
        xml = self._carve_encryption_xml(data)
        if xml is None:
            return None
        return _AGILE_STREAM_HEADER + xml

    def _carve_encryption_xml(self, data: bytes) -> bytes | None:
        """Carve a bare agile ``<encryption>...</encryption>`` descriptor from a store.

        Returns the descriptor bytes (opening tag through closing tag) or None when
        the store has no bare XML encryptor. Used only as the fallback when the
        framed blob is absent; agile is the sole scheme that exposes readable XML.
        """
        start = data.find(_ENCRYPTION_OPEN)
        if start == -1:
            return None
        close = data.find(_ENCRYPTION_CLOSE, start)
        if close == -1:
            return None
        return data[start : close + len(_ENCRYPTION_CLOSE)]
