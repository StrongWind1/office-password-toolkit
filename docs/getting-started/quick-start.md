# Quick start

Three commands handle every Office password scenario: `opt info` (inspect), `opt unlock` (remove protections), and `opt advanced` (fine-grained control). This page walks through the common workflows.

Two conventions hold throughout:

- **Hash to stdout, status to stderr.** `opt info FILE | hashcat ...` just works because only the hash reaches the pipe. The `status:scheme` gate summary prints to stderr.
- **The input file is never modified.** Every writing command produces a new file (`secret.unlocked.xlsx`), never overwrites the source.

## 1. Check what protections a file has

```console
$ opt info secret.xlsx
```

stderr shows each gate as a `status:scheme` tag on one line:

```
secret.xlsx   encrypted:agile-sha512  removable:sheets(3) removable:workbook
```

stdout emits the crackable hash (if any), ready to pipe. The six statuses tell you what each gate means at a glance:

| Status | Meaning |
|---|---|
| `encrypted:` | Password required to read the file |
| `removable:` | Stripped automatically, no password needed |
| `trivial:` | Instantly reversible (XOR, CRC, cleartext) |
| `info:` | Informational only, not a password gate |
| `blocked:` | Needs a certificate or RMS server |
| `open` | No protection |

## 2. Unlock a file automatically

```console
$ opt unlock secret.xlsx
```

`unlock` runs the full pipeline in one call: tries default passwords and keyless decodes, strips every `removable:` and `trivial:` gate, collides tiny verifiers, and writes a clean copy. If the file is genuinely encrypted and no default opens it, `unlock` emits the hash to stdout and exits with code 4 so your script can hand it to hashcat.

!!! tip
    `unlock` tries `VelvetSweatshop` and other built-in defaults silently. Files "encrypted" under a default password are decrypted without any `-p` flag.

## 3. Crack with hashcat

When `unlock` cannot decrypt, pipe the hash from `info` into hashcat, then feed the recovered password back:

```console
$ opt info secret.xlsx | hashcat -m 37000
$ opt unlock secret.xlsx -p recovered_password
```

The hashcat mode depends on the scheme `info` reported (`agile-sha512` = 9600, `rc4-sha1` = 9800, `standard` = 9400, etc.). The unified hash format (`-m 37000`) auto-detects the right algorithm.

!!! tip
    Use `opt info secret.xlsx 2>/dev/null` to get hashes only (no gate summary), or `2>&1 >/dev/null` to get the gate summary only (no hash).

## 4. Batch processing

Both `info` and `unlock` accept multiple files and globs. Hash output preserves file order with blank lines as separators, so file-to-hash alignment is maintained.

```console
$ opt info /path/to/office/files/
$ opt unlock *.xlsx --force
```

`--force` overwrites existing output files. Without it, `unlock` refuses if `secret.unlocked.xlsx` already exists.

!!! tip
    In batch mode, `info` pads the filename column to align tags across all files, making the output scannable.

## 5. Python API

The same detection and extraction logic is available as a library:

```python
import office_password_toolkit as opt

result = opt.detect("secret.xlsx")
# result.gates -> [Gate(status="encrypted", scheme="agile-sha512"), ...]

hashes = opt.extract_hashes("secret.xlsx")
# ["$office$*sha512*aes256*cbc*100000*<salt>*<verifier>*<hash>"]
```

`detect()` returns the same `status:scheme` gate list that `opt info` prints. `extract_hashes()` returns the hash lines that would go to stdout.
