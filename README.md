<h1 align="center">office-password-toolkit</h1>

<p align="center"><strong>Point it at an Office file. It strips what it can, decrypts what it can, and hands hashcat the rest.</strong></p>

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
  <a href="https://strongwind.dev/office-password-toolkit/research/overview/">Gate catalog</a> &bull;
  <a href="https://strongwind.dev/office-password-toolkit/">Documentation</a>
</p>

---

`office-password-toolkit` (CLI: `opt`) finds every password and protection gate in Microsoft Office and OpenDocument files and gets you past it. Most of those gates encrypt nothing, so it tries the free paths first: read a cleartext password, flip a protection flag, strip a record, forge a checksum, open with a built-in default, or decrypt with a key you supply. Only when a gate is real encryption with no shortcut does it stop and hand you a hashcat-ready hash line.

## Example

```console
$ opt info *.xlsx *.docx *.pst
secret.xlsx        encrypted:agile-sha512  removable:sheets(3) removable:workbook removable:write  removable:macros
book.xls           encrypted:rc4-sha1      removable:sheets(12) removable:write
report.docx        removable:write removable:restricted
payroll.xlsx       encrypted:agile-sha512  removable:sheets(1)
unlocked.docx      open
macro.xlsm         removable:macros
archive.pst        trivial:pst-advisory  info:pst-encoded
irm-doc.docx       blocked:rights-managed
signed.xlsx        info:signed
old.xls            trivial:xor-obfuscation  removable:sheets(5)
```

Each tag is `status:scheme` on stderr; any hash goes to stdout. `opt unlock` clears `removable:` and `trivial:` gates without a password, and `encrypted:` gates get a hash line for hashcat.

## Features

- **Three commands**: `opt info` (hash to stdout, status and scheme to stderr), `opt unlock` (try everything), and `opt advanced` (8 expert subcommands for surgical control).
- **Recovery ladder**: each gate gets the cheapest viable action, `DEFAULT` > `READ` > `DECODE` > `BYPASS` > `STRIP` > `COLLIDE` > `CRACK`, applied in order so free wins come first. The default passwords `VelvetSweatshop` and `/01Hannes Ruescher/01` are tried before any password you supply.
- **62 gates**: every password, protection, and permission mechanism across 11 products, including document-open encryption, modify/edit restrictions, sheet/workbook/range/revisions protection, section locks, VBA project passwords, advisory CRC passwords, keyless body ciphers, and digital signatures.
- **Hashcat integration**: `--format hashcat` emits hash lines ready for modes 9400, 9500, 9600, 9700, 9800, 25300, 18400, 18600, and 110. It is the default for `opt advanced extract`.
- **Self-describing hash lines**: `--format opt` on `opt advanced extract` (and `unified`, the `opt info` default) emits `$office-open$`, `$office-protect$`, `$office-vba$`, and `$odf$` lines that encode the algorithm, key size, and every parameter.
- **Built-in decryption**: ECMA-376 standard and agile, RC4+MD5, RC4-CryptoAPI, XOR obfuscation, ODF 1.1 (Blowfish), ODF 1.2 (AES-256), ODF 1.3 (Argon2id + AES-GCM), and MSISAM (Microsoft Money).
- **Input never modified**: every writing command opens the input read-only and produces a new file.
- **Python API**: the same detection, extraction, decryption, and bypass logic as a library (see [Python API](#python-api)).

## Installation

```sh
uv tool install office-password-toolkit   # recommended
pip install office-password-toolkit       # or with pip
```

From source:

```sh
uv tool install git+https://github.com/StrongWind1/office-password-toolkit
```

Both the `opt` and `office-password-toolkit` commands are installed.

## Quick start

```sh
opt info budget.xlsx                                   # gates to stderr, hash to stdout
opt unlock secret.docx -p 'Passw0rd'                   # decode, defaults, decrypt, collide, bypass
opt advanced extract secret.docx | hashcat -m 9600 -   # pipe the hash to hashcat
opt advanced decode legacy.xls                         # reverse keyless XOR obfuscation
opt advanced collide mailbox.pst                       # mint a CRC-32 collision password
opt advanced bypass budget.xlsx                        # strip all non-encrypting gates
```

Every `advanced` subcommand, flag, and exit code is in the [command reference](https://strongwind.dev/office-password-toolkit/usage/commands/).

## Supported formats

| Product | Legacy | Modern | Gates |
| --- | --- | --- | --- |
| Word | `.doc` | `.docx` `.docm` | open (XOR, RC4+MD5, RC4-CryptoAPI, ECMA-376 standard/agile), modify, VBA, signature |
| Excel | `.xls` `.xlsb` | `.xlsx` `.xlsm` | open (XOR, RC4+MD5, RC4-CryptoAPI, ECMA-376 standard/agile), sheet, workbook, range, revisions, modify, VBA, signature |
| PowerPoint | `.ppt` | `.pptx` `.pptm` | open (RC4-CryptoAPI, ECMA-376 standard/agile), modify, VBA, signature |
| Visio | `.vsd` | `.vsdx` | open, VBA |
| Project | `.mpp` | n/a | open, write-reservation |
| Publisher | `.pub` | n/a | open, VBA |
| OneNote | n/a | `.one` | section-open (agile, standard, RC4-CryptoAPI) |
| Outlook | `.pst` `.ost` | n/a | advisory CRC-32 password, keyless body cipher (Permute/Cyclic) |
| Access | `.mdb` `.mdw` | `.accdb` | database password (Jet 3/4 decode, ACE 2007 RC4-CryptoAPI, ACE 2010+ agile), User-Level Security (ULS) |
| Money | `.mny` | n/a | MSISAM page encryption (MD5/SHA-1 + RC4) |
| OpenDocument | n/a | `.odt` `.ods` `.odp` | open (Blowfish 1.1, AES-256 1.2, Argon2id 1.3), sheet/section protection |

The hashcat side of each scheme is in the [hashcat mode index](https://strongwind.dev/office-password-toolkit/hashcat/current/).

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

## Development

```sh
git clone https://github.com/StrongWind1/office-password-toolkit.git
cd office-password-toolkit
uv sync
make check   # ruff + ty + pytest + mkdocs --strict
```

How the code is laid out: [modular design](https://strongwind.dev/office-password-toolkit/design/modular-design/) and [code mapping](https://strongwind.dev/office-password-toolkit/design/toolkit-architecture/).

## Credits

- [olefile](https://github.com/decalage2/olefile): reads and rewrites the OLE/CFB containers (`.doc`, `.xls`, `.ppt`, and the wrapper around encrypted OOXML).
- [cryptography](https://github.com/pyca/cryptography) and [argon2-cffi](https://github.com/hynek/argon2-cffi): the cipher primitives and the Argon2id KDF for ODF 1.3.
- [Typer](https://github.com/fastapi/typer) and [Rich](https://github.com/Textualize/rich): the CLI and its stderr output.
- Microsoft Open Specifications [`[MS-OFFCRYPTO]`](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-offcrypto/3c34d72a-1a61-4b52-a893-196f9157f083), [`[MS-OVBA]`](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/575462ba-bf67-4190-9fac-c275523c75fc), and [`[MS-PST]`](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-pst/141923d5-15ab-4ef1-a524-6dce75aae546), plus [ECMA-376](https://ecma-international.org/publications-and-standards/standards/ecma-376/) and [OASIS OpenDocument](https://docs.oasis-open.org/office/OpenDocument/v1.3/): the formats and algorithms implemented.
- [hashcat](https://github.com/hashcat/hashcat): the cracker the hash lines are built for.
- John the Ripper's [office2john](https://github.com/openwall/john/blob/bleeding-jumbo/run/office2john.py) and [msoffcrypto-tool](https://github.com/nolze/msoffcrypto-tool): extraction and decryption are cross-checked against them.

## Related tools

- [**ArchiveWolf**](https://github.com/StrongWind1/ArchiveWolf): Encrypted ZIP / RAR / 7-Zip analyser and hashcat hash converter, with key recovery for RAR 1.3 and ZipCrypto

All tools: [strongwind.dev](https://strongwind.dev)

## Disclaimer

office-password-toolkit is for authorized security testing, research, and education. Use it only against systems and data you own or have written permission to test. You are responsible for how you use it.

## License

[Apache License 2.0](LICENSE)
