# Office 97 / 2000 / XP / 2003

Everything the toolkit handles for the legacy binary Office formats — `.doc`, `.xls`, `.ppt` — across Office 97, 2000, XP, and 2003. These four releases share the same OLE/CFB container and the same encryption infrastructure; they differ only in which CryptoAPI provider and key length the user selects (or the administrator enforces).

## Overview

| Detail | Value |
|---|---|
| Versions | Office 97, 2000, XP (2002), 2003 |
| Years | 1997 – 2006 |
| Container | OLE Compound File Binary ([MS-CFB]) |
| Encryption spec | [MS-OFFCRYPTO] Sections 2.3.5 – 2.3.7 |
| Key infrastructure | CryptoAPI CSPs (no CNG) |
| Default open encryption | RC4-CryptoAPI SHA-1 128-bit (XP/2003); RC4+MD5 40-bit (97/2000); XOR obfuscation (pre-97 holdover) |

## File types produced

| Extension | Application | Container |
|---|---|---|
| `.doc` / `.dot` | Word | OLE/CFB |
| `.xls` / `.xlt` / `.xla` | Excel | OLE/CFB |
| `.ppt` / `.pot` / `.ppa` | PowerPoint | OLE/CFB |

## Document-open encryption

Three encryption schemes exist for the legacy binary formats, selected by the user through the Tools > Options > Security > Advanced dialog (2003) or applied automatically (97/2000).

### XOR obfuscation ([MS-OFFCRYPTO] Section 2.3.7)

A keyless scramble that is NOT real encryption. The document body is XORed against a 16-byte array derived purely from the password — no salt, no iteration, no cipher key. The array can be reconstructed from the stored `XorKey` and known-plaintext BIFF records without knowing the password, so recovery is instant (`DECODE`). Excel stores a 16-bit `verificationBytes` + `XorKey` in the `FilePass` record; Word stores a 32-bit `lKey` in `FibBase`.

- **Recovery**: `DECODE` (rebuild the array from the file) or `COLLIDE` (mint a password matching the 16/32-bit verifier)
- **hashcat**: none — not a GPU target
- **Toolkit**: `opt advanced decode` (content recovery), `opt advanced collide` (password recovery)

### RC4 + MD5, 40-bit ([MS-OFFCRYPTO] Section 2.3.6)

The Office 97/2000 default. A single MD5 pass derives a 40-bit RC4 key — no iteration, no salt rotation. The 40-bit keyspace (2^40 ~ 1.1 trillion) is directly brute-forceable in GPU hours regardless of password strength, so the attack path is `KEYSPACE` (brute the key) rather than `CRACK` (brute the password).

- **KDF**: `t0 = MD5(UTF16LE(password))[:5]` → `t1 = MD5((t0 || salt) * 16)[:5]` → `key = MD5(t1 || LE32(block))[:16]`
- **Key size**: always 40-bit effective (two 5-byte truncations)
- **hashcat**: `9700` (`$oldoffice$0` for Word, `$oldoffice$1` for Excel), plus `9710`/`9720` collider/MITM variants
- **Toolkit `--format opt`**: `$office$*md5*rc4-40*stream*0*<salt>*<encverifier>*<encverifierhash>`

### RC4-CryptoAPI + SHA-1 ([MS-OFFCRYPTO] Section 2.3.5)

The Office XP/2003 encryption, and the first Office scheme with user-selectable key lengths. The `EncryptionHeader` names the CryptoAPI CSP, cipher (`AlgID = CALG_RC4`), hash (`AlgIDHash = CALG_SHA1`), and key size. The KDF is a single SHA-1 pass — no iteration.

- **KDF**: `H0 = SHA1(salt || UTF16LE(password))` → `key = SHA1(H0 || LE32(block))[:keyBytes]`
- **Key sizes**: 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128 bits (8-bit steps, [MS-OFFCRYPTO] Section 2.3.5)
- **40-bit special case**: key is `Hfinal[:5]` zero-padded to 16 bytes; the 2^40 keyspace is brute-forceable (`KEYSPACE`)
- **hashcat**: `9800` (`$oldoffice$3` for 40-bit, `$oldoffice$4` for >40-bit), plus `9810`/`9820` collider/MITM variants
- **Toolkit `--format opt`**: `$office$*sha1*rc4-{keybits}*stream*0*<salt>*<encverifier>*<encverifierhash>`

### CryptoAPI CSP inventory

The Encryption Type dialog (Tools > Options > Security > Advanced) lists the CSPs installed on the Windows machine. Office 2003 on XP SP3 shows 10 of the 14 available CSPs; Office 2003 on Windows 7 shows 10 (four XP-only CSPs were removed).

**Windows XP SP3 (14 CSPs):**
Gemplus GemSAFE Card, Infineon SICRYPT, Microsoft Base, Microsoft Base DSS and Diffie-Hellman, Microsoft Base DSS, Microsoft Base Smart Card, Microsoft DH SChannel, Microsoft Enhanced, Microsoft Enhanced DSS and Diffie-Hellman, Microsoft Enhanced RSA and AES (Prototype), Microsoft Exchange, Microsoft RSA SChannel, Microsoft Strong, Schlumberger.

**Windows 7 SP1 (10 CSPs):**
Microsoft Base, Microsoft Base DSS and Diffie-Hellman, Microsoft Base DSS, Microsoft Base Smart Card, Microsoft DH SChannel, Microsoft Enhanced, Microsoft Enhanced DSS and Diffie-Hellman, Microsoft Enhanced RSA and AES, Microsoft RSA SChannel, Microsoft Strong.

Removed from XP: Gemplus, Infineon, Exchange, Schlumberger. The `Enhanced RSA and AES` CSP lost its `(Prototype)` suffix.

## Protection gates

| Gate | Where | Recovery | Verifier | Note |
|---|---|---|---|---|
| Sheet protection | `.xls` `Password` record (0x13) in worksheet substream | `COLLIDE` / `STRIP` | 16-bit Method 1 | |
| Workbook protection | `.xls` `Password` record (0x13) in globals substream | `COLLIDE` / `STRIP` | 16-bit Method 1 | |
| Write-reservation (modify) | `.xls` `FileSharing` record (0x5B) | `COLLIDE` / `STRIP` | 16-bit Method 1 | |
| Allow-edit-ranges | `.xls` `Feat/FeatProtection` record (0x867) | `COLLIDE` / `STRIP` | 16-bit Method 1 | |
| Shared revisions | `.xls` `Prot4RevPass` record (0x1BC) | `COLLIDE` / `STRIP` | 16-bit Method 1 | |
| Restrict editing | `.doc` `DopBase.lKeyProtDoc` (Table stream) | `COLLIDE` / `STRIP` | 32-bit Method 2 | |
| Modify password | `.doc` `SttbfAssoc` index 0x11 (Table stream) | `READ` | cleartext UTF-16LE | Password stored verbatim |
| Modify password | `.ppt` `ModifyPasswordAtom` (0x0FBA, instance 3) | `READ` | cleartext UTF-16LE | Password stored verbatim |
| VBA project lock | `PROJECT` stream `DPB` value | `STRIP` / `CRACK` | SHA-1 or cleartext | hashcat 110 for hash case |
| Digital signature | `_signatures` stream | `NONE` | public-key | Not password-recoverable |

## Recovery summary

| Gate | Recovery | hashcat mode | Toolkit command |
|---|---|---|---|
| Open (XOR obfuscation) | `DECODE` | — | `opt advanced decode` |
| Open (RC4+MD5 40-bit) | `KEYSPACE` | 9700 / 9710 / 9720 | `opt advanced extract` |
| Open (RC4-CryptoAPI 40-bit) | `KEYSPACE` | 9800 / 9810 / 9820 | `opt advanced extract` |
| Open (RC4-CryptoAPI 48-128-bit) | `CRACK` | 9800 | `opt advanced extract` |
| Sheet / Workbook / Modify / Range / Revisions (.xls) | `COLLIDE` | — | `opt advanced collide` / `opt advanced bypass` |
| Restrict editing (.doc) | `STRIP` | — | `opt advanced bypass` |
| Modify (.doc cleartext) | `READ` | — | `opt info` (prints the password) |
| Modify (.ppt cleartext) | `READ` | — | `opt info` (prints the password) |
| VBA project lock | `STRIP` | 110 | `opt advanced bypass` / `opt advanced extract` |
| Digital signature | `NONE` | — | `opt advanced bypass --remove-signatures` |

## Extraction examples

```bash
# RC4-CryptoAPI SHA-1 128-bit (hashcat format, default)
$ opt info doc-open-rc4capi-enhanced-128.doc
$oldoffice$4*389eb85ba016979b45872262bd473d33*ae9b4378c00439...

# RC4-CryptoAPI SHA-1 128-bit (self-describing format)
$ opt info doc-open-rc4capi-enhanced-128.doc --format opt
$office$*sha1*rc4-128*stream*0*389eb85ba016979b45872262bd473d33*ae9b4378c00439...

# RC4+MD5 40-bit
$ opt info xls-open-rc4md5.xls --format opt
$office$*md5*rc4-40*stream*0*55045061647456688860411218030058*e7e24d163fbd7439...

# XOR obfuscation — not in extract (use decode/collide instead)
$ opt advanced decode xor-encryption-abc.xls
Decoded -> xor-encryption-abc.decoded.xls
```

## hashcat modes

| Mode | Name | What it cracks | Key size |
|---|---|---|---|
| `9700` | MS Office <= 2003 MD5+RC4 | RC4+MD5 password | 40-bit |
| `9710` | (collider variant of 9700) | RC4+MD5 key-seed collision | 40-bit |
| `9720` | (MITM variant of 9700) | RC4+MD5 password-from-key | 40-bit |
| `9800` | MS Office <= 2003 SHA1+RC4 | RC4-CryptoAPI password | 40-128-bit |
| `9810` | (collider variant of 9800) | RC4-CryptoAPI key collision | 40-bit |
| `9820` | (MITM variant of 9800) | RC4-CryptoAPI password-from-key | 40-bit only |
| `110` | sha1($pass.$salt) | VBA project SHA-1 verifier | — |
