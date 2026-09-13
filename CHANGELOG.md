# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

**3-command CLI restructure:**

- `opt info` — read-only triage with hash extraction: hash lines to stdout, `status:scheme` summary to stderr (`encrypted:agile-sha512`, `removable:sheets(3)`, `trivial:xor-obfuscation`, etc.)
- `opt unlock` — try everything: info -> decode -> decrypt -> collide -> bypass -> info, zero-config recovery pipeline
- `opt advanced` — 8 expert subcommands for individual operations (`extract`, `decode`, `collide`, `bypass`, `decrypt`, and others)

**Product detection:**

- Detects Word, Excel, PowerPoint, OneNote, Outlook, Access, Visio, Project, and Publisher from internal OLE/OOXML streams
- Extension fallback for encrypted OOXML files where stream inspection fails
- `detect_product()` exported in the public API

**Multi-file and directory input:**

- `opt info *.xlsx folder/ file1.docx` — glob, directory walk, and multi-path in a single invocation

**Output modes:**

- `--debug` — detailed container/gate/scheme analysis on stderr
- `--json` — structured output for programmatic consumption
- Clean ASCII output when piped (Rich auto-detects TTY, no ANSI escape sequences in non-interactive use)

**ODF 1.3 decryption:**

- Argon2id + AES-256-GCM decryption support via `argon2-cffi`

**Crypto abstraction layer:**

- `crypto/ciphers.py` — centralised cipher module; all `cryptography` library imports confined to this single file. Provides RC4 (pure-Python, RFC 6229-verified), AES-CBC/ECB/GCM, Blowfish-CFB, 3DES-CBC/ECB, RC2-CBC, DESX-CBC (per draft-ietf-ipsec-ciph-desx-00), and string-based agile dispatchers.
- `crypto/hashes.py` — centralised hash/KDF module; all `argon2-cffi` imports confined here. Pure-Python MD4 (RFC 1320) and MD2 (RFC 1319), unified `digest()`/`new()` dispatch over hashlib + legacy hashes, PBKDF2-HMAC-SHA1, Argon2id, and `compare_digest`.
- Protocol modules (`ecma376`, `odf`, `rc4legacy`, `protection`, etc.) import from `ciphers`/`hashes` instead of reaching into third-party libraries directly.

**Public API exports:**

- `FormatHandler`, `HandlerNotImplementedError`, and `detect_product` now exported from the top-level package

### Changed

- CLI restructured from 7 top-level commands to 3: `info` absorbs `extract` (hash lines go to stdout automatically), `advanced` absorbs `decode`, `collide`, `bypass`, `decrypt`
- Dropped `pycryptodome` dependency — sole usage (2-key 3DES-ECB in ULS password decode) replaced by `cryptography`'s TripleDES, which accepts 16-byte keys directly with identical output
- Four independent RC4 implementations (`rc4legacy`, `msisam`, `uls`, `formats/access`) consolidated into one canonical pure-Python implementation in `ciphers.py`
- All `hashlib` calls in production code routed through `hashes.digest()` or `hashes.new()` — `hashlib` now imported only in `hashes.py` and the algorithm-availability probe in `ecma376.py`
- AES-ECB implementation switched from CBC(IV=0)+XOR workaround to direct ECB mode (the workaround avoided a ruff S305 warning that is now suppressed in the centralised cipher module)
- Per-file ruff ignores in `pyproject.toml` audited and reduced from 8 entries to 6 — stale suppressions for `ecma376.py` removed after cipher code moved to `ciphers.py`
- `pytest` treats `DeprecationWarning` as error

### Fixed

- `_SCHEME_TO_TAG` missing `HashScheme.MSISAM` entry — MSISAM files rendered as `encrypted:open` instead of `encrypted:msisam` in CLI output
- Operator precedence in `unified_odf_line` — `or` / ternary grouped correctly by accident but was fragile; explicit parentheses added
- `_resolve_hash` return type narrowed to `_LegacyHashWrapper` but `hashes.new()` returns `hashlib._Hash` for standard algorithms — widened to correct union type
- Type errors in `uls.py` (`bytearray` passed where `bytes` typed) and `ooxml.py` (redundant `None` check on `unified_protect_line_from_sid`)
- `TypeError` used instead of `ValueError` for `isinstance` guard in ACE 2007 verifier (TRY004)
- `__main__.py` missing `__name__` guard
- Exception class in `extract`/`decrypt`/`bypass` docstrings referenced `NotImplementedError` instead of `HandlerNotImplementedError`
- Dead code removed: `_UNSUPPORTED_ALGORITHMS` (protection.py), `_block_size_for` (ecma376.py), unreachable `len(blob)==0` guard (access.py), `_AES_BLOCK` constant (ciphers.py)
- `Final` type annotations added to 7 constants in `formats/odf.py`
- Missing comments and docstrings added across 5 crypto modules (~30 constants + 5 functions)
- Duplicate comment block in `pyproject.toml` ruff per-file-ignores
- ANSI escape sequences leaked into piped output (Rich now detects TTY before emitting control codes)
- TripleDES deprecation warnings from `cryptography` library on short keys

## [0.1.0] - 2026-07-02

Initial release. `opt` triages a file, extracts crackable hashes, bypasses free gates, and decrypts document-open encryption with a known or default password — handing the GPU work to hashcat.

### Added

**5 CLI commands:**

- `opt info` — read-only triage: per-gate breakdown to stderr, machine-readable summary to stdout with plain-English name, cheapest recovery action, hashcat mode, and byte location
- `opt extract` — emit one hash line per crackable gate
- `opt bypass` — strip or clear every non-encrypting gate into a new file (sheet/workbook/document/write/range/revisions protection, VBA project lock, PST advisory password, ODF body protection, legacy `.xls` protection and file-sharing records)
- `opt decrypt` — write a plaintext copy using a known or default password
- `opt unlock` — the four wired together: info -> decrypt/extract -> bypass -> info

**Container detection:**

- Magic-byte detection for OLE/CFB, OOXML/ZIP, OpenDocument, OneNote, Outlook PST, and Access — format and type resolved by content, not extension
- Modern OOXML packages carrying a document-open password recognised by OLE `EncryptionInfo` re-wrap rather than by being a ZIP

**13 hashcat-compatible hash formats:**

- ECMA-376 standard: `9400` (SHA-1 x50000 + AES-ECB)
- ECMA-376 agile: `9500` (SHA-1 spin + AES-CBC), `9600` (SHA-512 spin + AES-CBC)
- Legacy RC4: `9700`/`9800` (RC4+MD5 / RC4-CryptoAPI+SHA-1), with `9710`/`9720`/`9810`/`9820` colliders
- ODF: `18400` (1.2 PBKDF2 + AES-256-CBC), `18600` (1.1 Blowfish-CFB)
- OneNote: emitted as `9600`
- ISO protection: `25300` (SHA-512, spinCount 100000, 16-byte salt)
- VBA project: `110` (SHA-1 verifier)

**Decryption:**

- ECMA-376 standard (SHA-1 x50000 + AES-ECB), ECMA-376 agile (SHA-1/SHA-512 spin + AES-CBC), legacy RC4 (RC4+MD5 and RC4-CryptoAPI+SHA-1), ODF (Blowfish-CFB 1.1, PBKDF2 + AES-256-CBC 1.2)
- Default passwords tried silently: empty string, `VelvetSweatshop` (Excel), `/01Hannes Ruescher/01` (PowerPoint), per `[MS-OFFCRYPTO]` section 2.4.2.3

**Legacy scramble recovery:**

- XOR-obfuscation decode and 16/32-bit verifier collision for `.doc`/`.xls` open scramble — content recovered with no password and no crack

**Safety invariant:**

- Every writing command opens input read-only and produces a new file: output path refused when it equals input (by real path), existing output refused without `--force`, write is an atomic rename from a temp file
- Exit codes: `0` success, `1` error, `2` unsupported gate/scheme, `3` no gate, `4` crack required, `5` unrecoverable (signature/IRM), `6` refused for safety

**Dependencies:**

- `typer`, `rich`, `olefile`, `cryptography` (AES/Blowfish/3DES/RC2/hashes/PBKDF2), `typing-extensions` (`@override` backport for 3.11 floor), `argon2-cffi` (ODF 1.3 Argon2id KDF)

### Known limitations

- ODF 1.3 (Argon2id + AES-256-GCM) detected but no hashcat mode — extraction reports a gap rather than emitting an unusable line
- Mode `25300` ingests only the modern Office default shape (SHA-512, spinCount 100000, 16-byte salt); other primitives, spin counts, or salt lengths are gaps; `bypass` is still the fast path since the body is unencrypted
- Non-default agile tuples (SHA-256/SHA-384, AES-192/3DES/RC2, non-100000 spin) and SHA-1/SHA-256 forms of the ISO protection hash are recognised but have no single hashcat profile
- Access (`.mdb`/`.accdb`), Microsoft Project (`.mpp`), and Office 95 and earlier are outside the spec corpus — handling is community reverse-engineering and marked UNCONFIRMED; the ACE `.accdb` agile-reuse mapping to mode `9600` is unverified
- Digital signatures and IRM/RMS (including Outlook EDP/WIP variant) carry no in-file password secret and are not password-recoverable; reported as such with exit `5`

[0.1.0]: https://github.com/StrongWind1/office-password-toolkit/releases/tag/v0.1.0
