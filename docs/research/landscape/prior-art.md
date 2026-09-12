# Related Work — Tools, Prior Art & Gap Resolution

Method: the distinctive fingerprints in the format/algorithm docs (structure names like `ObjectDataEncryptionKeyV2FNDX`, constants like `VelvetSweatshop`, hash tags like `$oldoffice$`) were used as `gh search code` seeds to find the repos, reverse-engineering, and research touching each mechanism; the top hits were deep-dived (README + implicated source) and a parallel web pass covered papers, blog RE writeups, and hashcat/JtR issues. Raw search data: `../_research/gh_search_raw.txt`; deep-dive returns: `../_research/deepdive_journal.jsonl`.

**Headline: four of the six UNCONFIRMED gaps are now RESOLVED**, largely by finding that existing tools already handle them (OneNote, VBA) or by pinning the exact parameters from primary source (ODF 1.3, Access `.accdb`).

## 1. Gap resolution table

| Gap | Prior status | Now | Key finding | Source |
|---|---|---|---|---|
| **OneNote (G5)** | "no extractor; needs RE of opaque blob" | **RESOLVED** | Password-protected OneNote 2013+ is **verbatim ECMA-376 agile**, and **`office2john.py` already extracts it** (a built-in "OneNote >= 2013 hack") → crack with **hashcat 9600**. No custom module or RE needed. | `openwall/john` `run/office2john.py:683-691` (verified); OneNote web RE |
| **Access `.accdb` (out-of-corpus)** | "UNCONFIRMED agile-style" | **RESOLVED** | Access **2010+** = agile **SHA-512 + AES-256-CBC**, spinCount 100000, salt 16, **per-4096-byte-page** CBC with `blockKey = encodingKey XOR pageNumber`; header page 0 is plaintext and carries the XML EncryptionInfo. Same verifier block-keys as Office agile. Access **2007** = SHA-1 + RC4 CryptoAPI. | Jackcess RE; ACE web research |
| **ODF 1.3 Argon2/GCM (G6)** | "URIs/params UNCONFIRMED" | **RESOLVED** | LibreOffice "Wholesome Encryption" (tdf#105844, default since **LO 24.8**, ODF 1.5). KDF URN `urn:org:documentfoundation:names:experimental:office:manifest:argon2id`; params `loext:argon2-iterations=3`, `loext:argon2-memory=65536` (KiB), `loext:argon2-lanes=4`; cipher `http://www.w3.org/2009/xmlenc11#aes256-gcm`; start-key **SHA-256** `http://www.w3.org/2001/04/xmlenc#sha256` (Argon2 input = SHA256(pw), 32 B). | LibreOffice core.git; OASIS |
| **VBA DPB (D3)** | "extractor missing" | **RESOLVED** | Extractor **exists**: Didier Stevens' `oledump.py` plugin **`plugin_vbaproject.py`** decodes the DPB obfuscation and emits the `SHA1(MBCS(pw)+4-byte-salt)` hash for cracking (→ `-m 110`). | oledump / SANS ISC 26390 |
| **Generalized agile (G1) + protection (G3)** | "no reference impl" | **CONFIRMED feasible** | `apache/poi` implements the full generalized agile verifier (`AgileDecryptor`, arbitrary hash/cipher/keyBits/spin) **and** the ISO §2.4.2.4 protection hash (`XSSFPasswordHelper`, `iteratorFirst=false`). Both are the authoritative port targets. Still no GPU kernel in either tool. | `apache/poi`; `ExcelDataReader` |
| **RC4 56-bit (G4)** | "typ 5 unread" | **CLARIFIED** | hashcat 9700/9800 crack old-Office RC4 **by password regardless of key length**; the 40-bit limit is only on the **KEYSPACE collider** (9710/9720, 9810/9820). `$4`/128-bit has **no** collider shortcut. A 128-bit file and a 40-bit file both extract as `$oldoffice$3` — the collider silently fails on the 128-bit one. | hashcat thread 3665; JtR |

## 2. Detailed findings

### OneNote — RESOLVED (it's agile; office2john already does it)
`office2john.py` (john) has a "OneNote handling hack for OneNote versions >= 2013 (see [MS-ONESTORE])": it detects the OneNote magic `e4525c7b8cd8`, carves the embedded `<?xml … </encryption>` block, and runs it through the same agile `xml_metadata_parser` used for Office 2013 → emits `$office$*2013*…`. The `[MS-OFFCRYPTO]` parsers `blu-base/libmson` (`EncryptedData.h`), `aspose-note-foss`, and Microsoft's own `OfficeDev/Interop-TestSuites` all confirm the `ObjectDataEncryptionKeyV2FNDX` blob is framed by `0xFB6BA385DAD1A067`/`0x2649294F8E198B3C` and spec-marked "MUST be ignored" — but the agile `<encryptedKey>` XML (`http://schemas.microsoft.com/office/2006/keyEncryptor/password`) lives inside it, which is why office2john's pragmatic string-carve works. **Action: OneNote is not a real gap** — extract with `office2john`, crack with `-m 9600`. A `PROPOSED_onenote` module is unnecessary; only non-2013 profiles or a clean extractor would be new work.

### Access `.accdb` — RESOLVED (agile SHA-512/AES-256, per-page)
ACE 2010+ reuses Office-2013 agile: `H0=SHA512(salt‖pwUTF16LE)`, spin 100000, final `SHA512(Hn‖blockKey)` truncated to 32; **same three block-key constants** as Office agile (`fea7d276…`, `d7aa0f6d…`, `146e0be7…`). Deviation (captured by `Jackcess`, undocumented in MS-OFFCRYPTO): the database is AES-256-**CBC** encrypted **per 4096-byte page**, with per-page `blockKey = 4-byte encodingKey XOR pageNumber (LE32)` and per-page IV `SHA512(keyData.salt‖blockKey)[:16]`; page 0 stays plaintext and holds the XML descriptor. ACE 2007 = SHA-1 + RC4 CryptoAPI. **Action: a custom `.accdb` extractor could emit the standard agile verifier line for `-m 9600`** (the verifier is byte-identical); page decryption then needs the Access-specific per-page blockKey. Confirm against a real file (Jackcess is the reference).

### ODF 1.3 "Wholesome Encryption" — RESOLVED (exact URIs + Argon2 params)
Corrects the guessed literals in `../algorithms/password/odf-encryption.md`: the Argon2id key-derivation-name is the LibreOffice **experimental URN** `urn:org:documentfoundation:names:experimental:office:manifest:argon2id` (not the bare `argon2id` we guessed); attributes are `loext:argon2-iterations` (t, default **3**), `loext:argon2-memory` (m, default **65536 KiB = 64 MiB**), `loext:argon2-lanes` (p, default **4**) — RFC 9106 second recommendation. Cipher URI `http://www.w3.org/2009/xmlenc11#aes256-gcm` (our guess was right). The Argon2id input is **SHA-256(password)** (start-key `http://www.w3.org/2001/04/xmlenc#sha256`, keysize 32), not the raw password. Default since LibreOffice 24.8 (Aug 2024); headed for ODF 1.5. Still no hashcat/JtR kernel (memory-hard KDF + AEAD tag).

### VBA project password — RESOLVED (extractor exists)
Confirms `../algorithms/password/vba-project-password.md` exactly: PROJECT stream `CMG`/`DPB`/`GC`; DPB = `16*HEXDIG`; the hash case (Length 29) = 4-byte salt + `SHA1(MBCS(password)‖salt)`, wrapped in the keyless seeded-XOR "Data Encryption" (§2.4.3.2). **The extractor we said was missing exists:** Didier Stevens' `oledump.py` `plugin_vbaproject.py` decodes the DPB and emits the hash → `-m 110`. `tidydevv/VBA-Password-Remover` is a *runtime* IAT-hook bypass (patches `DialogBoxParamA`), not a hash tool — a different, in-app technique.

### Office 97-2003 legacy weaknesses — context (why the fast paths work)
- **RC4 keystream reuse** across saves: Hongjun Wu, *"The Misuse of RC4 in Microsoft Word and Excel"*, IACR ePrint **2005/007** — re-saving an encrypted doc reuses the same keystream, enabling plaintext recovery without the password. Microsoft declined to fix it (David LeBlanc, *"Don't use Office RC4 encryption"*, MSDN 2010).
- **40-bit truncation → colliders**: hashcat thread **3665** (atom) is the design doc for 9700/9710/9720 + 9800/9810/9820 — the KDF truncates to 40 bits, so 9710/9810 brute the 2^40 RC4 key and 9720/9820 find colliding passwords (multiple valid, never marks "cracked"). `$4`/128-bit has no shortcut.

## 3. Tools & libraries by category

| Category | Repos (★ = notable) | Relevance |
|---|---|---|
| **Crackers / frontends** | ★`hashcat/hashcat`, ★`openwall/john` (+`office2john`/`odf2john`, and the OneNote hack), `nesfit/fitcrack`, `ZerkerEOD/krakenhashes`, `vishalpatil1337/…`, `xcdiv/OfficePasswordCrack` | The targets + the extraction/comparison baseline |
| **Decrypt / crypto libs (reference impls)** | ★`nolze/msoffcrypto-tool` (Python), ★`apache/poi` (Java, generalized agile + §2.4.2.4 protection), `ExcelDataReader` (C#), `woodbusy/ooxml_decrypt` (Ruby agile), `nissl-lab/npoi` (C#), `herumi/msoffice` | Port targets for the generalized-agile/protection modules |
| **Binary-format RE / parsers** | ★`hughbe/OfficeFileReader` (Swift, MS-DOC/PPT/OSHARED), ★`ONLYOFFICE/core` (C++, actual .ppt CryptoAPI decrypt), `EvolutionJobs/b2xtranslator` (C#), `LibreOffice/mso-dumper`, `renyxa/re-lab` | Extractor references for the binary formats |
| **Offensive Office** | ★`michaelweber/Macrome` (XLS XOR/VelvetSweatshop, XLM), `tidydevv/VBA-Password-Remover` (runtime hook) | XOR obfuscation + VBA bypass |
| **OneNote** | `blu-base/libmson` (C++ envelope), `DissectMalware/pyOneNote`, `alegrigoriev/onenote2xml`, `aspose-note-foss/…`, `OfficeDev/Interop-TestSuites` (MS) | Container parsers (extract the blob; office2john does the crypto) |
| **PST / MAPI** | `dionach/PANhunt` (PST CRC-32 + slicing-by-8 CRC-32), `DidierStevens/DidierStevensSuite` (`plugin_msg`), `microsoft/mfcmapi`, `grommunio/gromox`, libpff | PST open-password + body cipher reference |
| **VBA** | `decalage2/oletools` (olevba/oledump + `plugin_vbaproject.py`), `eiaccb/vbaProject-sign`, `coffeeforyou/vbasig` (signature) | DPB decode + macro signature |
| **Access** | `Jackcess` (Java, the ACE crypto reference), `mdbtools` | `.mdb` decode + `.accdb` agile params |

## 4. Research & reading list

- **hashcat forum thread 3665** — *Colliding Password Protected MS Office 97-2003 Documents* (atom) — the design of modes 9700–9720 / 9800–9820; the 40-bit collider. Primary source for the KEYSPACE class.
- **hashcat forum thread 12136** — *How do I format OneNote protected section hash into hashcat format?* — community hit on the OneNote case (resolved by office2john).
- **Hongjun Wu, IACR ePrint 2005/007** — *The Misuse of RC4 in Microsoft Word and Excel* — keystream reuse.
- **David LeBlanc (MSDN, 2010)** — *Don't use Office RC4 encryption* — why MS never fixed the reuse.
- **LibreOffice tdf#105844** ("ODF Wholesome Encryption") — the Argon2id/AES-GCM implementation + params.
- **[MS-OFFCRYPTO] §2.3.4 / §2.4.2.4**, **[MS-OVBA] §2.3.1/§2.4.3-4**, **[MS-ONESTORE] §2.5.19**, **[MS-PST] §2.4.3.3** — the primary specs (source markdown in `../_research/openspec_md_files/OfficeFileFormatsProtocols.zip.out/`).
- **`apache/poi` `poifs/crypt`** and **`nolze/msoffcrypto-tool`** — the two cleanest full reference implementations to port from.
- **John the Ripper issue #5652** — the one filed open ticket (ODF).

## 5. Appendix — all repos discovered
Full deduped list (noise-filtered) in `../_research/repos_filtered.txt` (~95 repos); raw hit data in `../_research/gh_search_raw.txt`. The high-signal subset is categorized in §3 above.
