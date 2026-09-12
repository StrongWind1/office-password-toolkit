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
- **Built-in decryption** — ECMA-376 standard and agile, RC4+MD5, RC4-CryptoAPI, XOR obfuscation, ODF 1.1 (Blowfish), ODF 1.2 (AES-256), and ODF 1.3 (Argon2id)
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
| Project | `.mpp` | — | open |
| Publisher | `.pub` | — | open, VBA |
| OneNote | — | `.one` | section-open (agile) |
| Outlook | `.pst` `.ost` | — | advisory CRC-32 password, keyless body cipher |
| Access | `.mdb` | `.accdb` | database password (Jet decode, ACE agile) |
| OpenDocument | — | `.odt` `.ods` `.odp` | open (Blowfish 1.1, AES-256 1.2, Argon2id 1.3), sheet/section protection |
| LibreOffice Calc | — | `.ods` | sheet protection (SHA-1, SHA-256, SHA-512) |

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

## Quick start

```bash
# 1. What protection does this file carry?
opt info quarterly_report.xlsx

# 2. Unlock everything automatically (decrypt + bypass + collide)
opt unlock quarterly_report.xlsx -p 'Passw0rd'

# 3. Extract a hash and crack it offline
opt info quarterly_report.xlsx 2>/dev/null | hashcat -m 9600 -

# 4. Strip all non-encrypting protection from a workbook
opt advanced bypass quarterly_report.xlsx -o unlocked.xlsx
```

## Documentation

Full documentation is available at **[strongwind.dev/office-password-toolkit](https://strongwind.dev/office-password-toolkit/)**, including the complete gate catalog, command reference, and Python API guide.

## License

Apache-2.0. See [LICENSE](LICENSE).
