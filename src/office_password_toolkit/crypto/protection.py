# SPDX-License-Identifier: Apache-2.0
"""ISO write/sheet/workbook/document protection verifier hash ([MS-OFFCRYPTO] Section 2.4.2.4).

This module implements the single password *verifier* that gates document-level
editing across the OOXML (``.docx``/``.xlsx``/``.pptx``) and binary (``.xlsb``)
Office family: "read-only recommended" / "password to modify", Protect Sheet,
Protect Workbook, Allow Edit Ranges, and Word Restrict Editing. It is a verifier
only -- the package body is plaintext ZIP, so this hash confirms a password but
decrypts nothing. The salt, spin count, algorithm name, and hash all sit in the
clear inside XML attributes (``algorithmName``/``saltValue``/``hashValue``/
``spinCount``) or a ``Brt*ProtectionIso`` binary record.

Key design decision -- iterator placement. The ISO write-protection KDF
*appends* the little-endian round counter to the previous digest
(``Hn = H(Hn-1 || LE32(i))``) and has **no** block key. This is the mirror image
of the document-*open* agile KDF ([MS-OFFCRYPTO] Section 2.3.4.11), which
*prepends* the counter (``Hn = H(LE32(i) || Hn-1)``) and finalises with a block
key. Both start from ``H(salt || password)``, but reversing the per-round order
silently produces a wrong digest -- the single most common implementation error
in this family. The self-test vectors in this module's tests pin the APPEND
order for both SHA-512 and SHA-1.

hashcat mode 25300 ("MS Office 2016 - SheetProtection") implements exactly this
KDF but hard-pins the SHA-512 + spinCount 100000 + 16-byte-salt shape; every
other ``algorithmName``/``spinCount``/salt length is a coverage gap that must be
verified with this standalone code instead.
"""

from __future__ import annotations

import logging
from base64 import b64decode, b64encode
from typing import TYPE_CHECKING, Final

from office_password_toolkit.crypto import hashes
from office_password_toolkit.crypto.xor import password_verifier_method2

if TYPE_CHECKING:
    import hashlib
    from collections.abc import Callable

logger = logging.getLogger(__name__)

# --- Algorithm dispatch ---

# The reserved algorithm set per [MS-OFFCRYPTO] Section 2.4.2.4 / [MS-OE376] Section 2.1.438.
# _canonical_algorithm() normalises the many wire variants ("SHA-512", "SHA512", "sha 512", ...)
# onto these keys; _resolve_hash() maps them to hashes.new() constructors.
_SUPPORTED_ALGORITHMS: Final[frozenset[str]] = frozenset({"SHA-1", "SHA-256", "SHA-384", "SHA-512", "MD5", "MD4", "MD2"})

# The counter appended each round is a 4-byte little-endian unsigned int
# ([MS-OFFCRYPTO] Section 1.3.6: all container integers are little-endian).
_COUNTER_WIDTH: Final = 4
_COUNTER_ORDER: Final = "little"

# --- 25300 hash-line constraints ---

# hashcat 25300 pins this exact shape (module_25300.c): SHA-512 digest (64 B),
# 16-byte salt, spinCount fixed at 100000.
_MODE_25300_SPIN_COUNT: Final = 100_000
_MODE_25300_SALT_LEN: Final = 16
_MODE_25300_DIGEST_LEN: Final = 64
# Signature literal; the trailing ``0`` is the SHEETPROTECTION subtype discriminator.
_MODE_25300_SIGNATURE: Final = "$office$2016$0"

# --- Generalized protection hash-line formats ---

# hashcat 25300 only ingests the SHA-512/spin-100000/16-byte-salt shape, so every
# other ISO primitive/spin/salt is a coverage gap. iso-protection-hash.md Section 7
# proposes a generalized line that also carries the primitive and an arbitrary salt:
#   $office$protect$<algo_id>$<spinCount>$<saltValue_b64>$<hashValue_b64>
# algo_id and the digest byte width per primitive are pinned by the [MS-OFFCRYPTO]
# Section 2.4.2.4 reserved-value table (widths repeated in iso-protection-hash.md
# Section 6). The width lets a caller check the hash is the primitive it claims.
_PROTECT_ALGO_PROFILES: Final[dict[str, tuple[int, int]]] = {
    "SHA-1": (0, 20),
    "SHA-256": (1, 32),
    "SHA-384": (2, 48),
    "SHA-512": (3, 64),
    "MD5": (4, 16),
    "MD4": (5, 16),
    "MD2": (6, 16),
}
# spinCount and salt bounds shared by every ISO carrier ([MS-OFFCRYPTO] Section 2.4.2.4).
_SPIN_COUNT_MAX: Final = 10_000_000
_SALT_LEN_MAX: Final = 65_536

# Word 2007 legacy documentProtection/writeProtection line
# (word2007-documentprotection.md Section 7). This is a DIFFERENT construction from
# the ISO KDF above -- a legacy-derived, salt-appended, iterated hash whose exact
# stage-1 math is UNCONFIRMED in the corpus (word2007-documentprotection.md Section
# 6.1), so this module only FORMATS the extraction line and does not recompute it.
#   $doc-protect$1*<cryptAlgorithmSid>*<cryptSpinCount>*<salt_b64>*<hash_b64>
# The leading type digit 1 selects the Word-2007 legacy-derived generation. The
# cryptAlgorithmSid is a CryptoAPI ALG_SID whose digest width is fixed
# (word2007-documentprotection.md Section 6, [MS-OE376] Section 2.1.410 note h).
_WORD2007_SID_DIGESTS: Final[dict[int, int]] = {
    1: 16,  # MD2
    2: 16,  # MD4
    3: 16,  # MD5
    4: 20,  # SHA-1 (Word 2007 default)
    12: 32,  # SHA-256
    13: 48,  # SHA-384
    14: 64,  # SHA-512
}
_WORD2007_SID_CANONICAL: Final[dict[int, str]] = {
    1: "MD2",
    2: "MD4",
    3: "MD5",
    4: "SHA-1",
    12: "SHA-256",
    13: "SHA-384",
    14: "SHA-512",
}
# Word clamps the iteration count tighter than the ISO carriers ([MS-OE376] Section 2.1.410 note j).
_WORD2007_SPIN_MAX: Final = 5_000_000


def _canonical_algorithm(algorithm_name: str) -> str:
    """Normalise an XML ``algorithmName`` string onto a canonical spec key.

    Real files and third-party producers spell the primitive several ways --
    ``"SHA-512"``, ``"SHA512"``, ``"sha 512"`` -- so we strip separators and
    case before matching. Returns the canonical key used by ``_HASH_CTORS`` /
    ``_UNSUPPORTED_ALGORITHMS`` (e.g. ``"SHA-512"``), or the upper-cased original
    when unrecognised so the caller can report it verbatim.
    """
    squashed = "".join(ch for ch in algorithm_name.upper() if ch.isalnum())
    lookup: dict[str, str] = {
        "SHA1": "SHA-1",
        "SHA256": "SHA-256",
        "SHA384": "SHA-384",
        "SHA512": "SHA-512",
        "MD5": "MD5",
        "MD2": "MD2",
        "MD4": "MD4",
    }
    return lookup.get(squashed, algorithm_name.upper())


def _resolve_hash(algorithm_name: str) -> Callable[[bytes], hashlib._Hash | hashes._LegacyHashWrapper]:
    """Resolve an ``algorithmName`` to a hashlib-compatible constructor.

    All algorithms (SHA-1/256/384/512, MD5, MD4, MD2) are routed through
    ``hashes.new()`` which handles both stdlib hashlib and the toolkit's own
    pure-Python MD4/MD2 implementations transparently.
    """
    canonical = _canonical_algorithm(algorithm_name)
    if canonical not in _SUPPORTED_ALGORITHMS:
        msg = f"Unknown algorithmName {algorithm_name!r}; not a reserved ISO write-protection primitive ([MS-OFFCRYPTO] Section 2.4.2.4)"
        raise ValueError(msg)
    hashlib_name = canonical.lower().replace("-", "")
    return lambda data, _name=hashlib_name: hashes.new(_name, data)


def iso_protection_hash(password: str, salt: bytes, spin_count: int, algorithm_name: str) -> bytes:
    """Compute the ISO write-protection verifier digest ([MS-OFFCRYPTO] Section 2.4.2.4).

    Steps, generalised over ``algorithmName``:

    1. Encode ``password`` as UTF-16LE (2 bytes/char, no BOM, no NUL) -- the
       encoding used by every MS Office password scheme.
    2. ``H0 = H(salt || pw)`` -- salt is **prepended** to the password.
    3. For ``i`` in ``0 .. spin_count-1``: ``Hn = H(Hn-1 || LE32(i))`` -- the
       4-byte little-endian round counter is **appended** after the prior digest,
       with **no** block key. The last counter value is ``spin_count - 1``.
    4. Return ``Hfinal`` (the final digest), compared against ``hashValue``.

    Args:
        password: Candidate password (Unicode string).
        salt: Raw salt bytes (base64-decoded ``saltValue``).
        spin_count: Iteration count from ``spinCount``; the loop runs exactly
            this many rounds. The initial hash is not counted as a round.
        algorithm_name: The ``algorithmName`` attribute selecting ``H()``.

    Returns:
        The verifier digest ``Hfinal`` (natural, big-endian digest byte order).

    """
    logger.debug("ISO protection hash: algo=%s spinCount=%d saltLen=%d", algorithm_name, spin_count, len(salt))
    hash_ctor = _resolve_hash(algorithm_name)
    # UTF-16LE password bytes, no BOM and no NUL terminator ([MS-OFFCRYPTO] Section 2.4.2.4).
    pw = password.encode("utf-16-le")
    # Initial hash: salt PREPENDED to the password. H0 = H(salt || pw).
    digest = hash_ctor(salt + pw).digest()
    # Spin loop: counter APPENDED as 4-byte LE, no block key. Hn = H(Hn-1 || LE32(i)).
    for i in range(spin_count):
        digest = hash_ctor(digest + i.to_bytes(_COUNTER_WIDTH, _COUNTER_ORDER)).digest()
    return digest


def verify(password: str, salt: bytes, spin_count: int, algorithm_name: str, expected_hash: bytes) -> bool:
    """Return True when ``password`` reproduces ``expected_hash`` under the ISO KDF.

    Recomputes the verifier via :func:`iso_protection_hash` and compares the full
    digest width in constant time. Because the compare is over a full-width
    cryptographic digest, false positives are cryptographically negligible.
    """
    got = iso_protection_hash(password, salt, spin_count, algorithm_name)
    result = hashes.compare_digest(got, expected_hash)
    logger.debug("ISO protection verify: %s (algo=%s)", "pass" if result else "fail", algorithm_name)
    return result


def hash_line_25300(salt_b64: str, hash_b64: str, spin_count: int = _MODE_25300_SPIN_COUNT) -> str:
    """Format a hashcat mode 25300 line, valid ONLY for the SHA-512 sheet-protection shape.

    Emits ``$office$2016$0$<spin>$<saltb64>$<hashb64>``. hashcat 25300
    (module_25300.c) hard-pins SHA-512, spinCount 100000, and a 16-byte salt, so
    this raises ValueError for any other shape. Callers use this only when the
    material matches that shape; otherwise they report the gate as a GAP with no
    crackable line (SHA-1, non-100000 spin counts, and other salt lengths have no
    hashcat mode).

    Args:
        salt_b64: Base64 ``saltValue`` (must decode to exactly 16 bytes).
        hash_b64: Base64 ``hashValue`` (must decode to exactly 64 bytes, SHA-512).
        spin_count: Iteration count; must be exactly 100000 for mode 25300.

    """
    # spinCount is fixed at 100000 by the 25300 parser (module_25300.c:164).
    if spin_count != _MODE_25300_SPIN_COUNT:
        msg = f"hashcat 25300 requires spinCount == {_MODE_25300_SPIN_COUNT}, got {spin_count}"
        raise ValueError(msg)
    # Salt must decode to exactly 16 bytes (module_25300.c:181).
    salt = b64decode(salt_b64)
    if len(salt) != _MODE_25300_SALT_LEN:
        msg = f"hashcat 25300 requires a {_MODE_25300_SALT_LEN}-byte salt, saltValue decodes to {len(salt)} bytes"
        raise ValueError(msg)
    # Hash must decode to exactly 64 bytes, which hard-wires SHA-512 (module_25300.c:199).
    digest = b64decode(hash_b64)
    if len(digest) != _MODE_25300_DIGEST_LEN:
        msg = f"hashcat 25300 requires a {_MODE_25300_DIGEST_LEN}-byte SHA-512 hash, hashValue decodes to {len(digest)} bytes"
        raise ValueError(msg)
    # Re-encode from the decoded bytes so the emitted line uses canonical base64.
    return f"{_MODE_25300_SIGNATURE}${spin_count}${b64encode(salt).decode('ascii')}${b64encode(digest).decode('ascii')}"


def word2007_protection_verify(password: str, crypt_algorithm_sid: int, spin_count: int, salt_b64: str, hash_b64: str) -> bool:
    """Verify a password against a Word 2007 legacy ``crypt*`` protection hash.

    The Word 2007 ``crypt*`` dialect (``cryptAlgorithmSid`` / ``cryptSpinCount``
    / ``w:salt`` / ``w:hash`` on ``<w:documentProtection>`` or
    ``<w:writeProtection>``) uses a KDF whose exact iteration math has NOT been
    confirmed against any public spec or reference implementation. The ISO KDF
    (counter APPENDED), the agile document-open KDF (counter PREPENDED), and
    several other standard variants have all been tested against corpus files
    and none reproduce the stored hash.

    The KDF for ``<w:documentProtection>`` has a legacy pre-stage: the password is
    first reduced through ``CreatePasswordVerifier_Method2`` (a 32-bit legacy hash),
    then rendered as uppercase hex LE-bytes, UTF-16LE-encoded, and hashed with the
    salt PREPENDED and the counter appended per round. Confirmed against 4 corpus
    vectors from Office 2007 and 2013. Note: the analysis doc (word2007-documentprotection.md
    §4) says salt is appended per [MS-OE376] §2.1.410 note f, but empirical testing
    shows salt is prepended — `H(salt || X)`, not `H(X || salt)`.

    ``<w:writeProtection>`` with ``crypt*`` attributes uses the standard ISO KDF
    instead — raw UTF-16LE password, salt prepended, counter appended — the same
    construction as ``iso_protection_hash`` (confirmed against corpus vectors).
    """
    digest_len = _WORD2007_SID_DIGESTS.get(crypt_algorithm_sid)
    if digest_len is None:
        msg = f"cryptAlgorithmSid {crypt_algorithm_sid} is not a Word-supported primitive"
        raise ValueError(msg)
    canonical = _WORD2007_SID_CANONICAL[crypt_algorithm_sid]
    hash_ctor = _resolve_hash(canonical)
    salt = b64decode(salt_b64)
    expected = b64decode(hash_b64)
    legacy_hash = password_verifier_method2(password)
    le_hex = legacy_hash.to_bytes(4, "little").hex().upper()
    pre_stage = le_hex.encode("utf-16-le")
    h = hash_ctor(salt + pre_stage).digest()
    for i in range(spin_count):
        h = hash_ctor(h + i.to_bytes(_COUNTER_WIDTH, _COUNTER_ORDER)).digest()
    return hashes.compare_digest(h, expected)


# --- Unified $protect$ line (docs/reference/hash-formats.md) ---


_SID_TO_HASH: Final[dict[int, str]] = {1: "md2", 2: "md4", 3: "md5", 4: "sha1", 12: "sha256", 13: "sha384", 14: "sha512"}


def unified_protect_line(algorithm_name: str, kdf: str, spin_count: int, salt_b64: str, hash_b64: str) -> str:
    """Emit the self-describing ``$protect$*...`` line for any ISO or Word 2007 protection verifier.

    Grammar (docs/reference/hash-formats.md):
    ``$protect$*<hashfunc>*<kdf>*<iters>*<salt_hex>*<hash_hex>``

    ``kdf`` is ``iso`` for the standard ISO write-protection KDF ([MS-OFFCRYPTO] Section 2.4.2.4:
    salt prepended, counter appended, no block key) or ``word2007`` for the legacy three-stage
    Word 2007 KDF ([MS-OE376] Section 2.1.410). Salt and hash are base64-decoded to lowercase
    hex for uniform byte representation across all formats.
    """
    hash_token = _canonical_algorithm(algorithm_name).lower().replace("-", "")
    salt_hex = b64decode(salt_b64).hex()
    hash_hex = b64decode(hash_b64).hex()
    return f"$protect$*{hash_token}*{kdf}*{spin_count}*{salt_hex}*{hash_hex}"


def unified_protect_line_from_sid(crypt_algorithm_sid: int, spin_count: int, salt_b64: str, hash_b64: str) -> str:
    """Emit the ``$protect$*...`` line from a Word 2007 ``cryptAlgorithmSid``."""
    hash_token = _SID_TO_HASH.get(crypt_algorithm_sid, f"sid{crypt_algorithm_sid}")
    salt_hex = b64decode(salt_b64).hex()
    hash_hex = b64decode(hash_b64).hex()
    return f"$protect$*{hash_token}*word2007*{spin_count}*{salt_hex}*{hash_hex}"
