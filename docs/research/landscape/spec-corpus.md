# Specification Corpus — Triage & Relevance Map

This document triages every Microsoft Open Specification in the `../_research/openspec_md_files/` corpus for relevance to cracking passwords out of Office documents at rest. It is the map that drives the algorithm specs in `../algorithms/`, the per-product tables in `../formats/`, and the hashcat design in `../../hash_analysis/new_hashcat/`.

**Corpus:** 424 specifications across 8 categories, converted from PDF to Markdown with **pymupdf4llm** (chosen over markitdown/docling/pdftotext because it was the only converter that preserved the encryption data-tables as real Markdown while staying fast enough for the ~17,000-page corpus on CPU).

| Category | Specs | Contents |
|---|---|---|
| `OfficeFileFormatsProtocols` | 24 | Binary + shared + crypto formats (`.doc`, `.xls`, `.ppt`, `.pst`, `.one`, VBA, **`[MS-OFFCRYPTO]`**) |
| `MSOFFSTAND` | 20 | OOXML + ODF standards support (ECMA-376, ISO 29500, ODF conformance) |
| `OfficeProto` | 74 | Office communications protocols (Lync / Skype / Groove / SIP / RTP) |
| `Exchange_Protocols` | 129 | Exchange Server + ActiveSync (MAPI, EWS, transport, calendar, contacts) |
| `Exchange_Standards` | 6 | IMAP / POP3 / iCalendar conformance notes |
| `SharePointProtocols` | 168 | SharePoint admin, search, forms, workflow, content databases, SSO |
| `Windows_Wordpad_Standards_Support` | 2 | WordPad ODF + ECMA-376 conformance |
| `other` | 1 | `[MS-VBAL]` VBA Language specification |

**Headline finding:** of 424 specs, exactly **15 define or carry password/encryption material** relevant to document-at-rest password recovery. The remaining 409 are communications protocols, server-side admin, email transport, drawing/chart/UI formats, or conformance notes that say "not supported." The expanded corpus (Exchange, SharePoint, WordPad, Exchange Standards) added **zero** new DIRECT or indirect specs — every crypto-term hit in the grep sweep was authentication in transit, "not supported" disclaimers, or a cross-reference to `[MS-OFFCRYPTO]`.

**Relevance ratings:**

- **DIRECT** — the document itself defines a password / encryption / hash / verifier algorithm or its on-disk wire structure. These are the primary sources for building a cracker.
- **indirect** — the document defines a container / binary / OOXML format that *holds* encrypted streams, but the encryption itself is defined elsewhere (usually `[MS-OFFCRYPTO]`).
- **context** — referenced by DIRECT/indirect specs but defines no algorithm and carries no encrypted data. Useful for cross-referencing, not for implementation.
- **none** — unrelated to document-at-rest password cracking.

**Tally:** 6 DIRECT · 9 indirect · ~10 context · ~399 none · 424 total.

## The 15 that matter

### DIRECT — defines password/encryption algorithms (6 specs)

| Spec | Source | Crypto sections | What it defines |
|---|---|---|---|
| `[MS-OFFCRYPTO]` | OfficeFileFormatsProtocols | §2.3.4–§2.3.7, §2.4, §2.5 | **The primary source.** Every password-based encryption scheme Office uses: agile (SHA-512/AES-256), standard (SHA-1/AES), RC4 CryptoAPI (SHA-1/RC4), legacy RC4 (MD5/RC4-40), XOR obfuscation, ISO write-protection hash, IRM/RMS data spaces, digital signatures. All KDFs, verifiers, wire structures, and constants. |
| `[MS-OVBA]` | OfficeFileFormatsProtocols | §2.3.1.15–.17, §2.4.3–.4 | VBA project password: DPB/CMG/GC obfuscation wrapper (seeded XOR, §2.4.3), SHA-1(password‖Key) verifier (§2.4.4.4), plaintext-password path, Encode/Decode Nulls. |
| `[MS-PST]` | OfficeFileFormatsProtocols | §2.4.3.3, §4.1–4.2, §5.1–5.3 | PST password (CRC-32 in `PidTagPstPassword`), NDB block ciphers (permutative/cyclic, keyless), CRC algorithm. Self-contained — does not use `[MS-OFFCRYPTO]`. |
| `[MS-OE376]` | MSOFFSTAND | §2.1.410, §2.1.438, §2.1.621, §2.1.681–.682 | OOXML protection password hash that ECMA-376 left unspecified: H(password,salt) + cryptSpinCount iterations, the ISO/Agile verifier wire structure (algorithmName, hashValue, saltValue, spinCount) for documentProtection, writeProtection, workbookProtection, sheetProtection. |
| `[MS-OI29500]` | MSOFFSTAND | §2.1.402, §2.1.426, §2.1.573, §2.1.586, §2.1.643, §2.1.653–.654, §2.1.1104 | ISO/IEC 29500 protection verifier: full iterated-hash algorithm H_init=H(salt,password) + spinCount cycles for documentProtection, writeProtection, fileSharing, workbookProtection, sheetProtection, protectedRange, modifyVerifier. |
| `[MS-XLSX]` | MSOFFSTAND | §2.4.10, §2.6.55–.56, §4.1–4.2 | CT_ProtectedRange wire structure: legacy 16-bit XOR verifier + modern algorithmName/hashValue/saltValue/spinCount attributes. Delegates algorithms to `[MS-OFFCRYPTO]`. |

### indirect — containers holding encrypted data (9 specs)

| Spec | Source | Why indirect |
|---|---|---|
| `[MS-DOC]` | OfficeFileFormatsProtocols | Binary `.doc` container: three password-to-open mechanisms (XOR, RC4-MD5, RC4-CryptoAPI) via `FibBase.fEncrypted`/`fObfuscated`, EncryptionHeader in Table stream, `SttbfAssoc` cleartext write-reservation, `Dop.lKeyProtDoc` protection verifier. Algorithms in `[MS-OFFCRYPTO]`. |
| `[MS-PPT]` | OfficeFileFormatsProtocols | Binary `.ppt` container: `CryptSession10Container` carries RC4 CryptoAPI encryption. Cleartext modify password in `ModifyPasswordAtom`. Algorithms in `[MS-OFFCRYPTO]`. |
| `[MS-XLS]` | OfficeFileFormatsProtocols | Binary `.xls` container: `FilePass` record selects encryption method, `Password` record (16-bit sheet/workbook), `FileSharing` (write-reservation), `Prot4RevPass` (revisions). VelvetSweatshop default password. Algorithms in `[MS-OFFCRYPTO]`. |
| `[MS-XLSB]` | OfficeFileFormatsProtocols | Binary `.xlsb` container: `BrtSheetProtectionIso`, `BrtBookProtectionIso`, `BrtFileSharingIso` records carry the same ISO protection hash. Algorithms in `[MS-OFFCRYPTO]`. |
| `[MS-XLDM]` | OfficeFileFormatsProtocols | PowerPivot data model: not itself encrypted (`EncryptionFlag` MUST be false), but defines `CryptKey.bin` whose key may come from `[MS-OFFCRYPTO]`. |
| `[MS-ONESTORE]` | OfficeFileFormatsProtocols | OneNote revision store: `ObjectDataEncryptionKeyV2FNDX` (§2.5.19) marks encrypted object spaces. The blob interior is an `[MS-OFFCRYPTO]` `EncryptionInfo` (agile/standard/CryptoAPI). |
| `[MS-OSHARED]` | OfficeFileFormatsProtocols | Shared structures: `DigSigBlob`/`WordSigBlob`/`DigSigInfoSerialized` (§2.3.2) for digital signatures. Defines the container the signature lives in. |
| `[MS-OFFMACRO2]` | MSOFFSTAND | OOXML macro-enabled formats (.docm/.xlsm/.pptm): the OPC package that gets wrapped by `[MS-OFFCRYPTO]` when encrypted. Defines no encryption itself. |
| `[MS-OODF14]` | MSOFFSTAND | ODF 1.4 conformance: enumerates ODF manifest encryption elements (manifest:encrypted-key, encryption-method, keyinfo, CipherData). Records that Office does not implement ODF encryption. |

## Context-only specs (~10 specs)

Referenced by the DIRECT/indirect specs but define no algorithm and carry no encrypted data.

| Spec | Source | Role |
|---|---|---|
| `[MS-OODF]` | MSOFFSTAND | ODF 1.1 conformance: references ODF encryption sections (17.3, 17.7.4–6) only to record that Office 2007 does not implement them. |
| `[MS-OODF2]` | MSOFFSTAND | ODF 1.1 v2 conformance matrix. Says "not supported" per feature. |
| `[MS-OODF3]` | MSOFFSTAND | ODF 1.1 v2 conformance for Office 2013+. |
| `[MS-OODF13]` | MSOFFSTAND | ODF 1.3 conformance: references Argon2id/AES-GCM encryption elements but confirms "not supported in Word/Excel/PowerPoint." No algorithm detail beyond `[MS-OODF14]`. |
| `[MS-ONE]` | OfficeFileFormatsProtocols | OneNote content model (pages, outlines, properties). The encryption container is `[MS-ONESTORE]`, not here. |
| `[MS-OFFDI]` | OfficeFileFormatsProtocols | Format roadmap: enumerates persistence formats across Office versions. No crypto. |
| `[MS-OFFMACRO]` | MSOFFSTAND | Original macro-enabled format delta. References VBA project storage but defines no encryption. |
| `[MS-OFORMS]` | OfficeFileFormatsProtocols | Office Forms (ActiveX controls). Contains VBA project references but no password/encryption. |
| `[MS-DOCX]` | MSOFFSTAND | Word OOXML extensions. Encryption lives in `[MS-OFFCRYPTO]`, not here. |
| `[MS-PPTX]` | MSOFFSTAND | PowerPoint OOXML extensions. No encryption. |

## Bulk triage — categories with zero crypto relevance

### OfficeProto/ — 74 specs, all out of scope

Real-time communications, presence, conferencing, transport, NAT-traversal, and telephony protocols for Lync / Skype for Business / Groove / SharePoint Workspace. None define encryption of an Office document at rest. Several contain cryptography (`[MS-SRTP]`, `[MS-SSRTP]` encrypt live RTP media; `[MS-GRVSSTPS]`, `[MS-SIPAE]`, `[MS-OCAUTHWS]` perform session/transport authentication), but all are wire/session credentials in transit — not password-derived document-file encryption at rest.

### Exchange_Protocols/ — 129 specs, all out of scope

Exchange Server and ActiveSync protocols: MAPI/RPC, EWS, ActiveSync commands, address book, calendar, contacts, message objects, transport rules. Crypto-term hits are all authentication-in-transit (`[MS-XLOGIN]` SMTP AUTH, `[MS-OXWSLVID]` LiveID/OAuth tokens, `[MS-ASPROV]` mobile device password policies) or email-message-level encryption (`[MS-OXOSMIME]` S/MIME CMS, `[MS-OXORMMS]` Rights-Managed Email, `[MS-ASRM]` ActiveSync IRM policy). None define password protection of an Office document file at rest.

### SharePointProtocols/ — 168 specs, all out of scope

SharePoint Server admin, site management, search, forms, workflow, content databases, file sync, user profiles, SSO, and web services. Crypto-term hits are server-side (`[MS-WSSO]` Single Sign-On credential storage, `[MS-IPFF2]` InfoPath form schema metadata, `[MS-WSSFO*]` content database IRM flags). None define document-at-rest password/encryption algorithms.

### Exchange_Standards/ — 6 specs, all out of scope

Standards conformance notes for IMAP (`[MS-STANOIMAP]`, `[MS-STANXIMAP]`), POP3 (`[MS-STANOPOP3]`, `[MS-STANXPOP3]`), and iCalendar (`[MS-STANOICAL]`, `[MS-STANXICAL]`). Crypto references are transport-layer (STARTTLS, SASL authentication).

### Windows_Wordpad_Standards_Support/ — 2 specs, all out of scope

`[MS-WPODF]` (WordPad ODF) references ODF encryption manifest elements only to state "not supported" 449 times. `[MS-WPE376]` (WordPad ECMA-376) has zero crypto references.

### other/ — 1 spec, out of scope

`[MS-VBAL]` (VBA Language specification) defines the VBA language syntax and runtime. No password, encryption, or hash content — the VBA *project password* is in `[MS-OVBA]`, not here.

## Remaining none-relevance specs in the core categories

### OfficeFileFormatsProtocols (12 of 24 are none)

| Spec | One-line purpose |
|---|---|
| `[MS-3DMDTP]` | 3-D Map Data Tour (Power Map). |
| `[MS-CTDOC]` | Word custom toolbar data. |
| `[MS-CTXLS]` | Excel custom toolbar data. |
| `[MS-DSEXPORT]` | Document Set Package export from SharePoint. |
| `[MS-ODCFF]` | Office Data Connection file format. |
| `[MS-ODRAW]` | OfficeArt binary drawing format. |
| `[MS-OGRAPH]` | Office Graph binary chart format. |
| `[MS-OWEMXML]` | Office Add-ins manifest XML. |
| `[MS-QDEFF]` | Excel .dqy/.iqy query definition files. |
| `[MS-QDEIF]` | Power Query definition transport format. |
| `[MS-WORDLFF]` | Co-authoring lock structure. |

### MSOFFSTAND (6 of 20 are none)

| Spec | One-line purpose |
|---|---|
| `[MS-CUSTOMUI]` | Custom UI XML (Ribbon). |
| `[MS-CUSTOMUI2]` | Custom UI XML Version 2. |
| `[MS-ODRAWXML]` | DrawingML OOXML extensions. |
| `[MS-OEXTXML]` | Extension list complex types. |
| `[MS-OINTXML]` | Observation/suggestion data extensions. |
| `[MS-OREACTXML]` | Comment reaction extensions. |
| `[MS-OTASKXML]` | Document task extensions. |
| `[MS-OWEXML]` | Office Add-in (web extension) structures. |
