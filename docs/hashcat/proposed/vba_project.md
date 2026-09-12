# `$vba$` — VBA Project Password (reuses mode 110)

No new hashcat mode needed. The VBA project password verifier is `SHA-1(password_MBCS || 4-byte_salt)` — exactly hashcat mode **110** (`sha1($pass.$salt)`) with `--hex-salt`.

## Hash line

```
$vba$*sha1*<hash_40hex>*<salt_8hex>
```

Or directly as mode 110 input:

```
<hash_40hex>:<salt_8hex>
```

## Why no new module

| Parameter | Mode 110 | VBA project |
|---|---|---|
| Hash | SHA-1 | SHA-1 |
| Iterations | 1 | 1 |
| Salt position | appended | appended |
| Salt length | variable | 4 bytes |
| Digest | 20 bytes | 20 bytes |

The only caveat: password is MBCS-encoded per `PROJECTCODEPAGE` (typically CP1252), not UTF-16LE. For ASCII passwords this is transparent. For non-ASCII, the cracking tool must encode candidates with the correct code page.

## Extraction

The `DPB=` value is wrapped in a reversible XOR obfuscation layer. The **toolkit** handles extraction — not hashcat:

1. Locate VBA storage (`vbaProject.bin` in OOXML, embedded in binary OLE)
2. Read `PROJECT` stream, parse `DPB=` hex value
3. XOR-wrapper decrypt (Seed, Version=2, ProjKey from CLSID byte-sum)
4. Discriminate payload: no-password (Length=1) / plaintext / hash (Length=29)
5. If hash: Decode Nulls to recover 4-byte Key + 20-byte SHA-1 hash
6. Emit `$vba$*sha1*<hash>*<key>` or mode-110 format `<hash>:<key>`

## Products with VBA

Word, Excel, PowerPoint, Access, Visio, Project, Publisher, Outlook — all use the same `[MS-OVBA]` format.
