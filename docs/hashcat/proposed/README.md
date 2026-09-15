# 6 Modes for Complete Office Coverage

## The problem

hashcat ships 12 Office-related modes, each pinned to one `(hash, cipher, iterations)` tuple. Anything that deviates — non-default spinCount, SHA-256 agile, 56-bit RC4, any protection hash other than SHA-512/100000 — is silently rejected at parse time.

## The solution: `module_kern_type_dynamic`

hashcat already has a mechanism for ONE mode number to dispatch to DIFFERENT compiled GPU kernels per hash at runtime: `module_kern_type_dynamic()`. **LUKS mode 14600** does this today with **15 hash×cipher combinations** (SHA-1/256/512/RIPEMD-160/Whirlpool × AES/Serpent/Twofish) under a single `-m 14600`. The module parser reads the hash/cipher fields from the hash line and returns a different `KERN_TYPE` constant per hash, selecting the correct pre-compiled kernel.

This means one Office module can accept a self-describing hash line, parse the algorithm fields, and dispatch to the right kernel — without the user ever caring about internal mode numbers.

## The 6 modes

```mermaid
flowchart TD
  subgraph M37000["Mode 37000 — MS Office Document Encryption"]
    direction TB
    K11["37011: Agile SHA-1\nSHA-1 spin + AES-CBC verify"]
    K12["37012: Agile SHA-256\nSHA-256 spin + AES verify"]
    K13["37013: Agile SHA-512\nSHA-512 spin + AES verify"]
    K14["37014: Agile SHA-384\nSHA-384 spin + AES verify"]
    K20["37020: Standard\nSHA-1×50k + AES-ECB verify"]
    K30["37030: RC4+MD5\nMD5 + RC4-40 verify"]
    K40["37040: RC4+SHA-1\nSHA-1 + RC4 verify"]
  end

  subgraph M37001["Mode 37001 — Key-Seed Brute Force"]
    direction TB
    KC1["37031: MD5 seed\nMD5(seed||block) → RC4 verify"]
    KC2["37041: SHA-1 seed\nSHA1(seed||block) → RC4 verify"]
  end

  subgraph M37002["Mode 37002 — Password-from-Seed Recovery"]
    direction TB
    KP1["37032: MD5 password\nMD5(pw) → truncate → match seed"]
    KP2["37042: SHA-1 password\nSHA1(salt||pw) → match seed"]
  end

  subgraph M37100["Mode 37100 — MS Office Protection Verifier"]
    direction TB
    P1["37111: ISO SHA-1"]
    P2["37112: ISO SHA-256"]
    P3["37113: ISO SHA-384"]
    P4["37114: ISO SHA-512"]
    P5["37115: ISO MD5"]
    P6["37116: Crypt SHA-1"]
    P7["37117: Crypt SHA-256"]
  end

  subgraph M37200["Mode 37200 — ODF Encryption (PBKDF2)"]
    direction TB
    D1["37211: Blowfish-CFB + SHA-1/1K"]
    D2["37212: AES-256-CBC + SHA-256/1K"]
    D3["37213: AES-256-GCM + tag verify"]
  end

  subgraph M37201["Mode 37201 — ODF Argon2id"]
    direction TB
    A1["37214: Argon2id + AES-256-CBC"]
    A2["37215: Argon2id + AES-256-GCM"]
  end
```

## Coverage comparison

| Axis | Current 12 modes | New 6 modes |
|---|---|---|
| Hash algorithms | 3 (MD5, SHA-1, SHA-512) | All 10 spec-legal |
| Ciphers | 5 (RC4-40/128, AES-128/256, Blowfish) | All 13 spec-legal |
| Spin counts | 4 fixed values (0, 1024, 50000, 100000) | Full range 0–10,000,000 |
| Salt lengths | Fixed 16 B | 1–65,536 B |
| Protection carriers | sheetProtection only (SHA-512/100000) | All 17 carrier elements, any hash/spinCount |
| ODF profiles | 1.1, 1.2 | 1.1, 1.2, 1.3 (GCM + Argon2id) |
| OneNote / Access / Visio | Not covered | Covered (same KDFs) |

## How `module_kern_type_dynamic` works

Precedent: LUKS mode 14600 (`src/modules/module_14600.c`)

```c
// One module, one -m flag, multiple kernels
static u32 module_kern_type_dynamic(const hashconfig_t *hc, const void *digest, const salt_t *salt, ...) {
    luks_t *luks = (luks_t *)esalt;
    // hash_type × cipher_type selects the kernel
    if (luks->hash_type == SHA1   && luks->cipher_type == AES)    return 14611;
    if (luks->hash_type == SHA256 && luks->cipher_type == AES)    return 14621;
    if (luks->hash_type == SHA512 && luks->cipher_type == AES)    return 14631;
    // ... 15 combinations total
}
```

Each `KERN_TYPE` maps to a separate `.cl` kernel file compiled at JIT time. The user sees only `-m 14600`. The parser reads the hash line, sets `esalt->hash_type` and `esalt->cipher_type`, and `module_kern_type_dynamic()` routes to the correct kernel.

**For Office, the same pattern:**

```c
static u32 module_kern_type_dynamic(...) {
    office_t *office = (office_t *)esalt;
    switch (office->scheme) {
        case AGILE_SHA1:    return 37011;
        case AGILE_SHA256:  return 37012;
        case AGILE_SHA512:  return 37013;
        case STANDARD:      return 37020;
        case RC4_MD5:       return 37030;
        case RC4_SHA1:      return 37040;
    }
}
```

## Per-family design docs

| Mode | Format | Design doc |
|---|---|---|
| 37000 | `$office$` | [office_open.md](office_open.md) |
| 37001 | `$office$` (key-seed brute) | [office_open.md](office_open.md) |
| 37002 | `$office$` + `:seed` (password-from-seed) | [office_open.md](office_open.md) |
| 37100 | `$protect$` | [office_protect.md](office_protect.md) |
| 37200 | `$odf$` | [odf_open.md](odf_open.md) |
| 37201 | `$odf$` (Argon2id) | [odf_open.md](odf_open.md) |
| (110) | `$vba$` | [vba_project.md](vba_project.md) |
| — | Not crackable | [not_crackable.md](not_crackable.md) |

## Backward compatibility

Existing mode numbers (9400, 9500, 9600, 9700, 9800, 25300, 18400, 18600) can be retained as **aliases** that auto-map to the corresponding `$office$`/`$protect$`/`$odf$` line internally. Existing hash lines (`$office$*2007*...`, `$oldoffice$3*...`, `$odf$*1*1*...`) continue to parse — the module recognizes both the legacy format and the new self-describing format, sets the same esalt fields, and dispatches to the same kernel.

## What is NOT a hashcat target

XOR obfuscation, 16-bit verifiers, PST CRC-32, cleartext passwords, default passwords (VelvetSweatshop, /01Hannes Ruescher/01), Jet .mdb XOR masks, IRM/RMS, digital signatures, PST body ciphers — all handled by decode/collide/strip tools, never submitted to GPU. See [not_crackable.md](not_crackable.md).
