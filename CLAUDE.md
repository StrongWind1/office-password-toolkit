# CLAUDE.md

Project-level instructions for working in this repository.

## What this project does

`office-password-toolkit` (CLI: `opt`) detects, extracts, bypasses, and decrypts password protection across 11 Microsoft Office products and OpenDocument formats. It walks a recovery ladder — cheapest action first (read a cleartext password, flip a flag, strip a record, forge a checksum, try a built-in default, decrypt with a known key) — and only hands off to hashcat when a gate is genuinely encrypted with no shortcut.

## Architecture

```
src/office_password_toolkit/
  __init__.py          Public API: detect, extract_hashes, bypass_file, decrypt_file, models
  models.py            Enums (ContainerKind, Product, GateType, RecoveryClass, HashScheme, Status)
                       and dataclasses (Gate, ExtractedHash, DetectResult)
  constants.py         Exit codes, magic bytes, default passwords
  detect.py            Container classification (magic bytes) and product detection (OLE streams / OPC content types)
  extract.py           detect() + handler.extract() — returns crackable hash lines
  decrypt.py           detect() + handler.decrypt() — writes plaintext copy
  bypass.py            detect() + handler.bypass() — writes copy with protection stripped

  cli/
    app.py             Typer CLI: info, unlock, advanced (8 subcommands)

  formats/
    base.py            FormatHandler ABC + HandlerNotImplementedError
    __init__.py         Handler registry: ContainerKind -> FormatHandler dispatch
    ole.py             OLE/CFB: legacy .doc/.xls/.ppt + encrypted-OOXML wrapper
    ooxml.py           OOXML/OPC: unencrypted .docx/.xlsx/.pptx/.xlsb
    odf.py             OpenDocument: .odt/.ods/.odp
    access.py          Access: .mdb/.accdb (Jet 3/4, ACE 2007/2010+)
    mdw.py             Access workgroup: .mdw/.mda (User-Level Security)
    onenote.py         OneNote: .one/.onetoc2
    outlook.py         Outlook: .pst/.ost

  crypto/
    ciphers.py         ALL cipher operations (sole cryptography import point)
    hashes.py          ALL hash/KDF operations (sole argon2-cffi import point, pure-Python MD4/MD2)
    ecma376.py         ECMA-376 standard/agile encryption (hashcat 9400/9500/9600)
    rc4legacy.py       Legacy RC4+MD5 / RC4-CryptoAPI+SHA-1 (hashcat 9700/9800)
    protection.py      ISO write/sheet/workbook protection verifier (hashcat 25300)
    odf.py             ODF manifest parse + Blowfish/AES-CBC/AES-GCM verify/decrypt (hashcat 18400/18600)
    xor.py             Legacy XOR obfuscation primitives
    vba.py             VBA project lock codec + SHA-1 verifier (hashcat 110)
    pst.py             PST CRC-32 password + NDB body ciphers (Permute/Cyclic)
    mpp.py             Microsoft Project Props-based XOR password decode
    msisam.py          MSISAM MD5/SHA-1 + RC4 page encryption (Microsoft Money)
    uls.py             Jet User-Level Security 3DES password decode + MDW parsing
```

## Key design rules

- **Third-party crypto isolation.** `cryptography` is imported only in `crypto/ciphers.py`. `argon2-cffi` is imported only in `crypto/hashes.py`. `hashlib` is imported only in `crypto/hashes.py` and the availability probe in `crypto/ecma376.py`. Protocol modules never import a crypto library directly — if a library changes an import path, only one file changes.
- **Input never modified.** Every writing command opens the input read-only and produces a new file. Output path is refused when it equals input (by real path), and existing output is refused without `--force`.
- **Recovery ladder ordering.** Gates are assigned the cheapest viable action: DEFAULT > READ > DECODE > BYPASS > STRIP > COLLIDE > DECRYPT > KEYSPACE > CRACK. The `unlock` command walks this automatically.
- **Spec compliance.** Every wire value, flag, and constant must be traceable to a spec section (e.g. `[MS-OFFCRYPTO] Section 2.3.4.7`) or documented as a deviation. Custom crypto implementations are verified against their RFCs (MD4/RFC 1320, MD2/RFC 1319, RC4/RFC 6229, CRC-32/RFC 1952, DESX/draft-ietf-ipsec-ciph-desx-00).

## Running checks

```bash
uv run ruff check src/             # lint (select = ALL, strictest)
uv run ruff format --check src/    # format check
uv run ty check                    # type check (all = error, error-on-warning)
uv run pytest                      # 752 tests
```

All four must pass before committing. The project has zero `noqa` directives, zero `type: ignore` comments, and zero inline suppressions.

## Ruff configuration

`select = ["ALL"]` with only 4 global ignores (formatter conflicts + docstring style conflicts). Per-file suppressions exist for:
- `tests/**` — exempt from linting entirely (still formatted)
- `constants.py` — S105 (spec-documented default passwords, not secrets)
- `cli/app.py` — PLR0913/BLE001/C901/PLR0912 (Typer param counts, broad Exception in verify, inherent command complexity)
- `formats/access.py` — PLR0911/PLR0912/C901 (gate enumeration complexity)
- `crypto/ciphers.py` — S305 (ECB mode required by format specs)
- `crypto/hashes.py` — PLR0913 (Argon2 spec has 6 parameters)

## Ty configuration

Maximum strictness: `all = "error"`, `error-on-warning = true`, `respect-type-ignore-comments = false`. Only escape: `replace-imports-with-any = ["olefile.**"]` (olefile ships no type stubs).

## Dependencies

Runtime: `typer`, `rich`, `olefile`, `cryptography`, `typing-extensions`, `argon2-cffi`. No `pycryptodome` — dropped in favour of `cryptography`'s TripleDES which accepts 16-byte (2-key) keys directly.

Dev: `pytest`, `pytest-cov`, `ruff`, `ty`, `pre-commit`.

## Commit style

Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `ci:`, `chore:`. Imperative mood. No AI attribution.
