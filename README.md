<p align="center"><strong><code>office-password-toolkit</code></strong></p>

<p align="center"><em>Detect, extract, bypass, and decrypt every password gate in Microsoft Office and OpenDocument files.</em></p>

<p align="center">
  <a href="https://github.com/StrongWind1/office-password-toolkit/actions/workflows/ci.yml"><img src="https://github.com/StrongWind1/office-password-toolkit/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/office-password-toolkit/"><img src="https://img.shields.io/pypi/v/office-password-toolkit.svg" alt="PyPI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python 3.11+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://strongwind.dev/office-password-toolkit/"><img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Docs"></a>
</p>

<p align="center">
  <a href="https://strongwind.dev/office-password-toolkit/getting-started/installation/">Installation</a> &bull;
  <a href="https://strongwind.dev/office-password-toolkit/getting-started/quick-start/">Quick start</a> &bull;
  <a href="https://strongwind.dev/office-password-toolkit/usage/commands/">Commands</a> &bull;
  <a href="https://strongwind.dev/office-password-toolkit/reference/gates/">Gate catalog</a> &bull;
  <a href="https://strongwind.dev/office-password-toolkit/">Documentation</a>
</p>

---

`office-password-toolkit` (CLI: `opt`) triages, extracts, bypasses, and decrypts passwords and protection across 11 Office products and 80+ file extensions. Point it at a file and it walks the recovery ladder automatically — read a cleartext password, flip a protection flag, strip a record, forge a checksum, open with a built-in default, or decrypt with a key you supply. 62 gates cover every protection type in the Microsoft Office and OpenDocument ecosystems. Only when a gate is genuinely encrypted and no shortcut exists does the tool stop and hand you a hashcat-ready hash line.

## Features

- **3 CLI commands** — `opt info` (hash to stdout, status/scheme to stderr), `opt unlock` (try everything), and `opt advanced` (8 expert subcommands for surgical control)
- **Recovery ladder** — each gate is assigned the cheapest viable action: `DEFAULT` > `READ` > `DECODE` > `BYPASS` > `STRIP` > `COLLIDE` > `CRACK`, applied in order so free wins come first
- **62 gates** — every password, protection, and permission mechanism across 11 products: document-open encryption, modify/edit restrictions, sheet/workbook/range/revisions protection, section locks, VBA project passwords, advisory CRC passwords, keyless body ciphers, and digital signatures
- **Self-describing unified format** — `--format opt` emits four hash families (`$office$`, `$protect$`, `$odf$`, `$vba$`) that encode algorithm, key size, and all parameters in a single parseable line
- **Hashcat integration** — `--format hashcat` (the default) emits hash lines ready for modes 9400, 9500, 9600, 9700, 9800, 25300, 18400, 18600, and 110
- **Built-in decryption** — ECMA-376 standard and agile, RC4+MD5, RC4-CryptoAPI, XOR obfuscation, ODF 1.1 (Blowfish), ODF 1.2 (AES-256), ODF 1.3 (Argon2id + AES-GCM), and MSISAM (Microsoft Money)
- **Default passwords tried automatically** — `VelvetSweatshop` and `/01Hannes Ruescher/01` are attempted before any user-supplied password
- **Input never modified** — every writing command opens the input read-only and produces a new file
- **Python API** — `import office_password_toolkit as opt; opt.detect("file.xlsx")` for programmatic access

## Supported formats

| Product | Legacy | Modern | Gates |
|---|---|---|---|
| Word | `.doc` | `.docx` `.docm` | open (XOR, RC4+MD5, RC4-CryptoAPI, ECMA-376 standard/agile), modify, VBA, signature |
| Excel | `.xls` `.xlsb` | `.xlsx` `.xlsm` | open (XOR, RC4+MD5, RC4-CryptoAPI, ECMA-376 standard/agile), sheet, workbook, range, revisions, modify, VBA, signature |
| PowerPoint | `.ppt` | `.pptx` `.pptm` | open (RC4-CryptoAPI, ECMA-376 standard/agile), modify, VBA, signature |
| Visio | `.vsd` | `.vsdx` | open, VBA |
| Project | `.mpp` | — | open, write-reservation |
| Publisher | `.pub` | — | open, VBA |
| OneNote | — | `.one` | section-open (agile, standard, RC4-CryptoAPI) |
| Outlook | `.pst` `.ost` | — | advisory CRC-32 password, keyless body cipher (Permute/Cyclic) |
| Access | `.mdb` `.mdw` | `.accdb` | database password (Jet 3/4 decode, ACE 2007 RC4-CryptoAPI, ACE 2010+ agile), User-Level Security (ULS) |
| Money | `.mny` | — | MSISAM page encryption (MD5/SHA-1 + RC4) |
| OpenDocument | — | `.odt` `.ods` `.odp` | open (Blowfish 1.1, AES-256 1.2, Argon2id 1.3), sheet/section protection |

hashcat modes emitted: **9400** (Office 2003 standard), **9500** / **9600** (Office 2007-2019 agile), **9700** / **9800** (legacy RC4), **25300** (ISO protection), **18400** / **18600** (ODF), **110** (VBA SHA-1).

## Example

```bash
# triage a file -- gates and hashes to stdout, human-readable status to stderr
opt info budget.xlsx

# try everything: decode, default passwords, decrypt, collide, bypass
opt unlock secret.docx -p 'Passw0rd'

# expert subcommands for surgical control
opt advanced extract secret.docx | hashcat -m 9600 -     # pipe the hash to hashcat
opt advanced extract secret.docx --format opt             # self-describing $office$*sha512*...
opt advanced decode legacy.xls                            # reverse keyless XOR obfuscation
opt advanced collide mailbox.pst                          # mint a CRC-32 collision password
opt advanced bypass budget.xlsx                           # strip all non-encrypting gates
opt advanced decrypt secret.docx -p 'Passw0rd'           # decrypt with a known password
```

## Python API

```python
import office_password_toolkit as opt

# detect container type and encryption status
result = opt.detect("secret.xlsx")
print(result.container, result.encrypted, result.product)

# extract crackable hash lines
hashes = opt.extract_hashes("secret.xlsx")
for h in hashes:
    print(h.value)  # $office$*2013*...

# enumerate gates (protection mechanisms)
handler = opt.handler_for(result.container)
for gate in handler.gates("secret.xlsx"):
    print(gate.display_name, gate.recovery)

# decrypt with a known password
opt.decrypt_file("secret.xlsx", "decrypted.xlsx", password="Passw0rd")

# bypass removable protection (no password needed)
opt.bypass_file("budget.xlsx", "unlocked.xlsx")
```

## Installation

Install from [PyPI](https://pypi.org/project/office-password-toolkit/) (recommended):

```bash
uv tool install office-password-toolkit    # exposes both `opt` and `office-password-toolkit`
```

Or with pip:

```bash
pip install office-password-toolkit
```

Or install from source:

```bash
git clone https://github.com/StrongWind1/office-password-toolkit.git
cd office-password-toolkit
uv sync
```

## Architecture

```
src/office_password_toolkit/
  detect.py / extract.py / decrypt.py / bypass.py    High-level API (detect -> dispatch to handler)
  models.py / constants.py                           Enums, dataclasses, exit codes, magic bytes
  cli/app.py                                         Typer CLI: info, unlock, advanced

  formats/                                           Per-container handlers (OLE, OOXML, ODF, ...)
    base.py                                          FormatHandler ABC
    ole.py / ooxml.py / odf.py / ...                 Container-specific gate enumeration + operations

  crypto/                                            Cryptographic primitives and protocol verifiers
    ciphers.py                                       All cipher operations (sole cryptography import)
    hashes.py                                        All hash/KDF operations (sole argon2-cffi import)
    ecma376.py / rc4legacy.py / odf.py / ...         Format-specific KDFs, verifiers, and decryptors
```

Third-party crypto libraries are imported in exactly two files: `ciphers.py` (for `cryptography`) and `hashes.py` (for `argon2-cffi` and pure-Python MD4/MD2). All other modules access cipher and hash operations through these abstractions, so a library API change touches one file.

## Documentation

Full documentation is available at **[strongwind.dev/office-password-toolkit](https://strongwind.dev/office-password-toolkit/)**, including the complete gate catalog, command reference, and Python API guide.

## License

Apache-2.0. See [LICENSE](LICENSE).
