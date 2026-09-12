# Corpus info pages

`opt info` triage for every file in the first-party corpus (4561 files). Regenerate with `regen_corpus_docs.py`.


## encrypted/ (4090 files)

```text
encrypted/35897-type4.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/50833.xls	ole-cfb	.xls	encrypted
  Open password: default (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F) --
encrypted/58616.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/60320-protected.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/Password_Protected-56-hello.ppt	ole-cfb	.ppt	encrypted
  Open password: crack (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/Password_Protected-hello.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/Password_Protected-np-hello.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/accdb-enc-2007.accdb	access	.accdb	encrypted
  Open password: crack @ ACE 2007 database (encoding key set) -- ACE 2007
encrypted/accdb-enc-2013.accdb	access	.accdb	encrypted
  Open password: crack (hashcat -m 9600) @ page 0 EncryptionInfo descriptor -- ACE
encrypted/bug53475-password-is-pass.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/bug53475-password-is-solrcell.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/cryptoapi-proc2356.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/doc-open-csp-base-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-csp-basedss-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-csp-dhschannel-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-csp-enhanced-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-csp-enhanceddss-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-csp-enhancedrsa-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-csp-rsaschannel-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-csp-strong-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9700) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-base-40-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-base-40-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-dss-40-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-dss-40-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-dss-56-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-dss-56-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-enhanced-128-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-enhanced-128-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-enhanced-40-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-enhanced-40-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-enhanced-56-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-enhanced-56-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-rsaschannel-128-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-rsaschannel-128-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-rsaschannel-40-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-rsaschannel-40-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-rsaschannel-56-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-rsaschannel-56-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-strong-128-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-strong-128-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-strong-40-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-strong-40-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-strong-56-props-off-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4capi-strong-56-props-on-2003.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/doc-open-rc4md5-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9700) @ WordDocument FibBase + Table stream
encrypted/doc-open-xor-2003.doc	ole-cfb	.doc	not encrypted
  Open password: decode @ WordDocument FibBase (fObfuscation=1); lKey verifier --
encrypted/docx-composite-open-restrict-vba-sig-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/docx-open-agile-2013.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-md5-3des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-3des112-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes128-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes192-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-aes256-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-desx-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-md5-rc2-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-3des112-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-3des112-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes128-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes192-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-aes256-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-desx-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha1-rc2-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha1-rc2-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-agile-sha256-3des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-3des112-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes128-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes192-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-aes256-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-desx-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha256-rc2-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-3des112-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes128-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes192-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-aes256-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-desx-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha384-rc2-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-3des112-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-aes128-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes128-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes192-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-aes256-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-agile-sha512-des-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-des-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-desx-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cbc-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s100000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s100000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s100000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s100000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s200000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s200000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s200000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s200000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s50000-salt16-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s50000-salt16-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s50000-salt8-props-off-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-agile-sha512-rc2-cfb-s50000-salt8-props-on-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/docx-open-default-2010.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/docx-open-default-2016.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/docx-open-standard-2007.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/docx-open-standard-aes128-props-off-2007.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/docx-open-standard-aes128-props-on-2007.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/docx-open-standard-aes128-req192-props-off-2007.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/docx-open-standard-aes128-req192-props-on-2007.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/docx-open-standard-aes128-req256-props-off-2007.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/docx-open-standard-aes128-req256-props-on-2007.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/ecma376standard_password.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/enc-api-test.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/encrypted_scriptsig_lo242.odt	odf-zip	.odt	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/encrypted_scriptsig_odf13.odt	odf-zip	.odt	encrypted
  Open password: crack (hashcat -m 18400) @ META-INF/manifest.xml
encrypted/example_password.decrypted.docx	ooxml-zip	.docx	not encrypted
  gates: none present
encrypted/example_password.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/example_password.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/m-doc-open-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9700) @ WordDocument FibBase + Table stream
encrypted/m-doc-open-modify-2003.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9700) @ WordDocument FibBase + Table stream
encrypted/m-docx-open-2013.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/m-docx-open-modify-2013.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/m-ppt-modify-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: default (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/m-ppt-open-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/m-pptx-open-2013.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/m-pptx-open-modify-2013.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/m-xls-open-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F)
encrypted/m-xls-open-modify-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F)
encrypted/m-xls-workbook-2003.xls	ole-cfb	.xls	encrypted
  Open password: default (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F) --
encrypted/m-xlsb-open-2013.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/m-xlsb-open-modify-2013.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/m-xlsb-open-sheet-2013.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/m-xlsx-open-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/m-xlsx-open-modify-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/m-xlsx-open-sheet-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/odfver-0.ods	odf-zip	.ods	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odfver-1.ods	odf-zip	.ods	encrypted
  Open password: crack (hashcat -m 18600) @ META-INF/manifest.xml
encrypted/odfver-2.ods	odf-zip	.ods	encrypted
  Open password: crack (hashcat -m 18600) @ META-INF/manifest.xml
encrypted/odfver-4.ods	odf-zip	.ods	encrypted
  Open password: crack (hashcat -m 18400) @ META-INF/manifest.xml
encrypted/odfver-5.ods	odf-zip	.ods	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odfver-7.ods	odf-zip	.ods	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odp-open-odf11-blowfish-lo.odp	odf-zip	.odp	encrypted
  Open password: crack (hashcat -m 18600) @ META-INF/manifest.xml
encrypted/odp-open-odf12-aes.odp	odf-zip	.odp	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odp-open-odf12-aescbc-lo.odp	odf-zip	.odp	encrypted
  Open password: crack (hashcat -m 18400) @ META-INF/manifest.xml
encrypted/odp-open-odf12-lo.odp	odf-zip	.odp	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/ods-open-odf11-blowfish-lo.ods	odf-zip	.ods	encrypted
  Open password: crack (hashcat -m 18600) @ META-INF/manifest.xml
encrypted/ods-open-odf12-aes.ods	odf-zip	.ods	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/ods-open-odf12-aescbc-lo.ods	odf-zip	.ods	encrypted
  Open password: crack (hashcat -m 18400) @ META-INF/manifest.xml
encrypted/ods-table-odf12-lo.ods	odf-zip	.ods	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odt-enc-test.odt	odf-zip	.odt	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odt-open-odf11-blowfish-lo.odt	odf-zip	.odt	encrypted
  Open password: crack (hashcat -m 18600) @ META-INF/manifest.xml
encrypted/odt-open-odf12-aes.odt	odf-zip	.odt	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odt-open-odf12-aescbc-lo.odt	odf-zip	.odt	encrypted
  Open password: crack (hashcat -m 18400) @ META-INF/manifest.xml
encrypted/odt-open-odf12-lo.odt	odf-zip	.odt	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odt-open-odf13-lo.odt	odf-zip	.odt	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/odt-section-odf12-lo.odt	odf-zip	.odt	encrypted
  Open password: crack @ META-INF/manifest.xml <manifest:encryption-data>
encrypted/onenote-section-pw-2010.one	onenote	.one	encrypted
  Open password: crack (hashcat -m 9500) @ ObjectDataEncryptionKeyV2FNDX blob ->
encrypted/onenote-section-pw-2013.one	onenote	.one	encrypted
  Open password: crack (hashcat -m 9600) @ ObjectDataEncryptionKeyV2FNDX blob ->
encrypted/onenote-section-pw-2016.one	onenote	.one	encrypted
  Open password: crack (hashcat -m 9600) @ ObjectDataEncryptionKeyV2FNDX blob ->
encrypted/p-ppt-modify-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: default (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/p-xls-windows-2003.xls	ole-cfb	.xls	encrypted
  Open password: default (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F) --
encrypted/p-xls-workbook-2003.xls	ole-cfb	.xls	encrypted
  Open password: default (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F) --
encrypted/p-xlsb-windows-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/p-xlsb-workbook-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/p-xlsx-windows-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/p-xlsx-workbook-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/password.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F)
encrypted/password_password_cryptoapi.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/password_tika_binaryrc4.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9700) @ WordDocument FibBase + Table stream
encrypted/ppt-modify-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: default (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-csp-enhanced-56-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: crack (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-hannes-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: default (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-dss-128-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-dss-128-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-dss-40-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-dss-40-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-dss-56-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-dss-56-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-enhanced-128-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-enhanced-128-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-enhanced-40-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-enhanced-40-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-enhanced-56-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-enhanced-56-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-rsaschannel-128-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-rsaschannel-128-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-rsaschannel-40-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-rsaschannel-40-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-rsaschannel-56-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-rsaschannel-56-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-strong-128-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-strong-128-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-strong-40-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-strong-40-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-strong-56-props-off-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt-open-rc4capi-strong-56-props-on-2003.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/ppt_with_png_encrypted.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/pptx-composite-open-modify-vba-sig-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/pptx-open-agile-2013.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-md5-3des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-3des112-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes128-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes192-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-aes256-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-desx-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-md5-rc2-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-3des112-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-3des112-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes128-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes192-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-aes256-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-desx-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha1-rc2-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha1-rc2-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-agile-sha256-3des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-3des112-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes128-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes192-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-aes256-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-desx-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha256-rc2-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-3des112-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes128-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes192-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-aes256-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-desx-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha384-rc2-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-3des112-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-aes128-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes128-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes192-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-aes256-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/pptx-open-agile-sha512-des-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-des-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-desx-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cbc-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s100000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s100000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s100000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s100000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s200000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s200000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s200000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s200000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s50000-salt16-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s50000-salt16-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s50000-salt8-props-off-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-agile-sha512-rc2-cfb-s50000-salt8-props-on-2016.pptx	ole-cfb	.pptx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/pptx-open-default-2010.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/pptx-open-standard-aes128-props-off-2007.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/pptx-open-standard-aes128-props-on-2007.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/pptx-open-standard-aes128-req192-props-off-2007.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/pptx-open-standard-aes128-req192-props-on-2007.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/pptx-open-standard-aes128-req256-props-off-2007.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/pptx-open-standard-aes128-req256-props-on-2007.pptx	ole-cfb	.pptx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/protect.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/protected_agile.docx	ole-cfb	.docx	encrypted
  Open password: default (hashcat -m 9500) @ EncryptionInfo -- opens with the
encrypted/protected_normal_case.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/protected_passtika.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/protected_upper_case.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/q-xlsb-windows-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/q-xlsb-workbook-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/q-xlsx-windows-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/q-xlsx-workbook-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/r-xlsb-windows-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/r-xlsb-workbook-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/r-xlsx-windows-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/r-xlsx-workbook-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: default (hashcat -m 9400) @ EncryptionInfo -- opens with the
encrypted/rc4cryptoapi_password.doc	ole-cfb	.doc	encrypted
  Open password: crack (hashcat -m 9800) @ WordDocument FibBase + Table stream
encrypted/rc4cryptoapi_password.ppt	ole-cfb	.ppt	encrypted
  Open password: crack (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/rc4cryptoapi_password.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/test-agile-md2-aes256-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/test-agile-md4-aes256-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/testAccess2_encrypted.accdb	access	.accdb	encrypted
  Open password: crack (hashcat -m 9600) @ page 0 EncryptionInfo descriptor -- ACE
encrypted/testEXCEL_protected_passtika.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F)
encrypted/testEXCEL_protected_passtika_2.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/testODTEncrypted.odt	odf-zip	.odt	encrypted
  Open password: crack (hashcat -m 18400) @ META-INF/manifest.xml
encrypted/testPPT_protected_passtika.ppt	ole-cfb	.ppt	encrypted
  Open password: keyspace (hashcat -m 9800) @ CryptSession10Container via Current
encrypted/testWORD_protected_drm.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
encrypted/testWORD_protected_passtika.doc	ole-cfb	.doc	encrypted
  Open password: keyspace (hashcat -m 9700) @ WordDocument FibBase + Table stream
encrypted/testWORD_protected_passtika.docx	ole-cfb	.docx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xls-composite-open-modify-sheet-vba-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-composite-open-modify-sheet-workbook-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-csp-base-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-csp-basedss-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-csp-dhschannel-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-csp-enhanced-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-csp-enhanceddss-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-csp-enhancedrsa-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-csp-rsaschannel-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-csp-strong-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-base-40-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-base-40-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-dss-40-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-dss-40-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-dss-56-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-dss-56-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-enhanced-128-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-enhanced-128-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-enhanced-40-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-enhanced-40-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-enhanced-56-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-enhanced-56-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-rsaschannel-128-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-rsaschannel-128-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-rsaschannel-40-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-rsaschannel-40-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-rsaschannel-56-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-rsaschannel-56-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-strong-128-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-strong-128-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-strong-40-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-strong-40-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-rc4capi-strong-56-props-off-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4capi-strong-56-props-on-2003.xls	ole-cfb	.xls	encrypted
  Open password: crack (hashcat -m 9800) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-rc4md5-2003.xls	ole-cfb	.xls	encrypted
  Open password: keyspace (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F)
encrypted/xls-open-velvetsweatshop-2003.xls	ole-cfb	.xls	encrypted
  Open password: default (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-open-xor-2003.xls	ole-cfb	.xls	not encrypted
  Open password: decode @ Workbook FilePass record (XOR obfuscation) -- keyless
  Workbook protection: collide @ Password record (rt=0x13) in the globals
  Shared-revisions lock: collide @ Prot4RevPass record (rt=0x1BC) -- 16-bit
encrypted/xls-protect-workbook-structure-2003.xls	ole-cfb	.xls	encrypted
  Open password: default (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F) --
encrypted/xls-protect-workbook-windows-2003.xls	ole-cfb	.xls	encrypted
  Open password: default (hashcat -m 9700) @ Workbook FilePass record (rt=0x2F) --
encrypted/xlsb-open-agile-md5-3des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-3des112-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes128-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes192-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-aes256-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-desx-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-md5-rc2-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-3des112-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-3des112-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes128-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes192-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-aes256-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-desx-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha1-rc2-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha1-rc2-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-agile-sha256-3des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-3des112-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes128-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes192-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-aes256-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-desx-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha256-rc2-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-3des112-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes128-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes192-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-aes256-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-desx-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha384-rc2-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-3des112-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-aes128-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes128-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes192-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-aes256-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsb-open-agile-sha512-des-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-des-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-desx-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cbc-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s100000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s100000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s100000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s100000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s200000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s200000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s200000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s200000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s50000-salt16-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s50000-salt16-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s50000-salt8-props-off-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-agile-sha512-rc2-cfb-s50000-salt8-props-on-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsb-open-default-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-default-2010.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-default-2013.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-default-2016.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsb-open-standard-aes128-props-off-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsb-open-standard-aes128-props-on-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsb-open-standard-aes128-req192-props-off-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsb-open-standard-aes128-req192-props-on-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsb-open-standard-aes128-req256-props-off-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsb-open-standard-aes128-req256-props-on-2007.xlsb	ole-cfb	.xlsb	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsx-composite-allgate-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-composite-open-sheet-modify-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-composite-outer-encrypt-inner-protect-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-modify-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-2013-default.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-md5-3des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-3des112-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes128-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes192-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-aes256-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-desx-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-md5-rc2-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-3des112-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-3des112-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes128-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes192-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-aes256-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-desx-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha1-rc2-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha1-rc2-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-agile-sha256-3des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-3des112-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes128-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes192-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-aes256-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-desx-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha256-rc2-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-3des112-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes128-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes192-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-aes256-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-desx-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha384-rc2-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-3des112-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-aes128-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes128-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes192-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-aes256-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9600) @ EncryptionInfo
encrypted/xlsx-open-agile-sha512-des-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-des-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-desx-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cbc-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s100000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s100000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s100000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s100000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s200000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s200000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s200000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s200000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s50000-salt16-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s50000-salt16-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s50000-salt8-props-off-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-agile-sha512-rc2-cfb-s50000-salt8-props-on-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack @ EncryptionInfo -- agile tuple has no hashcat mode -- GAP
encrypted/xlsx-open-default-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-default-2010.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-default-2013.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-default-2016.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9500) @ EncryptionInfo
encrypted/xlsx-open-standard-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsx-open-standard-aes128-props-off-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsx-open-standard-aes128-props-on-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsx-open-standard-aes128-req192-props-off-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsx-open-standard-aes128-req192-props-on-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsx-open-standard-aes128-req256-props-off-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xlsx-open-standard-aes128-req256-props-on-2007.xlsx	ole-cfb	.xlsx	encrypted
  Open password: crack (hashcat -m 9400) @ EncryptionInfo
encrypted/xor-encryption-abc.xls	ole-cfb	.xls	not encrypted
  Open password: decode @ Workbook FilePass record (XOR obfuscation) -- keyless
encrypted/xor_password_123456789012345.xls	ole-cfb	.xls	not encrypted
  Open password: decode @ Workbook FilePass record (XOR obfuscation) -- keyless
  Workbook protection: collide @ Password record (rt=0x13) in the globals
  Shared-revisions lock: collide @ Prot4RevPass record (rt=0x1BC) -- 16-bit
```


## protected/ (471 files)

```text
protected/47034.xls	ole-cfb	.xls	not encrypted
  Macro project lock (VBA): strip (hashcat -m 110) @ embedded VBA storage ->
protected/47889.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Sheet protection: strip @ xl/worksheets/sheet2.xml <sheetProtection>
  Sheet protection: strip @ xl/worksheets/sheet3.xml <sheetProtection>
protected/62834.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/63934.xlsx	ooxml-zip	.xlsx	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/CVLKRA-KYC_Download_File_Structure_V3.1.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
  Sheet protection: strip @ xl/worksheets/sheet2.xml <sheetProtection>
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet3.xml
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet4.xml
protected/EnforcedWith.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/doc-modify-2003.doc	ole-cfb	.doc	not encrypted
  Modify password: read @ Table stream SttbfAssoc[0x11] (cleartext UTF-16LE);
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/doc-restrict-forms-2013.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/doc-signature-2003.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/doc-vba-hash-2003.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/doc-vba-plaintext-2003.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/documentProtection_comments_no_password.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/documentProtection_forms_no_password.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/documentProtection_readonly_no_password.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/documentProtection_trackedChanges_no_password.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/docx-modify-2016.docx	ooxml-zip	.docx	not encrypted
  Modify password: strip @ word/settings.xml <w:writeProtection> -- Word 2007
protected/docx-restrict-comments-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/docx-restrict-comments-2013.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/docx-restrict-comments-nopw-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/docx-restrict-edit-comments-crypt-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/docx-restrict-edit-comments-crypt-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/docx-restrict-edit-forms-crypt-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/docx-restrict-edit-forms-crypt-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/docx-restrict-edit-reading-crypt-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/docx-restrict-edit-reading-crypt-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/docx-restrict-edit-revisions-crypt-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/docx-restrict-edit-revisions-crypt-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/docx-restrict-forms-nopw-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/docx-restrict-reading-nopw-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/docx-restrict-readonly-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/docx-restrict-revisions-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/docx-restrict-revisions-nopw-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection>
protected/docx-restrict-test-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/fileSharing_reservation.xlsm	ooxml-zip	.xlsm	not encrypted
  Modify password: strip (hashcat -m 25300) @ xl/workbook.xml <fileSharing> -- ISO
protected/hello-world-signed.docx	ooxml-zip	.docx	not encrypted
  Digital signature: none @ _xmlsignatures/ -- digital signature carries no
protected/hello-world-signed.pptx	ooxml-zip	.pptx	not encrypted
  Digital signature: none @ _xmlsignatures/ -- digital signature carries no
protected/hello-world-signed.xlsx	ooxml-zip	.xlsx	not encrypted
  Digital signature: none @ _xmlsignatures/ -- digital signature carries no
protected/m-doc-modify-2003.doc	ole-cfb	.doc	not encrypted
  Modify password: read @ Table stream SttbfAssoc[0x11] (cleartext UTF-16LE);
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/m-doc-restrict-comments-2003.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/m-doc-restrict-reading-2003.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/m-docx-modify-2013.docx	ooxml-zip	.docx	not encrypted
  Modify password: strip @ word/settings.xml <w:writeProtection> -- Word 2007
protected/m-docx-restrict-comments-2013.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/m-docx-restrict-forms-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/m-docx-restrict-reading-2013.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/m-docx-restrict-revisions-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/m-pptx-modify-2013.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/m-xls-modify-2003.xls	ole-cfb	.xls	not encrypted
  Modify password: collide @ FileSharing record (rt=0x5B, wResPass) -- 16-bit
protected/m-xls-range-2003.xls	ole-cfb	.xls	not encrypted
  gates: none present
protected/m-xls-sheet-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/m-xlsb-modify-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Modify password: strip @ xl/workbook.bin (BrtFileSharingIso) -- ISO protection
protected/m-xlsb-range-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.bin (BrtRangeProtectionIso) -- ISO
protected/m-xlsb-sheet-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/m-xlsb-windows-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/m-xlsb-workbook-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/m-xlsx-modify-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing> -- ISO protection
protected/m-xlsx-range-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange> -- ISO
protected/m-xlsx-sheet-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/m-xlsx-windows-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/m-xlsx-workbook-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/mdb-vba-hash-2003.mdb	access	.mdb	not encrypted
  Open password: decode @ header page 0, offset 0x42 (Jet 4) -- DECODE
protected/mdb-vba-plaintext-2003.mdb	access	.mdb	not encrypted
  Open password: decode @ header page 0, offset 0x42 (Jet 4) -- DECODE
protected/ods-table-protected-lo.ods	odf-zip	.ods	not encrypted
  Sheet protection: strip @ content.xml <table:table table:protected="true"> --
protected/odt-section-protected-lo.odt	odf-zip	.odt	not encrypted
  Section protection: strip @ content.xml <text:section text:protected="true"> --
protected/p-doc-modify-2003.doc	ole-cfb	.doc	not encrypted
  Modify password: read @ Table stream SttbfAssoc[0x11] (cleartext UTF-16LE);
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/p-doc-restrict-comments-2003.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/p-doc-restrict-reading-2003.doc	ole-cfb	.doc	not encrypted
  Restrict editing: strip @ Table stream Dop.lKeyProtDoc + fProt* flags (DopBase)
protected/p-docx-modify-2007.docx	ooxml-zip	.docx	not encrypted
  Modify password: strip @ word/settings.xml <w:writeProtection> -- Word 2007
protected/p-docx-modify-2010.docx	ooxml-zip	.docx	not encrypted
  Modify password: strip @ word/settings.xml <w:writeProtection> -- Word 2007
protected/p-docx-modify-2013.docx	ooxml-zip	.docx	not encrypted
  Modify password: strip @ word/settings.xml <w:writeProtection> -- Word 2007
protected/p-docx-modify-2016.docx	ooxml-zip	.docx	not encrypted
  Modify password: strip @ word/settings.xml <w:writeProtection> -- Word 2007
protected/p-docx-restrict-comments-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-comments-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-comments-2013.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-comments-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-forms-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-docx-restrict-forms-2010.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-docx-restrict-forms-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-docx-restrict-forms-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-docx-restrict-reading-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-reading-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-reading-2013.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-reading-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/p-docx-restrict-revisions-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-docx-restrict-revisions-2010.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-docx-restrict-revisions-2013.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-docx-restrict-revisions-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/p-pptx-modify-2007.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/p-pptx-modify-2010.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/p-pptx-modify-2013.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/p-pptx-modify-2016.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/p-xls-modify-2003.xls	ole-cfb	.xls	not encrypted
  Modify password: collide @ FileSharing record (rt=0x5B, wResPass) -- 16-bit
protected/p-xls-range-r1-2003.xls	ole-cfb	.xls	not encrypted
  gates: none present
protected/p-xls-range-r2-2003.xls	ole-cfb	.xls	not encrypted
  gates: none present
protected/p-xls-sheet00-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xls-sheet01-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xls-sheet02-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xls-sheet03-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xls-sheet04-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xls-sheet05-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xls-sheet06-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xls-sheet07-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/p-xlsb-modify-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Modify password: strip @ xl/workbook.bin (BrtFileSharingIso) -- ISO protection
protected/p-xlsb-modify-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Modify password: strip (hashcat -m 25300) @ xl/workbook.bin (BrtFileSharingIso)
protected/p-xlsb-range-r1-2007.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/p-xlsb-range-r1-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/p-xlsb-range-r1-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.bin (BrtRangeProtectionIso) -- ISO
protected/p-xlsb-range-r1-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-range-r2-2007.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/p-xlsb-range-r2-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/p-xlsb-range-r2-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.bin (BrtRangeProtectionIso) -- ISO
protected/p-xlsb-range-r2-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet00-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet00-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet01-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet01-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet02-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet02-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet03-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet03-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet04-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet04-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet05-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet05-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet06-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet06-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet07-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet07-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet08-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet08-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet09-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet09-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet10-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet10-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet11-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet11-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet12-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/p-xlsb-sheet12-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet12-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-sheet13-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/p-xlsb-sheet13-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/p-xlsb-windows-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/p-xlsb-windows-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.bin
protected/p-xlsb-workbook-2013.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/p-xlsb-workbook-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.bin
protected/p-xlsx-modify-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing>
protected/p-xlsx-modify-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing>
protected/p-xlsx-modify-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing> -- ISO protection
protected/p-xlsx-modify-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip (hashcat -m 25300) @ xl/workbook.xml <fileSharing> -- ISO
protected/p-xlsx-range-r1-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/p-xlsx-range-r1-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/p-xlsx-range-r1-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange> -- ISO
protected/p-xlsx-range-r1-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-range-r2-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/p-xlsx-range-r2-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/p-xlsx-range-r2-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange> -- ISO
protected/p-xlsx-range-r2-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet00-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet00-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet00-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet00-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet01-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet01-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet01-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet01-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet02-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet02-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet02-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet02-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet03-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet03-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet03-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet03-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet04-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet04-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet04-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet04-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet05-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet05-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet05-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet05-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet06-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet06-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet06-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet06-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet07-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet07-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet07-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet07-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet08-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet08-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet08-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet08-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet09-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet09-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet09-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet09-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet10-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet10-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet10-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet10-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet11-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet11-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet11-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet11-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet12-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet12-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet12-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet12-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-sheet13-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet13-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/p-xlsx-sheet13-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/p-xlsx-sheet13-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/p-xlsx-windows-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/p-xlsx-windows-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/p-xlsx-windows-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/p-xlsx-workbook-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/p-xlsx-workbook-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/p-xlsx-workbook-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/ppt-signature-2003.ppt	ole-cfb	.ppt	not encrypted
  gates: none present
protected/ppt-vba-hash-2003.ppt	ole-cfb	.ppt	not encrypted
  gates: none present
protected/ppt-vba-plaintext-2003.ppt	ole-cfb	.ppt	not encrypted
  gates: none present
protected/pptx-modify-2016.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/pptx-modifyverifier-iso-sha512-sdefault-2016.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/pptx-modifyverifier-iso-sha512-soffvalue-2016.pptx	ooxml-zip	.pptx	not encrypted
  Modify password: strip @ ppt/presentation.xml <p:modifyVerifier>
protected/protectedSheets.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/protected_sample.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/pst-Outlook-2003.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
protected/pst-Outlook-2007.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
protected/pst-Outlook-2013.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
protected/pst-Outlook-2016.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
protected/pst-backup-2003.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
  Open password: strip @ PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE
protected/pst-backup-2007.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
  Open password: strip @ PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE
protected/pst-backup-2010.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
  Open password: strip @ PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE
protected/pst-backup-2013.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
  Open password: strip @ PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE
protected/pst-backup-2016.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
  Open password: strip @ PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE
protected/pst-backup2-2003.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
  Open password: strip @ PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE
protected/pst-password-2013.pst	pst	.pst	not encrypted
  Mail body cipher: decode @ NDB header bCryptMethod (offset 0x0201) -- keyless
  Open password: strip @ PidTagPstPassword (0x67FF0003) on NID_MESSAGE_STORE
protected/q-docx-restrict-comments-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/q-docx-restrict-comments-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/q-docx-restrict-comments-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/q-docx-restrict-forms-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/q-docx-restrict-forms-2010.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/q-docx-restrict-forms-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/q-docx-restrict-reading-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/q-docx-restrict-reading-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/q-docx-restrict-reading-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/q-docx-restrict-revisions-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/q-docx-restrict-revisions-2010.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/q-docx-restrict-revisions-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/q-xlsb-modify-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Modify password: strip (hashcat -m 25300) @ xl/workbook.bin (BrtFileSharingIso)
protected/q-xlsb-range-r1-2007.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/q-xlsb-range-r1-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/q-xlsb-range-r1-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-range-r2-2007.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/q-xlsb-range-r2-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/q-xlsb-range-r2-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet00-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet01-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet02-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet03-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet04-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet05-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet06-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet07-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet08-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet09-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet10-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet11-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet12-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-sheet13-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/q-xlsb-windows-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.bin
protected/q-xlsb-workbook-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.bin
protected/q-xlsx-modify-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing>
protected/q-xlsx-modify-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing>
protected/q-xlsx-modify-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip (hashcat -m 25300) @ xl/workbook.xml <fileSharing> -- ISO
protected/q-xlsx-range-r1-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/q-xlsx-range-r1-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/q-xlsx-range-r1-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-range-r2-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/q-xlsx-range-r2-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/q-xlsx-range-r2-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet00-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet00-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet00-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet01-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet01-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet01-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet02-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet02-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet02-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet03-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet03-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet03-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet04-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet04-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet04-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet05-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet05-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet05-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet06-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet06-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet06-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet07-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet07-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet07-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet08-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet08-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet08-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet09-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet09-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet09-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet10-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet10-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet10-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet11-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet11-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet11-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet12-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet12-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet12-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-sheet13-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet13-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/q-xlsx-sheet13-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/q-xlsx-windows-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/q-xlsx-windows-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/q-xlsx-workbook-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/q-xlsx-workbook-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/r-docx-restrict-comments-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/r-docx-restrict-comments-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/r-docx-restrict-comments-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/r-docx-restrict-forms-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/r-docx-restrict-forms-2010.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/r-docx-restrict-forms-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/r-docx-restrict-reading-2007.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/r-docx-restrict-reading-2010.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/r-docx-restrict-reading-2016.docx	ooxml-zip	.docx	not encrypted
  gates: none present
protected/r-docx-restrict-revisions-2007.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/r-docx-restrict-revisions-2010.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/r-docx-restrict-revisions-2016.docx	ooxml-zip	.docx	not encrypted
  Restrict editing: strip @ word/settings.xml <w:documentProtection> -- Word 2007
protected/r-xlsb-modify-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Modify password: strip (hashcat -m 25300) @ xl/workbook.bin (BrtFileSharingIso)
protected/r-xlsb-range-r1-2007.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/r-xlsb-range-r1-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/r-xlsb-range-r1-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-range-r2-2007.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/r-xlsb-range-r2-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/r-xlsb-range-r2-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-range-r3-2007.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/r-xlsb-range-r3-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/r-xlsb-range-r3-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet00-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet01-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet02-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet03-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet04-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet05-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet06-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet07-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet08-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet09-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-sheet10-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/r-xlsb-windows-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.bin
protected/r-xlsb-workbook-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.bin
protected/r-xlsx-modify-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing>
protected/r-xlsx-modify-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing>
protected/r-xlsx-modify-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip (hashcat -m 25300) @ xl/workbook.xml <fileSharing> -- ISO
protected/r-xlsx-range-r1-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/r-xlsx-range-r1-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/r-xlsx-range-r1-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-range-r2-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/r-xlsx-range-r2-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/r-xlsx-range-r2-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-range-r3-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/r-xlsx-range-r3-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/r-xlsx-range-r3-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet00-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet00-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet00-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet01-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet01-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet01-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet02-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet02-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet02-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet03-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet03-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet03-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet04-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet04-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet04-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet05-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet05-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet05-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet06-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet06-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet06-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet07-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet07-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet07-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet08-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet08-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet08-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet09-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet09-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet09-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-sheet10-2007.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet10-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/r-xlsx-sheet10-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/r-xlsx-windows-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/r-xlsx-windows-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/r-xlsx-workbook-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/r-xlsx-workbook-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/sheetProtection_allLocked.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/testEXCEL_signed.xlsx	ooxml-zip	.xlsx	not encrypted
  Digital signature: none @ _xmlsignatures/ -- digital signature carries no
protected/testPPT_signed.pptx	ooxml-zip	.pptx	not encrypted
  Digital signature: none @ _xmlsignatures/ -- digital signature carries no
protected/testWORD_docSecurity.docx	ooxml-zip	.docx	not encrypted
  Modify password: strip @ word/settings.xml <w:writeProtection> -- Word 2007
protected/testWORD_signed.docx	ooxml-zip	.docx	not encrypted
  Digital signature: none @ _xmlsignatures/ -- digital signature carries no
protected/workbookProtection-sheet_password-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/workbookProtection-workbook_password-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/workbookProtection-workbook_password_user_range-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange>
protected/workbookProtection_workbook_revision_protected.xlsx	ooxml-zip	.xlsx	not encrypted
  Shared-revisions lock: strip @ xl/workbook.xml <workbookProtection revisions*>
protected/workbookProtection_workbook_structure_protected.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/workbookProtection_workbook_windows_protected.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
protected/xls-allow-edit-ranges-2003.xls	ole-cfb	.xls	not encrypted
  gates: none present
protected/xls-modify-2003.xls	ole-cfb	.xls	not encrypted
  Modify password: collide @ FileSharing record (rt=0x5B, wResPass) -- 16-bit
protected/xls-protect-sheet-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/xls-protect-sheet-2007.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/xls-sheetprotect-2003.xls	ole-cfb	.xls	not encrypted
  Sheet protection: collide @ Password record (rt=0x13) in the worksheet substream
protected/xls-signature-2003.xls	ole-cfb	.xls	not encrypted
  gates: none present
protected/xls-vba-hash-2003.xls	ole-cfb	.xls	not encrypted
  gates: none present
protected/xls-vba-plaintext-2003.xls	ole-cfb	.xls	not encrypted
  gates: none present
protected/xlsb-allow-edit-ranges-iso-sha1-sdefault-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.bin (BrtRangeProtectionIso) -- ISO
protected/xlsb-allow-edit-ranges-iso-sha1-soffvalue-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.bin (BrtRangeProtectionIso) -- ISO
protected/xlsb-allow-edit-ranges-iso-sha512-sdefault-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.bin (BrtRangeProtectionIso) -- ISO
protected/xlsb-allow-edit-ranges-iso-sha512-soffvalue-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Range passwords: strip @ xl/worksheets/sheet1.bin (BrtRangeProtectionIso) -- ISO
protected/xlsb-modify-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Modify password: strip @ xl/workbook.bin (BrtFileSharingIso) -- ISO protection
protected/xlsb-protect-sheet-iso-sha1-sdefault-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/xlsb-protect-sheet-iso-sha1-soffvalue-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/xlsb-protect-sheet-iso-sha512-sdefault-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/xlsb-protect-sheet-iso-sha512-soffvalue-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.bin (BrtSheetProtectionIso) --
protected/xlsb-protect-sheet-sha512-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.bin
protected/xlsb-protect-workbook-iso-sha1-sdefault-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/xlsb-protect-workbook-iso-sha1-soffvalue-2010.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/xlsb-protect-workbook-iso-sha512-sdefault-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/xlsb-protect-workbook-iso-sha512-soffvalue-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  Workbook protection: strip @ xl/workbook.bin (BrtBookProtectionIso) -- ISO
protected/xlsb-shared-revisions-iso-sha512-2016.xlsb	ooxml-zip	.xlsb	not encrypted
  gates: none present
protected/xlsm-vba-locked-2013.xlsm	ooxml-zip	.xlsm	not encrypted
  Macro project lock (VBA): strip (hashcat -m 110) @ xl/vbaProject.bin -- VBA
protected/xlsx-allow-edit-ranges-iso-sha1-sdefault-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange> -- ISO
protected/xlsx-allow-edit-ranges-iso-sha1-soffvalue-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange> -- ISO
protected/xlsx-allow-edit-ranges-iso-sha512-sdefault-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange> -- ISO
protected/xlsx-allow-edit-ranges-iso-sha512-soffvalue-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
  Range passwords: strip @ xl/worksheets/sheet1.xml <protectedRange> -- ISO
protected/xlsx-composite-sheet-workbook-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/xlsx-modify-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Modify password: strip @ xl/workbook.xml <fileSharing> -- ISO protection
protected/xlsx-protect-sheet-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/xlsx-protect-sheet-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/xlsx-protect-sheet-iso-sha1-sdefault-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/xlsx-protect-sheet-iso-sha1-soffvalue-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection> -- ISO
protected/xlsx-protect-sheet-iso-sha512-sdefault-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/xlsx-protect-sheet-iso-sha512-soffvalue-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/xlsx-protect-sheet-sha512-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip (hashcat -m 25300) @ xl/worksheets/sheet1.xml
protected/xlsx-protect-workbook-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/xlsx-protect-workbook-iso-sha1-sdefault-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/xlsx-protect-workbook-iso-sha1-soffvalue-2010.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/xlsx-protect-workbook-iso-sha512-sdefault-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/xlsx-protect-workbook-iso-sha512-soffvalue-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection> -- ISO
protected/xlsx-protect-workbook-sha512-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip (hashcat -m 25300) @ xl/workbook.xml
protected/xlsx-shared-revisions-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Shared-revisions lock: strip @ xl/workbook.xml <workbookProtection revisions*>
protected/xlsx-shared-revisions-iso-sha512-2016.xlsx	ooxml-zip	.xlsx	not encrypted
  gates: none present
protected/xlsx-shared-revisions-v2-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  gates: none present
protected/xlsx-shared-revisions-v3-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Shared-revisions lock: strip @ xl/workbook.xml <workbookProtection revisions*>
protected/xlsx-sheetprot-nopw-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Sheet protection: strip @ xl/worksheets/sheet1.xml <sheetProtection>
protected/xlsx-workbookprot-nopw-2013.xlsx	ooxml-zip	.xlsx	not encrypted
  Workbook protection: strip @ xl/workbook.xml <workbookProtection>
```

