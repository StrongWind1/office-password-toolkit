"""ODF encryption self-test against the verbatim hashcat 18400/18600 vectors.

Reconstructs an ``OdfEntry`` from each published ``$odf$`` self-test line
(odf-encryption.md Section 7 / hashcat ``module_18400.c`` & ``module_18600.c``)
and asserts:

* ``verify`` succeeds for the known password ``hashcat`` and fails for a wrong one;
* ``decrypt_entry`` reproduces the member plaintext (raw DEFLATE -> XML) and raises
  ``ValueError`` on a wrong password;
* ``odf_hash_line`` round-trips back to the exact published line;
* ``parse_manifest`` reads a synthetic manifest and returns ``[]`` when unencrypted;
* an ODF 1.3 Argon2id / AES-GCM member is flagged as a GAP, not cracked.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import os
import zlib

import pytest
from argon2.low_level import ARGON2_VERSION, Type, hash_secret_raw
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from office_password_toolkit.crypto.odf import (
    OdfEntry,
    OdfUnsupportedError,
    decrypt_entry,
    is_gap,
    odf_hash_line,
    parse_manifest,
    verify,
)

# Verbatim self-test lines (password "hashcat").
LINE_18400 = "$odf$*1*1*100000*32*751854d8b90731ce0579f96bea6f0d4ac2fb2f546b31f1b6af9a5f66952a0bf4*16*2185a966155baa9e2fb597298febecbc*16*c18eaae34bcbbe9119be017fe5f8b52d*0*051e0f1ce0e866f2b771029e03a6c7119aad132af54c4e45824f16f61f357a40407ab82744fe6370c7b2346075fcd4c2e58ab244411b3ab1d532a46e2321599ef13c3d3472fc2f14d480d8c33215e473da67f90540279d3ef1f62dde314fa222796046e496c951235ddf88aa754620b7810d22ebc8835c90dce9276946f52b8ea7d95d2f86e4cc725366a8b3edacc2ce88518e535991a5f84d5ea8795dc02bfb731b5f202ecaf7d4b245d928c4248709fcdf3fba2acf1a08be0c1eee7dbeda07e8c3a6983565635e99952b8ad79d31c965f245ae90b5cc3dba6387898c66fa35cad9ac9595c41b62e68efcdd73185b38e220cf004269b77ec6974474b03b7569afc3b503a2bf8b2d035756f3f4cb880d9ba815e5c944508a0bde214076c35bf0e0814a96d21ccaa744c9056948ed935209f5c7933841d2ede3d28dd84da89d477d4a0041ce6d8ddab891d929340db6daa921d69b46fd5aee306d0bcef88c38acbb495d0466df7e2f744e3d10201081215c02db5dd479a4cda15a3338969c7baec9d3d2c378a8dd30449319b149dc3b4e7f00996a59fcb5f243d0df2cbaf749241033f7865aefa960adfeb8ebf205b270f90b1f82c34f80d5a8a0db7aec89972a32f5daa2a73c5895d1fced01b3ab8e576bd2630eff01cad97781f4966d4b528e1b15f011f28ae907a352073c96b203adc7742d2b79b2e2f440b17e7856ae119e08d15d8bdf951f6d4a3f9b516da2d9a8f9dd93488f8e0119f3da19138ab787f0d7098a652cccd914aa0ff81d375bd6a5a165acc936f591639059287975cfc3ca4342e5f9501b3249a76d14e56d6d56b319e036bc0449ac7b5afa24ffbea11babed8183edf8d4fdca1c3f0d23bfd4a02797627d556634f1a9304e03737604bd86f6b5a26aa687d6df73383e0f7dfe62a131e8dbb8c3f4f13d24857dd29d76984eac6c45df7428fc79323ffa1f4e7962d705df74320141ed1f16d1ad483b872168df60315ffadbfa1b7f4afaed8a0017421bf5e05348cb5c707a5e852d6fee6077ec1c33bc707bcd97b7701ee05a03d6fa78b0d31c8c97ea16e0edf434961bd5cc7cbb7eb2553730f0405c9bd21cee09b3f7c1bc57779fdfc15f3935985737a1b522004c4436b631a39a66e8577a03f5020e6aa41952c0662c8c57f66caa483b47af38b8cb5d457245fd3241749e17433e6f929233e8862d7c584111b1991b2d6e94278e7e6e1908cee5a83d94c78b75a84a695d25aeb9fdde72174fe6dd75e8d406671f44892a385a4a1e249f61ebc993e985607423a0a5742e668d52c1ebf5cecae7c2b7908f4627b92ec49354a9ccff8cb5763ad074a00e65a485a41bf4c25ce7e6fae49358a58547b1c0ca79713e297310c0a367c3de196f1dd685ca4be643bdf1e4f6b034211d020557e37a3b6614d061010b4a3416b6b279728c245d3322"
LINE_18600 = "$odf$*0*0*1024*16*bff753835f4ea15644b8a2f8e4b5be3d147b9576*8*ee371da34333b69d*16*a902eff54a4d782a26a899a31f97bef4*0*dae7e41fbc3a500d3ce152edd8876c4f38fb17d673ee2ac44ef1e0e283622cd2ae298a82d8d98f2ea737247881fc353e73a2f535c6e13e0cdc60821c1a61c53a4b0c46ff3a3b355d7b793fad50de15999fc7c1194321d1c54316c3806956c4a3ade7daabb912a2a36398eba883af088b3cb69b43365d9ba9fce3fb0c1524f73947a7e9fc1bf3adb5f85a367035feacb5d97c578b037144c2793f34aa09dcd04bdaa455aee0d4c52fe377248611dd56f2bd4eb294673525db905f5d905a28dec0909348e6bf94bcebf03ddd61a48797cd5728ce6dbb71037b268f526e806401abcf495f6edd0b5d87118671ec690d4627f86a43e51c7f6d42a75a56eec51204d47e115e813ed4425c97b16b195e02ce776c185194b9de43ae89f356e29face016cb393d6fb93af8ea305d921d5592dd184051ac790b9b90266f52b8d53ce1cb1d762942d6d5bbd0e3821be21af9fa6874ba0c60e64f41d3e5b6caca1c53b575afdc5d8f6a3edbf874dbe009c6cb296466fe9637aed4aed8a43a95ea7d26b4090ad33d4ee7a83844b0893e8bc0f04944205fb9576cb5720f019028cd75ca9ac47b3e5fa231354d74135564df43b659cfaea7e195c4a896e0e0e0c85dc9ce3a9ce9ba552bc2a6dbac4901c19558818e1957ed72d78662bb5ba53475ca584371f1825ae0c92322a4404e63c2baad92665aac29b5c6f96e1e6338d48fb0aef4d0b686063974f58b839484f8dcf0a02537cba67a7d2c4de13125d74820cb07ec72782035af1ea6c4db61c77016d1c021b63c8b07adb4e8510f5c41bbc501f60f3dd16462399b52eb146787e38e700147c7aa23ac4d5d22d9d1c93e67a01c92a197d4765cbf8d56a862a1205abb450a182913a69b8d5334a59924f86fb3ccd0dcfe7426053e26ba26b57c05f38d85863fff1f81135b0366e8cd8680663ae8aaf7d005317b849d5e08be882708fa0d8d02d47e89150124b507c34845c922b95e62aa0b3fef218773d7aeb572c67b35ad8787f31ecc6e1846b673b8ba6172223176eabf0020b6aa3aa71405b40b2fc2127bf9741a103f1d8eca21bf27328cdf15153f2f223eff7b831a72ed8ecacf4ea8df4ea44f3a3921e5a88fb2cfa355ece0f05cbc88fdd1ecd368d6e3b2dfabd999e5b708f1bccaeebb296c9d7b76659967742fe966aa6871cbbffe710b0cd838c6e02e6eb608cb5c81d066b60b5b3604396331d97d4a2c4c2317406e48c9f5387a2c72511d1e6899bd450e9ca88d535755bcfddb53a6df118cd9cdc7d8b4b814f7bc17684d8e5975defaa25d06f410ed0724c16b8f69ec3869bc1f05c71483666968d1c04509875dadd72c6182733d564eb1a7d555dc34f6b817c5418626214d0b2c3901c5a46f5b20fddfdf9f71a7dfd75b9928778a3f65e1832dff22be973c2b259744d500a3027c2a2e08972eaaad4c5c4ec871"

# Manifest URI literals (OASIS ODF Part 3 Section 6), keyed by profile.
_NS = "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0"
_CIPHER = {0: "Blowfish CFB", 1: f"{_NS}#aes256-cbc"}
_CHECKSUM = {0: "SHA1/1K", 1: f"{_NS}#sha256-1k"}
# ODF 1.1 leaves the start key implicit (SHA-1); ODF 1.2 names SHA-256.
_STARTKEY = {0: "", 1: "http://www.w3.org/2000/09/xmldsig#sha256"}


def entry_from_line(line: str) -> OdfEntry:
    """Rebuild an OdfEntry from a $odf$ hash line (inverse of odf_hash_line)."""
    parts = line.split("*")
    cipher_type = int(parts[1])
    checksum_type = int(parts[2])
    return OdfEntry(
        full_path="content.xml",
        media_type="text/xml",
        size=len(binascii.unhexlify(parts[11])),
        checksum_type=_CHECKSUM[checksum_type],
        checksum=binascii.unhexlify(parts[5]),
        cipher=_CIPHER[cipher_type],
        iv=binascii.unhexlify(parts[7]),
        key_derivation="PBKDF2",
        iterations=int(parts[3]),
        key_size=int(parts[4]),
        salt=binascii.unhexlify(parts[9]),
        start_key=_STARTKEY[checksum_type],
        start_key_size=int(parts[4]),
        ciphertext=binascii.unhexlify(parts[11]),
    )


@pytest.mark.parametrize("line", [LINE_18400, LINE_18600])
def test_verify_accepts_correct_password(line):
    entry = entry_from_line(line)
    assert verify(entry, "hashcat", entry.ciphertext) is True


@pytest.mark.parametrize("line", [LINE_18400, LINE_18600])
def test_verify_rejects_wrong_password(line):
    entry = entry_from_line(line)
    assert verify(entry, "hashc4t", entry.ciphertext) is False
    assert verify(entry, "", entry.ciphertext) is False


@pytest.mark.parametrize("line", [LINE_18400, LINE_18600])
def test_hash_line_round_trips(line):
    # odf_hash_line must reproduce the published line byte-for-byte.
    assert odf_hash_line(entry_from_line(line)) == line


@pytest.mark.parametrize("line", [LINE_18400, LINE_18600])
def test_decrypt_entry_yields_xml(line):
    entry = entry_from_line(line)
    plaintext = decrypt_entry(entry, "hashcat", entry.ciphertext)
    # The member inflates to the start of an OpenDocument XML stream.
    assert plaintext.startswith(b"<?xml")


@pytest.mark.parametrize("line", [LINE_18400, LINE_18600])
def test_decrypt_entry_wrong_password_raises(line):
    entry = entry_from_line(line)
    with pytest.raises(ValueError, match="incorrect password"):
        decrypt_entry(entry, "wordpass", entry.ciphertext)


def _b64(raw: bytes) -> str:
    return base64.b64encode(raw).decode("ascii")


def test_parse_manifest_reads_aes_entry():
    # A minimal ODF 1.2 manifest with one encrypted content.xml member.
    checksum = _b64(bytes(range(32)))
    iv = _b64(bytes(range(16)))
    salt = _b64(bytes(range(16, 32)))
    manifest = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="{_NS}">
 <manifest:file-entry manifest:full-path="mimetype" manifest:media-type=""/>
 <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml" manifest:size="27017">
  <manifest:encryption-data manifest:checksum-type="{_NS}#sha256-1k" manifest:checksum="{checksum}">
   <manifest:algorithm manifest:algorithm-name="{_NS}#aes256-cbc" manifest:initialisation-vector="{iv}"/>
   <manifest:key-derivation manifest:key-derivation-name="PBKDF2" manifest:key-size="32" manifest:iteration-count="100000" manifest:salt="{salt}"/>
   <manifest:start-key-generation manifest:start-key-generation-name="http://www.w3.org/2000/09/xmldsig#sha256" manifest:key-size="32"/>
  </manifest:encryption-data>
 </manifest:file-entry>
</manifest:manifest>""".encode()

    entries = parse_manifest(manifest)
    assert len(entries) == 1
    entry = entries[0]
    assert entry.full_path == "content.xml"
    assert entry.iterations == 100000
    assert entry.key_size == 32
    assert entry.checksum == bytes(range(32))
    assert entry.iv == bytes(range(16))
    assert entry.salt == bytes(range(16, 32))
    assert is_gap(entry) is False


def test_parse_manifest_unencrypted_returns_empty():
    manifest = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="{_NS}">
 <manifest:file-entry manifest:full-path="/" manifest:media-type="application/vnd.oasis.opendocument.text"/>
 <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
</manifest:manifest>""".encode()
    assert parse_manifest(manifest) == []


# --- ODF 1.3 "Wholesome Encryption" (Argon2id + AES-256-GCM) -----------------
#
# No real LibreOffice-24.8 corpus sample exists, so these tests CONSTRUCT a
# spec-valid ODF 1.3 member (SHA-256 start key -> Argon2id -> AES-256-GCM, stored
# as IV(12) || ciphertext || tag(16), raw-DEFLATE payload) and round-trip it. The
# recipe mirrors LibreOffice core package/source/zipapi/{ZipFile,ciphercontext}.cxx
# and the URIs / defaults pinned in related-work.md Section 2. This is synthetic
# validation only -- it proves the code is internally consistent with the spec,
# not that it matches a byte stream a real LibreOffice produced.

_GCM_URI = "http://www.w3.org/2009/xmlenc11#aes256-gcm"
_ARGON2_URN = "urn:org:documentfoundation:names:experimental:office:manifest:argon2id"
_SHA256_STARTKEY = "http://www.w3.org/2001/04/xmlenc#sha256"


def build_odf13_member(plaintext: bytes, password: str, salt: bytes, iv: bytes, t_cost: int = 3, memory_kib: int = 65536, lanes: int = 4) -> tuple[bytes, OdfEntry]:
    """Encrypt one member the LibreOffice ODF 1.3 way; return (stored_bytes, entry).

    Stored member is IV(12) || AES-256-GCM(ciphertext) || tag(16); the key is
    Argon2id over SHA-256(password) with the given t/m/p and a 32-byte tag.
    """
    deflate = zlib.compressobj(9, zlib.DEFLATED, -15)
    compressed = deflate.compress(plaintext) + deflate.flush()
    start_key = hashlib.sha256(password.encode("utf-8")).digest()
    key = hash_secret_raw(secret=start_key, salt=salt, time_cost=t_cost, memory_cost=memory_kib, parallelism=lanes, hash_len=32, type=Type.ID, version=ARGON2_VERSION)
    ct_and_tag = AESGCM(key).encrypt(iv, compressed, None)
    member = iv + ct_and_tag
    entry = OdfEntry(
        full_path="content.xml",
        media_type="text/xml",
        size=len(compressed),
        checksum_type="",  # GCM has no plaintext checksum in the manifest
        checksum=b"",
        cipher=_GCM_URI,
        iv=iv,
        key_derivation=_ARGON2_URN,
        iterations=0,
        key_size=32,
        salt=salt,
        start_key=_SHA256_STARTKEY,
        start_key_size=32,
        argon2_iterations=t_cost,
        argon2_memory=memory_kib,
        argon2_lanes=lanes,
        ciphertext=member,
    )
    return member, entry


def test_odf13_manifest_parses_argon2_gcm_params():
    # A faithful ODF 1.3 manifest omits the checksum (AEAD has no plaintext digest).
    manifest = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="{_NS}" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0">
 <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml" manifest:size="27017">
  <manifest:encryption-data>
   <manifest:algorithm manifest:algorithm-name="{_GCM_URI}" manifest:initialisation-vector="{_b64(bytes(12))}"/>
   <manifest:key-derivation manifest:key-derivation-name="{_ARGON2_URN}" manifest:key-size="32" manifest:salt="{_b64(bytes(16))}" loext:argon2-iterations="3" loext:argon2-memory="65536" loext:argon2-lanes="4"/>
   <manifest:start-key-generation manifest:start-key-generation-name="{_SHA256_STARTKEY}" manifest:key-size="32"/>
  </manifest:encryption-data>
 </manifest:file-entry>
</manifest:manifest>""".encode()
    entry = parse_manifest(manifest)[0]
    # Still a GPU-cracking gap (no hashcat/John mode), but now fully decryptable.
    assert is_gap(entry) is True
    assert entry.argon2_iterations == 3
    assert entry.argon2_memory == 65536
    assert entry.argon2_lanes == 4


def test_odf13_round_trip_decrypts():
    plaintext = b"<?xml version='1.0' encoding='UTF-8'?><office:document-content>hello odf 1.3</office:document-content>"
    salt, iv = os.urandom(16), os.urandom(12)
    member, entry = build_odf13_member(plaintext, "Secret123!", salt, iv)
    # Correct password: tag validates and the deflate stream inflates back.
    assert verify(entry, "Secret123!", member) is True
    assert decrypt_entry(entry, "Secret123!", member) == plaintext


def test_odf13_wrong_password_rejected():
    plaintext = b"<?xml version='1.0'?><doc>x</doc>"
    salt, iv = os.urandom(16), os.urandom(12)
    member, entry = build_odf13_member(plaintext, "right-pass", salt, iv)
    assert verify(entry, "wrong-pass", member) is False
    with pytest.raises(ValueError, match="incorrect password"):
        decrypt_entry(entry, "wrong-pass", member)


def test_odf13_extended_hash_line():
    plaintext = b"<?xml version='1.0'?><doc>gcm line</doc>"
    salt, iv = os.urandom(16), os.urandom(12)
    member, entry = build_odf13_member(plaintext, "pw", salt, iv, t_cost=3, memory_kib=65536, lanes=4)
    line = odf_hash_line(entry)
    parts = line.split("*")
    # ODF 1.3 now emits the unified $odf$ format: 11 tokens.
    assert parts[0] == "$odf$"
    assert len(parts) == 11
    assert parts[1] == "sha256"  # start key
    assert parts[2] == "argon2"  # kdf
    assert parts[3] == "aes256gcm"  # cipher
    assert parts[4] == "3"  # t_cost (iters)
    assert parts[5] == "65536"  # m_cost (mem)
    assert parts[6] == "4"  # lanes
    assert parts[7] == salt.hex()
    assert parts[8] == iv.hex()


def test_odf13_unknown_cipher_still_raises():
    # A cipher outside the three profiles has no code path -> OdfUnsupportedError.
    entry = OdfEntry(
        full_path="content.xml",
        media_type="text/xml",
        size=0,
        checksum_type="",
        checksum=b"",
        cipher="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0#twofish-ctr",
        iv=bytes(16),
        key_derivation="PBKDF2",
        iterations=1024,
        key_size=32,
        salt=bytes(16),
        start_key="",
        start_key_size=20,
    )
    with pytest.raises(OdfUnsupportedError):
        verify(entry, "x", b"")
    with pytest.raises(OdfUnsupportedError):
        odf_hash_line(entry)
