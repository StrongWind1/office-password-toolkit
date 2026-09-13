# Office Permission Gates — Analysis

Research into every password, protection, and encryption mechanism across Microsoft Office file formats and OpenDocument, built from the Microsoft Open Specifications corpus and community reverse-engineering.

## Layout

```
analysis/
  overview.md                visual map — product × gate matrix, algorithm relationships, detection flowchart
  toolkit-architecture.md    how the analysis maps to the Python office-password-toolkit code

  landscape/                 strategic overview
    spec-corpus.md             44 MS specs — purpose + relevance triage (6 direct, 9 indirect, 29 none)
    prior-art.md               GitHub + web prior-art sweep, gap-resolution table, categorized tools map

  formats/                   per-product gate reference — start here for a specific file
    word.md                    .doc / .docx  (7 gates: open, modify, restrict-editing, VBA, signature, IRM)
    excel.md                   .xls / .xlsx / .xlsb  (8+ gates: open, modify, sheet, workbook, ranges, VBA, sig)
    powerpoint.md              .ppt / .pptx  (4 gates: open, modify, VBA, signature)
    onenote.md                 .one / .onetoc2  (1 gate: section-open — real encryption, no bypass)
    outlook.md                 .pst / .ost  (2 gates: advisory CRC-32 password, keyless body cipher)
    access.md                  .mdb / .accdb  (3 gates: Jet obfuscation, ACE encryption, VBA)
    opendocument.md            .odt / .ods / .odp  (ODF 1.1/1.2/1.3 encryption + body protection)
    visio.md                   .vsd / .vsdx  (open encrypt via MS-OFFCRYPTO, Lock* shape cells, VBA)
    project.md                 .mpp  (open + write passwords — OUT-OF-CORPUS, VBA)
    publisher.md               .pub  (minimal protection — OUT-OF-CORPUS, VBA)
    infopath.md                .xsn  (no file encryption — designMode flag only)

  algorithms/                the reusable crypto primitives (KDF, byte layout, constants, test vectors)
    password/                  password-derived — crackable
      ecma376-agile.md           Office 2010+ document-open (SHA-1/SHA-512 + AES-CBC, modes 9500/9600)
      ecma376-standard.md        Office 2007 document-open (SHA-1 × 50000 + AES-ECB, mode 9400)
      rc4-cryptoapi-sha1.md      Office XP/2003 document-open (SHA-1 + RC4, modes 9800/9810/9820)
      rc4-md5-legacy.md          Office 97/2000 document-open (MD5 + RC4-40, modes 9700/9710/9720)
      xor-obfuscation.md         legacy binary XOR (16/32-bit verifier + reversible byte transform)
      iso-protection-hash.md     OOXML editing/write/sheet/workbook protection (mode 25300 SHA-512 only)
      word2007-documentprotection.md   Word 2007 legacy-derived restrict-editing hash
      odf-encryption.md          ODF 1.1 Blowfish / 1.2 AES / 1.3 Argon2id (modes 18600/18400)
      vba-project-password.md    VBA "lock project for viewing" (DPB obfuscation + SHA-1, reuses mode 110)
      pst-crc32.md               Outlook PST advisory password (CRC-32, not real security)
    non-password/              not password-derived — not crackable by guessing
      irm-rms-encryption.md     IRM / RMS / extensible (certificate-wrapped, PKI — recovery class NONE)
      digital-signatures.md     CryptoAPI / XAdES / PKCS#7 (PKI integrity — strip only)
      pst-body-cipher.md        PST NDB permute/cyclic (keyless obfuscation — decode directly)
      access-jet-obfuscation.md Jet .mdb fixed-key/date-key XOR (instant decode)
      msisam-encryption.md      MSISAM page encryption — Money 2002+ (MD5/SHA-1 + RC4)
      uls-workgroup-security.md Jet ULS workgroup password/identity decode — .mdw (3DES fixed key)

  _research/                 raw OpenSpec documents and search data (source material for later analysis)
```

## The model

- A **file format** (`.docx`, `.xls`, `.pst`) exposes one or more **permission gates** (open password, modify password, protect sheet, restrict editing, VBA project lock). Each `formats/*` doc is the complete standalone reference for that product: the gate table, a per-gate recovery playbook (crack vs bypass/strip/collide/cleartext), and the tools/commands.
- Each gate uses exactly one **algorithm** (in `algorithms/password/` or `algorithms/non-password/`).
- Many named gates share the same algorithm — Protect-Sheet, Protect-Workbook, Restrict-Editing, Allow-Edit-Ranges, and the OOXML modify password are all `iso-protection-hash`. The format docs enumerate the gates; the algorithm docs are the finite, deduped set of primitives.
- [Current hashcat modes](../hashcat/current/README.md) documents existing modes. [Proposed unified modes](../hashcat/proposed/README.md) proposes 6 modes (37000-series).

## Relationship to hashcat/

[Current hashcat modes](../hashcat/current/README.md) documents existing hashcat modes. [Proposed unified modes](../hashcat/proposed/README.md) proposes 6 unified modes using `module_kern_type_dynamic`.
