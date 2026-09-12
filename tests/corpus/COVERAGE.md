# Corpus coverage — hashcat modules + spec-surface gap analysis

Every file in the first-party corpus (4561 files, 0 errors) bucketed against the full spec surface (`[MS-OFFCRYPTO]` / `[MS-*]` / OASIS) and the hashcat-module set from `docs/reference/hashcat-modes.md`. Regenerate with `regen_corpus_docs.py`.

## Part 1 — hashcat module coverage (700xx / 710xx / 720xx / 730xx / 790xx)

### Document-open modules (700xx)

| Module | Name | Corpus |
|---|---|---|
| 70000 | office-open/sha1/aes/ecb (standard) | covered |
| 70010 | office-open/sha1/aes/cbc-cfb (agile) | covered |
| 70011 | office-open/sha256/aes/cbc-cfb (agile) | covered |
| 70012 | office-open/sha384/aes/cbc-cfb (agile) | covered |
| 70013 | office-open/sha512/aes/cbc-cfb (agile) | covered |
| 70014 | office-open/md5/aes/cbc-cfb (agile) | covered |
| 70015 | office-open/md4/aes/cbc-cfb (agile) | covered |
| 70016 | office-open/md2/aes/cbc-cfb (agile) | covered |
| 70017 | office-open/ripemd128/aes/cbc-cfb (agile) | **GAP** |
| 70018 | office-open/ripemd160/aes/cbc-cfb (agile) | **GAP** |
| 70019 | office-open/whirlpool/aes/cbc-cfb (agile) | **GAP** |
| 70020 | office-open/sha1/rc2/cbc-cfb (agile) | covered |
| 70021 | office-open/sha256/rc2/cbc-cfb (agile) | covered |
| 70022 | office-open/sha384/rc2/cbc-cfb (agile) | covered |
| 70023 | office-open/sha512/rc2/cbc-cfb (agile) | covered |
| 70024 | office-open/md5/rc2/cbc-cfb (agile) | covered |
| 70025 | office-open/md4/rc2/cbc-cfb (agile) | **GAP** |
| 70026 | office-open/md2/rc2/cbc-cfb (agile) | **GAP** |
| 70027 | office-open/ripemd128/rc2/cbc-cfb (agile) | **GAP** |
| 70028 | office-open/ripemd160/rc2/cbc-cfb (agile) | **GAP** |
| 70029 | office-open/whirlpool/rc2/cbc-cfb (agile) | **GAP** |
| 70030 | office-open/sha1/des/cbc-cfb (agile) | covered |
| 70031 | office-open/sha256/des/cbc-cfb (agile) | covered |
| 70032 | office-open/sha384/des/cbc-cfb (agile) | covered |
| 70033 | office-open/sha512/des/cbc-cfb (agile) | covered |
| 70034 | office-open/md5/des/cbc-cfb (agile) | covered |
| 70035 | office-open/md4/des/cbc-cfb (agile) | **GAP** |
| 70036 | office-open/md2/des/cbc-cfb (agile) | **GAP** |
| 70037 | office-open/ripemd128/des/cbc-cfb (agile) | **GAP** |
| 70038 | office-open/ripemd160/des/cbc-cfb (agile) | **GAP** |
| 70039 | office-open/whirlpool/des/cbc-cfb (agile) | **GAP** |
| 70040 | office-open/sha1/desx/cbc-cfb (agile) | covered |
| 70041 | office-open/sha256/desx/cbc-cfb (agile) | covered |
| 70042 | office-open/sha384/desx/cbc-cfb (agile) | covered |
| 70043 | office-open/sha512/desx/cbc-cfb (agile) | covered |
| 70044 | office-open/md5/desx/cbc-cfb (agile) | covered |
| 70045 | office-open/md4/desx/cbc-cfb (agile) | **GAP** |
| 70046 | office-open/md2/desx/cbc-cfb (agile) | **GAP** |
| 70047 | office-open/ripemd128/desx/cbc-cfb (agile) | **GAP** |
| 70048 | office-open/ripemd160/desx/cbc-cfb (agile) | **GAP** |
| 70049 | office-open/whirlpool/desx/cbc-cfb (agile) | **GAP** |
| 70050 | office-open/sha1/3des/cbc-cfb (agile) | covered |
| 70051 | office-open/sha256/3des/cbc-cfb (agile) | covered |
| 70052 | office-open/sha384/3des/cbc-cfb (agile) | covered |
| 70053 | office-open/sha512/3des/cbc-cfb (agile) | covered |
| 70054 | office-open/md5/3des/cbc-cfb (agile) | covered |
| 70055 | office-open/md4/3des/cbc-cfb (agile) | **GAP** |
| 70056 | office-open/md2/3des/cbc-cfb (agile) | **GAP** |
| 70057 | office-open/ripemd128/3des/cbc-cfb (agile) | **GAP** |
| 70058 | office-open/ripemd160/3des/cbc-cfb (agile) | **GAP** |
| 70059 | office-open/whirlpool/3des/cbc-cfb (agile) | **GAP** |
| 70060 | office-open/md5/rc4 | covered |
| 70061 | office-open/sha1/rc4 | covered |

### Protection modules (710xx)

| Module | Name | Corpus |
|---|---|---|
| 71000 | office-protect/sha1/iso | covered |
| 71001 | office-protect/sha256/iso | **GAP** |
| 71002 | office-protect/sha384/iso | **GAP** |
| 71003 | office-protect/sha512/iso | covered |
| 71004 | office-protect/md5/iso | covered |
| 71005 | office-protect/md4/iso | covered |
| 71006 | office-protect/md2/iso | **GAP** |
| 71007 | office-protect/ripemd128/iso | **GAP** |
| 71008 | office-protect/ripemd160/iso | **GAP** |
| 71009 | office-protect/whirlpool/iso | **GAP** |
| 71010 | office-protect/sha1/word2007 | **GAP** |
| 71011 | office-protect/sha256/word2007 | **GAP** |
| 71012 | office-protect/sha384/word2007 | **GAP** |
| 71013 | office-protect/sha512/word2007 | **GAP** |
| 71014 | office-protect/md5/word2007 | **GAP** |

### OpenDocument (720xx), VBA (730xx), keyspace (790xx)

| Module | Name | Corpus |
|---|---|---|
| 72000 | odf/sha1/pbkdf2/blowfish (1.1) | covered |
| 72001 | odf/sha256/pbkdf2/aes (1.2) | covered |
| 72002 | odf/sha256/argon2/aes-gcm (1.3) | covered |
| 73000 | vba/sha1 | covered |
| 79000 | office-open/md5/rc4/keyspace | covered |
| 79001 | office-open/sha1/rc4/keyspace | covered |
| 79010 | office-open/md5/rc4/password-from-key | covered |
| 79011 | office-open/sha1/rc4/password-from-key | covered |

## Part 2 — spec-surface coverage

### Containers

| ContainerKind | files | status | spec |
|---|---|---|---|
| `ole-cfb` | 4096 | covered (4096) | [MS-CFB] |
| `ooxml-zip` | 420 | covered (420) | OPC/ZIP |
| `odf-zip` | 26 | covered (26) | OASIS Part 3 §3.4 |
| `onenote` | 3 | covered (3) | [MS-ONESTORE] §2.5.19 |
| `pst` | 11 | covered (11) | [MS-PST] |
| `access` | 5 | covered (5) | Jet/ACE (community RE) |

### Document-open schemes

| Scheme | detail | files | status | spec |
|---|---|---|---|---|
| ECMA-376 standard | sha1/aes128/ecb/50000 (Office ignores key-size request — always AES-128) | 50 | covered (50) | [MS-OFFCRYPTO] §2.3.4.5-9 |
| ECMA-376 agile 2010 default | sha1/aes128/cbc/100000 | 108 | covered (108) | [MS-OFFCRYPTO] §2.3.4.10-13 |
| ECMA-376 agile 2013+ default | sha512/aes256/cbc/100000 | 110 | covered (110) | [MS-OFFCRYPTO] §2.3.4.10-13 |
| ECMA-376 agile non-default tuples | CNG sweep: sha1-512/md5 x aes/3des/des/desx/rc2 x cbc/cfb | 3663 | covered (3663) | [MS-OFFCRYPTO] §2.3.4.10 |
| RC4 + MD5 (97/2000) | md5/rc4-40/stream | 19 | covered (19) | [MS-OFFCRYPTO] §2.3.6 |
| RC4 SHA-1/RC4 (XP/2003) | sha1/rc4/stream | 109 | covered (109) | [MS-OFFCRYPTO] §2.3.5 |
|   ↳ RC4 key length 40-bit | | 60 | covered (60) | |
|   ↳ RC4 key length 48-bit | | 3 | covered (3) | |
|   ↳ RC4 key length 56-bit | | 28 | covered (28) | |
|   ↳ RC4 key length 128-bit | | 40 | covered (40) | |
| XOR obfuscation | 16-bit (Excel) / 32-bit (Word) | 3 | covered (3) | [MS-OFFCRYPTO] §2.3.7 |
| ODF 1.1-blowfish | | 24 hash lines from 24 files | covered (24) | OASIS (18600) |
| ODF 1.2-aes | | 32 hash lines from 32 files | covered (32) | OASIS (18400) |
| ODF 1.3-argon2 | | 13 files | covered (13) | tdf#105844 (no mode) |
| OneNote agile sha512 (`.one`) | sha512/aes256 → 9600 | 2 | covered (2) | [MS-ONESTORE] §2.5.19 |
| OneNote agile sha1 (`.one`) | sha1/aes128 → 9500 | 1 | covered (1) | [MS-ONESTORE] §2.5.19 |
| OneNote standard (`.one`) | sha1/aes128/ecb → 9400 | 0 | covered (synthetic) | [MS-ONESTORE] §2.5.19 |
| OneNote RC4 CryptoAPI (`.one`) | sha1/rc4 → 9800 | 0 | covered (synthetic) | [MS-ONESTORE] §2.5.19 |

### Editing/permission protection (`$protect$` / `$doc-protect$`)

| Dialect / hashfunc | files | status | spec |
|---|---|---|---|
| ISO / sha1 | 47 | covered (47) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / sha256 | 0 | **GAP** (0) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / sha384 | 0 | **GAP** (0) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / sha512 | 128 | covered (128) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / md5 | 7 | covered (7) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / md4 | 48 | covered (48) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / md2 | 0 | **GAP** (0) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / ripemd128 | 0 | **GAP** (0) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / ripemd160 | 0 | **GAP** (0) | [MS-OFFCRYPTO] §2.4.2.4 |
| ISO / whirlpool | 0 | **GAP** (0) | [MS-OFFCRYPTO] §2.4.2.4 |
| word2007 / sha1 | 0 | **GAP** (0) | [MS-OE376] §2.1.410 |
| word2007 / sha256 | 0 | **GAP** (0) | [MS-OE376] §2.1.410 |
| word2007 / sha384 | 0 | **GAP** (0) | [MS-OE376] §2.1.410 |
| word2007 / sha512 | 0 | **GAP** (0) | [MS-OE376] §2.1.410 |
| word2007 / md5 | 0 | **GAP** (0) | [MS-OE376] §2.1.410 |

### Legacy fast verifiers (COLLIDE / DECODE / READ)

| Verifier | tier | files | status | spec |
|---|---|---|---|---|
| .xls sheet 16-bit | COLLIDE | 0 | 0 (0) | [MS-XLS] Password 0x13 |
| .xls workbook 16-bit | COLLIDE | 2 | covered (2) | [MS-XLS] |
| .xls range 16-bit | COLLIDE | 0 | 0 (0) | [MS-XLS] |
| .xls file-sharing 16-bit | COLLIDE | 22 | covered (22) | [MS-XLS] FileSharing 0x5B |
| .doc restrict-edit 32-bit | COLLIDE | 12 | covered (12) | [MS-DOC] Dop.lKeyProtDoc |
| XOR open verifier | COLLIDE | 3 | covered (3) | [MS-OFFCRYPTO] §2.3.7 |
| Access Jet 3/4 | DECODE | 2 | covered (2) | community RE |
| PST body cipher | DECODE | 11 | covered (11) | [MS-PST] §5.1/5.2 |
| .doc/.ppt cleartext modify | READ | 3 | covered (3) | [MS-OFFCRYPTO] §4.1.4 |

### VBA, defaults, no-secret

- **VBA project lock** (`$vba$` sha1 → 110): covered (2)
- **Default passwords** ([MS-OFFCRYPTO] §2.4.2.3):
    - `VelvetSweatshop`: covered (1)
    - `/01Hannes Ruescher/01`: covered (1)

## Part 3 — rollups

| HashScheme | files |
|---|---|
| `office-agile` | 3663 |
| `protect-iso-sha512` | 128 |
| `office-2013` | 110 |
| `oldoffice-rc4-sha1` | 109 |
| `office-2010` | 108 |
| `office-2007` | 50 |
| `protect-iso-md4` | 48 |
| `protect-iso-sha1` | 47 |
| `odf-1.2-aes` | 32 |
| `odf-1.1-blowfish` | 24 |
| `oldoffice-rc4-md5` | 19 |
| `odf-1.3-argon2` | 13 |
| `protect-iso-md5` | 7 |
| `vba-sha1` | 2 |

| hashcat mode | files |
|---|---|
| None | 3731 |
| 25300 | 175 |
| 9600 | 110 |
| 9800 | 109 |
| 9500 | 108 |
| 9400 | 50 |
| 18400 | 32 |
| 18600 | 24 |
| 9700 | 19 |
| 110 | 2 |

| GateType | files |
|---|---|
| `open` | 4097 |
| `protect-sheet` | 251 |
| `gates` | 60 |
| `restrict-edit` | 49 |
| `protect-workbook` | 45 |
| `allow-edit-ranges` | 45 |
| `modify` | 40 |
| `mail-body` | 11 |
| `signature` | 6 |
| `shared-revisions` | 5 |
| `vba-project` | 2 |
| `section` | 1 |

| RecoveryClass | gate occurrences |
|---|---|
| `crack` | 3990 |
| `strip` | 423 |
| `keyspace` | 68 |
| `none` | 66 |
| `default` | 26 |
| `collide` | 19 |
| `decode` | 17 |
| `read` | 3 |

## Part 4 — gap summary

**A. Real & producible — worth closing:**
- None — all producible gaps closed.

**B. Real but no shipping producer (out of scope for real-producer-only corpus):**
- ECMA-376 **standard AES-192/256** — Office always writes AES-128 in standard mode (verified on wire).
- **Exotic ISO protection hashes** (sha256/384/md5/md4/md2/ripemd/whirlpool) — Office writes only SHA-1 + SHA-512.
- **Exotic word2007 hashes** (sha256/384/512/md5) — Office writes SHA-1.
- **Exotic agile open cells** — full matrix in Part 1 (ripemd128/ripemd160/whirlpool x all ciphers; md4/md2 x non-AES; sha1/rc2).

**C. Unproducible (platform-impossible):**
- RIPEMD128, RIPEMD160, Whirlpool — NOT available as CNG algorithms on ANY Windows version. The hashcat modules 700xx that use these (indices 17-19, 25-29, 35-39, 45-49, 55-59) are spec-legal but platform-impossible. No files can be produced for them.

**D. Label artifacts (not real gaps):**
- RecoveryClass `decrypt`/`bypass`/`none` show 0: static enumeration reports the cheapest action; these are runtime actions.
- Some `.xls` 16-bit verifiers appear under STRIP (preferred action) rather than COLLIDE.

