# Office 2010

Everything the toolkit handles for Office 2010. This is the first release to use the ECMA-376 Agile encryption scheme and the CNG (Cryptography Next Generation) key infrastructure, which means the cipher, hash, and key size are no longer fixed — they are named in an XML descriptor and configurable via registry. Office 2010's defaults are SHA-1 / AES-128 / CBC / spinCount 100000.

## Overview

| Detail | Value |
|---|---|
| Version | Office 2010 (14.0) |
| Years | 2010 – 2013 |
| Container | OOXML/ZIP (.docx/.xlsx/.pptx), encrypted files re-wrapped as OLE/CFB |
| Encryption spec | [MS-OFFCRYPTO] Sections 2.3.4.10 – 2.3.4.15 (ECMA-376 Agile) |
| Key infrastructure | CNG (Cryptography Next Generation) — user-configurable via registry |
| Default open encryption | SHA-1 / AES-128 / CBC, spinCount 100000 |

## File types produced

Same as Office 2007 — `.docx`, `.xlsx`, `.pptx`, `.xlsb`, macro-enabled variants (`.docm`, `.xlsm`, `.pptm`), and templates. Encrypted files are physically OLE/CFB on disk.

## Document-open encryption

### ECMA-376 Agile ([MS-OFFCRYPTO] Sections 2.3.4.10 – 2.3.4.15)

The `\EncryptionInfo` stream is an XML descriptor (`<encryption>`) that names every parameter: `hashAlgorithm`, `cipherAlgorithm`, `cipherChaining`, `keyBits`, `blockSize`, `saltSize`, `hashSize`, and `spinCount`. This makes the scheme fully extensible — any combination of CNG-available primitives is legal.

**Default tuple (Office 2010):**

| Parameter | Value |
|---|---|
| `hashAlgorithm` | SHA-1 |
| `cipherAlgorithm` | AES |
| `cipherChaining` | ChainingModeCBC |
| `keyBits` | 128 |
| `spinCount` | 100000 |
| `saltSize` | 16 |

- **KDF**: `H0 = H(salt || UTF16LE(password))` → spin N rounds (`Hn = H(LE32(i) || Hn-1)`, iterator **prepended**) → `Hfinal = H(Hspin || blockKey)` → key = first `keyBits/8` bytes
- **hashcat**: `9500` (`$office$*2010*...`) — accepts ONLY the exact default tuple (SHA-1/AES-128/spin 100000)
- **Toolkit `--format opt`**: `$office$*sha1*aes128*cbc*100000*<salt>*<encverifier>*<encverifierhash>`

### Non-default agile tuples (registry-configured)

The CNG infrastructure on Windows 7+ exposes a much wider set of primitives. Changing the registry keys under `HKCU\Software\Microsoft\Office\14.0\<app>\Security\Crypto` allows any combination of:

**Available CNG ciphers:** AES (128/192/256), 3DES (192), 3DES_112 (128), DES (64), DESX (192), RC2 (40-128), RC4 (40-512)

**Available CNG hashes:** SHA-1, SHA-256, SHA-384, SHA-512, MD5, MD4, MD2

**Not available on any Windows (spec-legal but platform-impossible):** RIPEMD-128, RIPEMD-160, WHIRLPOOL

This produces 70 producible cipher × hash combinations, of which hashcat covers exactly **one** (SHA-1/AES-128, mode 9500). The toolkit extracts all 70 as the unified `$office$` line via `--format opt`, and falls back to the `$office-agile$` generalized line under `--format hashcat`.

## Protection gates

Office 2010 uses the same ISO write-protection verifier as Office 2007, but the default protection hash is still **SHA-1** (not SHA-512 — that default changes in Office 2013). This means the most common Office 2010 protection hash has no hashcat 25300 mode.

| Gate | Where | Recovery | Verifier | Note |
|---|---|---|---|---|
| Sheet protection | `xl/worksheets/sheetN.xml` `<sheetProtection>` | `STRIP` | ISO SHA-1 (default) | 25300 rejects SHA-1 |
| Workbook protection | `xl/workbook.xml` `<workbookProtection>` | `STRIP` | ISO SHA-1 | |
| Shared revisions | `xl/workbook.xml` `<workbookProtection revisions*>` | `STRIP` | ISO SHA-1 | |
| Write-reservation (modify) | `xl/workbook.xml` `<fileSharing>` | `STRIP` | ISO SHA-1 | |
| Allow-edit-ranges | `xl/worksheets/sheetN.xml` `<protectedRange>` | `STRIP` | ISO SHA-1 | |
| Restrict editing | `word/settings.xml` `<w:documentProtection>` | `STRIP` | ISO SHA-1 or Word 2007 crypt* | |
| Modify (Word) | `word/settings.xml` `<w:writeProtection>` | `STRIP` | ISO SHA-1 or crypt* | |
| Modify (PowerPoint) | `ppt/presentation.xml` `<p:modifyVerifier>` | `STRIP` | ISO SHA-1 | |
| VBA project lock | `vbaProject.bin` `PROJECT` stream `DPB` | `STRIP` / `CRACK` | SHA-1 or cleartext | hashcat 110 |
| Digital signature | `_xmlsignatures/` parts | `NONE` | public-key | Not password-recoverable |

## Recovery summary

| Gate | Recovery | hashcat mode | Toolkit command |
|---|---|---|---|
| Open (Agile SHA-1/AES-128, default) | `CRACK` | 9500 | `opt advanced extract` / `opt advanced decrypt` |
| Open (non-default agile tuple) | `CRACK` | — | `opt advanced extract --format opt` |
| Sheet / Workbook / Modify / Range / Revisions (ISO SHA-1) | `STRIP` | — (25300 rejects SHA-1) | `opt advanced bypass` / `opt advanced extract --format opt` |
| Restrict editing (Word 2007 crypt*) | `STRIP` | — | `opt advanced bypass` |
| VBA project lock | `STRIP` | 110 | `opt advanced bypass` / `opt advanced extract` |
| Digital signature | `NONE` | — | `opt advanced bypass --remove-signatures` |

## Extraction examples

```bash
# Agile SHA-1/AES-128 default (hashcat format)
$ opt info encrypted-2010.xlsx
$office$*2010*100000*128*16*a1b2c3d4e5f6071829384a5b6c7d8e9f*0f1e2d3c4b5a6978...

# Agile SHA-1/AES-128 default (self-describing)
$ opt info encrypted-2010.xlsx --format opt
$office$*sha1*aes128*cbc*100000*a1b2c3d4e5f6071829384a5b6c7d8e9f*0f1e2d3c4b5a6978...

# Non-default agile tuple (e.g. SHA-256/AES-256 via registry) — no hashcat mode
$ opt info encrypted-sha256-aes256-2010.docx --format opt
$office$*sha256*aes256*cbc*100000*<salt>*<encverifier>*<encverifierhash>
```

## hashcat modes

| Mode | Name | What it cracks | Constraint |
|---|---|---|---|
| `9500` | MS Office 2010 | Agile SHA-1 / AES-128 | spinCount MUST be 100000; keySize MUST be 128 |
| `25300` | MS Office 2016 SheetProtection | ISO SHA-512 protection only | NOT the SHA-1 default for 2010 |
| `110` | sha1($pass.$salt) | VBA project SHA-1 verifier | — |
