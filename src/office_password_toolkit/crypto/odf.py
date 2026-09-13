# SPDX-License-Identifier: Apache-2.0
"""OpenDocument (ODF) document-open encryption -- manifest parse, verify, decrypt.

An ODF file (``.odt`` / ``.ods`` / ``.odp`` ...) is a plain ZIP. Its crypto
parameters are not a binary header: they live as Base64-encoded XML attributes in
``META-INF/manifest.xml`` (OASIS *OpenDocument v1.2 Part 3: Packages* Section 3.4
"Encryption"; the older ODF 1.1 Blowfish profile predates that split and is
defined in the ODF 1.1 spec Section 17.3). Encryption is per-stream: every
non-metadata member (``content.xml``, ``styles.xml`` ...) is DEFLATE-compressed
and then individually encrypted in place, while the ZIP directory, ``mimetype``,
member names, and the manifest itself stay in clear. A password guess is
confirmed by decrypting a member and re-hashing the first <=1024 decrypted (still
DEFLATE-compressed) plaintext bytes against a stored checksum -- there is no
MS-Office ``EncryptedVerifier`` blob and no separate modify/macro password; one
password gates the whole package.

Two profiles are implemented, byte-for-byte matching hashcat 18600 / 18400 and
the odf2john / libreoffice2john ``$odf$`` hash line:

* **ODF 1.1** (hashcat 18600): SHA-1 start key -> PBKDF2-HMAC-SHA1 (default 1024
  rounds) -> Blowfish / CFB-64 (8-byte IV), checksum SHA-1/1K (20 bytes).
* **ODF 1.2** (hashcat 18400): SHA-256 start key -> PBKDF2-HMAC-SHA1 (default
  100000 rounds) -> AES-256-CBC (16-byte IV), checksum SHA-256/1K (32 bytes).

The **ODF 1.3** "Wholesome Encryption" profile (LibreOffice 24.8+, tdf#105844) is
also implemented: SHA-256 start key -> Argon2id (t/m/p from the ``loext:`` manifest
attributes, default 3 / 65536 KiB / 4) -> AES-256-GCM. The stored member is
``IV(12) || ciphertext || tag(16)`` and the 16-byte GCM auth tag *is* the verifier
(an AEAD cipher has no separate plaintext checksum). It has no hashcat / John mode
-- a memory-hard KDF plus AEAD tag is a GPU-cracking GAP -- so :func:`is_gap` still
flags it, but :func:`verify` / :func:`decrypt_entry` handle it with a known
password and :func:`odf_hash_line` emits the extended ``$odf$*2*...`` line. The
exact URIs / parameters are pinned in ``related-work.md`` Section 2. Any cipher
outside the three profiles (Blowfish / AES-CBC / AES-GCM) still raises
:class:`OdfUnsupportedError` with the observed parameters instead of crashing.

Two facts diverge sharply from MS-OFFCRYPTO and are the usual source of silent
failure:

* The password is hashed as its **raw UTF-8 bytes** -- no UTF-16LE expansion, no
  BOM, no NUL terminator, no length prefix.
* The PBKDF2 PRF is **always HMAC-SHA1**, even in the SHA-256 profile (SHA-256 is
  only the start-key pre-hash and the checksum, never the stretch PRF).

See ``office/analysis/password-algorithms/odf-encryption.md`` Sections 3-7 and 11.
"""

from __future__ import annotations

import base64
import logging
import xml.parsers.expat
import zlib
from dataclasses import dataclass

from office_password_toolkit.crypto.ciphers import InvalidTag, aes_cbc_decrypt, aes_gcm_decrypt, blowfish_cfb_decrypt
from office_password_toolkit.crypto.hashes import argon2id, compare_digest, pbkdf2_hmac_sha1
from office_password_toolkit.crypto.hashes import digest as _digest

__all__ = [
    "OdfEntry",
    "OdfUnsupportedError",
    "decrypt_entry",
    "is_gap",
    "odf_hash_line",
    "parse_manifest",
    "verify",
]

logger = logging.getLogger(__name__)

# --- Constants ---

# We match attributes by local name (the suffix after the ``:`` prefix) so the
# manifest: prefix and the loext: prefix used for the experimental Argon2
# attributes are both handled without pinning either full namespace URI.
#
# Marker substrings used to classify the algorithm/checksum/KDF URIs. The OASIS
# schema lets the start-key / KDF / cipher / checksum axes vary independently, so
# we key off the meaningful token in each URI rather than an exact string match.
_MARK_BLOWFISH = "blowfish"  # e.g. "Blowfish CFB" or "...#blowfish"
_MARK_AES_CBC = "aes256-cbc"  # "...#aes256-cbc"
_MARK_GCM = "gcm"  # "...#aes256-gcm" -- ODF 1.3 AEAD, GAP
_MARK_SHA256 = "sha256"  # start-key / checksum SHA-256 selector
_MARK_ARGON2 = "argon2"  # "...:argon2id" key-derivation -- ODF 1.3, GAP

# Child element local names carried inside a <manifest:encryption-data> block.
_EL_ENCRYPTION_DATA = "encryption-data"
_EL_ALGORITHM = "algorithm"
_EL_KEY_DERIVATION = "key-derivation"
_EL_START_KEY = "start-key-generation"
_CRYPTO_ELEMENTS = frozenset({_EL_ENCRYPTION_DATA, _EL_ALGORITHM, _EL_KEY_DERIVATION, _EL_START_KEY})

# AES block size -- CBC consumes whole 16-byte blocks; a stored member is always a
# multiple of the block size, but a caller may hand us a 1024-byte prefix that we
# trim to the last full block before decrypting ([odf-encryption.md] Section 5).
_AES_BLOCK_BYTES = 16

# The "/1K" checksum covers only the first 1024 plaintext bytes; the extractor and
# hashcat both cap the stored ciphertext at 1024 bytes for the same reason.
_CHECKSUM_WINDOW_BYTES = 1024
_CIPHERTEXT_CAP_BYTES = 1024

# ODF members are *raw* DEFLATE streams (no zlib 2-byte header, no gzip wrapper);
# inflate with a negative window size to select the raw codec.
_RAW_DEFLATE_WBITS = -15


# ODF 1.3 "Wholesome Encryption" (LibreOffice 24.8+, tdf#105844): Argon2id key
# derivation + AES-256-GCM. The stored member is IV(12) || ciphertext || tag(16):
# the 12-byte GCM nonce is carried both prepended to the stream *and* in the
# manifest initialisation-vector, and LibreOffice checks the two match on read
# (LibreOffice core package/source/zipapi/ciphercontext.cxx
# OCipherContext::finalizeCipherContextAndDispose). No associated data is
# authenticated -- the AAD is empty (CK_GCM_PARAMS.pAAD = NULL).
_GCM_IV_BYTES = 12
_GCM_TAG_BYTES = 16
_AES_256_KEY_BYTES = 32

# Argon2id defaults used when the loext attributes are absent -- RFC 9106 second
# recommended profile, matching LibreOffice's defaults ([related-work.md] Section 2):
# t = 3 passes, m = 65536 KiB (64 MiB), p = 4 lanes. LibreOffice always writes the
# loext attributes, so these are a defensive fallback rather than the common path.
_ARGON2_DEFAULT_ITERATIONS = 3
_ARGON2_DEFAULT_MEMORY_KIB = 65536
_ARGON2_DEFAULT_LANES = 4


class OdfUnsupportedError(NotImplementedError):
    """Raised for a member whose cipher no shipped primitive can handle.

    Now that ODF 1.3 (Argon2id + AES-256-GCM) is implemented alongside ODF 1.1
    (Blowfish CFB) and ODF 1.2 (AES-256-CBC), this is reserved for a manifest whose
    ``algorithm-name`` names none of those three ciphers -- a legal-but-unusual
    combination the OASIS schema permits but that we have no code path for.
    """


@dataclass(frozen=True)
class OdfEntry:
    """Crypto parameters for one encrypted package member, from the manifest.

    Every field except :attr:`ciphertext` comes straight from that member's
    ``<manifest:encryption-data>`` block; string fields keep the raw manifest URI
    / name so nothing is lost, and byte fields hold the Base64-decoded value.
    :attr:`full_path` is the member's name inside the ZIP -- i.e. where the
    ciphertext lives -- and :attr:`ciphertext` holds those stored bytes once the
    package reader has fetched them (the manifest alone cannot supply them, so
    :func:`parse_manifest` leaves it empty).
    """

    full_path: str  # manifest:full-path -- member name / ciphertext location in the ZIP
    media_type: str  # manifest:media-type
    size: int  # manifest:size -- declared *plaintext* length of the member
    checksum_type: str  # manifest:checksum-type URI (SHA1/1K or #sha256-1k)
    checksum: bytes  # manifest:checksum -- digest of the first <=1024 plaintext bytes
    cipher: str  # manifest:algorithm-name URI (Blowfish CFB / #aes256-cbc / #aes256-gcm)
    iv: bytes  # manifest:initialisation-vector (8 B Blowfish / 16 B AES-CBC / GCM nonce)
    key_derivation: str  # manifest:key-derivation-name ("PBKDF2" or "...:argon2id")
    iterations: int  # manifest:iteration-count (PBKDF2 rounds; 0 when Argon2)
    key_size: int  # manifest:key-size -- derived key length in bytes (16 or 32)
    salt: bytes  # manifest:salt (16 bytes typical)
    start_key: str  # manifest:start-key-generation-name URI ("" => implicit SHA-1, ODF 1.1)
    start_key_size: int  # manifest:start-key-generation/@key-size (20 or 32)
    argon2_iterations: int | None = None  # loext:argon2-iterations (t cost) -- ODF 1.3 only
    argon2_memory: int | None = None  # loext:argon2-memory in KiB (m cost) -- ODF 1.3 only
    argon2_lanes: int | None = None  # loext:argon2-lanes (p / parallelism) -- ODF 1.3 only
    ciphertext: bytes = b""  # the member's stored encrypted bytes (filled from the ZIP)


# --- Profile classification ---
#
# The OASIS schema treats start-key hash, KDF, cipher, and checksum as independent
# axes. We classify each from the meaningful token in its URI rather than assuming
# a fixed pairing, so a legal-but-unusual manifest is read faithfully.


def _uses_sha256_start(entry: OdfEntry) -> bool:
    """Return True when the start key is SHA-256 (ODF 1.2), else SHA-1 (ODF 1.1)."""
    # ODF 1.1 omits the start-key-generation element entirely -> implicit SHA-1.
    return _MARK_SHA256 in entry.start_key.lower()


def _uses_sha256_checksum(entry: OdfEntry) -> bool:
    """Return True when the /1K checksum is SHA-256, else SHA-1."""
    return _MARK_SHA256 in entry.checksum_type.lower()


def _is_aes_cbc(entry: OdfEntry) -> bool:
    """Return True for the AES-256-CBC cipher (ODF 1.2)."""
    return _MARK_AES_CBC in entry.cipher.lower()


def _is_blowfish(entry: OdfEntry) -> bool:
    """Return True for the Blowfish CFB-64 cipher (ODF 1.1)."""
    return _MARK_BLOWFISH in entry.cipher.lower()


def _uses_gcm(entry: OdfEntry) -> bool:
    """Return True for the AES-256-GCM cipher (ODF 1.3 AEAD -- GAP)."""
    return _MARK_GCM in entry.cipher.lower()


def _uses_argon2(entry: OdfEntry) -> bool:
    """Return True for the Argon2id key derivation (ODF 1.3 -- GAP)."""
    return _MARK_ARGON2 in entry.key_derivation.lower()


def is_gap(entry: OdfEntry) -> bool:
    """Return True when this member has no hashcat / John cracking mode (ODF 1.3).

    A member is in the GPU-cracking gap when it uses Argon2id key derivation or the
    AES-256-GCM AEAD cipher: a memory-hard KDF plus an AEAD tag has no hashcat mode.
    Such a member is still *decryptable* here with a known password (via
    :func:`verify` / :func:`decrypt_entry`) and still emits an extended
    ``$odf$*2*...`` line -- callers branch on this only to pick the hashcat mode
    (there is none) or to label the profile, not to skip the member.
    """
    return _uses_gcm(entry) or _uses_argon2(entry)


def _require_supported(entry: OdfEntry) -> None:
    """Raise :class:`OdfUnsupportedError` unless this member's cipher has a code path.

    All three ODF profiles are supported: Blowfish CFB (1.1), AES-256-CBC (1.2), and
    AES-256-GCM (1.3). Only a manifest naming some other cipher is rejected, with the
    observed value so the caller can report it.
    """
    if not (_uses_gcm(entry) or _is_aes_cbc(entry) or _is_blowfish(entry)):
        msg = f"unrecognized ODF cipher {entry.cipher!r} for member {entry.full_path!r}"
        raise OdfUnsupportedError(msg)


# --- Key derivation and decryption ---


def _derive_key(entry: OdfEntry, password: str) -> bytes:
    """Derive the symmetric key from ``password`` per [odf-encryption.md] Section 4.

    Three stages: (1) hash the raw UTF-8 password bytes to a start key
    (SHA-256 for ODF 1.2 / 1.3, SHA-1 for ODF 1.1); (2) stretch it -- PBKDF2-HMAC-SHA1
    over the manifest salt and iteration count (ODF 1.1 / 1.2) or Argon2id over the
    ``loext`` t/m/p parameters (ODF 1.3); (3) the result is the manifest key size
    (16 bytes Blowfish / 32 bytes AES-256). For PBKDF2 the PRF is HMAC-SHA1 in both
    profiles; the Argon2id input is the SHA-256 start key, not the raw password
    ([related-work.md] Section 2).
    """
    # ODF deviation: password is the raw UTF-8 bytes, never UTF-16LE, no NUL.
    password_bytes = password.encode("utf-8")

    # SHA-256 start key (32 B) for ODF 1.2 / 1.3; SHA-1 (20 B) for ODF 1.1. SHA-1
    # here is a legacy KDF primitive fixed by the format, not a security choice.
    start_key = _digest("sha256", password_bytes) if _uses_sha256_start(entry) else _digest("sha1", password_bytes)

    # ODF 1.3 replaces the PBKDF2 stretch with a memory-hard Argon2id pass.
    if _uses_argon2(entry):
        return _derive_key_argon2(entry, start_key)

    # PBKDF2 password is the *start key*, not the raw password; block counter is
    # big-endian 1-based; excess HMAC output is truncated to dkLen (handled by
    # pbkdf2_hmac's dklen). RFC 2898.
    return pbkdf2_hmac_sha1(start_key, entry.salt, entry.iterations, entry.key_size)


def _derive_key_argon2(entry: OdfEntry, start_key: bytes) -> bytes:
    """Derive the AES-256 key with Argon2id (ODF 1.3, [related-work.md] Section 2).

    LibreOffice feeds the SHA-256 start key (``start_key``) as the Argon2id secret,
    the manifest salt as the salt, and the ``loext:argon2-iterations`` / ``-memory``
    / ``-lanes`` attributes as t / m (KiB) / p, producing a 32-byte tag with
    argon2id v1.3 (LibreOffice core package/source/zipapi/ZipFile.cxx argon2id_ctx).
    Missing attributes fall back to the RFC 9106 second-recommendation defaults.
    """
    t_cost = entry.argon2_iterations or _ARGON2_DEFAULT_ITERATIONS
    memory_kib = entry.argon2_memory or _ARGON2_DEFAULT_MEMORY_KIB
    lanes = entry.argon2_lanes or _ARGON2_DEFAULT_LANES
    key_size = entry.key_size or _AES_256_KEY_BYTES
    return argon2id(secret=start_key, salt=entry.salt, time_cost=t_cost, memory_cost=memory_kib, parallelism=lanes, hash_len=key_size)


def _gcm_decrypt(entry: OdfEntry, key: bytes, member: bytes) -> bytes:
    """AES-256-GCM-decrypt one ODF 1.3 member; raise :class:`InvalidTag` if wrong.

    The stored member is ``IV(12) || ciphertext || tag(16)`` (LibreOffice core
    package/source/zipapi/ciphercontext.cxx). NSS decrypts with the manifest IV as
    the nonce and everything after the prepended IV (ciphertext followed by the
    16-byte tag) as the AEAD input; ``cryptography``'s :class:`AESGCM` expects the
    tag appended to the ciphertext, which is exactly ``member[12:]``. The AAD is
    empty. A wrong key (wrong password) fails the tag and raises
    :class:`~cryptography.exceptions.InvalidTag`.
    """
    ct_and_tag = member[_GCM_IV_BYTES:]
    return aes_gcm_decrypt(key, entry.iv, ct_and_tag, None)


def _inflate(plaintext: bytes) -> bytes:
    """Raw-DEFLATE-inflate a decrypted ODF member (no zlib header; wbits -15).

    ``flush()`` returns any buffered tail; a truncated prefix simply yields the
    partial inflate without raising.
    """
    inflater = zlib.decompressobj(_RAW_DEFLATE_WBITS)
    return inflater.decompress(plaintext) + inflater.flush()


def _decrypt_cipher(entry: OdfEntry, key: bytes, ciphertext: bytes) -> bytes:
    """Decrypt ``ciphertext`` with the profile's cipher ([odf-encryption.md] Section 5).

    ODF 1.2 uses AES-256-CBC; ODF 1.1 uses Blowfish in full 8-byte-feedback CFB-64
    (``cryptography``'s :class:`CFB` is full-block feedback, i.e. CFB-64 for the
    64-bit Blowfish block). Neither mode pads, so no unpadding is done.
    """
    if _is_aes_cbc(entry):
        # CBC needs whole blocks; trim any trailing partial block from a capped prefix.
        usable = len(ciphertext) - (len(ciphertext) % _AES_BLOCK_BYTES)
        return aes_cbc_decrypt(key, entry.iv, ciphertext[:usable])

    # Blowfish CFB-64 -- a stream mode, so any ciphertext length is accepted.
    return blowfish_cfb_decrypt(key, entry.iv, ciphertext)


def _plaintext_checksum(entry: OdfEntry, plaintext: bytes) -> bytes:
    """Return the SHA/1K digest of the first <=1024 decrypted plaintext bytes.

    The digest is over the *compressed* plaintext (the raw DEFLATE stream) -- never
    inflate before hashing. SHA-256 for the ODF 1.2 profile, SHA-1 for ODF 1.1.
    """
    window = plaintext[:_CHECKSUM_WINDOW_BYTES]
    if _uses_sha256_checksum(entry):
        return _digest("sha256", window)
    return _digest("sha1", window)


def verify(entry: OdfEntry, password: str, ciphertext: bytes) -> bool:
    """Return True iff ``password`` decrypts ``ciphertext`` correctly.

    ODF 1.1 / 1.2 derive the key ([odf-encryption.md] Section 4), decrypt, and
    compare the SHA/1K digest of the first <=1024 plaintext bytes against the
    manifest checksum with a constant-time compare (Section 5) -- ``ciphertext`` is
    the member's stored bytes (a >=1024-byte prefix is enough). ODF 1.3 (AES-GCM)
    has no plaintext checksum: the 16-byte GCM auth tag is the verifier, so the
    whole ``IV || ciphertext || tag`` member is required and the password is correct
    iff the tag validates. Raises :class:`OdfUnsupportedError` for an unknown cipher.
    """
    _require_supported(entry)
    key = _derive_key(entry, password)

    # ODF 1.3: the AEAD tag both authenticates and verifies the password.
    if _uses_gcm(entry):
        try:
            _gcm_decrypt(entry, key, ciphertext)
        except InvalidTag:
            logger.debug("ODF verify: fail (cipher=%s, GCM tag invalid)", entry.cipher)
            return False
        logger.debug("ODF verify: pass (cipher=%s, GCM tag valid)", entry.cipher)
        return True

    plaintext = _decrypt_cipher(entry, key, ciphertext)
    digest = _plaintext_checksum(entry, plaintext)
    # Full-width, constant-time compare -- a match is the correct password.
    result = compare_digest(digest, entry.checksum)
    logger.debug("ODF verify: %s (cipher=%s)", "pass" if result else "fail", entry.cipher)
    return result


def decrypt_entry(entry: OdfEntry, password: str, ciphertext: bytes, *, verify: bool = True) -> bytes:
    """Decrypt and inflate one member; raise ``ValueError`` on the wrong password.

    ODF 1.1 / 1.2 run PBKDF2 key derivation -> cipher decrypt -> checksum gate ->
    raw-DEFLATE inflate. ODF 1.3 runs Argon2id key derivation -> AES-256-GCM decrypt
    (the tag gates the password) -> raw-DEFLATE inflate; ``ciphertext`` must be the
    whole ``IV || ciphertext || tag`` member. On a correct password the inflated
    member bytes are returned; a checksum or GCM-tag mismatch raises ``ValueError``.

    Pass ``verify=False`` to skip the plaintext-checksum gate for a CBC/CFB member
    once the package password is already confirmed against ``content.xml``: some
    small LibreOffice members -- embedded Basic macro scripts especially -- carry a
    stored ``/1K`` checksum that does not match the recomputed one even though the
    key is correct, so a strict per-member gate would spuriously reject a good
    password. GCM always enforces its tag (the bytes cannot be recovered without
    it). Raises :class:`OdfUnsupportedError` for an unknown cipher.
    """
    _require_supported(entry)
    key = _derive_key(entry, password)

    # ODF 1.3: no plaintext checksum -- an InvalidTag means the wrong password.
    if _uses_gcm(entry):
        try:
            plaintext = _gcm_decrypt(entry, key, ciphertext)
        except InvalidTag as exc:
            msg = f"incorrect password for ODF member {entry.full_path!r}: GCM authentication tag mismatch"
            raise ValueError(msg) from exc
        return _inflate(plaintext)

    plaintext = _decrypt_cipher(entry, key, ciphertext)
    if verify and not compare_digest(_plaintext_checksum(entry, plaintext), entry.checksum):
        msg = f"incorrect password for ODF member {entry.full_path!r}: checksum mismatch"
        raise ValueError(msg)
    return _inflate(plaintext)


# --- Hash-line emission (odf2john / hashcat 18400 & 18600 + ODF 1.3 extension) ---


def _cipher_type(entry: OdfEntry) -> int:
    """Map the cipher to the ``$odf$`` cipher_type token (0/1 hashcat, 2 = AES-GCM)."""
    if _uses_gcm(entry):
        return 2  # [odf-encryption.md] Section 7 proposed extension: AES-256-GCM
    if _is_aes_cbc(entry):
        return 1
    return 0  # Blowfish CFB


def odf_hash_line(entry: OdfEntry) -> str:
    """Return the ``$odf$*...`` hash line for this member ([odf-encryption.md] Section 7).

    For ODF 1.1 / 1.2 this is the twelve-token, ``*``-separated odf2john /
    libreoffice2john layout that hashcat 18600 (Blowfish, ``cipher_type=0``) and
    18400 (AES-CBC, ``cipher_type=1``) load::

        $odf$ * cipher_type * checksum_type * iterations * key_size * checksum
              * iv_len * iv * salt_len * salt * unused(0) * ciphertext

    For ODF 1.3 (Argon2id + AES-256-GCM) it emits the Section 7 *extension*: the same
    twelve leading tokens (``cipher_type=2``, an empty checksum since AEAD has no
    plaintext digest, and the ``iterations`` token 0 for a non-PBKDF2 KDF) followed
    by six trailing tokens ``kdf * gcm_tag * start_key * m_cost * t_cost * lanes``.
    No hashcat mode loads that line -- it is a labelled, self-contained record.

    ``checksum`` / ``iv`` / ``salt`` / ``ciphertext`` / ``gcm_tag`` are lowercase
    hex. Requires :attr:`OdfEntry.ciphertext` to be populated. Raises
    :class:`OdfUnsupportedError` for an unknown cipher.
    """
    _require_supported(entry)
    if is_gap(entry):
        return unified_odf_line(entry)

    # Fixed token values enforced by the hashcat parsers: cipher_type pairs with
    # checksum_type (0,0 = Blowfish/SHA-1 ; 1,1 = AES-CBC/SHA-256).
    checksum_type = 1 if _uses_sha256_checksum(entry) else 0
    tokens = [
        "$odf$",
        str(_cipher_type(entry)),
        str(checksum_type),
        str(entry.iterations),
        str(entry.key_size),
        entry.checksum.hex(),
        str(len(entry.iv)),
        entry.iv.hex(),
        str(len(entry.salt)),
        entry.salt.hex(),
        "0",  # token 10 "unused" -- parsers require it to be 0
        entry.ciphertext[:_CIPHERTEXT_CAP_BYTES].hex(),
    ]
    return "*".join(tokens)


def unified_odf_line(entry: OdfEntry) -> str:
    """Emit the self-describing ``$odf$*...`` line with named primitives.

    Grammar (docs/reference/hash-formats.md):
    ``$odf$*<startkey>*<kdf>*<cipher>*<iters>*<mem>*<lanes>*<salt>*<iv>*<checksum>*<ciphertext>``

    Uses named tokens (``sha1``/``sha256``, ``pbkdf2``/``argon2``, ``blowfish``/``aes256``/
    ``aes256gcm``) instead of the hashcat-era numeric type codes. For ODF 1.3 (GCM), the
    checksum field carries the 16-byte auth tag and ``iters`` is the Argon2id time cost.
    Raises :class:`OdfUnsupportedError` for an unknown cipher (same as ``odf_hash_line``).
    """
    _require_supported(entry)
    startkey = "sha256" if _uses_sha256_start(entry) else "sha1"
    kdf = "argon2" if _uses_argon2(entry) else "pbkdf2"
    if _uses_gcm(entry):
        cipher = "aes256gcm"
    elif _is_aes_cbc(entry):
        cipher = "aes256"
    else:
        cipher = "blowfish"
    iters = (entry.argon2_iterations or _ARGON2_DEFAULT_ITERATIONS) if _uses_argon2(entry) else entry.iterations
    mem = (entry.argon2_memory or _ARGON2_DEFAULT_MEMORY_KIB) if _uses_argon2(entry) else 0
    lanes = (entry.argon2_lanes or _ARGON2_DEFAULT_LANES) if _uses_argon2(entry) else 0
    if _uses_gcm(entry) and len(entry.ciphertext) >= _GCM_IV_BYTES + _GCM_TAG_BYTES:
        checksum_hex = entry.ciphertext[-_GCM_TAG_BYTES:].hex()
        ct_hex = entry.ciphertext[_GCM_IV_BYTES:-_GCM_TAG_BYTES].hex()
    else:
        checksum_hex = entry.checksum.hex()
        ct_hex = entry.ciphertext[:_CIPHERTEXT_CAP_BYTES].hex()
    return f"$odf$*{startkey}*{kdf}*{cipher}*{iters}*{mem}*{lanes}*{entry.salt.hex()}*{entry.iv.hex()}*{checksum_hex}*{ct_hex}"


# --- Manifest parsing ---


def _local_name(qualified: str) -> str:
    """Return the local part of a namespace-qualified XML name (drop the prefix)."""
    return qualified.rsplit(":", 1)[-1]


def _attr_map(attrs: dict[str, str]) -> dict[str, str]:
    """Re-key an expat attribute dict by local name (drop the namespace prefix)."""
    # Local names within one element are unique in the ODF schema, so a flat map is
    # safe (e.g. manifest:full-path -> full-path, loext:argon2-memory -> argon2-memory).
    return {_local_name(name): value for name, value in attrs.items()}


def _b64(value: str) -> bytes:
    """Base64-decode a manifest attribute value (empty string -> empty bytes)."""
    if not value:
        return b""
    return base64.b64decode(value)


def _opt_int(value: str | None) -> int | None:
    """Parse an optional decimal attribute; return None when absent/empty."""
    if value is None or value == "":
        return None
    return int(value)


class _ManifestReader:
    """Streaming collector for ``META-INF/manifest.xml`` crypto blocks.

    Driven by :mod:`xml.parsers.expat` start/end callbacks (registered in
    :func:`parse_manifest`) rather than DOM parsing -- no tree is materialised and
    no external entities are resolved. For each ``<manifest:file-entry>`` we buffer
    its ``<encryption-data>`` / ``<algorithm>`` / ``<key-derivation>`` /
    ``<start-key-generation>`` children and emit one :class:`OdfEntry` per
    encrypted member when the entry closes.
    """

    def __init__(self) -> None:
        """Initialise the collector state."""
        self.entries: list[OdfEntry] = []
        self._in_entry = False
        self._fe_attrs: dict[str, str] = {}
        self._elements: dict[str, dict[str, str]] = {}

    def start_element(self, name: str, attrs: dict[str, str]) -> None:
        """Handle an expat start-element event (also fires for self-closing tags)."""
        local = _local_name(name)
        if local == "file-entry":
            # A new member begins -- reset the per-entry accumulator.
            self._in_entry = True
            self._fe_attrs = _attr_map(attrs)
            self._elements = {}
            return
        if self._in_entry and local in _CRYPTO_ELEMENTS:
            self._elements[local] = _attr_map(attrs)

    def end_element(self, name: str) -> None:
        """Handle an expat end-element event, finalising a file-entry."""
        if _local_name(name) == "file-entry" and self._in_entry:
            built = self._build()
            if built is not None:
                self.entries.append(built)
            self._in_entry = False

    def _build(self) -> OdfEntry | None:
        """Assemble an :class:`OdfEntry` for the current member, or None if unencrypted."""
        enc = self._elements.get(_EL_ENCRYPTION_DATA)
        if enc is None:
            # No <encryption-data> child -> this member is stored in the clear.
            return None

        alg = self._elements.get(_EL_ALGORITHM, {})
        kdf = self._elements.get(_EL_KEY_DERIVATION, {})
        start = self._elements.get(_EL_START_KEY, {})

        return OdfEntry(
            full_path=self._fe_attrs.get("full-path", ""),
            media_type=self._fe_attrs.get("media-type", ""),
            size=int(self._fe_attrs.get("size", "0") or "0"),
            checksum_type=enc.get("checksum-type", ""),
            checksum=_b64(enc.get("checksum", "")),
            cipher=alg.get("algorithm-name", ""),
            iv=_b64(alg.get("initialisation-vector", "")),
            key_derivation=kdf.get("key-derivation-name", ""),
            iterations=int(kdf.get("iteration-count", "0") or "0"),
            key_size=int(kdf.get("key-size", "0") or "0"),
            salt=_b64(kdf.get("salt", "")),
            start_key=start.get("start-key-generation-name", ""),
            start_key_size=int(start.get("key-size", "0") or "0"),
            argon2_iterations=_opt_int(kdf.get("argon2-iterations")),
            argon2_memory=_opt_int(kdf.get("argon2-memory")),
            argon2_lanes=_opt_int(kdf.get("argon2-lanes")),
        )


def parse_manifest(manifest_xml: bytes) -> list[OdfEntry]:
    """Parse ``META-INF/manifest.xml`` into one :class:`OdfEntry` per encrypted member.

    Reads each ``<manifest:file-entry>`` and, when it carries a
    ``<manifest:encryption-data>`` child, extracts the cipher, key-derivation
    (name / iterations / key-size / salt), start-key algorithm, IV, and checksum.
    Members stored in the clear (no ``<encryption-data>``) are skipped, so an
    unencrypted package yields ``[]``. ODF 1.3 Argon2id / AES-GCM members are
    parsed and returned too (with their loext Argon2 parameters); use
    :func:`is_gap` to detect them before attempting to crack. :attr:`ciphertext`
    is not set -- the manifest does not contain it -- and must be filled from the
    member's stored ZIP bytes.
    """
    reader = _ManifestReader()
    parser = xml.parsers.expat.ParserCreate()
    parser.StartElementHandler = reader.start_element
    parser.EndElementHandler = reader.end_element
    # expat consumes the raw bytes and honours the XML declaration's encoding/BOM.
    is_final = True  # single-shot parse: the whole document is supplied at once
    parser.Parse(manifest_xml, is_final)
    logger.debug("ODF manifest: %d encrypted entries", len(reader.entries))
    return reader.entries
