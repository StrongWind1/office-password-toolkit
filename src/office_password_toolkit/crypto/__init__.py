# SPDX-License-Identifier: Apache-2.0
"""Cryptographic primitives and verifiers used by the format handlers.

Modules:
``xor`` (legacy 16/32-bit verifiers + obfuscation array, [MS-OFFCRYPTO] Section 2.3.7),
``rc4legacy`` (MD5 and CryptoAPI-SHA1 RC4 KDFs, [MS-OFFCRYPTO] Sections 2.3.5-2.3.6),
``ecma376`` (standard 50000-iter and agile spin KDFs + AES verifier/decrypt, Sections 2.3.4.5-2.3.4.15),
``protection`` (ISO write-protection iterated hash, Section 2.4.2.4),
``odf`` (PBKDF2 + Blowfish/AES / Argon2id + AES-GCM, OASIS OpenDocument Part 3 Section 3.4),
``vba`` (VBA project lock codec + SHA-1 verifier, [MS-OVBA] Sections 2.3.1 / 2.4.3-2.4.4),
``pst`` (advisory CRC-32 password + NDB body cipher, [MS-PST] Sections 2.4.3.3 / 5.1-5.3),
``uls`` (Jet User-Level Security 3DES-EDE2 password decode, reversed from msjet40.dll),
``msisam`` (MSISAM MD5/SHA-1 + RC4 page encryption, Microsoft Money 2002+).
"""

from __future__ import annotations
