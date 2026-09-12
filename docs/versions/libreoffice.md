# LibreOffice (OpenDocument)

Everything the toolkit handles for LibreOffice and OpenDocument Format (ODF) files — `.odt`, `.ods`, `.odp`. LibreOffice is the primary producer of encrypted ODF packages; Apache OpenOffice and StarOffice use the same ODF encryption profiles. The crypto is entirely separate from Microsoft's [MS-OFFCRYPTO] stack: different key derivation, different ciphers, different password encoding, and different verification.

## Overview

| Detail | Value |
|---|---|
| Application | LibreOffice (also Apache OpenOffice, StarOffice) |
| Container | ODF/ZIP (OASIS OpenDocument Part 3) |
| Encryption spec | ODF 1.1 Section 17.3; ODF 1.2 Part 3 Section 3.4; ODF 1.3 tdf#105844 |
| Key infrastructure | PBKDF2-HMAC-SHA1 (1.1/1.2) or Argon2id (1.3) |
| Password encoding | raw **UTF-8** bytes (NOT UTF-16LE — the single biggest divergence from Microsoft) |

## File types produced

| Extension | Application | Container |
|---|---|---|
| `.odt` | Writer (text) | ODF/ZIP |
| `.ods` | Calc (spreadsheet) | ODF/ZIP |
| `.odp` | Impress (presentation) | ODF/ZIP |
| `.odg` | Draw (drawing) | ODF/ZIP |
| `.odf` | Math (formula) | ODF/ZIP |

## Document-open encryption

ODF encryption is per-stream: each significant member (`content.xml`, `styles.xml`, etc.) is raw-DEFLATE compressed and then individually encrypted, while the ZIP directory, `mimetype`, member names, and `META-INF/manifest.xml` stay in cleartext. The crypto parameters are Base64 XML attributes in the manifest — not a binary header.

### ODF 1.1 — Blowfish CFB (hashcat 18600)

The oldest profile, still produced by older LibreOffice installs and Apache OpenOffice.

| Parameter | Value |
|---|---|
| Start-key hash | SHA-1 (20-byte) |
| KDF | PBKDF2-HMAC-SHA1, **1024 rounds** (default) |
| Cipher | Blowfish CFB-64 (8-byte IV) |
| Key size | 16 bytes (128-bit Blowfish key) |
| Checksum | SHA-1 / first 1024 bytes (`/1K`) |

- **Password encoding**: raw UTF-8, no BOM, no NUL
- **PBKDF2 input**: the SHA-1 **start key** (`SHA1(password_utf8)`), NOT the raw password
- **PBKDF2 PRF**: always HMAC-SHA1 (even in the SHA-256 profile below — a common implementation mistake is to use HMAC-SHA256)
- **hashcat**: `18600` (`$odf$*0*0*1024*16*<checksum>*8*<iv>*16*<salt>*0*<ciphertext>`)
- **Toolkit `--format opt`**: `$odf$*sha1*pbkdf2*blowfish*1024*0*0*<salt>*<iv>*<checksum>*<ciphertext>`

### ODF 1.2 — AES-256-CBC (hashcat 18400)

The current LibreOffice default for new encrypted files.

| Parameter | Value |
|---|---|
| Start-key hash | SHA-256 (32-byte) |
| KDF | PBKDF2-HMAC-SHA1, **100000 rounds** (default) |
| Cipher | AES-256-CBC (16-byte IV) |
| Key size | 32 bytes (256-bit AES key) |
| Checksum | SHA-256 / first 1024 bytes (`/1K`) |

- **hashcat**: `18400` (`$odf$*1*1*100000*32*<checksum>*16*<iv>*16*<salt>*0*<ciphertext>`)
- **Toolkit `--format opt`**: `$odf$*sha256*pbkdf2*aes256*100000*0*0*<salt>*<iv>*<checksum>*<ciphertext>`

### ODF 1.3 — Argon2id + AES-256-GCM (no hashcat mode)

LibreOffice 24.8+ "Wholesome Encryption" (tdf#105844). A memory-hard KDF plus AEAD — the strongest profile and the only one with no hashcat / John mode by design.

| Parameter | Value |
|---|---|
| Start-key hash | SHA-256 (32-byte) |
| KDF | Argon2id (default: t=3, m=65536 KiB, p=4) |
| Cipher | AES-256-GCM (12-byte IV / nonce) |
| Key size | 32 bytes (256-bit AES key) |
| Verifier | 16-byte GCM auth tag (no plaintext checksum — the AEAD tag is the verifier) |

- **Stored member layout**: `IV(12) || ciphertext || tag(16)`
- **hashcat**: none — Argon2id is memory-hard, no GPU kernel exists
- **Toolkit**: fully decryptable with a known password (`opt advanced decrypt`), hash line emitted as extended `$odf$*2*...` for record-keeping
- **Toolkit `--format opt`**: `$odf$*sha256*argon2*aes256gcm*3*65536*4*<salt>*<iv>*<gcmtag>*<ciphertext>`

## Protection gates

ODF body protection is a flag, not encryption — the document body is plaintext XML inside the ZIP.

| Gate | Where | Recovery | Verifier | Note |
|---|---|---|---|---|
| Sheet protection | `content.xml` `<table:table table:protected="true">` | `STRIP` | flag + optional digest | Body is plaintext; delete the attribute |
| Section protection | `content.xml` `<text:section text:protected="true">` | `STRIP` | flag + optional digest | Body is plaintext; delete the attribute |

There is no VBA project lock, no modify password, no digital signature gate, and no IRM in ODF files. The encryption is the only real gate.

## Recovery summary

| Gate | Recovery | hashcat mode | Toolkit command |
|---|---|---|---|
| Open (ODF 1.1 Blowfish) | `CRACK` | 18600 | `opt advanced extract` / `opt advanced decrypt` |
| Open (ODF 1.2 AES-256) | `CRACK` | 18400 | `opt advanced extract` / `opt advanced decrypt` |
| Open (ODF 1.3 Argon2id+GCM) | `CRACK` | — (GPU gap) | `opt advanced extract --format opt` / `opt advanced decrypt` |
| Sheet protection (flag) | `STRIP` | — | `opt advanced bypass` |
| Section protection (flag) | `STRIP` | — | `opt advanced bypass` |

## Extraction examples

```bash
# ODF 1.2 AES-256 (hashcat format)
$ opt info encrypted-lo.odt
$odf$*1*1*100000*32*751854d8b90731ce0579f96bea6f0d4ac2fb2f546b31f1b6af9a5f66952a0bf4*16*c18eaae34bcbbe9119be017fe5f8b52d*16*2185a966155baa9e2fb597298febecbc*0*<ciphertext>

# ODF 1.2 AES-256 (self-describing)
$ opt info encrypted-lo.odt --format opt
$odf$*sha256*pbkdf2*aes256*100000*0*0*2185a966155baa9e2fb597298febecbc*c18eaae34bcbbe9119be017fe5f8b52d*751854d8b90731ce0579f96bea6f0d4ac2fb2f546b31f1b6af9a5f66952a0bf4*<ciphertext>

# ODF 1.1 Blowfish (hashcat format)
$ opt info encrypted-bf.ods
$odf$*0*0*1024*16*<checksum>*8*<iv>*16*<salt>*0*<ciphertext>

# ODF 1.3 Argon2id+GCM (self-describing — no hashcat mode)
$ opt info encrypted-argon2.odp --format opt
$odf$*sha256*argon2*aes256gcm*3*65536*4*<salt>*<iv>*<gcmtag>*<ciphertext>
```

## hashcat modes

| Mode | Name | What it cracks | Profile |
|---|---|---|---|
| `18400` | ODF 1.2 (SHA-256, AES) | PBKDF2-HMAC-SHA1 + AES-256-CBC | ODF 1.2 default |
| `18600` | ODF 1.1 (SHA-1, Blowfish) | PBKDF2-HMAC-SHA1 + Blowfish-CFB64 | ODF 1.1 default |
| — | ODF 1.3 | Argon2id + AES-256-GCM | no hashcat mode (memory-hard KDF) |
