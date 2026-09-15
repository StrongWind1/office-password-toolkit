# SPDX-License-Identifier: Apache-2.0
"""OLE/CFB handler -- legacy ``.doc``/``.xls``/``.ppt`` and the encrypted-OOXML wrapper.

This is the widest handler in the toolkit: a single [MS-CFB] compound file can be
either (a) a *modern* encrypted Office package -- the whole OPC ZIP re-wrapped in
an OLE container carrying an ``EncryptionInfo`` + ``EncryptedPackage`` stream pair
([MS-OFFCRYPTO] Section 2.3.4) -- or (b) a *legacy* binary Word/Excel/PowerPoint
97-2003 document. The routing is decided by opening the container, never by the
file extension (an encrypted ``.docx`` is on disk an OLE file).

Design decisions worth stating up front:

* **Detection is stream-driven.** ``EncryptionInfo`` present -> modern wrapper.
  Otherwise the root streams identify the application: ``WordDocument`` -> ``.doc``,
  ``Workbook``/``Book`` -> ``.xls``, ``PowerPoint Document`` -> ``.ppt``.
* **is_encrypted means "needs a key".** Only the schemes whose body cannot be read
  without deriving a key from the password return ``True`` here: RC4+MD5,
  RC4-CryptoAPI, and the ECMA-376 wrapper. The legacy XOR "password to open" is a
  keyless scramble (``RecoveryClass.DECODE`` per ``docs/reference/gates.md``) and,
  like the protection-only verifiers, reports ``False`` -- it is still surfaced as
  an Open gate by :meth:`OleHandler.gates`.
* **The input file is never modified.** ``bypass`` and ``decrypt`` copy the input
  to the caller-supplied output and edit only the copy (``olefile`` ``write_stream``
  performs same-size stream overwrites in place).

The wire layouts and hash-line grammars are ported from the [MS-OFFCRYPTO],
[MS-DOC], [MS-XLS] and [MS-PPT] specs; the concrete stream/record offsets were
cross-checked byte-for-byte against ``office2john`` and ``msoffcrypto-tool``.
"""

from __future__ import annotations

import logging
import shutil
import struct
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, cast

import olefile
from typing_extensions import override

from office_password_toolkit.constants import (
    DEFAULT_PASSWORD_EXCEL,
    DEFAULT_PASSWORD_POWERPOINT,
)
from office_password_toolkit.crypto import ecma376, rc4legacy, vba, xor
from office_password_toolkit.crypto import mpp as mpp_crypto
from office_password_toolkit.crypto.rc4legacy import Rc4Scheme, Rc4StreamParams
from office_password_toolkit.formats.base import FormatHandler, HandlerNotImplementedError
from office_password_toolkit.models import (
    ContainerKind,
    ExtractedHash,
    Gate,
    GateType,
    HashScheme,
    RecoveryClass,
)

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)

# --- Stream names ([MS-CFB] directory entries) ---------------------------------
_ENCRYPTION_INFO: Final = "EncryptionInfo"  # modern wrapper descriptor ([MS-OFFCRYPTO] Section 2.3.4.5/2.3.4.10)
_ENCRYPTED_PACKAGE: Final = "EncryptedPackage"  # modern wrapper ciphertext ([MS-OFFCRYPTO] Section 2.3.4.4)
_WORD_DOCUMENT: Final = "WordDocument"  # [MS-DOC] main stream (holds the FIB)
_WORKBOOK_STREAMS: Final = ("Workbook", "Book")  # [MS-XLS] BIFF8 / older BIFF stream
_PPT_DOCUMENT: Final = "PowerPoint Document"  # [MS-PPT] presentation stream
_CURRENT_USER: Final = "Current User"  # [MS-PPT] edit-chain entry point
_SIGNATURES: Final = "_signatures"  # legacy digital-signature stream

# Storages that host an embedded VBA project ([MS-OVBA]); the PROJECT stream we
# want is a child of one of these (or of any storage that also carries a "dir").
_VBA_STORAGES: Final = ("Macros", "_VBA_PROJECT_CUR", "VBA")

# --- Encryption version words ([MS-OFFCRYPTO] Section 2.1.4 / 2.3.5.1) ---------
_VERSION_MINOR_EXTENSIBLE: Final = 0x0003  # extensible/IRM -- not password-recoverable
_VERSION_MINOR_STANDARD: Final = 0x0002  # ECMA-376 standard (and CryptoAPI RC4) wrapper

# --- FibBase bit layout ([MS-DOC] Section 2.5.2) -------------------------------
_FIB_WIDENT: Final = 0xA5EC  # magic that opens every Word 97+ FIB
_FIB_FLAGS_OFFSET: Final = 10  # offset of the 16-bit flag word in FibBase
_FIB_IKEY_OFFSET: Final = 14  # offset of IKey/lKey (u32): XOR verifier or header size
_FIB_BIT_FENCRYPTED: Final = 8  # fEncrypted
_FIB_BIT_FWHICHTBLSTM: Final = 9  # fWhichTblStm (0 -> 0Table, 1 -> 1Table)
_FIB_BIT_FREADONLY: Final = 10  # fReadOnlyRecommended
_FIB_BIT_FWRITERESERVATION: Final = 11  # fWriteReservation (modify password present)
_FIB_BIT_FOBFUSCATION: Final = 15  # fObfuscation (XOR "password to open")
_FIB_BASE_LEN: Final = 32  # length of the packed FibBase
_FIB_LEN: Final = 0x44  # length of the un-encrypted FIB prefix (68 bytes)

# --- FibRgFcLcb97 pair indices ([MS-DOC] Section 2.5.6) ------------------------
# Each entry is an (fc u32, lcb u32) pair; the blob follows FibBase + FibRgW + FibRgLw.
_FCLCB_INDEX_DOP: Final = 31  # fcDop / lcbDop
_FCLCB_INDEX_STTBF_ASSOC: Final = 32  # fcSttbfAssoc / lcbSttbfAssoc
_FCLCB_PAIR_LEN: Final = 8  # fc(4) + lcb(4)

# --- DopBase restrict-editing fields ([MS-DOC] Section 2.7.2) ------------------
# lKeyProtDoc is the 32-bit legacy document-protection verifier; the fProt* bits sit in
# the second 32-bit flag dword at DopBase offset 4 (letters map to bit positions).
_DOP_FLAGS2_OFFSET: Final = 4  # second bitfield dword inside DopBase
_DOP_LKEYPROTDOC_OFFSET: Final = 80  # lKeyProtDoc (u32) inside DopBase
_DOP_BIT_FREVMARKING: Final = 15  # V - fRevMarking
_DOP_BIT_FLOCKATN: Final = 20  # a - fLockAtn
_DOP_BIT_FPROTENABLED: Final = 25  # f - fProtEnabled
_DOP_BIT_FLOCKREV: Final = 30  # k - fLockRev
_DOP_PROTECTION_BITS: Final = (_DOP_BIT_FREVMARKING, _DOP_BIT_FLOCKATN, _DOP_BIT_FPROTENABLED, _DOP_BIT_FLOCKREV)

# --- SttbfAssoc ([MS-DOC] Section 2.9.276) ------------------------------------
_STTB_EXTEND_MARKER: Final = 0xFFFF  # fExtend: strings are Unicode (UTF-16LE)
_STTB_HEADER_LEN: Final = 6  # fExtend(2) + cData(2) + cbExtra(2)
_ASSOC_WRITE_RESERVATION_INDEX: Final = 0x11  # SttbfAssoc entry holding the modify password

# --- BIFF record types ([MS-XLS] Section 2.3) ---------------------------------
_RT_BOF: Final = 0x0809  # Beginning Of File (must not be encrypted)
_RT_FILEPASS: Final = 0x002F  # FilePass -- selects the open-encryption scheme
_RT_PASSWORD: Final = 0x0013  # 16-bit sheet/workbook protection verifier
_RT_FILESHARING: Final = 0x005B  # write-reservation (modify) 16-bit verifier
_RT_PROT4REVPASS: Final = 0x01BC  # shared-revisions 16-bit verifier
_RT_FEAT: Final = 0x0867  # Feat record carrying per-feature data ([MS-XLS] Section 2.4.99)
_FEAT_ISF_PROTECTION: Final = 0x0002  # SharedFeatureType ISFPROTECTION ([MS-XLS] Section 2.5.124)
_FEAT_HEADER_FIXED: Final = 9  # isf(2) + reserved1(1) + reserved2(4) + cRef(2) in FeatHdrData
_FEAT_REF8_SIZE: Final = 8  # each Ref8 entry is 8 bytes (rwFirst(2) + rwLast(2) + colFirst(2) + colLast(2))
_FEAT_CBFEATDATA_SIZE: Final = 4  # cbFeatData u32
_FEAT_RESERVED3_SIZE: Final = 2  # reserved3 u16
_FEAT_FSD_SIZE: Final = 4  # FeatProtection.fSD u32 ([MS-XLS] Section 2.5.124)
_RT_BOUNDSHEET8: Final = 0x0085  # sheet directory (lbPlyPos must stay plaintext)

# BOF.dt (docType, [MS-XLS] Section 2.4.21) distinguishes the substream a record
# lives in. A Password record (0x13) in the globals substream is protect-WORKBOOK;
# in a worksheet substream it is protect-SHEET.
_BOF_DT_OFFSET: Final = 2  # dt sits at offset 2 in the BOF body (after vers)
_BOF_DT_GLOBALS: Final = 0x0005  # workbook globals substream
_BOF_DT_WORKSHEET: Final = 0x0010  # worksheet or dialog-sheet substream
_BOUNDSHEET8_PLAINTEXT_PREFIX: Final = 4  # lbPlyPos: first 4 bytes stay in the clear
_XLS_XORKEY_OFFSET: Final = 2  # XorKey u16 offset inside the FilePass body
_XLS_VERIFIER_OFFSET: Final = 4  # verificationBytes u16 offset inside the FilePass body
# Records that [MS-XLS] Section 2.4.117 forbids from being obfuscated/encrypted.
_BIFF_UNENCRYPTED: Final = frozenset(
    {_RT_BOF, _RT_FILEPASS, 0x0194, 0x0195, 0x00E1, 0x0196, 0x0138},
)  # BOF, FilePass, UsrExcl, FileLock, InterfaceHdr, RRDInfo, RRDHead

# FilePass wEncryptionType discriminators ([MS-XLS] Section 2.4.117).
_FILEPASS_XOR: Final = 0x0000
_FILEPASS_RC4: Final = 0x0001

# --- PowerPoint record types ([MS-PPT] Section 2.13.24 et al.) -----------------
_RT_USEREDITATOM: Final = 0x0FF5
_RT_PERSISTDIRECTORYATOM: Final = 0x1772
_RT_CRYPTSESSION10CONTAINER: Final = 0x2F14
_PPT_RH_LEN: Final = 8  # RecordHeader length
_USEREDITATOM_ENCRYPTED_LEN: Final = 0x20  # recLen when encryptSessionPersistIdRef is present
_USEREDITATOM_PLAIN_LEN: Final = 0x1C  # recLen once the encryption reference is dropped
_CURRENTUSER_EDIT_OFFSET: Final = 16  # offset of offsetToCurrentEdit in CurrentUserAtom
_CURRENTUSER_HEADER_TOKEN_OFFSET: Final = 12  # offset of headerToken in CurrentUserAtom
_CURRENTUSER_TOKEN_PLAIN: Final = 0xE391C05F  # headerToken value for an unencrypted document
_RT_CSTRING: Final = 0x0FBA  # RecordHeader.recType for a CString atom ([MS-PPT] Section 2.13.24)
_MODIFY_PASSWORD_INSTANCE: Final = 0x003  # ModifyPasswordAtom rh.recInstance ([MS-PPT] Section 2.4.7)
_PPT_RECVER_CONTAINER: Final = 0xF  # rh.recVer that marks a record whose body is more records
_PPT_MODIFY_MAX_LEN: Final = 510  # ModifyPasswordAtom rh.recLen MUST be <= 510

# --- Legacy RC4 scheme version words -------------------------------------------
_RC4_MD5_VERSION: Final = (1, 1)  # (vMajor, vMinor) for RC4+MD5 ([MS-OFFCRYPTO] Section 2.3.6.1)

# --- Small structural widths ---------------------------------------------------
_ENC_VERSION_LEN: Final = 4  # EncryptionVersionInfo: vMajor(u16) + vMinor(u16)
_U16_LEN: Final = 2  # width of a 16-bit field (wEncryptionType, a verifier)
_XOR_FILEPASS_LEN: Final = 6  # wEncryptionType(2) + XorKey(2) + verifier(2)
_XOR_ARRAY_SLOTS: Final = 16  # the obfuscation array is always 16 bytes ([MS-OFFCRYPTO] Section 2.3.7.2)
_MIN_VBA_PATH_DEPTH: Final = 2  # PROJECT stream must be nested under a VBA storage
_RC4_MD5_HEADER_LEN: Final = 48  # salt(16) + encVerifier(16) + encVerifierHash(16)

# --- Hashcat oldoffice version digits ------------------------------------------
# The digit is metadata only (the crypto is identical); office2john assigns
# 0 = Excel, 1 = Word for RC4+MD5, and 3/4 = 40/128-bit for RC4-CryptoAPI. We
# mirror that so extracted lines match office2john byte-for-byte.
_DIGIT_MD5_XLS: Final = 0
_DIGIT_MD5_DOC: Final = 1
_DIGIT_CAPI_40: Final = 3
_DIGIT_CAPI_128: Final = 4
_KEY_BITS_40: Final = 40
_KEY_BITS_128: Final = 128
_KEY_BITS_256: Final = 256
# Above this KDF work factor, read-only triage skips the default-password probe.
# Office's own default-encrypted files use spinCount 100000, so a far higher count
# is either hostile or not a default-encryption case worth probing during `opt info`.
_MAX_DEFAULT_PROBE_SPIN: Final = 1_000_000

# In-place RC4 re-key block sizes differ per app: 512 for Word streams, 1024 for
# the Excel Workbook stream (empirically pinned against msoffcrypto-tool).
_DOC_BLOCK_SIZE: Final = 512
_XLS_BLOCK_SIZE: Final = 1024
# office2john reads a 32-byte "second block" for 40-bit CryptoAPI (the -m 9800
# meet-in-the-middle field); the source offset is app-specific.
_SECOND_BLOCK_LEN: Final = 32
_DOC_SECOND_BLOCK_OFFSET: Final = 512
_XLS_SECOND_BLOCK_OFFSET: Final = 1024
_PPT_SECOND_BLOCK_OFFSET: Final = 0

# Exceptions raised by olefile / struct while parsing hostile input. Caught
# everywhere detection must degrade rather than crash.
_PARSE_ERRORS: Final = (OSError, ValueError, struct.error, KeyError, IndexError)


class _LegacyApp:
    """Legacy binary applications, keyed by their signature stream or directory."""

    DOC: Final = "doc"
    XLS: Final = "xls"
    PPT: Final = "ppt"
    MPP: Final = "mpp"


# MPP version-specific OLE directory names (MPXJ MPP9Reader/MPP12Reader/MPP14Reader).
_MPP_DIRECTORIES: Final[dict[str, str]] = {
    "   19": "mpp9",
    "   112": "mpp12",
    "   114": "mpp14",
}


@dataclass(frozen=True)
class _Rc4Open:
    """A parsed legacy RC4 document-open descriptor (both MD5 and CryptoAPI).

    Bundled so the extractor/gate/decrypt helpers take a single value instead of
    six positional arguments. ``second_block`` is the 40-bit CryptoAPI MITM field
    (empty otherwise); ``digit`` is the ``$oldoffice$`` version digit.
    """

    scheme: Rc4Scheme
    salt: bytes
    key_bits: int
    enc_verifier: bytes
    enc_verifier_hash: bytes
    digit: int
    second_block: bytes = b""

    @property
    def is_md5(self) -> bool:
        """Whether this is the Office 97/2000 RC4+MD5 scheme (always 40-bit)."""
        return self.scheme is Rc4Scheme.MD5

    @property
    def is_forty_bit(self) -> bool:
        """Whether the effective RC4 key is 40 bits (the KEYSPACE shortcut applies)."""
        return self.is_md5 or self.key_bits == _KEY_BITS_40

    def hash_line(self) -> str:
        """Format the ``$oldoffice$`` line hashcat 9700/9800 consumes."""
        if self.is_md5:
            return rc4legacy.rc4_md5_hash_line(self.digit, self.salt, self.enc_verifier, self.enc_verifier_hash)
        base = rc4legacy.rc4_cryptoapi_hash_line(self.digit, self.key_bits, self.salt, self.enc_verifier, self.enc_verifier_hash)
        # 40-bit CryptoAPI additionally carries the second-block MITM field; hashcat
        # 9800's "alternative format" (module_09800.c) accepts the six-token line.
        return f"{base}*{self.second_block.hex()}" if self.second_block else base

    @property
    def hash_scheme(self) -> HashScheme:
        """The :class:`HashScheme` (9700 for MD5, 9800 for CryptoAPI-SHA1)."""
        return HashScheme.OLDOFFICE_RC4_MD5 if self.is_md5 else HashScheme.OLDOFFICE_RC4_SHA1

    @property
    def hashcat_mode(self) -> int:
        """The hashcat ``-m`` mode for this scheme."""
        return 9700 if self.is_md5 else 9800

    def verify(self, password: str) -> bool:
        """Return whether ``password`` opens the document."""
        if self.is_md5:
            return rc4legacy.rc4_md5_verify(password, self.salt, self.enc_verifier, self.enc_verifier_hash)
        return rc4legacy.rc4_cryptoapi_verify(password, self.salt, self.key_bits, self.enc_verifier, self.enc_verifier_hash)


# --- Low-level OLE / binary helpers --------------------------------------------


def _stream_names(ole: olefile.OleFileIO) -> set[str]:
    """Return the set of root-level stream/storage names in ``ole``."""
    names: set[str] = set()
    for entry in ole.listdir(streams=True, storages=True):
        if entry:
            names.add(entry[0])
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("streams: %s", ", ".join(sorted(names)))
    return names


def _resolve_stream(ole: olefile.OleFileIO, parts: list[str]) -> list[str] | None:
    """Return the actual stream path matching ``parts`` case-insensitively, or ``None``.

    A few non-Microsoft producers write the wrapper streams uppercase
    (``ENCRYPTIONINFO``), which a case-sensitive lookup would miss and mis-report as
    unencrypted.
    """
    if ole.exists("/".join(parts)):
        return parts
    target = [part.lower() for part in parts]
    for entry in ole.listdir(streams=True, storages=True):
        if [part.lower() for part in entry] == target:
            return [str(p) for p in entry]
    return None


def _has_stream(names: set[str], target: str) -> bool:
    """Case-insensitive membership test for a root-level stream name."""
    lowered = target.lower()
    return any(name.lower() == lowered for name in names)


def _read_stream(ole: olefile.OleFileIO, path: str | list[str]) -> bytes | None:
    """Read a whole stream by path (case-insensitive leaf), or ``None`` if absent."""
    parts = [path] if isinstance(path, str) else path
    actual = _resolve_stream(ole, parts)
    if actual is None:
        return None
    try:
        with ole.openstream(actual) as stream:
            return cast("bytes", stream.read())
    except _PARSE_ERRORS:
        return None


def _classify_legacy(names: set[str]) -> str | None:
    """Identify the legacy application from the root stream names (case-insensitive)."""
    if _has_stream(names, _WORD_DOCUMENT):
        logger.debug("legacy app: doc")
        return _LegacyApp.DOC
    if any(_has_stream(names, wb) for wb in _WORKBOOK_STREAMS):
        logger.debug("legacy app: xls")
        return _LegacyApp.XLS
    if _has_stream(names, _PPT_DOCUMENT):
        logger.debug("legacy app: ppt")
        return _LegacyApp.PPT
    for mpp_dir, mpp_ver in _MPP_DIRECTORIES.items():
        if _has_stream(names, mpp_dir):
            logger.debug("legacy app: mpp (%s)", mpp_ver)
            return _LegacyApp.MPP
    logger.debug("legacy app: unrecognised")
    return None


def _bit(value: int, index: int) -> int:
    """Extract a single bit from ``value``."""
    return (value >> index) & 1


# --- FIB (Word) parsing ([MS-DOC] Section 2.5.1) -------------------------------


@dataclass(frozen=True)
class _FibInfo:
    """The FibBase fields that drive Word gate detection ([MS-DOC] Section 2.5.2)."""

    f_encrypted: int
    f_obfuscation: int
    f_which_tbl_stm: int
    f_read_only: int
    f_write_reservation: int
    l_key: int

    @property
    def table_stream(self) -> str:
        """The Table stream that carries the encryption header / Dop / Sttbf."""
        return "1Table" if self.f_which_tbl_stm else "0Table"


def _parse_fib(word_document: bytes) -> _FibInfo | None:
    """Parse FibBase from the head of the ``WordDocument`` stream."""
    if len(word_document) < _FIB_LEN:
        return None
    w_ident = struct.unpack_from("<H", word_document, 0)[0]
    if w_ident != _FIB_WIDENT:
        return None
    flags = struct.unpack_from("<H", word_document, _FIB_FLAGS_OFFSET)[0]
    l_key = struct.unpack_from("<I", word_document, _FIB_IKEY_OFFSET)[0]
    return _FibInfo(
        f_encrypted=_bit(flags, _FIB_BIT_FENCRYPTED),
        f_obfuscation=_bit(flags, _FIB_BIT_FOBFUSCATION),
        f_which_tbl_stm=_bit(flags, _FIB_BIT_FWHICHTBLSTM),
        f_read_only=_bit(flags, _FIB_BIT_FREADONLY),
        f_write_reservation=_bit(flags, _FIB_BIT_FWRITERESERVATION),
        l_key=l_key,
    )


def _rc4_open_from_versioned(blob: bytes, md5_digit: int, second_block: bytes) -> _Rc4Open | None:
    """Build an :class:`_Rc4Open` from a stream that starts with the version words.

    Both the Word Table stream and the PowerPoint CryptSession10 payload begin
    with ``EncryptionVersionInfo`` (vMajor, vMinor) followed by either the RC4+MD5
    verifier or the RC4-CryptoAPI header.
    """
    if len(blob) < _ENC_VERSION_LEN:
        return None
    v_major, v_minor = struct.unpack_from("<HH", blob, 0)
    if (v_major, v_minor) == _RC4_MD5_VERSION:
        # RC4+MD5: salt(16) || encVerifier(16) || encVerifierHash(16) right after the words.
        if len(blob) < _ENC_VERSION_LEN + _RC4_MD5_HEADER_LEN:
            return None
        return _Rc4Open(
            scheme=Rc4Scheme.MD5,
            salt=blob[4:20],
            key_bits=_KEY_BITS_128,
            enc_verifier=blob[20:36],
            enc_verifier_hash=blob[36:52],
            digit=md5_digit,
        )
    return _rc4_open_from_cryptoapi(blob, second_block)


def _rc4_open_from_cryptoapi(blob: bytes, second_block: bytes) -> _Rc4Open | None:
    """Build an :class:`_Rc4Open` from an RC4-CryptoAPI header blob.

    The blob starts at ``EncryptionVersionInfo``; the provided crypto parser owns
    the field layout ([MS-OFFCRYPTO] Section 2.3.5.1). A ``keySize`` of 0 means
    40-bit per the spec.
    """
    try:
        info = rc4legacy.parse_rc4_cryptoapi_header(blob)
    except (ValueError, struct.error):
        return None
    key_bits = cast("int", info["key_size"]) or _KEY_BITS_40
    # [MS-OFFCRYPTO] Section 2.3.5: digit 3 = 40-bit (zero-padded key),
    # digit 4 = any size > 40-bit (key truncated to keyBits/8 bytes).
    digit = _DIGIT_CAPI_40 if key_bits == _KEY_BITS_40 else _DIGIT_CAPI_128
    return _Rc4Open(
        scheme=Rc4Scheme.CRYPTOAPI,
        salt=cast("bytes", info["salt"]),
        key_bits=key_bits,
        enc_verifier=cast("bytes", info["encrypted_verifier"]),
        enc_verifier_hash=cast("bytes", info["encrypted_verifier_hash"]),
        digit=digit,
        second_block=second_block if digit == _DIGIT_CAPI_40 else b"",
    )


def _doc_open(ole: olefile.OleFileIO, fib: _FibInfo) -> _Rc4Open | None:
    """Extract the Word document-open RC4 descriptor from the Table stream."""
    if not fib.f_encrypted or fib.f_obfuscation:
        return None  # unencrypted or XOR-obfuscated (handled elsewhere)
    table = _read_stream(ole, fib.table_stream)
    if table is None:
        return None
    second = table[_DOC_SECOND_BLOCK_OFFSET : _DOC_SECOND_BLOCK_OFFSET + _SECOND_BLOCK_LEN]
    return _rc4_open_from_versioned(table, _DIGIT_MD5_DOC, second)


# --- Word Table-stream structures ([MS-DOC] Section 2.5.6 / 2.7.2 / 2.9.276) ---


def _fclcb_pair(word_document: bytes, index: int) -> tuple[int, int] | None:
    """Return the ``(fc, lcb)`` pair at ``index`` of FibRgFcLcb97 ([MS-DOC] Section 2.5.6).

    The blob's position is not fixed: it follows the FibBase, the variable ``FibRgW``
    (``csw`` u16 values) and ``FibRgLw`` (``cslw`` u32 values), each length prefixed. We
    read ``csw``/``cslw``/``cbRgFcLcb`` from the FIB rather than assuming Word-97 sizes,
    so the same code locates ``fcDop`` (index 31) and ``fcSttbfAssoc`` (index 32) in any
    nFib. Returns ``None`` when the stream is too short or the index is out of range.
    """
    csw_offset = _FIB_BASE_LEN
    if len(word_document) < csw_offset + _U16_LEN:
        return None
    csw = struct.unpack_from("<H", word_document, csw_offset)[0]
    cslw_offset = csw_offset + _U16_LEN + csw * _U16_LEN
    if len(word_document) < cslw_offset + _U16_LEN:
        return None
    cslw = struct.unpack_from("<H", word_document, cslw_offset)[0]
    cbrgfclcb_offset = cslw_offset + _U16_LEN + cslw * 4
    if len(word_document) < cbrgfclcb_offset + _U16_LEN:
        return None
    cb_rg_fc_lcb = struct.unpack_from("<H", word_document, cbrgfclcb_offset)[0]
    blob = cbrgfclcb_offset + _U16_LEN
    if index >= cb_rg_fc_lcb:
        return None
    pair = blob + index * _FCLCB_PAIR_LEN
    if len(word_document) < pair + _FCLCB_PAIR_LEN:
        return None
    fc, lcb = struct.unpack_from("<II", word_document, pair)
    return int(fc), int(lcb)


@dataclass(frozen=True)
class _DopProtection:
    """The restrict-editing state read from ``Dop.DopBase`` ([MS-DOC] Section 2.7.2)."""

    l_key_prot_doc: int
    flags2: int
    table_offset: int  # byte offset of DopBase inside the Table stream

    @property
    def protected(self) -> bool:
        """Whether any restrict-editing lock (or the legacy verifier) is active."""
        return self.l_key_prot_doc != 0 or any((self.flags2 >> bit) & 1 for bit in _DOP_PROTECTION_BITS)


def _parse_dop_protection(word_document: bytes, table: bytes) -> _DopProtection | None:
    """Read ``DopBase.lKeyProtDoc`` and the fProt* flags from the Table-stream ``Dop``."""
    located = _fclcb_pair(word_document, _FCLCB_INDEX_DOP)
    if located is None:
        return None
    fc_dop, lcb_dop = located
    if lcb_dop < _DOP_LKEYPROTDOC_OFFSET + 4 or fc_dop + lcb_dop > len(table):
        return None
    flags2 = struct.unpack_from("<I", table, fc_dop + _DOP_FLAGS2_OFFSET)[0]
    l_key = struct.unpack_from("<I", table, fc_dop + _DOP_LKEYPROTDOC_OFFSET)[0]
    return _DopProtection(l_key_prot_doc=l_key, flags2=flags2, table_offset=fc_dop)


def _strip_dop_protection(table: bytes, dop: _DopProtection) -> bytes:
    """Zero ``lKeyProtDoc`` and clear the fProt* bits in a copy of the Table stream."""
    data = bytearray(table)
    struct.pack_into("<I", data, dop.table_offset + _DOP_LKEYPROTDOC_OFFSET, 0)
    flags2 = dop.flags2
    for bit in _DOP_PROTECTION_BITS:
        flags2 &= ~(1 << bit)
    struct.pack_into("<I", data, dop.table_offset + _DOP_FLAGS2_OFFSET, flags2)
    return bytes(data)


def _sttbf_assoc_string(word_document: bytes, table: bytes, index: int) -> str | None:
    """Return one SttbfAssoc string ([MS-DOC] Section 2.9.276), decoded from UTF-16LE.

    SttbfAssoc is an extended (Unicode) STTB with ``fExtend=0xFFFF`` and ``cbExtra=0``.
    Entry ``0x11`` holds the write-reservation ("password to modify") string in clear.
    Returns ``None`` when the table cannot be located or ``index`` is out of range.
    """
    located = _fclcb_pair(word_document, _FCLCB_INDEX_STTBF_ASSOC)
    if located is None:
        return None
    fc, lcb = located
    if lcb < _STTB_HEADER_LEN or fc + lcb > len(table):
        return None
    blob = table[fc : fc + lcb]
    if struct.unpack_from("<H", blob, 0)[0] != _STTB_EXTEND_MARKER:
        return None  # only the Unicode SttbfAssoc form is defined
    return _sttb_entry(blob, struct.unpack_from("<H", blob, 2)[0], index)


def _sttb_entry(blob: bytes, count: int, index: int) -> str | None:
    """Walk an extended (Unicode) STTB body and return entry ``index`` as text."""
    if index >= count:
        return None
    pos = _STTB_HEADER_LEN
    for i in range(count):
        if pos + _U16_LEN > len(blob):
            return None
        cch = struct.unpack_from("<H", blob, pos)[0]
        pos += _U16_LEN
        string_bytes = blob[pos : pos + cch * 2]
        pos += cch * 2
        if i == index:
            return string_bytes.decode("utf-16-le", errors="replace")
    return None


# --- BIFF (Excel) parsing ([MS-XLS] Section 2.1.7) -----------------------------


def _iter_biff(data: bytes) -> list[tuple[int, int, int]]:
    """Return ``(record_type, data_offset, size)`` for every BIFF record in ``data``."""
    records: list[tuple[int, int, int]] = []
    pos = 0
    length = len(data)
    while pos + 4 <= length:
        rt, size = struct.unpack_from("<HH", data, pos)
        body = pos + 4
        if body + size > length:
            break
        records.append((rt, body, size))
        pos = body + size
    return records


def _find_filepass(data: bytes) -> tuple[int, int] | None:
    """Return ``(data_offset, size)`` of the FilePass record, or ``None``."""
    for rt, offset, size in _iter_biff(data):
        if rt == _RT_FILEPASS:
            return offset, size
    return None


def _xls_open(workbook: bytes) -> _Rc4Open | None:
    """Extract the Excel RC4 document-open descriptor from the Workbook stream.

    Returns ``None`` for the XOR scheme (keyless) and for unencrypted workbooks;
    those are surfaced separately by the gate enumerator.
    """
    located = _find_filepass(workbook)
    if located is None:
        return None
    offset, size = located
    data = workbook[offset : offset + size]
    if len(data) < _U16_LEN:
        return None
    w_encryption_type = struct.unpack_from("<H", data, 0)[0]
    if w_encryption_type != _FILEPASS_RC4:
        return None  # XOR obfuscation (0x0000) -- not a keyed scheme
    second = workbook[_XLS_SECOND_BLOCK_OFFSET : _XLS_SECOND_BLOCK_OFFSET + _SECOND_BLOCK_LEN]
    return _rc4_open_from_versioned(data[2:], _DIGIT_MD5_XLS, second)


def _xls_xor_verifier(workbook: bytes) -> tuple[int, int] | None:
    """Return the ``(key, verifier)`` of an XOR-obfuscated Workbook, or ``None``."""
    located = _find_filepass(workbook)
    if located is None:
        return None
    offset, size = located
    data = workbook[offset : offset + size]
    if len(data) < _XOR_FILEPASS_LEN or struct.unpack_from("<H", data, 0)[0] != _FILEPASS_XOR:
        return None
    key, verifier = struct.unpack_from("<HH", data, 2)
    return int(key), int(verifier)


# --- Legacy XOR obfuscation decode ([MS-OFFCRYPTO] Section 2.3.7.3, xor-obfuscation.md) ---

# Well-known BIFF8 Globals records whose body is a fixed constant when Excel writes a
# workbook. These are used ONLY to narrow the password-free obfuscation-array search
# (see :func:`xor.reconstruct_password`); the final proof is always the 32-bit
# XorKey+verifier match, so a wrong guess here can never yield a wrong decode.
_XLS_XOR_KNOWN_PLAINTEXT: Final[dict[int, bytes]] = {
    0x0042: b"\xb0\x04",  # CodePage = 1200 ([MS-XLS] Section 2.4.52)
    0x0022: b"\x00\x00",  # Date1904 ([MS-XLS] Section 2.4.77)
    0x000E: b"\x01\x00",  # CalcPrecision ([MS-XLS] Section 2.4.53)
    0x0040: b"\x00\x00",  # Backup ([MS-XLS] Section 2.4.14)
    0x008D: b"\x00\x00",  # HideObj ([MS-XLS] Section 2.4.145)
    0x00DA: b"\x00\x00",  # BookBool ([MS-XLS] Section 2.4.20)
    0x01B7: b"\x00\x00",  # RefreshAll ([MS-XLS] Section 2.4.216)
    0x013D: b"\x01\x00",  # RRTabId, single sheet ([MS-XLS] Section 2.4.230)
    0x008C: b"\x01\x00\x01\x00",  # Country ([MS-XLS] Section 2.4.68)
}


def _rol5(value: int) -> int:
    """Rotate an 8-bit value left by five bits (inverse of the decode's ``ror5``)."""
    return ((value << 5) | (value >> 3)) & 0xFF


def _xls_xor_known_array(workbook: bytes) -> list[int | None]:
    """Pin obfuscation-array bytes from well-known Globals records ([MS-XLS] Section 2.2.10).

    For each trusted fixed-body record we invert the Method 1 decode
    (``plain = ror5(cipher XOR array[idx])`` implies ``array[idx] = cipher XOR ror5(plain)``)
    at every byte position, seeding the per-record array index from the record's end
    offset ([MS-OFFCRYPTO] Section 2.3.7.3, cross-checked against msoffcrypto-tool). The
    result is a 16-slot array with ``None`` where nothing was pinned.
    """
    known: list[int | None] = [None] * _XOR_ARRAY_SLOTS
    for rt, offset, size in _iter_biff(workbook):
        plaintext = _XLS_XOR_KNOWN_PLAINTEXT.get(rt)
        if plaintext is None or len(plaintext) != size:
            continue
        idx = (offset + size) % _XOR_ARRAY_SLOTS
        for i in range(size):
            if known[idx] is None:
                known[idx] = workbook[offset + i] ^ _rol5(plaintext[i])
            idx = (idx + 1) % _XOR_ARRAY_SLOTS
    return known


def _decode_xls_xor(workbook: bytes, xor_array: bytes) -> bytes:
    """Decode an XOR-obfuscated Workbook stream and neutralise its FilePass record.

    Implements the Excel side of [MS-XLS] Section 2.2.10 / [MS-OFFCRYPTO] Section 2.3.7.3:
    record framing (``rt``/``size``) and the exempt records stay in the clear, every
    other record body is run through the Method 1 transform, and the per-record array
    index is seeded from the record's end offset modulo 16. The BoundSheet8 ``lbPlyPos``
    prefix stays plaintext but still advances the index. Finally the FilePass record is
    blanked (``rt`` -> 0, body zeroed) exactly as msoffcrypto-tool does, so the output
    workbook is a valid, unencrypted stream of identical length.
    """
    out = bytearray(workbook)
    for rt, offset, size in _iter_biff(workbook):
        if rt in _BIFF_UNENCRYPTED:
            continue
        seed = offset + size  # per-record XorArrayIndex seed (record end offset)
        body = workbook[offset : offset + size]
        if rt == _RT_BOUNDSHEET8:
            keep = _BOUNDSHEET8_PLAINTEXT_PREFIX
            out[offset + keep : offset + size] = xor.xor_decode_method1(body[keep:], xor_array, seed + keep)
        else:
            out[offset : offset + size] = xor.xor_decode_method1(body, xor_array, seed)
    located = _find_filepass(workbook)
    if located is not None:
        _neutralize_filepass(out, located)
    return bytes(out)


def _neutralize_filepass(out: bytearray, located: tuple[int, int]) -> None:
    """Blank a FilePass record in place: zero its ``rt`` and its whole body."""
    body_offset, size = located
    struct.pack_into("<H", out, body_offset - 4, 0)  # rt -> 0 (record becomes a no-op)
    out[body_offset : body_offset + size] = bytes(size)


# --- Legacy 16-bit protection verifiers ([MS-XLS] Section 2.2.9 / xor-obfuscation.md) ---

# The wPassword hash sits at a different offset per record. Every value is a 16-bit
# CreatePasswordVerifier_Method1 output ([MS-OFFCRYPTO] Section 2.3.7.1) -- collidable.
_XLS_FILESHARING_VERIFIER_OFFSET: Final = 2  # wResPass sits at body+2 in FileSharing


@dataclass(frozen=True)
class _XlsProtection:
    """One readable 16-bit protection verifier and the gate it drives."""

    gate: GateType
    verifier: int
    where: str
    record_type: int
    verifier_offset: int


def _xls_protection_records(workbook: bytes) -> list[_XlsProtection]:
    """Enumerate every readable 16-bit protection verifier in a plaintext Workbook.

    Walks the BIFF record chain, tracking the enclosing substream via ``BOF.dt`` so a
    ``Password`` record (0x13) is routed to protect-WORKBOOK when it sits in the globals
    substream (``dt=0x0005``) and to protect-SHEET otherwise ([MS-XLS] Section 2.4.191 /
    excel.md). Also surfaces FileSharing (write-reservation), Prot4RevPass (shared
    revisions) and FeatProtection (allow-edit-ranges). Records whose verifier is 0 are
    skipped -- a zero hash means "protected, no password" and there is nothing to crack.
    """
    found: list[_XlsProtection] = []
    dt: int | None = None
    for rt, offset, size in _iter_biff(workbook):
        if rt == _RT_BOF and size >= _BOF_DT_OFFSET + _U16_LEN:
            dt = int(struct.unpack_from("<H", workbook, offset + _BOF_DT_OFFSET)[0])
            continue
        record = _xls_protection_from_record(workbook, rt, offset, size, dt)
        if record is not None:
            found.append(record)
    return found


def _parse_feat_protection(workbook: bytes, offset: int, size: int, rt: int) -> _XlsProtection | None:
    """Navigate the Feat record structure to extract the FeatProtection wPassword.

    A Feat record (rt=0x0867, [MS-XLS] Section 2.4.99) wraps per-feature data inside
    a variable-length header: isf(2) + reserved1(1) + reserved2(4) + cRef(2) followed
    by cRef Ref8 entries (8 bytes each), then cbFeatData(4) + reserved3(2), and finally
    the type-specific rgbFeat payload. For ISFPROTECTION (isf=2), rgbFeat is a
    FeatProtection struct: fSD(4) + wPassword(2) ([MS-XLS] Section 2.5.124). Returns
    ``None`` when the record is not a protection Feat, is truncated, or has no password.
    """
    data = workbook[offset : offset + size]
    if len(data) < _FEAT_HEADER_FIXED:
        return None
    isf = struct.unpack_from("<H", data, 0)[0]
    if isf != _FEAT_ISF_PROTECTION:
        return None
    c_ref = struct.unpack_from("<H", data, 7)[0]
    refs_end = _FEAT_HEADER_FIXED + c_ref * _FEAT_REF8_SIZE
    payload_start = refs_end + _FEAT_CBFEATDATA_SIZE + _FEAT_RESERVED3_SIZE
    wpassword_offset = payload_start + _FEAT_FSD_SIZE
    if wpassword_offset + _U16_LEN > len(data):
        return None
    verifier = struct.unpack_from("<H", data, wpassword_offset)[0]
    if not verifier:
        return None
    return _XlsProtection(GateType.ALLOW_EDIT_RANGES, verifier, f"Feat/FeatProtection record (rt=0x867, isf=2, wPassword at body+0x{wpassword_offset:02X})", rt, wpassword_offset)


def _xls_protection_from_record(workbook: bytes, rt: int, offset: int, size: int, dt: int | None) -> _XlsProtection | None:
    """Route a BIFF record to the appropriate protection verifier parser, or ``None``."""
    if rt == _RT_PASSWORD and size >= _U16_LEN:
        verifier = struct.unpack_from("<H", workbook, offset)[0]
        in_globals = dt == _BOF_DT_GLOBALS
        gate = GateType.PROTECT_WORKBOOK if in_globals else GateType.PROTECT_SHEET
        where = "Password record (rt=0x13) in the " + ("globals substream" if in_globals else "worksheet substream")
        return _XlsProtection(gate, verifier, where, rt, 0) if verifier else None
    if rt == _RT_FILESHARING and size >= _XLS_FILESHARING_VERIFIER_OFFSET + _U16_LEN:
        verifier = struct.unpack_from("<H", workbook, offset + _XLS_FILESHARING_VERIFIER_OFFSET)[0]
        return _XlsProtection(GateType.MODIFY, verifier, "FileSharing record (rt=0x5B, wResPass)", rt, _XLS_FILESHARING_VERIFIER_OFFSET) if verifier else None
    if rt == _RT_PROT4REVPASS and size >= _U16_LEN:
        verifier = struct.unpack_from("<H", workbook, offset)[0]
        return _XlsProtection(GateType.SHARED_REVISIONS, verifier, "Prot4RevPass record (rt=0x1BC)", rt, 0) if verifier else None
    if rt == _RT_FEAT:
        return _parse_feat_protection(workbook, offset, size, rt)
    return None


def _strip_xls_verifiers(workbook: bytes) -> bytes | None:
    """Zero every readable 16-bit protection verifier, or ``None`` if there were none.

    Overwrites each ``wPassword``/``wResPass`` hash with 0 (an empty password), a
    same-size edit that leaves the record framing intact so the Workbook stream can be
    written back in place. This lifts sheet/workbook/range/write-reservation protection
    without cracking ([MS-XLS] Section 2.2.9).
    """
    data = bytearray(workbook)
    changed = False
    dt: int | None = None
    for rt, offset, size in _iter_biff(workbook):
        if rt == _RT_BOF and size >= _BOF_DT_OFFSET + _U16_LEN:
            dt = int(struct.unpack_from("<H", workbook, offset + _BOF_DT_OFFSET)[0])
            continue
        record = _xls_protection_from_record(workbook, rt, offset, size, dt)
        if record is not None:
            old_val = struct.unpack_from("<H", data, offset + record.verifier_offset)[0]
            struct.pack_into("<H", data, offset + record.verifier_offset, 0)
            logger.debug("strip: zeroed %s at offset 0x%04x (was 0x%04x)", record.gate.value, offset + record.verifier_offset, old_val)
            changed = True
    if changed:
        logger.debug("strip: verifiers zeroed")
    return bytes(data) if changed else None


# --- PowerPoint parsing ([MS-PPT] Section 2.1.2) -------------------------------


def _ppt_offset_to_current_edit(current_user: bytes) -> int | None:
    """Read ``offsetToCurrentEdit`` from the CurrentUserAtom."""
    if len(current_user) < _CURRENTUSER_EDIT_OFFSET + 4:
        return None
    return cast("int", struct.unpack_from("<I", current_user, _CURRENTUSER_EDIT_OFFSET)[0])


def _ppt_parse_rh(data: bytes, offset: int) -> tuple[int, int] | None:
    """Parse a PowerPoint RecordHeader at ``offset`` -> ``(recType, recLen)``."""
    if offset < 0 or offset + _PPT_RH_LEN > len(data):
        return None
    rec_type = int(struct.unpack_from("<H", data, offset + 2)[0])
    rec_len = int(struct.unpack_from("<I", data, offset + 4)[0])
    return rec_type, rec_len


@dataclass(frozen=True)
class _UserEdit:
    """The UserEditAtom fields needed to find the encryption container ([MS-PPT] Section 2.3.3)."""

    rec_len: int
    offset_last_edit: int
    offset_persist_directory: int
    encrypt_session_persist_id_ref: int | None


def _ppt_parse_user_edit(ppt: bytes, offset: int) -> _UserEdit | None:
    """Parse the UserEditAtom at ``offset`` in the PowerPoint Document stream."""
    header = _ppt_parse_rh(ppt, offset)
    if header is None or header[0] != _RT_USEREDITATOM:
        return None
    _, rec_len = header
    base = offset + _PPT_RH_LEN
    if base + 0x1C > len(ppt):
        return None
    offset_last_edit = struct.unpack_from("<I", ppt, base + 8)[0]
    offset_persist_directory = struct.unpack_from("<I", ppt, base + 12)[0]
    enc_ref: int | None = None
    if rec_len == _USEREDITATOM_ENCRYPTED_LEN and base + 0x20 <= len(ppt):
        enc_ref = int(struct.unpack_from("<I", ppt, base + 28)[0])
    return _UserEdit(rec_len=rec_len, offset_last_edit=offset_last_edit, offset_persist_directory=offset_persist_directory, encrypt_session_persist_id_ref=enc_ref)


def _ppt_persist_entries(ppt: bytes, directory_offset: int) -> dict[int, int]:
    """Parse one PersistDirectoryAtom into a ``{persistId: streamOffset}`` map."""
    header = _ppt_parse_rh(ppt, directory_offset)
    if header is None or header[0] != _RT_PERSISTDIRECTORYATOM:
        return {}
    _, rec_len = header
    entries: dict[int, int] = {}
    pos = directory_offset + _PPT_RH_LEN
    end = min(pos + rec_len, len(ppt))
    while pos + 4 <= end:
        packed = struct.unpack_from("<I", ppt, pos)[0]
        pos += 4
        persist_id = packed & 0xFFFFF
        c_persist = (packed >> 20) & 0xFFF
        for i in range(c_persist):
            if pos + 4 > end:
                break
            entries[persist_id + i] = struct.unpack_from("<I", ppt, pos)[0]
            pos += 4
    return entries


@dataclass(frozen=True)
class _PptEditChain:
    """The merged persist-object directory plus the active encryption reference."""

    directory: dict[int, int]
    encrypt_session_persist_id_ref: int | None
    current_edit_offset: int


def _ppt_build_chain(current_user: bytes, ppt: bytes) -> _PptEditChain | None:
    """Walk the UserEditAtom chain to build the persist directory ([MS-PPT] Section 2.1.2)."""
    start = _ppt_offset_to_current_edit(current_user)
    if start is None:
        return None
    edits: list[_UserEdit] = []
    offset = start
    seen: set[int] = set()
    while offset not in seen:
        seen.add(offset)
        edit = _ppt_parse_user_edit(ppt, offset)
        if edit is None:
            break
        edits.append(edit)
        if edit.offset_last_edit == 0:
            break
        offset = edit.offset_last_edit
    if not edits:
        return None
    # Merge oldest-first so newer PersistDirectoryAtoms override older offsets.
    directory: dict[int, int] = {}
    for edit in reversed(edits):
        directory.update(_ppt_persist_entries(ppt, edit.offset_persist_directory))
    return _PptEditChain(directory=directory, encrypt_session_persist_id_ref=edits[0].encrypt_session_persist_id_ref, current_edit_offset=start)


def _ppt_open(current_user: bytes, ppt: bytes) -> _Rc4Open | None:
    """Extract the PowerPoint RC4-CryptoAPI document-open descriptor."""
    chain = _ppt_build_chain(current_user, ppt)
    if chain is None or chain.encrypt_session_persist_id_ref is None:
        return None
    container_offset = chain.directory.get(chain.encrypt_session_persist_id_ref)
    if container_offset is None:
        return None
    header = _ppt_parse_rh(ppt, container_offset)
    if header is None or header[0] != _RT_CRYPTSESSION10CONTAINER:
        return None
    _, rec_len = header
    payload = ppt[container_offset + _PPT_RH_LEN : container_offset + _PPT_RH_LEN + rec_len]
    second = ppt[_PPT_SECOND_BLOCK_OFFSET : _PPT_SECOND_BLOCK_OFFSET + _SECOND_BLOCK_LEN]
    return _rc4_open_from_cryptoapi(payload, second)


# --- PowerPoint ModifyPasswordAtom ([MS-PPT] Section 2.4.7) --------------------


@dataclass(frozen=True)
class _PptModifyPassword:
    """A located ModifyPasswordAtom: its body offset, byte length and cleartext value."""

    body_offset: int
    length: int
    password: str


def _ppt_find_modify_password(ppt: bytes) -> _PptModifyPassword | None:
    """Find the ModifyPasswordAtom by walking the record tree ([MS-PPT] Section 2.4.7).

    The atom is a ``RT_CString`` (0x0FBA) with ``recInstance=0x003`` whose body is the
    modify password as a ``PrintableUnicodeString`` (UTF-16LE, no terminator). It lives
    inside a ``PP10DocBinaryTagExtension`` off the ``DocumentContainer``; rather than
    hard-code that path we recurse into every container (``recVer=0xF``) and match the
    atom directly. Returns ``None`` when the stream carries no modify password.
    """
    return _ppt_scan_modify_password(ppt, 0, len(ppt))


def _ppt_scan_modify_password(ppt: bytes, start: int, end: int) -> _PptModifyPassword | None:
    """Recursively scan ``ppt[start:end]`` for the ModifyPasswordAtom."""
    pos = start
    while pos + _PPT_RH_LEN <= end:
        ver_inst = struct.unpack_from("<H", ppt, pos)[0]
        rec_type = struct.unpack_from("<H", ppt, pos + 2)[0]
        rec_len = struct.unpack_from("<I", ppt, pos + 4)[0]
        body = pos + _PPT_RH_LEN
        if body + rec_len > end:
            return None  # truncated record -- stop scanning this level
        rec_ver = ver_inst & 0x0F
        rec_instance = ver_inst >> 4
        if rec_type == _RT_CSTRING and rec_instance == _MODIFY_PASSWORD_INSTANCE and rec_len <= _PPT_MODIFY_MAX_LEN:
            password = ppt[body : body + rec_len].decode("utf-16-le", errors="replace")
            return _PptModifyPassword(body_offset=body, length=rec_len, password=password)
        if rec_ver == _PPT_RECVER_CONTAINER:
            nested = _ppt_scan_modify_password(ppt, body, body + rec_len)
            if nested is not None:
                return nested
        pos = body + rec_len
    return None


def _ppt_strip_modify_password(ppt: bytes, atom: _PptModifyPassword) -> bytes:
    """Blank a ModifyPasswordAtom body in place (same-size), clearing the password.

    olefile can only overwrite a stream with one of identical length, so the atom cannot
    be deleted; zeroing the ``modifyPassword`` bytes turns it into an empty password,
    which lifts the "password to modify" prompt. Deleting the record outright would need
    a resizing CFB rewrite (out of scope for the in-place writer).
    """
    data = bytearray(ppt)
    data[atom.body_offset : atom.body_offset + atom.length] = bytes(atom.length)
    return bytes(data)


# --- VBA project lock ([MS-OVBA] Section 2.3.1) --------------------------------


def _find_project_stream(ole: olefile.OleFileIO) -> list[str] | None:
    """Locate the PROJECT stream path of an embedded VBA project, if any."""
    for entry in ole.listdir(streams=True, storages=False):
        if entry and entry[-1].upper() == "PROJECT" and len(entry) >= _MIN_VBA_PATH_DEPTH:
            return list(entry)
    return None


def _project_dpb(project_text: str) -> str | None:
    """Return the ``DPB`` value (uppercase hex) from a PROJECT INI stream."""
    for raw in project_text.splitlines():
        line = raw.strip()
        if line.upper().startswith("DPB="):
            return line[4:].strip().strip('"')
    return None


def _vba_dpb(ole: olefile.OleFileIO) -> str | None:
    """Return the raw DPB hex value from an embedded VBA project, or ``None``."""
    project_path = _find_project_stream(ole)
    if project_path is None:
        return None
    raw = _read_stream(ole, project_path)
    if raw is None:
        return None
    return _project_dpb(raw.decode("latin-1", errors="replace"))


def _vba_hash_line(ole: olefile.OleFileIO) -> str | None:
    """Return the hashcat -m 110 line for a hash-protected VBA project, or ``None``."""
    dpb = _vba_dpb(ole)
    if not dpb:
        return None
    try:
        return vba.extract_vba_hash(dpb)
    except (ValueError, struct.error, IndexError):
        return None


# The classic same-size bypass renames DPB= to DPx= so the VBE cannot find the password
# state and opens the project unprotected ([MS-OVBA]; vba-project-password.md Section 8).
_DPB_KEY: Final = "DPB="
_DPX_KEY: Final = "DPx="
_CMG_KEY: Final = "CMG="
_CMG_CLEAR_STATE: Final = b"\x00\x00\x00\x00"  # ProjectProtectionState with no bits set


def _clear_vba_protection(project_raw: bytes) -> bytes | None:
    """Return a same-length PROJECT stream with the VBA project lock cleared, or ``None``.

    Two edits, both length-preserving so ``olefile.write_stream`` can store them in place:

    * ``CMG`` -- decode the ProjectProtectionState, clear every protection bit, and re-encode
      with the ORIGINAL seed and ProjKey (:func:`vba.decode_data_encryption` /
      :func:`vba.encode_data_encryption`), which reproduces the exact hex length.
    * ``DPB`` -- rename the key to ``DPx`` so the password state is ignored ([MS-OVBA]
      Section 2.3.1.16). The macro source is never encrypted, so this opens it unprotected.

    Returns ``None`` when the stream carries no ``CMG``/``DPB`` protection lines.
    """
    text = project_raw.decode("latin-1")
    out_lines: list[str] = []
    changed = False
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        upper = stripped.upper()
        if upper.startswith(_CMG_KEY):
            rebuilt = _rewrite_cmg_line(line)
            out_lines.append(rebuilt)
            changed = changed or rebuilt != line
        elif upper.startswith(_DPB_KEY):
            out_lines.append(line[: line.upper().index(_DPB_KEY)] + _DPX_KEY + line.split("=", 1)[1])
            changed = True
        else:
            out_lines.append(line)
    if not changed:
        return None
    result = "".join(out_lines).encode("latin-1")
    if len(result) != len(project_raw):
        return None  # refuse to emit a different-size stream (the in-place writer needs same size)
    return result


def _rewrite_cmg_line(line: str) -> str:
    """Re-encode a ``CMG=`` line with all protection bits cleared, preserving its length."""
    prefix_len = line.upper().index(_CMG_KEY) + len(_CMG_KEY)
    prefix, value = line[:prefix_len], line[prefix_len:]
    quote = '"' if value.lstrip().startswith('"') else ""
    hex_value = value.strip().strip('"')
    try:
        encrypted = bytes.fromhex(hex_value)
        seed = encrypted[0]
        proj_key = encrypted[0] ^ encrypted[2]
        cleared = vba.encode_data_encryption(_CMG_CLEAR_STATE, seed, proj_key)
    except (ValueError, IndexError):
        return line  # malformed CMG -- leave it untouched rather than corrupt the stream
    if len(cleared) != len(hex_value):
        return line  # different length -- cannot substitute in place
    return f"{prefix}{quote}{cleared}{quote}" + value[len(value.rstrip()) :]


# --- Modern (ECMA-376 wrapper) helpers -----------------------------------------


def _modern_scheme(info: ecma376.EncryptionInfo) -> tuple[HashScheme | None, int | None]:
    """Map a parsed EncryptionInfo to its ``(HashScheme, hashcat_mode)``.

    Returns ``(None, None)`` for agile tuples with no hashcat mode (a documented
    GAP -- real encryption, but no single mode ingests it).
    """
    if info.kind is ecma376.EncryptionKind.STANDARD:
        return HashScheme.OFFICE_2007, 9400
    algo = info.hash_algorithm.upper().replace("-", "")
    if algo == "SHA1" and info.key_bits == _KEY_BITS_128:
        return HashScheme.OFFICE_2010, 9500
    if algo == "SHA512" and info.key_bits == _KEY_BITS_256:
        return HashScheme.OFFICE_2013, 9600
    return None, None


def _default_candidates(app: str | None, password: str) -> list[str]:
    """Ordered password candidates for decrypt: the caller's, then app defaults.

    The empty string and the spec-fixed defaults (VelvetSweatshop for Excel,
    ``/01Hannes Ruescher/01`` for PowerPoint) cover the auto-encrypted files that
    round-trip an encrypted stream while opening with no prompt.
    """
    candidates = [password, ""]
    if app in (_LegacyApp.XLS, None):
        candidates.append(DEFAULT_PASSWORD_EXCEL)
    if app in (_LegacyApp.PPT, None):
        candidates.append(DEFAULT_PASSWORD_POWERPOINT)
    seen: set[str] = set()
    ordered: list[str] = []
    for candidate in candidates:
        if candidate not in seen:
            seen.add(candidate)
            ordered.append(candidate)
    return ordered


# --- In-place stream decryption (legacy) ---------------------------------------


def _rc4_params(open_info: _Rc4Open, block_size: int) -> Rc4StreamParams:
    """Build the per-app stream-walk parameters for :func:`rc4legacy.decrypt_stream`."""
    return Rc4StreamParams(scheme=open_info.scheme, key_bits=open_info.key_bits, block_size=block_size)


def _clear_fib_encryption(word_document: bytes) -> bytes:
    """Return the 68-byte FIB prefix with fEncrypted/fObfuscation and lKey cleared.

    Both the RC4 and XOR decode paths must mark the decoded WordDocument stream as
    plaintext ([MS-DOC] Section 2.5.2): the encryption flags are turned off and the
    ``IKey``/``lKey`` field is zeroed so nothing re-reads the (now stale) verifier.
    """
    header = bytearray(word_document[:_FIB_LEN])
    flags = struct.unpack_from("<H", header, _FIB_FLAGS_OFFSET)[0]
    flags &= ~(1 << _FIB_BIT_FENCRYPTED)
    flags &= ~(1 << _FIB_BIT_FOBFUSCATION)
    struct.pack_into("<H", header, _FIB_FLAGS_OFFSET, flags)
    struct.pack_into("<I", header, _FIB_IKEY_OFFSET, 0)
    return bytes(header)


def _xls_xor_password_ok(password: str, key: int, verifier: int) -> bool:
    """Whether ``password`` reproduces the stored Excel XorKey and 16-bit verifier."""
    try:
        return xor.create_xor_key_method1(password) == key and xor.password_verifier_method1(password) == verifier
    except ValueError:
        return False  # empty / oversized candidate can never be the XOR password


def _doc_xor_password_ok(password: str, l_key: int) -> bool:
    """Whether ``password`` reproduces the stored Word 32-bit lKey verifier."""
    try:
        return xor.password_verifier_method2(password) == l_key
    except ValueError:
        return False


def _decrypt_doc_streams(ole: olefile.OleFileIO, password: str, open_info: _Rc4Open) -> dict[str, bytes]:
    """Decrypt the WordDocument, Table and (optional) Data streams ([MS-OFFCRYPTO] Section 2.3.6)."""
    params = _rc4_params(open_info, _DOC_BLOCK_SIZE)
    result: dict[str, bytes] = {}
    word_document = _read_stream(ole, _WORD_DOCUMENT)
    if word_document is None:
        return result
    # Rebuild the FIB prefix in the clear, then splice in the decrypted body from 0x44 on.
    decrypted = rc4legacy.decrypt_stream(password, open_info.salt, word_document, params)
    result[_WORD_DOCUMENT] = _clear_fib_encryption(word_document) + decrypted[_FIB_LEN:]

    fib = _parse_fib(word_document)
    if fib is not None:
        table = _read_stream(ole, fib.table_stream)
        if table is not None:
            result[fib.table_stream] = rc4legacy.decrypt_stream(password, open_info.salt, table, params)
    data = _read_stream(ole, "Data")
    if data is not None:
        result["Data"] = rc4legacy.decrypt_stream(password, open_info.salt, data, params)
    return result


_KEEP: Final = -1  # overlay sentinel: keep the RC4-decrypted byte at this position


def _build_xls_buffers(records: list[tuple[int, int, int]], workbook: bytes) -> tuple[bytearray, list[int]]:
    """Split the Workbook into (ciphertext-to-decrypt, plaintext-overlay) buffers.

    ``encrypted`` carries the real ciphertext at data positions and zeros at record
    headers / exempt records so the block-RC4 keystream stays byte-aligned with the
    original stream. ``overlay`` marks each byte as keep-decrypted (``_KEEP``) or as
    a literal plaintext byte to restore ([MS-XLS] Section 2.4.117 exemption list).
    """
    encrypted = bytearray()
    overlay: list[int] = []
    for rt, offset, size in records:
        body = workbook[offset : offset + size]
        header = struct.pack("<HH", rt, size)
        if rt == _RT_FILEPASS:
            # Neutralise FilePass: zero its type so the output workbook is unencrypted.
            overlay += [0, 0, *struct.pack("<H", size), *([0] * size)]
            encrypted += bytes(4 + size)
        elif rt in _BIFF_UNENCRYPTED:
            overlay += [*header, *body]
            encrypted += bytes(4 + size)
        elif rt == _RT_BOUNDSHEET8:
            overlay += [*header, *body[:4], *([_KEEP] * (size - 4))]
            encrypted += bytes(8) + body[4:]
        else:
            overlay += [*header, *([_KEEP] * size)]
            encrypted += bytes(4) + body
    # Trailing bytes after the last BIFF record (stream padding) are plaintext;
    # they must be included so the output matches the original stream length.
    consumed = len(encrypted)
    if consumed < len(workbook):
        tail = workbook[consumed:]
        encrypted += tail
        overlay += list(tail)
    return encrypted, overlay


def _decrypt_xls_workbook(password: str, open_info: _Rc4Open, workbook: bytes) -> bytes:
    """Decrypt the Excel Workbook stream, preserving the exempt records verbatim."""
    records = _iter_biff(workbook)
    encrypted, overlay = _build_xls_buffers(records, workbook)
    params = _rc4_params(open_info, _XLS_BLOCK_SIZE)
    out = bytearray(rc4legacy.decrypt_stream(password, open_info.salt, bytes(encrypted), params))
    # Overlay literal plaintext bytes; _KEEP positions retain the decrypted value.
    for i, marker in enumerate(overlay):
        if marker != _KEEP:
            out[i] = marker
    return bytes(out[: len(workbook)])


# --- PowerPoint stream decryption ([MS-PPT] Section 2.3) -----------------------


def _decrypt_ppt_document(password: str, open_info: _Rc4Open, chain: _PptEditChain, ppt: bytes) -> bytes:
    """Decrypt every persist object, zero the CryptSession10Container, mark unencrypted.

    Per ppt97 in msoffcrypto-tool the current UserEditAtom's ``recLen`` is trimmed
    from ``0x20`` to ``0x1C`` so the dropped ``encryptSessionPersistIdRef`` field is
    no longer read -- a same-size edit that leaves the stream length intact.
    """
    out = bytearray(ppt)
    offsets = sorted(set(chain.directory.values()))
    for index, offset in enumerate(offsets):
        header = _ppt_parse_rh(ppt, offset)
        if header is None:
            continue
        rec_type, rec_len = header
        if rec_type == _RT_CRYPTSESSION10CONTAINER:
            out[offset : offset + _PPT_RH_LEN + rec_len] = bytes(_PPT_RH_LEN + rec_len)  # drop the container
            continue
        if rec_type in (_RT_USEREDITATOM, _RT_PERSISTDIRECTORYATOM):
            continue
        end = offsets[index + 1] if index + 1 < len(offsets) else len(ppt)
        block_bytes = end - offset
        persist_id = next((pid for pid, off in chain.directory.items() if off == offset), 0)
        # Each persist object is one RC4 block keyed by its persist_id -- no re-keying
        # within the object. Set block_size > block_bytes so decrypt_stream derives
        # one key for the whole span (msoffcrypto-tool ppt97 model).
        block_size = block_bytes + open_info.key_bits
        params = Rc4StreamParams(scheme=Rc4Scheme.CRYPTOAPI, key_bits=open_info.key_bits, block_size=block_size, first_block=persist_id)
        out[offset : offset + block_bytes] = rc4legacy.decrypt_stream(password, open_info.salt, ppt[offset : offset + block_bytes], params)
    _clear_ppt_encryption_marker(out, chain)
    return bytes(out[: len(ppt)])


def _clear_ppt_encryption_marker(ppt: bytearray, chain: _PptEditChain) -> None:
    """Trim the current UserEditAtom recLen so the encryption reference is dropped."""
    start = chain.current_edit_offset
    header = _ppt_parse_rh(bytes(ppt), start)
    if header is None or header[0] != _RT_USEREDITATOM or header[1] != _USEREDITATOM_ENCRYPTED_LEN:
        return
    struct.pack_into("<I", ppt, start + 4, _USEREDITATOM_PLAIN_LEN)


# --- Gate construction ---------------------------------------------------------


def _rc4_open_gate(app: str, open_info: _Rc4Open, opens_with_default: str | None) -> Gate:
    """Build the Open-password gate for a legacy RC4 scheme."""
    where = {
        _LegacyApp.DOC: "WordDocument FibBase + Table stream encryption header",
        _LegacyApp.XLS: "Workbook FilePass record (rt=0x2F)",
        _LegacyApp.PPT: "CryptSession10Container via Current User -> UserEditAtom",
    }[app]
    if opens_with_default is not None:
        return Gate(gate=GateType.OPEN, recovery=RecoveryClass.DEFAULT, scheme=open_info.hash_scheme, hashcat_mode=open_info.hashcat_mode, where=where, note=f"opens with the default password {opens_with_default!r}")
    recovery = RecoveryClass.KEYSPACE if open_info.is_forty_bit else RecoveryClass.CRACK
    note = "40-bit RC4 -- brute the 2^40 key directly (faster than the password)" if open_info.is_forty_bit else f"{open_info.key_bits}-bit RC4 -- extract and crack the SHA-1 verifier"
    return Gate(gate=GateType.OPEN, recovery=recovery, scheme=open_info.hash_scheme, hashcat_mode=open_info.hashcat_mode, where=where, note=note)


def _vba_gate(ole: olefile.OleFileIO) -> Gate | None:
    """Build the VBA-project-lock gate if an embedded project is present."""
    if _find_project_stream(ole) is None:
        return None
    has_hash = _vba_hash_line(ole) is not None
    scheme = HashScheme.VBA_SHA1 if has_hash else None
    mode = 110 if has_hash else None
    note = "macro source is not encrypted -- clear the DPB/CMG lock (crack the SHA-1 verifier only for the literal password)"
    return Gate(gate=GateType.VBA_PROJECT, recovery=RecoveryClass.STRIP, scheme=scheme, hashcat_mode=mode, where="embedded VBA storage -> PROJECT stream (DPB=)", note=note)


def _signature_gate(names: set[str]) -> Gate | None:
    """Build the digital-signature gate if a ``_signatures`` stream is present."""
    if _SIGNATURES not in names:
        return None
    return Gate(gate=GateType.SIGNATURE, recovery=RecoveryClass.NONE, where=_SIGNATURES, note="public-key integrity -- run `opt bypass --remove-signatures` to drop the claim; never recoverable")


def _irm_gate(names: set[str]) -> Gate | None:
    """Build the IRM gate if a ``DRMContent`` storage is present (MSG files with RMS protection)."""
    if not any(n.lower() == "drmcontent" for n in names):
        return None
    return Gate(gate=GateType.IRM, recovery=RecoveryClass.NONE, where="DRMContent storage (IRM/RMS)", note="message encrypted with Azure RMS -- requires the RMS server and recipient credentials; not password-recoverable")


class OleHandler(FormatHandler):
    """Handler for the OLE Compound File Binary container ([MS-CFB])."""

    container = ContainerKind.OLE_CFB

    # --- Public API ------------------------------------------------------------

    @override
    def is_encrypted(self, path: Path) -> bool:
        """Report document-open encryption that needs a key (see module docstring)."""
        try:
            with olefile.OleFileIO(str(path)) as ole:
                names = _stream_names(ole)
                if _has_stream(names, _ENCRYPTION_INFO):
                    logger.debug("is_encrypted: EncryptionInfo present (modern wrapper)")
                    return True  # modern wrapper: the OPC package is AES-encrypted
                result = self._legacy_needs_key(ole, names)
                logger.debug("is_encrypted: legacy_needs_key=%s", result)
                return result
        except _PARSE_ERRORS:
            return False

    @override
    def gates(self, path: Path) -> list[Gate]:
        """Enumerate every password/permission gate present in ``path``."""
        try:
            with olefile.OleFileIO(str(path)) as ole:
                names = _stream_names(ole)
                if _has_stream(names, _ENCRYPTION_INFO):
                    logger.debug("gates: routing=modern")
                    gates = self._modern_gates(ole)
                    logger.debug("gates: %d gates enumerated", len(gates))
                    return gates
                logger.debug("gates: routing=legacy")
                gates = self._legacy_gates(ole, names)
                logger.debug("gates: %d gates enumerated", len(gates))
                return gates
        except _PARSE_ERRORS:
            return []

    @override
    def extract(self, path: Path) -> list[ExtractedHash]:
        """Extract crackable hash lines (open hash + VBA 110)."""
        try:
            with olefile.OleFileIO(str(path)) as ole:
                names = _stream_names(ole)
                if _has_stream(names, _ENCRYPTION_INFO):
                    logger.debug("extract: routing=modern")
                    hashes = self._modern_hashes(ole)
                else:
                    logger.debug("extract: routing=legacy")
                    hashes = self._legacy_hashes(ole, names)
                logger.debug("extract: %d hashes", len(hashes))
                return hashes
        except _PARSE_ERRORS:
            return []

    @override
    def bypass(self, path: Path, out: Path, *, remove_signatures: bool = False) -> int:
        """Copy ``path`` to ``out`` with removable (non-encrypting) protection cleared.

        The edits are computed from the input BEFORE ``out`` is written, so an honest
        failure (e.g. an XOR-obfuscated workbook whose array cannot be reconstructed)
        raises out of here instead of silently leaving a byte-identical copy behind.

        When ``remove_signatures`` is set, the legacy ``_signatures`` stream is zeroed
        so the digital signature no longer validates -- opt-in and destructive. (CFB
        streams can only be overwritten in place, not deleted, so the emptied stream
        remains but the signature blob is gone.)
        """
        try:
            with olefile.OleFileIO(str(path)) as ole:
                names = _stream_names(ole)
                app = _classify_legacy(names)
        except _PARSE_ERRORS:
            shutil.copyfile(str(path), str(out))
            return 0  # unreadable container -- a faithful copy is the best we can do
        edits = self._bypass_edits(path, app, remove_signatures=remove_signatures)  # may raise ValueError on an honest failure
        logger.debug("bypass: app=%s edits=%d", app or "unknown", len(edits))
        shutil.copyfile(str(path), str(out))
        if not edits:
            return 0  # nothing removable -- a faithful copy is still the correct output
        with olefile.OleFileIO(str(out), write_mode=True) as out_ole:
            for stream_path, data in edits.items():
                logger.debug("bypass: writing %s (%d bytes)", stream_path, len(data))
                out_ole.write_stream(stream_path.split("/"), data)
        return len(edits)

    @override
    def decrypt(self, path: Path, out: Path, password: str) -> None:
        """Decrypt the document-open gate to ``out`` (raises ``ValueError`` if wrong)."""
        with olefile.OleFileIO(str(path)) as ole:
            names = _stream_names(ole)
            if _has_stream(names, _ENCRYPTION_INFO):
                logger.debug("decrypt: routing=modern")
                self._decrypt_modern(ole, out, password)
                return
            app = _classify_legacy(names)
            logger.debug("decrypt: routing=legacy app=%s", app)
            self._decrypt_legacy(ole, path, out, password, app)

    # --- Modern wrapper --------------------------------------------------------

    def _modern_info(self, ole: olefile.OleFileIO) -> ecma376.EncryptionInfo | None:
        """Parse the EncryptionInfo stream, or ``None`` for CryptoAPI-RC4/IRM."""
        blob = _read_stream(ole, _ENCRYPTION_INFO)
        if blob is None:
            return None
        try:
            return ecma376.parse_encryption_info(blob)
        except ValueError:
            return None

    def _modern_gates(self, ole: olefile.OleFileIO) -> list[Gate]:
        """Build the Open (and IRM) gate for a modern encrypted package."""
        info = self._modern_info(ole)
        if info is None:
            return self._modern_gate_fallback(ole)
        scheme, mode = _modern_scheme(info)
        opens_with_default = self._modern_default(info)
        if opens_with_default is not None:
            return [Gate(gate=GateType.OPEN, recovery=RecoveryClass.DEFAULT, scheme=scheme, hashcat_mode=mode, where=_ENCRYPTION_INFO, note=f"opens with the default password {opens_with_default!r}")]
        recovery = RecoveryClass.CRACK
        note = "" if mode is not None else "agile tuple has no hashcat mode -- GAP"
        return [Gate(gate=GateType.OPEN, recovery=recovery, scheme=scheme, hashcat_mode=mode, where=_ENCRYPTION_INFO, note=note)]

    def _modern_gate_fallback(self, ole: olefile.OleFileIO) -> list[Gate]:
        """Gate for the CryptoAPI-RC4 wrapper / IRM cases parse_encryption_info rejects."""
        blob = _read_stream(ole, _ENCRYPTION_INFO)
        if blob is None or len(blob) < _ENC_VERSION_LEN:
            return []
        v_minor = struct.unpack_from("<H", blob, 2)[0]
        if v_minor == _VERSION_MINOR_EXTENSIBLE:
            return [Gate(gate=GateType.IRM, recovery=RecoveryClass.NONE, where=_ENCRYPTION_INFO, note="extensible/IRM -- content key is off-file, not recoverable")]
        open_info = _rc4_open_from_cryptoapi(blob, b"")
        if open_info is None:
            return []
        return [Gate(gate=GateType.OPEN, recovery=RecoveryClass.CRACK, scheme=open_info.hash_scheme, hashcat_mode=open_info.hashcat_mode, where=_ENCRYPTION_INFO, note="CryptoAPI-RC4 inside a modern wrapper")]

    def _modern_default(self, info: ecma376.EncryptionInfo) -> str | None:
        """Return the default password that opens ``info``, or ``None``.

        Skips the probe when the KDF work factor is implausibly high: read-only
        triage must not run an attacker-controlled spin loop (a crafted file could
        set spinCount into the hundreds of millions). Office default-encrypted files
        use spinCount 100000, well under the bound.
        """
        if info.spin_count > _MAX_DEFAULT_PROBE_SPIN:
            return None
        for candidate in ("", DEFAULT_PASSWORD_EXCEL, DEFAULT_PASSWORD_POWERPOINT):
            try:
                if ecma376.verify_password(info, candidate):
                    return candidate
            except ValueError:
                return None
        return None

    def _modern_hashes(self, ole: olefile.OleFileIO) -> list[ExtractedHash]:
        """Emit the ``$office$`` (or CryptoAPI ``$oldoffice$``) line for the wrapper."""
        info = self._modern_info(ole)
        if info is None:
            return self._modern_hash_fallback(ole)
        scheme, mode = _modern_scheme(info)
        opt_line = ecma376.unified_office_line(info)
        if scheme is None:
            return [ExtractedHash(scheme=HashScheme.OFFICE_2013, hashcat_mode=None, value=opt_line, gate=GateType.OPEN, opt_value=opt_line)]
        try:
            line = ecma376.office_hash_line(info)
        except ValueError:
            return []
        return [ExtractedHash(scheme=scheme, hashcat_mode=mode, value=line, gate=GateType.OPEN, opt_value=opt_line)]

    def _modern_hash_fallback(self, ole: olefile.OleFileIO) -> list[ExtractedHash]:
        """Emit a CryptoAPI-RC4 ``$oldoffice$`` line for the rare wrapped-RC4 case."""
        blob = _read_stream(ole, _ENCRYPTION_INFO)
        if blob is None:
            return []
        open_info = _rc4_open_from_cryptoapi(blob, b"")
        if open_info is None:
            return []
        opt_line = rc4legacy.unified_rc4_office_line(open_info.scheme, open_info.salt, open_info.key_bits, open_info.enc_verifier, open_info.enc_verifier_hash)
        return [ExtractedHash(scheme=open_info.hash_scheme, hashcat_mode=open_info.hashcat_mode, value=open_info.hash_line(), gate=GateType.OPEN, opt_value=opt_line)]

    def _decrypt_modern(self, ole: olefile.OleFileIO, out: Path, password: str) -> None:
        """Decrypt the modern wrapper to the plaintext OPC ZIP at ``out``."""
        logger.debug("decrypt modern: parsing EncryptionInfo")
        info = self._modern_info(ole)
        if info is None:
            msg = "EncryptionInfo is CryptoAPI-RC4 or IRM -- not decryptable by the modern path"
            raise ValueError(msg)
        package = _read_stream(ole, _ENCRYPTED_PACKAGE)
        if package is None:
            msg = "modern wrapper has no EncryptedPackage stream"
            raise ValueError(msg)
        logger.debug("decrypt modern: EncryptedPackage is %d bytes", len(package))
        for candidate in _default_candidates(None, password):
            try:
                plaintext = ecma376.decrypt_package(info, candidate, package)
            except ValueError:
                continue
            logger.debug("decrypt modern: password accepted, writing %d bytes to %s", len(plaintext), out)
            out.write_bytes(plaintext)
            return
        msg = "incorrect password: no candidate opened the package"
        raise ValueError(msg)

    # --- Legacy binary ---------------------------------------------------------

    def _legacy_needs_key(self, ole: olefile.OleFileIO, names: set[str]) -> bool:
        """Whether a legacy document carries a keyed (RC4) open scheme."""
        app = _classify_legacy(names)
        if app == _LegacyApp.DOC:
            fib = _parse_fib(_read_stream(ole, _WORD_DOCUMENT) or b"")
            return bool(fib and fib.f_encrypted and not fib.f_obfuscation)
        if app == _LegacyApp.XLS:
            workbook = self._workbook(ole)
            return workbook is not None and _xls_open(workbook) is not None
        if app == _LegacyApp.PPT:
            return self._ppt_open_info(ole) is not None
        if app == _LegacyApp.MPP:
            mpp_dir = mpp_crypto.detect_mpp_version(ole)
            if mpp_dir is not None:
                props_data = mpp_crypto.locate_props_stream(ole, mpp_dir)
                if props_data is not None:
                    props = mpp_crypto.parse_props(props_data)
                    if mpp_crypto.has_open_password(props) and mpp_crypto.decode_mpp9_password(props) is None:
                        return True
            return False
        return False

    def _workbook(self, ole: olefile.OleFileIO) -> bytes | None:
        """Read whichever of the Workbook/Book streams exists."""
        for name in _WORKBOOK_STREAMS:
            data = _read_stream(ole, name)
            if data is not None:
                return data
        return None

    def _ppt_open_info(self, ole: olefile.OleFileIO) -> _Rc4Open | None:
        """Read the two PowerPoint streams and parse the open descriptor."""
        current_user = _read_stream(ole, _CURRENT_USER)
        ppt = _read_stream(ole, _PPT_DOCUMENT)
        if current_user is None or ppt is None:
            return None
        return _ppt_open(current_user, ppt)

    def _legacy_open_info(self, ole: olefile.OleFileIO, app: str | None) -> _Rc4Open | None:
        """Dispatch to the per-app RC4 open-descriptor parser."""
        if app == _LegacyApp.DOC:
            fib = _parse_fib(_read_stream(ole, _WORD_DOCUMENT) or b"")
            return _doc_open(ole, fib) if fib else None
        if app == _LegacyApp.XLS:
            workbook = self._workbook(ole)
            return _xls_open(workbook) if workbook is not None else None
        if app == _LegacyApp.PPT:
            return self._ppt_open_info(ole)
        # MPP uses a proprietary Props-based password scheme, not [MS-OFFCRYPTO] RC4.
        return None

    def _legacy_open_gate(self, ole: olefile.OleFileIO, app: str) -> Gate | None:
        """Build the Open gate for a legacy document (RC4 or XOR)."""
        open_info = self._legacy_open_info(ole, app)
        if open_info is not None:
            logger.debug("open gate: %s keyBits=%d", open_info.scheme.value, open_info.key_bits)
            opens_with = self._legacy_default(app, open_info)
            if opens_with:
                logger.debug("open gate: opens with default password")
            return _rc4_open_gate(app, open_info, opens_with)
        if app == _LegacyApp.XLS:
            workbook = self._workbook(ole)
            if workbook is not None and _xls_xor_verifier(workbook) is not None:
                return Gate(gate=GateType.OPEN, recovery=RecoveryClass.DECODE, where="Workbook FilePass record (XOR obfuscation)", note="keyless scramble -- rebuild the 16-byte array from known plaintext, or COLLIDE the 16-bit verifier")
        if app == _LegacyApp.DOC:
            fib = _parse_fib(_read_stream(ole, _WORD_DOCUMENT) or b"")
            if fib and fib.f_encrypted and fib.f_obfuscation:
                return Gate(gate=GateType.OPEN, recovery=RecoveryClass.DECODE, where="WordDocument FibBase (fObfuscation=1); lKey verifier", note="keyless XOR scramble -- rebuild the array, or COLLIDE the 32-bit verifier")
        if app == _LegacyApp.MPP:
            return self._mpp_open_gate(ole)
        return None

    def _mpp_open_gate(self, ole: olefile.OleFileIO) -> Gate | None:
        """Detect and decode the MPP open password.

        MPP9: DECODE — plaintext password recovered via XOR+permutation.
        MPP14: probe for [MS-OFFCRYPTO] EncryptionInfo XML in the Props value.
        MPP12: unknown encryption, honest GAP.
        """
        mpp_dir = mpp_crypto.detect_mpp_version(ole)
        if mpp_dir is None:
            return None
        props_data = mpp_crypto.locate_props_stream(ole, mpp_dir)
        if props_data is None:
            return None
        props = mpp_crypto.parse_props(props_data)
        if not mpp_crypto.has_open_password(props):
            return None
        password = mpp_crypto.decode_mpp9_password(props)
        if password is not None:
            note = f"DECODE: MPP9 password recovered directly from Props stream ({len(password)} chars)"
            return Gate(gate=GateType.OPEN, recovery=RecoveryClass.DECODE, where="MPP Props9 PROTECTION_PASSWORD_HASH", note=note)
        return self._mpp_probe_encryption_info(props, mpp_dir)

    def _mpp_probe_encryption_info(self, props: dict[int, bytes], mpp_dir: str) -> Gate:
        """Probe whether the Props password-data value contains [MS-OFFCRYPTO] EncryptionInfo.

        MPP14 may store standard Office encryption XML in the PROTECTION_PASSWORD_HASH
        property (MPXJ variable name ``encryptionXmlPresent`` suggests this). If found,
        the existing ecma376 parser handles it and hashcat modes 9400-9600 apply.
        """
        pw_data = props.get(mpp_crypto.PROPS_KEY_PASSWORD_DATA)
        if pw_data is not None and (b"<encryption" in pw_data or b"<?xml" in pw_data):
            try:
                agile_header = b"\x04\x00\x04\x00\x40\x00\x00\x00"
                blob = agile_header + pw_data if b"<encryption" in pw_data else pw_data
                info = ecma376.parse_encryption_info(blob)
                ecma376.office_hash_line(info)
                logger.debug("MPP14 agile EncryptionInfo found in Props")
                note = f"MPP14 open password: standard [MS-OFFCRYPTO] agile encryption found in Props ({mpp_dir}) -> hashcat -m 9600"
                return Gate(gate=GateType.OPEN, recovery=RecoveryClass.CRACK, scheme=HashScheme.OFFICE_2013, hashcat_mode=9600, where=f"MPP Props {mpp_dir} PROTECTION_PASSWORD_HASH (agile XML)", note=note)
            except (ValueError, struct.error):
                logger.debug("MPP Props password data looks like XML but failed to parse as EncryptionInfo")
        note = f"MPP open password detected (PASSWORD_FLAG set) but decode failed -- {mpp_dir} encryption not yet supported (MPP12/14 GAP)"
        return Gate(gate=GateType.OPEN, recovery=RecoveryClass.CRACK, where=f"MPP Props {mpp_dir} PASSWORD_FLAG set", note=note)

    def _mpp_protection_gates(self, ole: olefile.OleFileIO) -> list[Gate]:
        """Detect the MPP9 write-reservation gate (DECODE class)."""
        mpp_dir = mpp_crypto.detect_mpp_version(ole)
        if mpp_dir is None:
            return []
        props_data = mpp_crypto.locate_props_stream(ole, mpp_dir)
        if props_data is None:
            return []
        props = mpp_crypto.parse_props(props_data)
        if not mpp_crypto.has_write_reservation(props):
            return []
        password = mpp_crypto.decode_mpp9_write_password(props)
        if password is None:
            return [Gate(gate=GateType.MODIFY, recovery=RecoveryClass.CRACK, where="MPP Props PASSWORD_FLAG bit 1", note="MPP write-reservation detected but decode failed")]
        note = f"DECODE: MPP9 write-reservation password recovered ({len(password)} chars)"
        return [Gate(gate=GateType.MODIFY, recovery=RecoveryClass.DECODE, where="MPP Props9 WRITE_RESERVATION_PASSWORD_HASH", note=note)]

    def _legacy_default(self, app: str, open_info: _Rc4Open) -> str | None:
        """Return the default password that opens ``open_info`` for ``app``."""
        for candidate in _default_candidates(app, ""):
            if not candidate:
                continue
            if open_info.verify(candidate):
                return candidate
        return None

    def _legacy_gates(self, ole: olefile.OleFileIO, names: set[str]) -> list[Gate]:
        """Collect every gate on a legacy binary document."""
        app = _classify_legacy(names)
        gates: list[Gate] = []
        if app is not None:
            open_gate = self._legacy_open_gate(ole, app)
            if open_gate is not None:
                gates.append(open_gate)
            gates.extend(self._legacy_protection_gates(ole, app))
        vba_gate = _vba_gate(ole)
        if vba_gate is not None:
            gates.append(vba_gate)
        signature_gate = _signature_gate(names)
        if signature_gate is not None:
            gates.append(signature_gate)
        irm_gate = _irm_gate(names)
        if irm_gate is not None:
            gates.append(irm_gate)
        return gates

    def _legacy_protection_gates(self, ole: olefile.OleFileIO, app: str) -> list[Gate]:
        """Enumerate the non-encrypting protection gates per legacy app."""
        if app == _LegacyApp.XLS:
            return self._xls_protection_gates(ole)
        if app == _LegacyApp.DOC:
            return self._doc_protection_gates(ole)
        if app == _LegacyApp.PPT:
            return self._ppt_protection_gates(ole)
        if app == _LegacyApp.MPP:
            return self._mpp_protection_gates(ole)
        return []

    def _ppt_protection_gates(self, ole: olefile.OleFileIO) -> list[Gate]:
        """PowerPoint modify-password gate from the cleartext ModifyPasswordAtom ([MS-PPT] Section 2.4.7)."""
        if self._ppt_open_info(ole) is not None:
            return []  # open-encrypted: the atom is inside the encrypted stream -- decrypt first
        ppt = _read_stream(ole, _PPT_DOCUMENT)
        if ppt is None:
            return []
        atom = _ppt_find_modify_password(ppt)
        if atom is None:
            return []
        return [Gate(gate=GateType.MODIFY, recovery=RecoveryClass.READ, where="ModifyPasswordAtom (RT_CString 0x0FBA, recInstance 0x003)", note=f"modify password (cleartext): {atom.password!r} -- read it, or STRIP the atom")]

    def _xls_protection_gates(self, ole: olefile.OleFileIO) -> list[Gate]:
        """16-bit verifier gates in a plaintext Workbook (Password/FileSharing/Prot4Rev/Feat).

        The Password record (0x13) is routed to protect-WORKBOOK vs protect-SHEET by the
        enclosing ``BOF.dt`` substream ([MS-XLS] Section 2.4.191), correcting the previous
        blanket protect-SHEET label.
        """
        workbook = self._workbook(ole)
        if workbook is None or _xls_open(workbook) is not None:
            return []  # encrypted workbook -- the records are unreadable until decrypted
        notes = {
            GateType.PROTECT_WORKBOOK: "16-bit verifier -- mint any colliding password or delete the record",
            GateType.PROTECT_SHEET: "16-bit verifier -- mint any colliding password or delete the record",
            GateType.MODIFY: "16-bit write-reservation verifier",
            GateType.SHARED_REVISIONS: "16-bit shared-revisions verifier",
            GateType.ALLOW_EDIT_RANGES: "16-bit allow-edit-ranges verifier",
        }
        records = _xls_protection_records(workbook)
        logger.debug("xls protection: %d records", len(records))
        return [Gate(gate=record.gate, recovery=RecoveryClass.COLLIDE, where=record.where, note=notes.get(record.gate, "")) for record in records]

    def _doc_protection_gates(self, ole: olefile.OleFileIO) -> list[Gate]:
        """Word write-reservation (cleartext) and restrict-editing (Dop) gates."""
        word_document = _read_stream(ole, _WORD_DOCUMENT)
        fib = _parse_fib(word_document or b"")
        if word_document is None or fib is None or fib.f_encrypted:
            return []  # encrypted/obfuscated: the Table-stream fields are unreadable until decoded
        table = _read_stream(ole, fib.table_stream)
        gates: list[Gate] = []
        if fib.f_write_reservation or fib.f_read_only:
            gates.append(self._doc_write_reservation_gate(word_document, table))
        if table is not None:
            dop = _parse_dop_protection(word_document, table)
            if dop is not None and dop.protected:
                gates.append(Gate(gate=GateType.RESTRICT_EDIT, recovery=RecoveryClass.STRIP, where="Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)", note=f"lKeyProtDoc=0x{dop.l_key_prot_doc:08x} -- zero it and clear the fProt* bits (body is never encrypted; or COLLIDE the 32-bit verifier)"))
        return gates

    def _doc_write_reservation_gate(self, word_document: bytes, table: bytes | None) -> Gate:
        """Build the modify gate, reading the cleartext SttbfAssoc[0x11] string when present."""
        note = "the modify password is stored in clear -- read it (or clear fWriteReservation)"
        if table is not None:
            password = _sttbf_assoc_string(word_document, table, _ASSOC_WRITE_RESERVATION_INDEX)
            if password:
                note = f"modify password (cleartext): {password!r}"
        return Gate(gate=GateType.MODIFY, recovery=RecoveryClass.READ, where="Table stream SttbfAssoc[0x11] (cleartext UTF-16LE); FibBase.fWriteReservation", note=note)

    def _legacy_hashes(self, ole: olefile.OleFileIO, names: set[str]) -> list[ExtractedHash]:
        """Emit the open ``$oldoffice$`` line, any ``$officexor$`` verifier lines, and VBA 110."""
        app = _classify_legacy(names)
        hashes: list[ExtractedHash] = []
        open_info = self._legacy_open_info(ole, app)
        if open_info is not None:
            opt_line = rc4legacy.unified_rc4_office_line(open_info.scheme, open_info.salt, open_info.key_bits, open_info.enc_verifier, open_info.enc_verifier_hash)
            hashes.append(ExtractedHash(scheme=open_info.hash_scheme, hashcat_mode=open_info.hashcat_mode, value=open_info.hash_line(), gate=GateType.OPEN, opt_value=opt_line))
        vba_line = _vba_hash_line(ole)
        if vba_line is not None:
            dpb = _vba_dpb(ole)
            opt_vba = vba.unified_vba_line(dpb) if dpb else None
            hashes.append(ExtractedHash(scheme=HashScheme.VBA_SHA1, hashcat_mode=110, value=vba_line, gate=GateType.VBA_PROJECT, opt_value=opt_vba))
        return hashes

    # --- Legacy decrypt --------------------------------------------------------

    def _decrypt_legacy(self, ole: olefile.OleFileIO, path: Path, out: Path, password: str, app: str | None) -> None:
        """Decrypt a legacy RC4 or XOR-obfuscated document, writing a NEW OLE copy to ``out``."""
        open_info = self._legacy_open_info(ole, app)
        if open_info is None:
            logger.debug("decrypt legacy: no RC4 open info, trying XOR decode for app=%s", app)
            edits = self._decrypt_legacy_xor(ole, app, password)
            if edits is None:
                operation = f"legacy decryption for {app or 'unknown'}"
                raise HandlerNotImplementedError(operation, "ole-cfb")
        else:
            logger.debug("decrypt legacy: app=%s scheme=%s keyBits=%d", app, open_info.scheme.value, open_info.key_bits)
            used = self._pick_legacy_password(open_info, app, password)
            logger.debug("decrypt legacy: password accepted")
            edits = self._decrypt_legacy_streams(ole, app, used, open_info)
        shutil.copyfile(str(path), str(out))
        with olefile.OleFileIO(str(out), write_mode=True) as out_ole:
            for stream_path, data in edits.items():
                logger.debug("decrypt legacy: writing stream %s (%d bytes)", stream_path, len(data))
                out_ole.write_stream(stream_path.split("/"), data)

    def _decrypt_legacy_xor(self, ole: olefile.OleFileIO, app: str | None, password: str) -> dict[str, bytes] | None:
        """Decode a keyless XOR-obfuscated open gate with the supplied password.

        XOR obfuscation is a DECODE, not a keyed decrypt ([MS-OFFCRYPTO] Section 2.3.7):
        the 16-byte array is derived straight from the password, so once the password is
        confirmed against the stored verifier the body is reversible. Returns the decoded
        stream overrides, ``None`` when the document is not XOR-obfuscated (so the caller
        falls through to ``HandlerNotImplementedError``), or raises ``ValueError`` when the
        password does not match the stored verifier.
        """
        if app == _LegacyApp.XLS:
            workbook = self._workbook(ole)
            if workbook is None:
                return None
            verifier = _xls_xor_verifier(workbook)
            if verifier is None:
                return None
            return self._decode_xls_xor_streams(ole, workbook, verifier, password)
        if app == _LegacyApp.DOC:
            fib = _parse_fib(_read_stream(ole, _WORD_DOCUMENT) or b"")
            if fib is None or not (fib.f_encrypted and fib.f_obfuscation):
                return None
            return self._decode_doc_xor_streams(ole, fib, password)
        return None

    def _decode_xls_xor_streams(self, ole: olefile.OleFileIO, workbook: bytes, verifier: tuple[int, int], password: str) -> dict[str, bytes]:
        """Confirm the password against the stored (key, verifier) and decode the Workbook."""
        key, verif16 = verifier
        used = next((c for c in _default_candidates(_LegacyApp.XLS, password) if _xls_xor_password_ok(c, key, verif16)), None)
        if used is None:
            msg = "incorrect password: no candidate matched the XOR verifier"
            raise ValueError(msg)
        array = xor.create_xor_array_method1(used)
        name = next(n for n in _WORKBOOK_STREAMS if _read_stream(ole, n) is not None)
        return {name: _decode_xls_xor(workbook, array)}

    def _decode_doc_xor_streams(self, ole: olefile.OleFileIO, fib: _FibInfo, password: str) -> dict[str, bytes]:
        """Confirm the 32-bit lKey and decode the WordDocument/Table/Data streams (Method 2)."""
        used = next((c for c in _default_candidates(_LegacyApp.DOC, password) if _doc_xor_password_ok(c, fib.l_key)), None)
        if used is None:
            msg = "incorrect password: candidate did not match the XOR lKey verifier"
            raise ValueError(msg)
        array = xor.create_xor_array_method1(used)
        result: dict[str, bytes] = {}
        word_document = _read_stream(ole, _WORD_DOCUMENT)
        if word_document is not None:
            # First 68 bytes are stored untransformed ([MS-DOC] Section 2.2.6.1); rebuild
            # the FIB with the encryption flags cleared and transform the rest.
            body = xor.xor_transform_method2(word_document[_FIB_LEN:], array, _FIB_LEN)
            result[_WORD_DOCUMENT] = _clear_fib_encryption(word_document) + body
        table = _read_stream(ole, fib.table_stream)
        if table is not None:
            result[fib.table_stream] = xor.xor_transform_method2(table, array, 0)
        data = _read_stream(ole, "Data")
        if data is not None:
            result["Data"] = xor.xor_transform_method2(data, array, 0)
        return result

    def _pick_legacy_password(self, open_info: _Rc4Open, app: str | None, password: str) -> str:
        """Return the first candidate password that verifies, or raise ``ValueError``."""
        for candidate in _default_candidates(app, password):
            if open_info.verify(candidate):
                return candidate
        msg = "incorrect password: no candidate opened the document"
        raise ValueError(msg)

    def _decrypt_legacy_streams(self, ole: olefile.OleFileIO, app: str | None, password: str, open_info: _Rc4Open) -> dict[str, bytes]:
        """Produce the decrypted stream overrides for the legacy app."""
        if app == _LegacyApp.DOC:
            return _decrypt_doc_streams(ole, password, open_info)
        if app == _LegacyApp.XLS:
            workbook = self._workbook(ole)
            if workbook is None:
                return {}
            name = next(n for n in _WORKBOOK_STREAMS if _read_stream(ole, n) is not None)
            return {name: _decrypt_xls_workbook(password, open_info, workbook)}
        if app == _LegacyApp.PPT:
            return self._decrypt_ppt_streams(ole, password, open_info)
        return {}

    def _decrypt_ppt_streams(self, ole: olefile.OleFileIO, password: str, open_info: _Rc4Open) -> dict[str, bytes]:
        """Decrypt the PowerPoint Document stream and clear the CurrentUser encryption token."""
        current_user = _read_stream(ole, _CURRENT_USER)
        ppt = _read_stream(ole, _PPT_DOCUMENT)
        if current_user is None or ppt is None:
            return {}
        chain = _ppt_build_chain(current_user, ppt)
        if chain is None:
            return {}
        # headerToken 0xE391C05F marks the document as SHOULD-NOT-be-encrypted ([MS-PPT] Section 2.3.2).
        clean_current_user = bytearray(current_user)
        if len(clean_current_user) >= _CURRENTUSER_HEADER_TOKEN_OFFSET + 4:
            struct.pack_into("<I", clean_current_user, _CURRENTUSER_HEADER_TOKEN_OFFSET, _CURRENTUSER_TOKEN_PLAIN)
        return {_CURRENT_USER: bytes(clean_current_user), _PPT_DOCUMENT: _decrypt_ppt_document(password, open_info, chain, ppt)}

    # --- Legacy bypass ---------------------------------------------------------

    def _bypass_edits(self, path: Path, app: str | None, *, remove_signatures: bool = False) -> dict[str, bytes]:
        """Compute same-size stream overrides that clear removable protection.

        Combines the app-specific protection strip with the app-independent VBA project
        lock strip (a macro project can live in a .doc/.xls/.ppt alike), plus -- when
        ``remove_signatures`` is set -- the legacy digital-signature strip.
        """
        edits: dict[str, bytes] = {}
        with olefile.OleFileIO(str(path)) as ole:
            if app == _LegacyApp.XLS:
                edits.update(self._bypass_xls(ole))
            elif app == _LegacyApp.DOC:
                edits.update(self._bypass_doc(ole))
            elif app == _LegacyApp.PPT:
                edits.update(self._bypass_ppt(ole))
            edits.update(self._bypass_vba(ole))
            if remove_signatures:
                logger.debug("bypass: removing digital signatures")
                edits.update(self._bypass_signatures(ole))
        for stream_path, data in edits.items():
            logger.debug("bypass edit: stream=%s size=%d bytes", stream_path, len(data))
        return edits

    def _bypass_signatures(self, ole: olefile.OleFileIO) -> dict[str, bytes]:
        """Zero the legacy ``_signatures`` stream so the digital signature no longer validates.

        olefile can only overwrite a CFB stream in place (same size), not delete it, so
        the stream is filled with zeros -- the signature blob is destroyed and the
        integrity claim drops, though an empty ``_signatures`` stream remains. A file
        with no such stream yields no edit (a plain no-op).
        """
        data = _read_stream(ole, _SIGNATURES)
        if data is None:
            return {}
        return {_SIGNATURES: bytes(len(data))}

    def _bypass_ppt(self, ole: olefile.OleFileIO) -> dict[str, bytes]:
        """Strip the PowerPoint ModifyPasswordAtom (same-size, empties the modify password)."""
        if self._ppt_open_info(ole) is not None:
            return {}  # open-encrypted: decrypt before the atom is readable
        ppt = _read_stream(ole, _PPT_DOCUMENT)
        if ppt is None:
            return {}
        atom = _ppt_find_modify_password(ppt)
        if atom is None:
            return {}
        logger.debug("bypass ppt: stripping ModifyPasswordAtom")
        return {_PPT_DOCUMENT: _ppt_strip_modify_password(ppt, atom)}

    def _bypass_vba(self, ole: olefile.OleFileIO) -> dict[str, bytes]:
        """Strip the embedded VBA project lock by rewriting the PROJECT stream ([MS-OVBA])."""
        project_path = _find_project_stream(ole)
        if project_path is None:
            return {}
        raw = _read_stream(ole, project_path)
        if raw is None:
            return {}
        modified = _clear_vba_protection(raw)
        if modified is None:
            return {}
        logger.debug("bypass vba: clearing DPB/CMG/GC protection in PROJECT stream")
        return {"/".join(project_path): modified}

    def _bypass_xls(self, ole: olefile.OleFileIO) -> dict[str, bytes]:
        """Strip removable Workbook protection, decoding XOR obfuscation first if present."""
        workbook = self._workbook(ole)
        if workbook is None:
            return {}
        decoded_xor = False
        if _find_filepass(workbook) is not None:
            verifier = _xls_xor_verifier(workbook)
            if verifier is None:
                logger.debug("bypass xls: RC4-encrypted, deferring to decrypt")
                return {}
            logger.debug("bypass xls: XOR obfuscation, decoding")
            workbook = self._bypass_xls_xor(workbook, verifier)  # decode; raises on honest failure
            decoded_xor = True
        stripped = _strip_xls_verifiers(workbook)
        if stripped is not None:
            logger.debug("bypass xls: stripped protection verifiers")
            workbook = stripped
        elif not decoded_xor:
            return {}  # plaintext workbook with nothing removable
        name = next(n for n in _WORKBOOK_STREAMS if _read_stream(ole, n) is not None)
        logger.debug("bypass xls: writing %s (%d bytes)", name, len(workbook))
        return {name: workbook}

    def _bypass_xls_xor(self, workbook: bytes, verifier: tuple[int, int]) -> bytes:
        """Decode an XOR-obfuscated Workbook with no password, then return the plaintext stream.

        Reconstructs the 16-byte obfuscation array from the stored ``XorKey``, the fixed
        ``PadArray`` and known-plaintext Globals records (:func:`xor.reconstruct_password`,
        validated by the 32-bit XorKey+verifier match). If reconstruction fails there is no
        honest way to strip the protection, so this raises instead of silently returning an
        unchanged copy (the exact bug this path fixes).
        """
        key, verif16 = verifier
        logger.debug("XOR decode: xorKey=0x%04x verifier=0x%04x", key, verif16)
        known = _xls_xor_known_array(workbook)
        logger.debug("XOR decode: %d known-plaintext records for array reconstruction", len(known))
        password = xor.reconstruct_password(key, verif16, known)
        if password is None:
            msg = "cannot bypass XOR obfuscation: password-free array reconstruction failed -- run `decrypt` with the password"
            raise ValueError(msg)
        logger.debug("XOR decode: array reconstructed, decoding %d bytes", len(workbook))
        return _decode_xls_xor(workbook, xor.create_xor_array_method1(password))

    def _bypass_doc(self, ole: olefile.OleFileIO) -> dict[str, bytes]:
        """Clear the write-reservation flag and strip the restrict-editing Dop state."""
        word_document = _read_stream(ole, _WORD_DOCUMENT)
        fib = _parse_fib(word_document or b"")
        if word_document is None or fib is None:
            return {}
        edits: dict[str, bytes] = {}
        if fib.f_write_reservation:
            logger.debug("bypass doc: clearing fWriteReservation flag")
            data = bytearray(word_document)
            flags = struct.unpack_from("<H", data, _FIB_FLAGS_OFFSET)[0]
            flags &= ~(1 << _FIB_BIT_FWRITERESERVATION)
            struct.pack_into("<H", data, _FIB_FLAGS_OFFSET, flags)
            edits[_WORD_DOCUMENT] = bytes(data)
        if not fib.f_encrypted:
            table = _read_stream(ole, fib.table_stream)
            if table is not None:
                dop = _parse_dop_protection(word_document, table)
                if dop is not None and dop.protected:
                    logger.debug("bypass doc: stripping DOP protection (lKeyProtDoc=0x%08x)", dop.l_key_prot_doc)
                    edits[fib.table_stream] = _strip_dop_protection(table, dop)
        return edits
