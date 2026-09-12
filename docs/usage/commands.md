# CLI Command Reference

## Overview

`opt` has three commands:

| Command | Purpose | Scope |
|---|---|---|
| `opt info` | Show protection gates and emit crackable hashes | Multi-file, multi-directory |
| `opt unlock` | Try everything cheapest-first to recover file(s) | Multi-file, multi-directory |
| `opt advanced` | Expert single-file tools (8 subcommands) | Single file |

`info` and `unlock` accept files, directories (recursively scanned for Office extensions), and shell globs. `advanced` subcommands operate on one file at a time.

**stdout is machine-readable, stderr is human.** Hash lines and produced paths go to stdout for piping; status output, diagnostics, and errors go to stderr with color when the terminal supports it. `opt info secret.docx 2>/dev/null | hashcat -m 9600` works because only the hash reaches the pipe.

**The input is never modified.** Every writing command opens the input read-only and writes a separate file. A guard refuses to overwrite the input (exit 6) and refuses to overwrite an existing output unless `--force` is passed.


## `opt info` — show gates and extract hashes

Show what protects each file and emit crackable hash lines for piping to hashcat.

### Synopsis

```
opt info [OPTIONS] FILE...
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE...` | yes | Office / OpenDocument files or directories (recursive) |
| `--format FORMAT` | no | Hash output format: `unified` (default, self-describing), `hashcat` (hashcat-compatible), or `json` (structured JSON to stderr) |
| `--no-hash` | no | Suppress stdout hash output |
| `--json` | no | Output structured JSON to stderr instead of one-liners |
| `-q`, `--quiet` | no | Suppress stderr output (hash lines only, same as `2>/dev/null`) |

**stdout:** one hash line per file (blank line when no crackable hash exists), maintaining file-to-line alignment for batch processing. Only `encrypted:` gates produce hash lines.

**stderr:** one `status:scheme` tag line per file (or JSON with `--json`/`--format json`).

### Status tags

Each gate is classified into one of six statuses, ordered by severity:

| Status | Meaning | What `opt unlock` does |
|---|---|---|
| `encrypted:` | You need the password to read this file | Tries defaults silently, then outputs hash for cracking |
| `removable:` | Can be removed without the password | Strips it automatically |
| `trivial:` | Instantly reversible, no password needed | Decodes/collides it automatically |
| `info:` | Something to know about, not a password gate | Reports it, no action needed |
| `blocked:` | Not recoverable — needs a certificate or server key | Reports it, cannot help |
| `open` | No protection at all | Nothing to do |

Tags are ordered by severity on each line. Countable gates show their count in parentheses (e.g. `sheets(3)`).

### Examples

Single file:

```console
$ opt info secret.xlsx
secret.xlsx  encrypted:agile-sha512  removable:sheets(3)  removable:workbook  removable:write
```

Multiple files with aligned output:

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

Recursive directory scan:

```console
$ opt info documents/
```

Pipe hashes to hashcat:

```console
$ opt info *.docx 2>/dev/null | hashcat -m 9600
```

Hashes only (suppress stderr):

```console
$ opt info secret.xlsx -q
$office$*sha512*aes256*cbc*100000*<salt>*<verifier>*<hash>
```

Status only (suppress hashes):

```console
$ opt info --no-hash secret.xlsx
secret.xlsx  encrypted:agile-sha512  removable:sheets(3)
```

JSON output:

```console
$ opt info --format json secret.xlsx
```

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

### Gate scheme reference

??? note "Encryption schemes (`encrypted:`)"

    | Scheme | File type |
    |---|---|
    | `agile-sha512` | Office 2013+ default (SHA-512 + AES-256-CBC) |
    | `agile-sha256` | Non-default agile (SHA-256) |
    | `agile-sha384` | Non-default agile (SHA-384) |
    | `agile-sha1` | Office 2010 default (SHA-1 + AES-128-CBC) |
    | `standard` | Office 2007 (SHA-1 x 50000 + AES-ECB) |
    | `rc4-sha1` | Office XP/2003 (RC4 CryptoAPI + SHA-1) |
    | `rc4-md5` | Office 97/2000 (RC4 + MD5, 40-bit effective) |
    | `odf11` | ODF 1.1 (Blowfish-CFB, ~1024 iterations) |
    | `odf12` | ODF 1.2 (AES-256-CBC, 100000 iterations) |
    | `odf13` | ODF 1.3 (Argon2id + AES-256-GCM) |
    | `ace` | Access 2010+ (ACE agile) |

??? note "Removable schemes (`removable:`)"

    | Scheme | Gate |
    |---|---|
    | `sheets(N)` | N worksheets with sheet protection |
    | `workbook` | Workbook structure/windows locked |
    | `write` | Write reservation / modify password |
    | `restricted` | Editing restricted (tracked changes, comments, forms, read-only) |
    | `ranges(N)` | N cell ranges with edit-range passwords |
    | `revisions` | Shared workbook revision log locked |
    | `macros` | VBA project locked for viewing |
    | `modify` | PowerPoint modify password |

??? note "Trivial schemes (`trivial:`)"

    | Scheme | Gate |
    |---|---|
    | `xor-obfuscation` | Legacy XOR "encryption" (.doc/.xls) — array reconstructable from known plaintext |
    | `pst-advisory` | PST open password — CRC-32, encrypts nothing |
    | `jet-password` | Access .mdb database password — fixed/date-key XOR, instant decode |
    | `cleartext-write` | Word .doc write-reservation — password stored in the clear |
    | `cleartext-modify` | PowerPoint .ppt modify — password stored in the clear |

??? note "Informational schemes (`info:`)"

    | Scheme | Meaning |
    |---|---|
    | `signed` | File has a digital signature (PKI integrity, can be stripped) |
    | `pst-encoded` | PST body uses keyless permute/cyclic cipher (decoded automatically) |
    | `design-locked` | InfoPath designMode=protected (application-level flag) |
    | `shape-locked` | Visio Lock* cells (UI-level advisory, no password) |

??? note "Blocked schemes (`blocked:`)"

    | Scheme | Meaning |
    |---|---|
    | `rights-managed` | IRM / RMS — needs the certificate private key or RMS server authorization |
    | `irm-certificate` | Certificate-wrapped encryption — needs the X.509 private key |


## `opt unlock` — try everything

The one-call recovery path. Runs the full recovery ladder cheapest-first on each file, writing the most-usable output achievable without manual cracking.

### Synopsis

```
opt unlock [OPTIONS] FILE...
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE...` | yes | Office / OpenDocument files or directories (recursive) |
| `-p`, `--password` | no | Document-open password to try after the built-in defaults |
| `--wordlist`, `--password-file` | no | File of candidate passwords, one per line, tried after `-p` |
| `--remove-signatures` | no | Also delete digital signatures in the bypass step (destructive, cannot be undone) |
| `--force` | no | Overwrite output if it already exists |
| `-o`, `--output` | no | Output path (only valid with a single input file) |

### Recovery ladder

`unlock` walks each file through a fixed sequence, cheapest-first. Each step degrades gracefully when it does not apply or when its handler is unfinished.

| Step | Action | What happens |
|---|---|---|
| 1 | **INFO** | Print the `status:scheme` triage line |
| 2 | **DECODE** | Reverse keyless obfuscation (XOR body, PST body cipher) |
| 3 | **DECRYPT** | Try built-in defaults, then `-p`, then `--wordlist` entries |
| 4 | **COLLIDE** | Report any collidable tiny verifiers (16/32-bit, CRC-32) |
| 5 | **BYPASS** | Strip every remaining non-encrypting gate |
| 6 | **INFO** | Print a final triage of the produced file |

If decryption fails (no candidate password works), `unlock` emits the hash lines to stdout for cracking and continues to the collide and bypass steps for any non-encrypting gates.

!!! note "Built-in default passwords"
    `unlock` silently tries the empty string, `VelvetSweatshop`, and `/01Hannes Ruescher/01` before any user-supplied password. A large fraction of "encrypted" Office files open on one of these with no cracking.

### Examples

Auto-recover an unencrypted protected file:

```console
$ opt unlock sheetProtection_allLocked.xlsx

--- sheetProtection_allLocked.xlsx ---
sheetProtection_allLocked.xlsx  removable:sheets
Bypassed -> sheetProtection_allLocked.bypassed.xlsx
Final triage:
sheetProtection_allLocked.bypassed.xlsx  open
```

Try a known password:

```console
$ opt unlock secret.xlsx -p "hunter2"
```

Batch with wordlist:

```console
$ opt unlock *.docx --wordlist passwords.txt
```

Recurse a directory, overwriting previous output:

```console
$ opt unlock folder/ --force
```

Encrypted file, opened by built-in default:

```console
$ opt unlock protected_agile.docx

--- protected_agile.docx ---
protected_agile.docx  encrypted:agile-sha512
Decrypted -> protected_agile.decrypted.docx
Bypassed -> protected_agile.decrypted.bypassed.docx
Final triage:
protected_agile.decrypted.bypassed.docx  open
```

Encrypted file, no available password (exit 4):

```console
$ opt unlock example_password.docx

--- example_password.docx ---
example_password.docx  encrypted:agile-sha512
Cannot produce plaintext; emitting hashes for cracking.
$office$*2013*100000*256*16*cbca1c999343fbad92075634150034b0*...
$ echo $?
4
```


## `opt advanced` — expert tools

Eight single-file subcommands for when you need precise control over one step of the recovery process.

```
opt advanced <subcommand> [OPTIONS] FILE [OUT]
```

---

### `opt advanced extract`

Emit crackable hash lines for every password gate the file carries.

```
opt advanced extract [OPTIONS] FILE
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE` | yes | Office / OpenDocument file |
| `--format FORMAT` | no | `hashcat` (default, hashcat-compatible lines) or `opt` (self-describing 4-family lines) |
| `--hashcat-only` | no | Emit only lines that hashcat can ingest |

XOR and PST verifiers are filtered out — they are `decode`/`collide` targets, not GPU crack targets. Never writes a file.

```console
$ opt advanced extract example_password.docx
$office$*2013*100000*256*16*cbca1c999343fbad92075634150034b0*39eea54e26e514798c284bc7714d38ac*14376d6d817334e6b0ff4fd8221a7c678e5d8a784e8f999f4c188930c36a4b29
```

Exit 0 if any hash is emitted, 3 if no gate exists, 7 if gates exist but none produce a hash.

---

### `opt advanced decode`

Reverse keyless obfuscation — no password needed.

```
opt advanced decode [OPTIONS] FILE [OUT]
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE` | yes | Input file (never modified) |
| `OUT` | no | Output path (default: `<stem>.decoded<ext>`) |
| `--force` | no | Overwrite output if it already exists |

Handles XOR-obfuscated `.xls`/`.doc`, Outlook PST/OST body cipher (NDB_CRYPT_PERMUTE / NDB_CRYPT_CYCLIC), and Access Jet `.mdb` password decode. For Jet `.mdb`, the recovered cleartext password is printed to stdout instead of writing a file.

```console
$ opt advanced decode mailbox.pst
Decoded -> mailbox.decoded.pst
mailbox.decoded.pst

$ opt advanced decode legacy.mdb
Jet database password recovered: 'secret'
secret
```

Exit 0 on success, 2 when the container has no decode path.

---

### `opt advanced collide`

Mint a password that satisfies a tiny verifier — instant, read-only.

```
opt advanced collide FILE
```

| Argument | Required | Description |
|---|---|---|
| `FILE` | yes | File to inspect for collidable verifiers |

Handles PST advisory CRC-32 (mints a 4-byte preimage), legacy `.xls` 16-bit protection verifiers (sheet / workbook / modify / range / revisions), and `.doc` 32-bit restrict-editing verifier. The original password is not recovered — only a value with the same checksum. Never writes a file.

```console
$ opt advanced collide mailbox.pst
PST CRC-32 collided: a36564ea
a36564ea
```

Exit 0 when at least one collision is printed, 7 when no collidable verifier is found.

---

### `opt advanced bypass`

Strip all non-encrypting gates into a new file. Signatures are preserved unless `--remove-signatures` is passed.

```
opt advanced bypass [OPTIONS] FILE [OUT]
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE` | yes | Input file (never modified) |
| `OUT` | no | Output path (default: `<stem>.bypassed<ext>`) |
| `--remove-signatures` | no | Also delete digital signatures (destructive, cannot be undone) |
| `--force` | no | Overwrite output if it already exists |

Clears modify / write-reservation, sheet / workbook / document / range / revisions protection, VBA project lock, PST advisory password, and ODF body protection. Does not touch open-encryption — use `decrypt` for that.

```console
$ opt advanced bypass sheetProtection_allLocked.xlsx
Bypassed -> sheetProtection_allLocked.bypassed.xlsx
sheetProtection_allLocked.bypassed.xlsx

$ opt advanced bypass protectedSheets.xlsx clean.xlsx
Bypassed -> clean.xlsx
clean.xlsx
```

Exit 0 on success, 2 when unsupported, 6 when the output would overwrite the input or an existing file.

---

### `opt advanced strip`

Strip ALL non-encrypting protection INCLUDING digital signatures. The most aggressive non-encrypting recovery. Equivalent to `bypass --remove-signatures`.

```
opt advanced strip [OPTIONS] FILE [OUT]
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE` | yes | Input file (never modified) |
| `OUT` | no | Output path (default: `<stem>.stripped<ext>`) |
| `--force` | no | Overwrite output if it already exists |

```console
$ opt advanced strip signed_and_protected.xlsx
Stripped -> signed_and_protected.stripped.xlsx
signed_and_protected.stripped.xlsx
```

Exit 0 on success, 2 when unsupported, 6 when the output would overwrite.

!!! warning
    `strip` removes the digital signature integrity claim. This is destructive and cannot be undone.

---

### `opt advanced decrypt`

Decrypt document-open encryption into a new plaintext file.

```
opt advanced decrypt [OPTIONS] FILE [OUT]
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE` | yes | Encrypted input file (never modified) |
| `OUT` | no | Output path (default: `<stem>.decrypted<ext>`) |
| `-p`, `--password` | no | Password to try after built-in defaults |
| `--wordlist`, `--password-file` | no | File of candidate passwords, one per line |
| `--force` | no | Overwrite output if it already exists |

Candidates are tried in order: built-in defaults (empty string, `VelvetSweatshop`, `/01Hannes Ruescher/01`), then `-p`, then each `--wordlist` line. Stops on the first that opens the file.

```console
$ opt advanced decrypt secret.docx -p solrcell
Decrypted -> secret.decrypted.docx. Next: run `opt info secret.decrypted.docx` and `opt advanced bypass secret.decrypted.docx`.
secret.decrypted.docx
```

!!! tip
    The decrypted output may still carry inner protection (sheet protection, write reservation, etc.). Run `opt info` and `opt advanced bypass` on it to clear those gates.

Exit 0 on success, 3 if the file is not encrypted, 4 if no candidate password works, 5 if the file is IRM/RMS protected, 6 when the output would overwrite.

---

### `opt advanced verify`

Verify a file's integrity after decryption or bypass.

```
opt advanced verify [OPTIONS] FILE
```

| Argument / Option | Required | Description |
|---|---|---|
| `FILE` | yes | File to verify |
| `-p`, `--password` | no | Test this password against a still-encrypted file |

Opens the container (OLE/CFB or ZIP) to confirm structural validity, checks encryption state, and enumerates remaining gates. Never writes a file.

Reported statuses:

- `valid Office document` — container opens cleanly, not encrypted
- `corrupt/truncated` — container fails integrity checks
- `still encrypted` — document-open encryption is present
- `not an Office file` — not a recognized container

```console
$ opt advanced verify secret.decrypted.xlsx
valid Office document

$ opt advanced verify secret.xlsx -p "hunter2"
still encrypted: password valid
```

Exit 0 when valid, 1 if corrupt, 2 if not a recognized container, 4 if still encrypted.

---

### `opt advanced detail`

Verbose per-gate breakdown for a single file — the expert's starting point.

```
opt advanced detail FILE
```

| Argument | Required | Description |
|---|---|---|
| `FILE` | yes | Office / OpenDocument file |

Prints the container type, encryption state, and every gate with its recovery class, hashcat mode, location within the file, and notes. The machine-readable summary (tab-delimited) goes to stdout; the per-gate breakdown goes to stderr.

```console
$ opt advanced detail workbookProtection-workbook_password_user_range-2010.xlsx
workbookProtection-workbook_password_user_range-2010.xlsx	ooxml-zip	.xlsx	not encrypted
Workbook protection: strip @ xl/workbook.xml <workbookProtection>
Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
```

Exit 0 in normal operation.


## Global options

| Option | Description |
|---|---|
| `--version` | Print version and exit |
| `--debug`, `-d` | Enable debug output on stderr (container detection, handler dispatch, stream details, encryption parameters) |

Global options go before the command:

```console
$ opt --version
office-password-toolkit 0.1.0

$ opt --debug info secret.xlsx
opt: debug mode enabled
opt: container=ole-cfb  encrypted=True  extension=.xlsx  product=Excel
...
```


## Exit codes

The exit code contract is shared across all commands. Each command reaches only a subset.

| Code | Name | Meaning |
|---|---|---|
| 0 | `ok` | Success |
| 1 | `error` | General error (unexpected failure) |
| 2 | `unsupported` | Container recognised, but its gate/scheme is not yet handled |
| 3 | `not encrypted` | File carries no password/protection gate |
| 4 | `crack required` | Hashes emitted, no plaintext produced — hand them to hashcat |
| 5 | `unrecoverable` | No recoverable password secret (IRM/RMS, certificate-only) |
| 6 | `refused` | Output would overwrite the input or an existing file (pass `--force`) |
| 7 | `no hash` | Gate(s) present but none produce a crackable hash (try decode / collide / bypass) |

Exit codes by command:

| Command | Possible exit codes |
|---|---|
| `info` | 0, 1 |
| `unlock` | 0, 1, 4, 5, 6 |
| `advanced extract` | 0, 2, 3, 7 |
| `advanced decode` | 0, 2 |
| `advanced collide` | 0, 2, 7 |
| `advanced bypass` | 0, 2, 6 |
| `advanced strip` | 0, 2, 6 |
| `advanced decrypt` | 0, 3, 4, 5, 6 |
| `advanced verify` | 0, 1, 2, 4 |
| `advanced detail` | 0 |
