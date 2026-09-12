"""Self-test vectors for the ECMA-376 standard and agile crypto module.

Each vector is a published hashcat self-test hash for the password ``hashcat``
(modes 9400 / 9500 / 9600). We rebuild an ``EncryptionInfo`` from the hash-line
tokens, then assert that:

* the correct password verifies and a wrong one does not,
* the low-level ``_verify_standard`` / ``_verify_agile`` drivers agree, and
* ``office_hash_line`` round-trips back to the original line.
"""

from __future__ import annotations

import pytest

from office_password_toolkit.crypto.ecma376 import (
    EncryptionInfo,
    EncryptionKind,
    _verify_agile,
    _verify_standard,
    office_hash_line,
    verify_password,
)

PASSWORD = "hashcat"
WRONG = "Password1!"

# hashcat 9400 (Office 2007 standard, AES-128 + SHA-1 x50000).
VECTOR_9400 = "$office$*2007*20*128*16*18410007331073848057180885845227*944c70a5ee6e5ab2a6a86ff54b5f621a*e6650f1f2630c27fd8fc0f5e56e2e01f99784b9f"
# hashcat 9500 (Office 2010 agile, AES-128 + SHA-1 x100000).
VECTOR_9500 = "$office$*2010*100000*128*16*34170046140146368675746031258762*de5bc114991bb3a5679a6e24320bdb09*1b72a4ddffba3dcd5395f6a5ff75b126cb832b733c298e86162028ca47a235a9"
# hashcat 9600 (Office 2013 agile, AES-256 + SHA-512 x100000).
VECTOR_9600 = "$office$*2013*100000*256*16*67805436882475302087847656644837*0c392d3b9ca889656d1e615c54f9f3c9*612b79e33b96322c3253fc8a0f314463cd76bc4efe1352f7efffca0f374f7e4b"


def _standard_info(line: str) -> EncryptionInfo:
    parts = line.split("*")
    return EncryptionInfo(
        kind=EncryptionKind.STANDARD,
        version_major=4,
        version_minor=2,
        salt=bytes.fromhex(parts[5]),
        key_bits=int(parts[3]),
        spin_count=50000,
        hash_algorithm="SHA-1",
        cipher_algorithm="AES",
        cipher_chaining="ChainingModeECB",
        block_size=16,
        hash_size=int(parts[2]),
        enc_verifier=bytes.fromhex(parts[6]),
        enc_verifier_hash=bytes.fromhex(parts[7]),
    )


def _agile_info(line: str, hash_algorithm: str) -> EncryptionInfo:
    parts = line.split("*")
    key_bits = int(parts[3])
    return EncryptionInfo(
        kind=EncryptionKind.AGILE,
        version_major=4,
        version_minor=4,
        salt=bytes.fromhex(parts[5]),
        key_bits=key_bits,
        spin_count=int(parts[2]),
        hash_algorithm=hash_algorithm,
        cipher_algorithm="AES",
        cipher_chaining="ChainingModeCBC",
        block_size=16,
        hash_size=20 if key_bits == 128 else 64,
        enc_verifier=bytes.fromhex(parts[6]),
        enc_verifier_hash=bytes.fromhex(parts[7]),
    )


def test_9400_standard_verifies():
    info = _standard_info(VECTOR_9400)
    assert verify_password(info, PASSWORD) is True
    assert verify_password(info, WRONG) is False
    # low-level driver, straight from the parsed EncryptionInfo
    assert _verify_standard(info, PASSWORD) is True
    assert _verify_standard(info, WRONG) is False


def test_9500_agile_verifies():
    info = _agile_info(VECTOR_9500, "SHA-1")
    assert verify_password(info, PASSWORD) is True
    assert verify_password(info, WRONG) is False
    assert _verify_agile(info, PASSWORD) is True


def test_9600_agile_verifies():
    info = _agile_info(VECTOR_9600, "SHA512")
    assert verify_password(info, PASSWORD) is True
    assert verify_password(info, WRONG) is False
    assert _verify_agile(info, PASSWORD) is True


@pytest.mark.parametrize(
    ("line", "info"),
    [
        (VECTOR_9400, _standard_info(VECTOR_9400)),
        (VECTOR_9500, _agile_info(VECTOR_9500, "SHA-1")),
        (VECTOR_9600, _agile_info(VECTOR_9600, "SHA512")),
    ],
)
def test_hash_line_round_trips(line: str, info: EncryptionInfo):
    assert office_hash_line(info) == line
