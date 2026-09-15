# office-password-toolkit

**Detect, extract, bypass, and decrypt every password gate in Microsoft Office and OpenDocument files.**

---

`office-password-toolkit` (CLI: **`opt`**) triages, extracts, bypasses, and decrypts passwords and protection across 11 Office products and 80+ file extensions. Point it at a file and it walks the recovery ladder automatically — read a cleartext password, flip a protection flag, strip a record, forge a checksum, open with a built-in default, or decrypt with a key you supply. Only when a gate is genuinely encrypted and no shortcut exists does the tool stop and hand you a hashcat-ready hash line.

!!! tip "The core insight"
    Most Office "passwords" are not real encryption. Only the *document-open* password on a genuine scheme (plus OneNote, ODF-open, ACE, and enterprise IRM) actually encrypts content. Every other gate leaves the content in plain sight and is defeated for free: read a cleartext password, flip a flag, delete a record, forge a 16/32-bit checksum, or open with a built-in default like `VelvetSweatshop`. The tool always tries the free path first and only emits a hash when cracking is unavoidable.

## Features

- **3 CLI commands** — `opt info` (hash to stdout, status/scheme to stderr), `opt unlock` (try everything), and `opt advanced` (8 expert subcommands for surgical control)
- **Recovery ladder** — each gate is assigned the cheapest viable action: `DEFAULT` > `READ` > `DECODE` > `BYPASS` > `STRIP` > `COLLIDE` > `CRACK`, applied in order so free wins come first
- **62 gates** — every password, protection, and permission mechanism across 11 products
- **Self-describing unified format** — `--format unified` emits five hash families (`$office-open$`, `$office-protect$`, `$office-vba$`, `$office-msisam$`, `$odf$`) encoding algorithm, key size, and all parameters
- **Hashcat integration** — `--format hashcat` (the default) emits lines ready for modes 9400, 9500, 9600, 9700, 9800, 25300, 18400, 18600, and 110
- **Built-in decryption** — ECMA-376 standard/agile, RC4+MD5, RC4-CryptoAPI, XOR obfuscation, ODF 1.1/1.2/1.3
- **Default passwords tried automatically** — `VelvetSweatshop` and `/01Hannes Ruescher/01` before any user-supplied password
- **Input never modified** — every writing command opens input read-only and produces a new file
- **Python API** — `import office_password_toolkit as opt; opt.detect("file.xlsx")`

## Supported formats

| Product | Legacy | Modern | Gates |
|---|---|---|---|
| **Word** | `.doc` | `.docx` `.docm` | open (XOR, RC4+MD5, RC4-CryptoAPI, ECMA-376), modify, VBA, signature |
| **Excel** | `.xls` `.xlsb` | `.xlsx` `.xlsm` | open (XOR, RC4+MD5, RC4-CryptoAPI, ECMA-376), sheet, workbook, range, revisions, modify, VBA, signature |
| **PowerPoint** | `.ppt` | `.pptx` `.pptm` | open (RC4-CryptoAPI, ECMA-376), modify, VBA, signature |
| **Visio** | `.vsd` | `.vsdx` | open, VBA |
| **Project** | `.mpp` | — | open, VBA |
| **Publisher** | `.pub` | — | VBA |
| **OneNote** | — | `.one` | section-open (agile) |
| **Outlook** | `.pst` `.ost` | — | advisory CRC-32, keyless body cipher |
| **Access** | `.mdb` | `.accdb` | database password (Jet decode, ACE agile) |
| **OpenDocument** | — | `.odt` `.ods` `.odp` | open (Blowfish 1.1, AES-256 1.2, Argon2id 1.3), sheet/section protection |
| **LibreOffice** | — | `.ods` | sheet protection (SHA-1, SHA-256, SHA-512) |

## Quick example

=== "Triage"

    ```bash
    # What protection does this file carry?
    opt info budget.xlsx
    ```

=== "Unlock"

    ```bash
    # Try everything: decode, default passwords, decrypt, collide, bypass
    opt unlock secret.docx -p 'Passw0rd'
    ```

=== "Advanced"

    ```bash
    # Extract a hash and pipe it to hashcat
    opt advanced extract secret.docx | hashcat -m 9600 - wordlist.txt

    # Self-describing format
    opt advanced extract secret.docx --format opt

    # Reverse XOR obfuscation (no password needed)
    opt advanced decode legacy.xls

    # Mint a CRC-32 collision password (instant)
    opt advanced collide mailbox.pst

    # Strip all non-encrypting gates
    opt advanced bypass budget.xlsx

    # Decrypt with a known password
    opt advanced decrypt secret.docx -p 'Passw0rd'
    ```

## Installation

=== "uv (recommended)"

    ```bash
    uv tool install office-password-toolkit
    ```

=== "pip"

    ```bash
    pip install office-password-toolkit
    ```

=== "From source"

    ```bash
    git clone https://github.com/StrongWind1/office-password-toolkit.git
    cd office-password-toolkit
    uv sync
    ```

Both `opt` and `office-password-toolkit` are available as CLI entry points after installation.

## Documentation

<div class="grid cards" markdown>

-   :material-rocket-launch: **Getting started**

    ---

    Install the tool and run your first triage in under a minute.

    [:octicons-arrow-right-24: Installation](getting-started/installation.md) &nbsp; [:octicons-arrow-right-24: Quick start](getting-started/quick-start.md)

-   :material-console: **Commands**

    ---

    Full reference for all three commands, flags, and exit codes.

    [:octicons-arrow-right-24: Command reference](usage/commands.md)


</div>
