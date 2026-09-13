# Gap Analysis — Existing Toolkit vs. Design Goals

Compares the current `office-password-toolkit` (~13,600 lines, 33 files) against the complete 62-gate inventory from `../research/`, the recovery techniques in `../recovery/`, and the hashcat designs in `../hashcat/`.

**Related documents:**

- [toolkit-architecture.md](toolkit-architecture.md) — analysis → code mapping with cross-reference tables
- [modular-design.md](modular-design.md) — the complete modular architecture blueprint
- [../hashcat/proposed/README.md](../hashcat/proposed/README.md) — proposed 6-mode hashcat design (37000-series)
- [../recovery/README.md](../recovery/README.md) — non-GPU recovery techniques

## Status Overview

```mermaid
flowchart LR
  subgraph status ["62 gates across 16 product variants"]
    A["✅ 58 fully\nimplemented"]
    B["⚠️ 2 partial\n(stubs)"]
    C["❌ 2 out-of-corpus\n(Project .mpp)"]
  end
```

**Bottom line: the toolkit is production-quality code covering 94% of all gates end-to-end. The "gaps" are minor stubs and out-of-corpus formats, not missing architecture.**

## Gate-by-Gate Coverage

### 🔴 Document-Open Encryption (real ciphertext — must crack or decrypt)

| Gate | Product | Toolkit module | detect | extract | verify | decrypt | Status |
|---|---|---|---|---|---|---|---|
| Agile SHA-1/AES-128 | Word/Excel/PPT .docx/.xlsx/.pptx | `crypto/ecma376.py` + `formats/ole.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| Agile SHA-512/AES-256 | Word/Excel/PPT .docx/.xlsx/.pptx | `crypto/ecma376.py` + `formats/ole.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| Agile (any non-default tuple) | Any OOXML | `crypto/ecma376.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| Standard AES-128/256 | Word/Excel/PPT .docx/.xlsx/.pptx | `crypto/ecma376.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| Standard AES-192 | Any OOXML | `crypto/ecma376.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| RC4 CryptoAPI + SHA-1 | Word/Excel/PPT .doc/.xls/.ppt | `crypto/rc4legacy.py` + `formats/ole.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| RC4 + MD5 (40-bit) | Word/Excel .doc/.xls | `crypto/rc4legacy.py` + `formats/ole.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| OneNote section (agile/standard/CryptoAPI) | OneNote .one | `crypto/ecma376.py` + `formats/onenote.py` | ✅ | ✅ | ✅ | ⚠️ STUB | ⚠️ |
| Visio open (.vsd) | Visio .vsd | Routes through `formats/ole.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| Visio open (.vsdx) | Visio .vsdx | Routes through `formats/ole.py` (encrypted) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Access ACE 2010+ | Access .accdb | `crypto/ecma376.py` + `formats/access.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| Access ACE 2007 (RC4) | Access .accdb | `formats/access.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| ODF 1.1 (Blowfish-CFB) | ODF .odt/.ods/.odp | `crypto/odf.py` + `formats/odf.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| ODF 1.2 (AES-256-CBC) | ODF .odt/.ods/.odp | `crypto/odf.py` + `formats/odf.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| ODF 1.3 (Argon2id/AES-GCM) | ODF .odt/.ods/.odp | `crypto/odf.py` + `formats/odf.py` | ✅ | ✅ | ✅ | ✅ | ✅ |
| Project .mpp open | Project .mpp | ❌ No handler | ❌ | ❌ | ❌ | ❌ | ❌ OUT-OF-CORPUS |

### 🟡 Protection Verifiers (content is plaintext — strip or crack for literal password)

| Gate | Product | Toolkit module | extract | verify | strip | Status |
|---|---|---|---|---|---|---|
| Sheet protection (ISO all primitives) | Excel .xlsx/.xlsb | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Workbook protection (ISO) | Excel .xlsx/.xlsb | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Edit ranges (ISO) | Excel .xlsx/.xlsb | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Write reservation (ISO) | Excel .xlsx/.xlsb | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Revision protection (ISO) | Excel .xlsx/.xlsb | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Document protection ISO | Word .docx | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Document protection Word2007 | Word .docx | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Write protection ISO | Word .docx | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| Modify verifier ISO | PPT .pptx | `crypto/protection.py` + `formats/ooxml.py` | ✅ | ✅ | ✅ | ✅ |
| VBA project lock | All VBA hosts | `crypto/vba.py` | ✅ | ✅ | ✅ | ✅ |

### 🟢 Cleartext / Decode / Collide / Default (instant recovery, no cracking)

| Gate | Product | Toolkit module | Technique | Status |
|---|---|---|---|---|
| VelvetSweatshop default | Excel .xls/.xlsx | `defaults.py` | Try default password | ✅ |
| /01Hannes Ruescher/01 default | PPT .ppt | `defaults.py` | Try default password | ✅ |
| Word .doc write-res (cleartext) | Word .doc | `formats/ole.py` | Read SttbfAssoc[0x11] | ✅ |
| PPT .ppt modify (cleartext) | PPT .ppt | `formats/ole.py` | Read ModifyPasswordAtom | ✅ |
| XOR obfuscation decode | Word/Excel .doc/.xls | `crypto/xor.py` | Known-plaintext array reconstruction | ✅ |
| 16-bit verifier collide | Excel .xls sheet/workbook/write | `crypto/xor.py` | Instant collision (0xCE4B) | ✅ |
| 32-bit verifier collide | Word .doc lKeyProtDoc | `crypto/xor.py` | Instant collision | ✅ |
| PST CRC-32 collide | Outlook .pst | `crypto/pst.py` | Gaussian elimination | ✅ |
| PST CRC-32 strip | Outlook .pst | `formats/outlook.py` | Zero PidTagPstPassword | ✅ |
| PST body cipher decode | Outlook .pst | `crypto/pst.py` | Permute/cyclic (keyless) | ✅ |
| Access Jet 3/4 decode | Access .mdb | `formats/access.py` | Fixed/date-key XOR undo | ✅ |
| VBA DPB wrapper decode | All VBA hosts | `crypto/vba.py` | Seeded XOR decrypt | ✅ |

### ⚪ PKI / Non-Password (not recoverable or strip-only)

| Gate | Product | Toolkit | Status |
|---|---|---|---|
| Digital signatures | All | Strip via bypass() | ✅ |
| IRM/RMS | Word/Excel/PPT | Classified as NONE | ✅ |
| PST WIP/EDP (0x10) | Outlook | Classified as NONE | ✅ |

## Stubs to Complete

| Stub | File | What's needed | Effort |
|---|---|---|---|
| OneNote decrypt() | `formats/onenote.py` | Use the extracted EncryptionInfo + cracked password → call `ecma376.decrypt_agile()` on the object space data. The crypto is already implemented; only the container-level write-back is missing. | Low — ~50-100 lines |
| OneNote bypass() | `formats/onenote.py` | Not meaningful — content is real ciphertext, bypass cannot work. Should remain as `raise` with a clear message. | N/A (by design) |
| Access .mdb bypass() | `formats/access.py` | Write a copy with the password field zeroed in the Jet header. The decode logic already exists. | Low — ~20 lines |

## Missing Handlers

| Product | Why missing | Impact | Recommendation |
|---|---|---|---|
| Visio .vsd/.vsdx | No dedicated VisioHandler | **Low** — .vsd routes through OleHandler (RC4 CryptoAPI), encrypted .vsdx routes through OleHandler (agile EncryptionInfo), plain .vsdx routes through OoxmlHandler (protection XML). All crypto already works. | Add a thin VisioHandler that delegates to OleHandler/OoxmlHandler with Visio-specific gate names (Lock* cells). Or just document the routing. |
| Project .mpp | OUT-OF-CORPUS — proprietary encryption scheme unknown | **Medium** — can't handle .mpp open/write passwords. VBA lock works through OleHandler. | Wait for .mpp RE or community contribution. VBA works today. |
| Publisher .pub | No [MS-PUB] spec, minimal protection | **Low** — .pub is OLE/CFB, VBA lock works through OleHandler. No document-open encryption documented. | Add a thin PublisherHandler that delegates to OleHandler for VBA only. |
| InfoPath .xsn | CAB archive, no file-level encryption | **None** — no password to handle. designMode flag is application-level. | Optional: add InfoPathHandler that reports "no encryption" on info command. |
| .msg (Outlook single message) | OLE/CFB, can carry IRM | **Low** — IRM messages are classified as NONE (need private key/RMS auth). No password-based recovery possible. | Optional: add MsgHandler that detects IRM and reports NONE. |

## Hashcat Hash-Line Emission

### Current support (existing hashcat modes)

| hashcat mode | Hash scheme in toolkit | Emitter | Status |
|---|---|---|---|
| 9400 | `OFFICE_2007` | `crypto/ecma376.py` → `$office$*2007*...` | ✅ |
| 9500 | `OFFICE_2010` | `crypto/ecma376.py` → `$office$*2010*...` | ✅ |
| 9600 | `OFFICE_2013` | `crypto/ecma376.py` → `$office$*2013*...` | ✅ |
| 9700 | `OLDOFFICE_RC4_MD5` | `crypto/rc4legacy.py` → `$oldoffice$0*...` | ✅ |
| 9800 | `OLDOFFICE_RC4_SHA1` | `crypto/rc4legacy.py` → `$oldoffice$3*...` | ✅ |
| 25300 | `OFFICE_SHEETPROT` | `crypto/protection.py` → `$office$2016$0$...` | ✅ |
| 18400 | `ODF` (1.2) | `crypto/odf.py` → `$odf$*1*1*...` | ✅ |
| 18600 | `ODF` (1.1) | `crypto/odf.py` → `$odf$*0*0*...` | ✅ |
| 110 | `VBA_SHA1` | `crypto/vba.py` → `<sha1>:<key>` | ✅ |

### Self-describing unified lines (`--format opt`)

| Format family | Emitter | Status |
|---|---|---|
| `$office$*<hashfunc>*<cipher>*<mode>*<iters>*...` | `crypto/ecma376.py` → `unified_office_line()` | ✅ |
| `$protect$*<hashfunc>*<kdf>*<iters>*...` | `crypto/protection.py` → `unified_protect_line()` | ✅ |
| `$odf$*<startkey>*<kdf>*<cipher>*<iters>*...` | `crypto/odf.py` → `unified_odf_line()` | ✅ |
| `$vba$*<hashfunc>*<hash>*<salt>` | `crypto/vba.py` → `unified_vba_line()` | ✅ |

### New hashcat modes (from `hash_analysis/new_hashcat/`)

The toolkit already emits the self-describing unified lines that map to the proposed modes. When the new modes (37000/37001/37002/37100/37200/37201) are built in hashcat, the toolkit needs:

| Task | Effort | Details |
|---|---|---|
| Map unified lines → new mode numbers | Low | Add `hashcat_mode` mappings in `models.py` for `OFFICE_AGILE` → 37000, `OFFICE_PROTECT` → 37100, etc. |
| Emit new `$office$` format as default | Low | Change `extract --format hashcat` default emitter from legacy `$office$*2013*` to new `$office$*sha512*aes256*cbc*...` |
| Backward compatibility | None needed | Keep legacy emitters as `--format hashcat-legacy` option |

## Fast Recovery Coverage

Every technique in `fast_recovery/` is already implemented in the toolkit:

| Technique | fast_recovery/ doc | Toolkit implementation |
|---|---|---|
| Default passwords | `defaults.md` | `defaults.py` — VelvetSweatshop + /01Hannes Ruescher/01, auto-tried by `unlock` |
| Cleartext reading | `cleartext.md` | `formats/ole.py` — SttbfAssoc[0x11], ModifyPasswordAtom |
| XOR/Jet/PST decode | `decode.md` | `crypto/xor.py`, `crypto/pst.py`, `formats/access.py` |
| Protection stripping | `strip.md` | `formats/ooxml.py` bypass(), `formats/odf.py` bypass() |
| 16/32-bit collision | `collide.md` | `crypto/xor.py`, `crypto/pst.py` (Gaussian CRC-32) |
| VBA bypass | `bypass.md` | `crypto/vba.py` — DPB rewrite, unprotected triple |

## Summary Scorecard

```mermaid
flowchart TD
  subgraph score ["Toolkit Scorecard"]
    direction TB
    S1["🔴 Document-Open Encryption\n15/16 ✅ · 1 ⚠️ OneNote decrypt · 1 ❌ Project .mpp"]
    S2["🟡 Protection Verifiers\n10/10 ✅"]
    S3["🟢 Fast Recovery\n12/12 ✅"]
    S4["⚪ PKI / Non-Password\n3/3 ✅"]
    S5["📤 Hashcat Emission\n9/9 current modes ✅\n4/4 unified formats ✅"]
  end
```

| Category | Covered | Partial | Missing | Score |
|---|---|---|---|---|
| 🔴 Document-open encryption | 15 | 1 (OneNote decrypt stub) | 1 (Project .mpp) | 94% |
| 🟡 Protection verifiers | 10 | 0 | 0 | 100% |
| 🟢 Fast recovery | 12 | 0 | 0 | 100% |
| ⚪ PKI / non-password | 3 | 0 | 0 | 100% |
| 📤 Current hashcat emission | 9 | 0 | 0 | 100% |
| 📤 Unified format emission | 4 | 0 | 0 | 100% |
| **Total** | **53** | **1** | **1** | **96%** |
