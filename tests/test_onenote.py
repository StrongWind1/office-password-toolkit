"""OneNote handler tests.

The public corpus contains NO password-protected ``.one`` sample -- every Tika
``.one`` is plaintext -- so the encrypted paths are exercised against SYNTHETIC
stores built from real [MS-OFFCRYPTO] ``EncryptionInfo`` descriptors lifted out of
the encrypted OLE/OOXML corpus. Each descriptor is framed by the [MS-ONESTORE]
Section 2.5.19 sentinels (0xFB6BA385DAD1A067 / 0x2649294F8E198B3C) exactly as a
real ObjectDataEncryptionKeyV2FNDX blob would frame it, and embedded behind the
OneNote header GUID. We then prove the handler routes each scheme by its version
words and reproduces the same hash line ``ecma376``/``rc4legacy`` emit for the
descriptor read from a real file:

* agile SHA-512/AES-256 (``example_password.docx``) -> ``$office$*2013`` (9600),
* standard SHA-1/AES (``ecma376standard_password.docx``) -> ``$office$*2007`` (9400),
* RC4 CryptoAPI SHA-1 (``rc4cryptoapi_password.doc``) -> ``$oldoffice$4`` (9800).

These are SYNTHETIC round-trips (no real encrypted ``.one`` exists); they are not
dressed up as real-file validation.
"""

from __future__ import annotations

from pathlib import Path

import olefile
import pytest

from office_password_toolkit.crypto import ecma376, rc4legacy
from office_password_toolkit.formats.base import HandlerNotImplementedError
from office_password_toolkit.formats.onenote import OneNoteHandler
from office_password_toolkit.models import GateType, HashScheme, RecoveryClass

CORPUS = Path(__file__).parent / "corpus"
# Borrowed files promoted to first-party corpus.
ONENOTE_MAGIC = b"\xe4\x52\x5c\x7b\x8c\xd8\xa7\x4d\xae\xb1\x53\x78\xd0\x29\x96\xd3"
BLOB_HEADER = (0xFB6BA385DAD1A067).to_bytes(8, "little")
BLOB_FOOTER = (0x2649294F8E198B3C).to_bytes(8, "little")


def _ole_stream(name: str, stream: str) -> bytes:
    """Read a single OLE stream out of a corpus file."""
    ole = olefile.OleFileIO(str(CORPUS / "encrypted" / name))
    try:
        return ole.openstream(stream).read()
    finally:
        ole.close()


def _framed_store(blob: bytes) -> bytes:
    """Embed a raw EncryptionInfo blob in a OneNote-magic + sentinel-framed store.

    The padding before the header sentinel and after the footer stands in for the
    [MS-ONESTORE] header fields and the surrounding object space, proving the carve
    is offset-robust. The sentinels frame a 16-byte preamble + the blob, exactly as
    a real ObjectDataEncryptionKeyV2FNDX FileNodeChunkReference does (Section 2.5.19):
    [type:4][total_len:4][enc_info_offset:4][enc_info_len:4][EncryptionInfo blob].
    """
    import struct

    preamble_size = 16
    total_interior = preamble_size + len(blob)
    preamble = struct.pack("<IIII", 3, total_interior, preamble_size, len(blob))
    prefix = ONENOTE_MAGIC + b"\x00" * 64
    suffix = b"\x00" * 128
    return prefix + BLOB_HEADER + preamble + blob + BLOB_FOOTER + suffix


def _rc4_blob_and_line() -> tuple[bytes, str]:
    """Lift the real RC4 CryptoAPI EncryptionInfo blob from a corpus Word doc.

    ``rc4cryptoapi_password.doc`` stores the [MS-OFFCRYPTO] Section 2.3.5.1 blob at
    the start of its ``1Table`` stream. We slice out exactly the EncryptionInfo
    (header + verifier) and compute the canonical hash line ``rc4legacy`` produces
    for it, so the OneNote round-trip is checked against a real descriptor.
    """
    table = _ole_stream("rc4cryptoapi_password.doc", "1Table")
    header = rc4legacy.parse_rc4_cryptoapi_header(table)
    key_bits = int(header["key_size"]) or 40
    blob_len = 12 + int(header["header_size"]) + 4 + 16 + 16 + 4 + int(header["verifier_hash_size"])
    blob = table[:blob_len]
    digit = 4 if key_bits == 128 else 3
    salt = header["salt"]
    enc_verifier = header["encrypted_verifier"]
    enc_hash = header["encrypted_verifier_hash"]
    assert isinstance(salt, bytes)
    assert isinstance(enc_verifier, bytes)
    assert isinstance(enc_hash, bytes)
    line = rc4legacy.rc4_cryptoapi_hash_line(digit, key_bits, salt, enc_verifier, enc_hash)
    return blob, line


def _run_case(store: bytes, scheme: HashScheme, mode: int, expected_line: str, prefix: str) -> None:
    """Write ``store`` to a temp .one, then assert gates + extract match the scheme."""
    path = CORPUS / "_synthetic_encrypted.one"
    path.write_bytes(store)
    try:
        handler = OneNoteHandler()
        assert handler.is_encrypted(path) is True

        gates = handler.gates(path)
        assert len(gates) == 1
        gate = gates[0]
        assert gate.gate is GateType.OPEN
        assert gate.recovery is RecoveryClass.CRACK
        assert gate.scheme is scheme
        assert gate.hashcat_mode == mode

        hashes = handler.extract(path)
        assert len(hashes) == 1
        assert hashes[0].scheme is scheme
        assert hashes[0].hashcat_mode == mode
        assert hashes[0].value == expected_line
        assert hashes[0].value.startswith(prefix)
    finally:
        path.unlink()


def test_agile_section_routes_to_office_2013() -> None:
    blob = _ole_stream("example_password.docx", "EncryptionInfo")
    expected = ecma376.office_hash_line(ecma376.parse_encryption_info(blob))
    _run_case(_framed_store(blob), HashScheme.OFFICE_2013, 9600, expected, "$office$*2013*")


def test_standard_section_routes_to_office_2007() -> None:
    blob = _ole_stream("ecma376standard_password.docx", "EncryptionInfo")
    expected = ecma376.office_hash_line(ecma376.parse_encryption_info(blob))
    _run_case(_framed_store(blob), HashScheme.OFFICE_2007, 9400, expected, "$office$*2007*")


def test_rc4_cryptoapi_section_routes_to_oldoffice() -> None:
    blob, expected = _rc4_blob_and_line()
    _run_case(_framed_store(blob), HashScheme.OLDOFFICE_RC4_SHA1, 9800, expected, "$oldoffice$4*")


def test_bare_xml_fallback_still_extracts_agile() -> None:
    # office2john-style store: the agile <encryption> XML with no sentinel framing.
    blob = _ole_stream("example_password.docx", "EncryptionInfo")
    descriptor = blob[8:].rstrip(b"\x00")  # XML declaration + <encryption>...</encryption>
    expected = ecma376.office_hash_line(ecma376.parse_encryption_info(blob))
    store = ONENOTE_MAGIC + b"\x00" * 32 + descriptor + b"\x00" * 32
    _run_case(store, HashScheme.OFFICE_2013, 9600, expected, "$office$*2013*")


def test_plaintext_onenote_reports_no_encryption() -> None:
    # A OneNote store with the header GUID but no encryption blob or descriptor.
    path = CORPUS / "_synthetic_plain.one"
    path.write_bytes(ONENOTE_MAGIC + b"\x00" * 256)
    try:
        handler = OneNoteHandler()
        assert handler.is_encrypted(path) is False
        assert handler.gates(path) == []
        assert handler.extract(path) == []
    finally:
        path.unlink()


def test_non_onenote_file_is_ignored() -> None:
    path = CORPUS / "_synthetic_notone.bin"
    path.write_bytes(b"PK\x03\x04" + b"\x00" * 64)
    try:
        handler = OneNoteHandler()
        assert handler.is_encrypted(path) is False
        assert handler.gates(path) == []
        assert handler.extract(path) == []
    finally:
        path.unlink()


def test_missing_file_does_not_crash() -> None:
    handler = OneNoteHandler()
    assert handler.is_encrypted(CORPUS / "does_not_exist.one") is False


def test_unrecognized_scheme_reports_gate_without_line() -> None:
    # A sentinel-framed blob whose version words match no recoverable scheme
    # (vMinor == 3 is extensible/IRM). is_encrypted is True (there IS a blob), the
    # gate is reported honestly, but extract emits no crackable line.
    bogus = b"\x03\x00\x03\x00" + b"\x00" * 24
    store = _framed_store(bogus)
    path = CORPUS / "_synthetic_irm.one"
    path.write_bytes(store)
    try:
        handler = OneNoteHandler()
        assert handler.is_encrypted(path) is True
        gates = handler.gates(path)
        assert len(gates) == 1
        assert gates[0].gate is GateType.OPEN
        assert gates[0].recovery is RecoveryClass.CRACK
        assert gates[0].scheme is None
        assert gates[0].hashcat_mode is None
        assert handler.extract(path) == []
    finally:
        path.unlink()


def test_verify_password_agile_correct() -> None:
    blob = _ole_stream("example_password.docx", "EncryptionInfo")
    store = _framed_store(blob)
    path = CORPUS / "_synthetic_verify.one"
    path.write_bytes(store)
    try:
        assert OneNoteHandler().verify_password(path, "Password1234_") is True
    finally:
        path.unlink()


def test_verify_password_agile_wrong() -> None:
    blob = _ole_stream("example_password.docx", "EncryptionInfo")
    store = _framed_store(blob)
    path = CORPUS / "_synthetic_verify.one"
    path.write_bytes(store)
    try:
        assert OneNoteHandler().verify_password(path, "wrong") is False
    finally:
        path.unlink()


def test_verify_password_standard_correct() -> None:
    blob = _ole_stream("ecma376standard_password.docx", "EncryptionInfo")
    store = _framed_store(blob)
    path = CORPUS / "_synthetic_verify.one"
    path.write_bytes(store)
    try:
        assert OneNoteHandler().verify_password(path, "Password1234_") is True
    finally:
        path.unlink()


def test_verify_password_rc4_correct() -> None:
    blob, _ = _rc4_blob_and_line()
    store = _framed_store(blob)
    path = CORPUS / "_synthetic_verify.one"
    path.write_bytes(store)
    try:
        assert OneNoteHandler().verify_password(path, "Password1234_") is True
    finally:
        path.unlink()


def test_verify_password_plaintext_returns_false() -> None:
    path = CORPUS / "_synthetic_verify.one"
    path.write_bytes(ONENOTE_MAGIC + b"\x00" * 256)
    try:
        assert OneNoteHandler().verify_password(path, "anything") is False
    finally:
        path.unlink()


def test_bypass_and_decrypt_are_crack_only() -> None:
    handler = OneNoteHandler()
    src = CORPUS / "_synthetic_x.one"
    src.write_bytes(ONENOTE_MAGIC + b"\x00" * 32)
    out = CORPUS / "_synthetic_out.one"
    try:
        with pytest.raises(HandlerNotImplementedError):
            handler.bypass(src, out)
        with pytest.raises(HandlerNotImplementedError):
            handler.decrypt(src, out, "whatever")
        assert not out.exists()
    finally:
        src.unlink()
