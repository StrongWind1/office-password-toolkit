# CLI Output Design — `opt info`

## One-liner format (default)

One line per file. `status:scheme` tags tell you what each gate means for YOU. Hash to stdout (one per line, matching file order).

```
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
template.xsn       info:design-locked
visio.vsdx         encrypted:agile-sha512  info:shape-locked
```

## The 6 statuses

| Status | What it tells you | What `opt unlock` does |
|---|---|---|
| `encrypted:` | You need the password to read this file | Tries defaults silently, then outputs hash for cracking |
| `removable:` | This gate can be removed without the password | Strips/collides it automatically |
| `trivial:` | This is instantly reversible, no password needed | Decodes/collides it automatically |
| `info:` | Something to know about, not a password gate | Reports it, no action needed |
| `blocked:` | Not recoverable — needs a certificate or server | Reports it, can't help |
| `open` | No protection at all | Nothing to do |

## Gate schemes by status

### `encrypted:` — you need the password

| Scheme | What the file has |
|---|---|
| `encrypted:agile-sha512` | Office 2013+ default (SHA-512 + AES-256-CBC) |
| `encrypted:agile-sha256` | Non-default agile (SHA-256) |
| `encrypted:agile-sha384` | Non-default agile (SHA-384) |
| `encrypted:agile-sha1` | Office 2010 default (SHA-1 + AES-128-CBC) |
| `encrypted:standard` | Office 2007 (SHA-1 × 50000 + AES-ECB) |
| `encrypted:rc4-sha1` | Office XP/2003 (RC4 CryptoAPI + SHA-1) |
| `encrypted:rc4-md5` | Office 97/2000 (RC4 + MD5, 40-bit effective) |
| `encrypted:odf11` | ODF 1.1 (Blowfish-CFB, ~1024 iterations — fast) |
| `encrypted:odf12` | ODF 1.2 (AES-256-CBC, 100000 iterations) |
| `encrypted:odf13` | ODF 1.3 (Argon2id + AES-256-GCM — hard) |
| `encrypted:ace` | Access 2010+ (ACE agile) |

### `removable:` — opt unlock strips this

| Scheme | What the file has |
|---|---|
| `removable:sheets(N)` | N worksheets with sheet protection |
| `removable:workbook` | Workbook structure/windows locked |
| `removable:write` | Write reservation / modify password |
| `removable:restricted` | Editing restricted (tracked changes, comments, forms, read-only) |
| `removable:ranges(N)` | N cell ranges with edit-range passwords |
| `removable:revisions` | Shared workbook revision log locked |
| `removable:macros` | VBA project locked for viewing |
| `removable:modify` | PowerPoint modify password |

### `trivial:` — instantly reversible

| Scheme | What the file has |
|---|---|
| `trivial:xor-obfuscation` | Legacy XOR "encryption" (.doc/.xls) — array reconstructable from known plaintext |
| `trivial:pst-advisory` | PST open password — CRC-32, encrypts nothing |
| `trivial:jet-password` | Access .mdb database password — fixed/date-key XOR, instant decode |
| `trivial:cleartext-write` | Word .doc write-reservation — password stored in the clear |
| `trivial:cleartext-modify` | PowerPoint .ppt modify — password stored in the clear |

### `info:` — FYI, not a password gate

| Scheme | What it means |
|---|---|
| `info:signed` | File has a digital signature (PKI integrity, can be stripped) |
| `info:pst-encoded` | PST body uses keyless permute/cyclic cipher (decoded automatically) |
| `info:design-locked` | InfoPath designMode=protected (application-level flag) |
| `info:shape-locked` | Visio Lock* cells (UI-level advisory, no password) |

### `blocked:` — not recoverable

| Scheme | What it means |
|---|---|
| `blocked:rights-managed` | IRM / RMS — needs the certificate private key or RMS server authorization |
| `blocked:irm-certificate` | Certificate-wrapped encryption — needs the X.509 private key |

### `open` — no protection

| Scheme | What it means |
|---|---|
| `open` | No protection gates found |

## stdout — hash lines

One hash line per file on stdout. Blank line if no crackable hash. Keeps file-to-hash alignment for batch processing.

```
stdout:
$office$*sha512*aes256*cbc*100000*<salt>*<verifier>*<hash>
$office$*sha1*rc4-128*stream*0*<salt>*<verifier>*<hash>


$office$*sha512*aes256*cbc*100000*<salt>*<verifier>*<hash>




```

Only `encrypted:` gates produce hash lines. `removable:`, `trivial:`, `info:`, `blocked:` gates do not — they're handled by `opt unlock` or `opt advanced`.

## Formatting rules

- **One line per file**: `<filename>  <status:scheme status:scheme ...>`
- **Filename column**: left-aligned, padded to longest filename in the batch
- **Tags ordered by severity**: `encrypted:` first, then `removable:`, `trivial:`, `info:`, `blocked:`
- **Counts in parens**: `sheets(3)` not three separate tags
- **Default passwords tried silently by `opt unlock`** — never shown in `opt info` output
- **No recovery instructions in the output** — that's what `opt unlock` and `opt advanced` are for
- **Exit code**: 0 = at least one hash emitted, 1 = no crackable hashes, 2 = error

## `opt info --help`

```
Usage: opt info [OPTIONS] FILE...

Show protection gates on Office files.

  stdout → crackable hash lines (pipe to hashcat)
  stderr → gate summary, one line per file

Status:
  encrypted:   You need the password to read this file
  removable:   Can be removed without the password (opt unlock)
  trivial:     Instantly reversible, no password needed (opt unlock)
  info:        Not a password gate — just informational
  blocked:     Not recoverable (needs certificate or server key)
  open         No protection at all

Examples:
  opt info secret.xlsx                    Show gates + hash
  opt info *.docx | hashcat -m 37000     Batch extract + crack
  opt info *.xlsx 2>/dev/null             Hashes only (for scripting)
  opt info file.xlsx 2>&1 >/dev/null      Info only (no hash)

Options:
  --format [hashcat|unified|json]   Hash output format (default: hashcat)
  --no-hash                         Suppress stdout hash output
  --json                            Output stderr as JSON
  -q, --quiet                       Suppress stderr (hash only, same as 2>/dev/null)
```

## JSON output (`--json`)

```json
{
  "files": [
    {
      "path": "secret.xlsx",
      "container": "OOXML",
      "product": "Excel",
      "gates": [
        {"status": "encrypted", "scheme": "agile-sha512"},
        {"status": "removable", "scheme": "sheets", "count": 3},
        {"status": "removable", "scheme": "workbook"},
        {"status": "removable", "scheme": "write"}
      ],
      "hash": "$office$*sha512*aes256*cbc*100000*...",
      "hash_format": "unified"
    }
  ]
}
```
