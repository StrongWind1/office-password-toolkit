# Office 2007

Everything the toolkit handles for Office 2007 — the first release to use the OOXML/ZIP container and the ECMA-376 Standard encryption scheme. Office 2007 is a transitional version: the encryption is strong (AES, iterated SHA-1), but the protection verifier defaults to SHA-1 — a critical gap because hashcat 25300 only accepts SHA-512.

## Overview

| Detail | Value |
|---|---|
| Version | Office 2007 (12.0) |
| Years | 2007 – 2010 |
| Container | OOXML/ZIP (.docx/.xlsx/.pptx), encrypted files re-wrapped as OLE/CFB |
| Encryption spec | [MS-OFFCRYPTO] Sections 2.3.4.5 – 2.3.4.9 (ECMA-376 Standard) |
| Key infrastructure | Fixed — no CSP dialog, no CNG, no user-selectable cipher |
| Default open encryption | AES-128-ECB, SHA-1, 50000 iterations (hardcoded) |

## File types produced

| Extension | Application | Container | Encrypted container |
|---|---|---|---|
| `.docx` / `.docm` / `.dotx` / `.dotm` | Word | OOXML/ZIP | OLE/CFB wrapper |
| `.xlsx` / `.xlsm` / `.xltx` / `.xltm` / `.xlsb` | Excel | OOXML/ZIP | OLE/CFB wrapper |
| `.pptx` / `.pptm` / `.potx` / `.potm` | PowerPoint | OOXML/ZIP | OLE/CFB wrapper |

When a document-open password is set, Office 2007 re-wraps the entire OPC/ZIP package inside an OLE/CFB container carrying `\EncryptionInfo` and `\EncryptedPackage` streams. The file keeps its `.docx`/`.xlsx`/`.pptx` extension but is physically OLE on disk.

## Document-open encryption

### ECMA-376 Standard ([MS-OFFCRYPTO] Sections 2.3.4.5 – 2.3.4.9)

Office 2007 introduced a single, fixed encryption shape — there is no CSP dialog and no way to select a different cipher or hash from the UI. The `EncryptionInfo` stream carries a binary header (not XML) with `AlgID` and `KeySize` fields.

- **KDF**: `H0 = SHA1(salt || UTF16LE(password))` → spin 50000 rounds (`Hn = SHA1(LE32(i) || Hn-1)`, iterator **prepended**) → `Hfinal = SHA1(Hspin || LE32(0))` → ipad/opad key expansion → key = first `keyBits/8` bytes
- **Cipher**: AES-ECB (not CBC — the only Office scheme that uses ECB)
- **Hash**: SHA-1 (fixed, `AlgIDHash = 0x8004`)
- **Key sizes**: 128 (default). The spec also allows `AlgID` values for AES-192 (`0x660F`) and AES-256 (`0x6610`), but Office 2007's UI always writes AES-128. AES-192/256 requires registry manipulation.
- **Iterations**: 50000 (fixed, hardcoded in the spec)
- **hashcat**: `9400` (`$office$*2007*...`). Note: hashcat 9400 accepts keySize 128 and 256 but **rejects 192**.
- **Toolkit `--format opt`**: `$office$*sha1*aes128*ecb*50000*<salt>*<encverifier>*<encverifierhash>`

## Protection gates

Office 2007 introduced the ISO write-protection verifier ([MS-OFFCRYPTO] Section 2.4.2.4) for sheet/workbook/document protection in OOXML files. It also carries the legacy Word 2007 `crypt*` dialect for document protection.

| Gate | Where | Recovery | Verifier | Note |
|---|---|---|---|---|
| Sheet protection | `xl/worksheets/sheetN.xml` `<sheetProtection>` | `STRIP` | ISO SHA-1 (default) | hashcat 25300 rejects SHA-1 |
| Workbook protection | `xl/workbook.xml` `<workbookProtection>` | `STRIP` | ISO SHA-1 | |
| Shared revisions | `xl/workbook.xml` `<workbookProtection revisions*>` | `STRIP` | ISO SHA-1 | |
| Write-reservation (modify) | `xl/workbook.xml` `<fileSharing>` | `STRIP` | ISO SHA-1 | |
| Allow-edit-ranges | `xl/worksheets/sheetN.xml` `<protectedRange>` | `STRIP` | ISO SHA-1 | |
| Restrict editing | `word/settings.xml` `<w:documentProtection>` | `STRIP` | Word 2007 crypt* dialect | Legacy KDF, no hashcat mode |
| Modify (Word) | `word/settings.xml` `<w:writeProtection>` | `STRIP` | Word 2007 crypt* or ISO | |
| Modify (PowerPoint) | `ppt/presentation.xml` `<p:modifyVerifier>` | `STRIP` | ISO SHA-1 | |
| VBA project lock | `vbaProject.bin` `PROJECT` stream `DPB` | `STRIP` / `CRACK` | SHA-1 or cleartext | hashcat 110 |
| Digital signature | `_xmlsignatures/` parts | `NONE` | public-key | Not password-recoverable |

### The SHA-1 protection gap

Office 2007's default ISO protection verifier uses **SHA-1** (`algorithmName` defaults to SHA-1 when unset, per [MS-OFFCRYPTO] Section 2.4.2.4 note `<27>`). hashcat mode 25300 only accepts SHA-512, so the most common Office 2007 protection hash has **no hashcat mode**. The toolkit extracts it as a `$protect$*sha1*iso*...` line (`--format opt`) or a `$office$protect$` generalized line (`--format hashcat`).

Since the document body is plaintext (protection does not encrypt), `opt advanced bypass` strips the protection instantly — cracking the password is only needed when the literal password string is the objective.

## Recovery summary

| Gate | Recovery | hashcat mode | Toolkit command |
|---|---|---|---|
| Open (Standard AES-128) | `CRACK` | 9400 | `opt advanced extract` / `opt advanced decrypt` |
| Sheet / Workbook / Modify / Range / Revisions (ISO SHA-1) | `STRIP` | — (25300 rejects SHA-1) | `opt advanced bypass` / `opt advanced extract --format opt` |
| Restrict editing (Word 2007 crypt*) | `STRIP` | — | `opt advanced bypass` |
| VBA project lock | `STRIP` | 110 | `opt advanced bypass` / `opt advanced extract` |
| Digital signature | `NONE` | — | `opt advanced bypass --remove-signatures` |

## Extraction examples

```bash
# Standard AES-128 (hashcat format)
$ opt info encrypted-2007.docx
$office$*2007*20*128*16*18410007331073848057180885845227*944c70a5ee6e5ab2a6a86ff54b5f621a*e6650f1f2630c27fd8fc0f5e56e2e01f99784b9f

# Standard AES-128 (self-describing)
$ opt info encrypted-2007.docx --format opt
$office$*sha1*aes128*ecb*50000*18410007331073848057180885845227*944c70a5ee6e5ab2a6a86ff54b5f621a*e6650f1f2630c27fd8fc0f5e56e2e01f99784b9f

# ISO SHA-1 sheet protection (self-describing — no hashcat mode)
$ opt info protected-2007.xlsx --format opt
$protect$*sha1*iso*100000*bf803ef68f477e4eea5080e6ec74c9ff*0c631275689932d50efe11a904992a86e19f59f3
```

## hashcat modes

| Mode | Name | What it cracks |
|---|---|---|
| `9400` | MS Office 2007 | Standard AES-ECB / SHA-1 / 50000 iterations |
| `25300` | MS Office 2016 SheetProtection | ISO SHA-512 protection only (NOT the SHA-1 default for 2007) |
| `110` | sha1($pass.$salt) | VBA project SHA-1 verifier |
