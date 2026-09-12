# Office 2013 / 2016 / 2019 / 365

Everything the toolkit handles for Office 2013 and later — including 2016, 2019, and Microsoft 365. These releases all share the same encryption defaults (SHA-512 / AES-256 / CBC) and the same CNG infrastructure, so they are treated as one family. The only meaningful change since 2013 is that Microsoft 365 occasionally bumps the default `spinCount` above 100000, which hashcat 9600 rejects.

## Overview

| Detail | Value |
|---|---|
| Versions | Office 2013 (15.0), 2016 (16.0), 2019 (16.0), Microsoft 365 |
| Years | 2013 – present |
| Container | OOXML/ZIP (.docx/.xlsx/.pptx), encrypted files re-wrapped as OLE/CFB |
| Encryption spec | [MS-OFFCRYPTO] Sections 2.3.4.10 – 2.3.4.15 (ECMA-376 Agile) |
| Key infrastructure | CNG (same tunability as 2010) |
| Default open encryption | SHA-512 / AES-256 / CBC, spinCount 100000 |

## File types produced

Same as Office 2007/2010 — `.docx`, `.xlsx`, `.pptx`, `.xlsb`, macro-enabled variants, and templates. Encrypted files are physically OLE/CFB on disk.

## Document-open encryption

### ECMA-376 Agile — 2013+ defaults ([MS-OFFCRYPTO] Sections 2.3.4.10 – 2.3.4.15)

The agile XML descriptor is identical in structure to Office 2010; only the default parameter values changed.

**Default tuple (Office 2013+):**

| Parameter | Value |
|---|---|
| `hashAlgorithm` | SHA-512 |
| `cipherAlgorithm` | AES |
| `cipherChaining` | ChainingModeCBC |
| `keyBits` | 256 |
| `spinCount` | 100000 |
| `saltSize` | 16 |

- **KDF**: same agile spin-loop as 2010 but with SHA-512 (64-byte digest) and a 256-bit AES key
- **hashcat**: `9600` (`$office$*2013*...`) — accepts ONLY SHA-512/AES-256/spin 100000. Any other spinCount is rejected.
- **Toolkit `--format opt`**: `$office$*sha512*aes256*cbc*100000*<salt>*<encverifier>*<encverifierhash>`

### Non-default agile tuples

The same CNG registry tunability as Office 2010 applies. Any combination of the 7 producible hashes × 10 cipher configs is legal. hashcat covers only the SHA-512/AES-256 default; every other tuple routes to the `$office$` unified line via `--format opt`.

### OneNote sections

OneNote 2013+ password-protects sections using the same agile `EncryptionInfo` blob framed inside the [MS-ONESTORE] revision store. The default is SHA-512/AES-256 (hashcat 9600), but older OneNote versions may use SHA-1/AES-128 (9500), Standard AES-ECB (9400), or even RC4-CryptoAPI (9800).

### Access .accdb 2010+

Access 2010 and later reuse the agile SHA-512/AES-256 scheme for database-open encryption, with a per-page AES-CBC deviation for the body. The hash extraction is identical to 9600; decryption uses the Access-specific block-key derivation (UNCONFIRMED, per Jackcess).

## Protection gates

Office 2013 changed the default ISO protection hash from **SHA-1 to SHA-512**, making it the first version whose default protection verifier has a hashcat mode (25300). Earlier versions' SHA-1 protection is still accepted but not the default.

| Gate | Where | Recovery | Verifier | Note |
|---|---|---|---|---|
| Sheet protection | `xl/worksheets/sheetN.xml` `<sheetProtection>` | `STRIP` | ISO SHA-512 (default) | hashcat 25300 |
| Workbook protection | `xl/workbook.xml` `<workbookProtection>` | `STRIP` | ISO SHA-512 | hashcat 25300 |
| Shared revisions | `xl/workbook.xml` `<workbookProtection revisions*>` | `STRIP` | ISO SHA-512 | hashcat 25300 |
| Write-reservation (modify) | `xl/workbook.xml` `<fileSharing>` | `STRIP` | ISO SHA-512 | hashcat 25300 |
| Allow-edit-ranges | `xl/worksheets/sheetN.xml` `<protectedRange>` | `STRIP` | ISO SHA-512 | hashcat 25300 |
| Restrict editing | `word/settings.xml` `<w:documentProtection>` | `STRIP` | ISO SHA-512 | hashcat 25300 |
| Modify (Word) | `word/settings.xml` `<w:writeProtection>` | `STRIP` | ISO SHA-512 | hashcat 25300 |
| Modify (PowerPoint) | `ppt/presentation.xml` `<p:modifyVerifier>` | `STRIP` | ISO SHA-512 | hashcat 25300 |
| VBA project lock | `vbaProject.bin` `PROJECT` stream `DPB` | `STRIP` / `CRACK` | SHA-1 or cleartext | hashcat 110 |
| Digital signature | `_xmlsignatures/` parts | `NONE` | public-key | Not password-recoverable |
| IRM / Rights Management | `\EncryptionInfo` vMinor=3 | `NONE` | off-file (cert/RMS) | Not password-recoverable |

### .xlsb binary protection

Excel Binary Workbook (`.xlsb`) files carry protection in BIFF12 binary records (`BrtSheetProtectionIso`, `BrtBookProtectionIso`, `BrtRangeProtectionIso`, etc.) instead of XML attributes. The toolkit parses these via a BIFF12 record walk and extracts the same `IsoPasswordData` body. The hashcat mode and recovery are identical to the XML path.

## Recovery summary

| Gate | Recovery | hashcat mode | Toolkit command |
|---|---|---|---|
| Open (Agile SHA-512/AES-256, default) | `CRACK` | 9600 | `opt advanced extract` / `opt advanced decrypt` |
| Open (non-default agile tuple) | `CRACK` | — | `opt advanced extract --format opt` |
| Open (OneNote agile) | `CRACK` | 9600 (default) / 9500 / 9400 / 9800 | `opt advanced extract` |
| Open (Access .accdb 2010+) | `CRACK` | 9600 | `opt advanced extract` / `opt advanced decrypt` |
| Sheet / Workbook / Modify / Range / Revisions (ISO SHA-512) | `STRIP` | 25300 | `opt advanced bypass` / `opt advanced extract` |
| Restrict editing (ISO SHA-512) | `STRIP` | 25300 | `opt advanced bypass` / `opt advanced extract` |
| VBA project lock | `STRIP` | 110 | `opt advanced bypass` / `opt advanced extract` |
| Digital signature | `NONE` | — | `opt advanced bypass --remove-signatures` |
| IRM / Rights Management | `NONE` | — | not recoverable |

## Extraction examples

```bash
# Agile SHA-512/AES-256 default (hashcat format)
$ opt info encrypted-2013.docx
$office$*2013*100000*256*16*67805436882475302087847656644837*0c392d3b9ca88965...

# Agile SHA-512/AES-256 default (self-describing)
$ opt info encrypted-2013.docx --format opt
$office$*sha512*aes256*cbc*100000*67805436882475302087847656644837*0c392d3b9ca88965...

# ISO SHA-512 sheet protection (hashcat format)
$ opt info protected-2016.xlsx
$office$2016$0$100000$f3be8c2e8293ab8dbefc32e9e35e6265$4cd0efa6f632be54...

# ISO SHA-512 sheet protection (self-describing)
$ opt info protected-2016.xlsx --format opt
$protect$*sha512*iso*100000*f3be8c2e8293ab8dbefc32e9e35e6265*4cd0efa6f632be54...

# OneNote section
$ opt info encrypted-section.one
$office$*2013*100000*256*16*<salt>*<encverifier>*<encverifierhash>
```

## hashcat modes

| Mode | Name | What it cracks | Constraint |
|---|---|---|---|
| `9600` | MS Office 2013 | Agile SHA-512 / AES-256 | spinCount MUST be 100000 |
| `9500` | MS Office 2010 | Agile SHA-1 / AES-128 (OneNote 2010 sections) | spinCount MUST be 100000 |
| `25300` | MS Office 2016 SheetProtection | ISO SHA-512 protection (2013+ default) | spin=100000, salt=16B, SHA-512 only |
| `110` | sha1($pass.$salt) | VBA project SHA-1 verifier | — |
