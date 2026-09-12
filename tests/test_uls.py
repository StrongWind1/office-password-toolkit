# SPDX-License-Identifier: Apache-2.0
"""Tests for the Jet ULS (User-Level Security) 3DES password codec.

Test vectors were generated on a Windows XP SP3 lab VM running Access 2003 SP3
via DAO.DBEngine.36 ``CreateUser`` calls.  The 40-byte ``MSysAccounts.Password``
fields were extracted from the resulting ``.mdw`` workgroup files with Jackcess
4.0.11 + jackcess-encrypt 4.0.4 (CryptCodecProvider).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from office_password_toolkit.crypto.uls import (
    WORKGROUP_KEY,
    WorkgroupIdentity,
    decode_password,
    decode_pid,
    decode_workgroup_identity,
    encode_password,
    is_blank,
    is_mdw,
    parse_mdw,
)


# --- Single-character password vectors (passwords 'a' through 'p') ---------
# Created as users ua-up in Fresh.mdw on 10.0.0.205 (XP SP3, Access 2003).
# The password is the single lowercase letter; the engine uppercases it.

_SINGLE_CHAR_VECTORS: dict[str, str] = {
    "a": "acb29254de02720e" + "6952ad67f3d5e1e6" * 4,
    "b": "863e10ec9df6edd0" + "6952ad67f3d5e1e6" * 4,
    "c": "8f0982ca56c50bcf" + "6952ad67f3d5e1e6" * 4,
    "d": "8366753a91e9fe08" + "6952ad67f3d5e1e6" * 4,
    "e": "2b4696d796adadcd" + "6952ad67f3d5e1e6" * 4,
    "f": "5e22ab25bc6d839f" + "6952ad67f3d5e1e6" * 4,
    "g": "19c7d633cad0a0e8" + "6952ad67f3d5e1e6" * 4,
    "h": "3d63eab9578e0266" + "6952ad67f3d5e1e6" * 4,
    "i": "f9dc35ce891bfaa5" + "6952ad67f3d5e1e6" * 4,
    "j": "81a420ad1d5950c9" + "6952ad67f3d5e1e6" * 4,
    "k": "18cc1bd308c041b5" + "6952ad67f3d5e1e6" * 4,
    "l": "601b8238fe693220" + "6952ad67f3d5e1e6" * 4,
    "m": "9fade5de81f3599b" + "6952ad67f3d5e1e6" * 4,
    "n": "6f78050bb18782b0" + "6952ad67f3d5e1e6" * 4,
    "o": "61a723b552483d92" + "6952ad67f3d5e1e6" * 4,
    "p": "8382dc028d5af24e" + "6952ad67f3d5e1e6" * 4,
}

# --- Multi-character password vectors (from System-vectors.mdw) -------------

_MULTI_CHAR_VECTORS: dict[str, str] = {
    "TestPw1": "da203f8e0bd06174e697af638a2a22e4" + "6952ad67f3d5e1e6" * 3,
    "UserPw2": "64c80c84477acb532d92f726400acb9b" + "6952ad67f3d5e1e6" * 3,
    "P@ss!": "cf53e4e95cbefa15837eb22095b4b641" + "6952ad67f3d5e1e6" * 3,
}

# --- Blank password ---------------------------------------------------------

_BLANK_HEX: str = "6952ad67f3d5e1e6" * 5


class TestDecodePassword:
    """Verify 3DES-EDE2 decode against real vectors."""

    @pytest.mark.parametrize("password", sorted(_SINGLE_CHAR_VECTORS.keys()))
    def test_single_char(self, password: str) -> None:
        field = bytes.fromhex(_SINGLE_CHAR_VECTORS[password])
        assert decode_password(field) == password.upper()

    @pytest.mark.parametrize("password", sorted(_MULTI_CHAR_VECTORS.keys()))
    def test_multi_char(self, password: str) -> None:
        field = bytes.fromhex(_MULTI_CHAR_VECTORS[password])
        assert decode_password(field) == password

    def test_blank_password(self) -> None:
        field = bytes.fromhex(_BLANK_HEX)
        assert decode_password(field) == ""

    def test_blank_is_detected(self) -> None:
        field = bytes.fromhex(_BLANK_HEX)
        assert is_blank(field) is True

    def test_non_blank_is_detected(self) -> None:
        field = bytes.fromhex(_SINGLE_CHAR_VECTORS["a"])
        assert is_blank(field) is False


class TestEncodePassword:
    """Verify the encode (inverse) round-trips correctly."""

    @pytest.mark.parametrize("password", sorted(_SINGLE_CHAR_VECTORS.keys()))
    def test_single_char_roundtrip(self, password: str) -> None:
        field = bytes.fromhex(_SINGLE_CHAR_VECTORS[password])
        # DAO uppercased these before storing, so encode the uppercase version.
        encoded = encode_password(password.upper())
        assert encoded == field

    @pytest.mark.parametrize("password", sorted(_MULTI_CHAR_VECTORS.keys()))
    def test_multi_char_roundtrip(self, password: str) -> None:
        field = bytes.fromhex(_MULTI_CHAR_VECTORS[password])
        encoded = encode_password(password)
        assert encoded == field
        assert decode_password(encoded) == password

    def test_blank_roundtrip(self) -> None:
        encoded = encode_password("")
        assert encoded == bytes.fromhex(_BLANK_HEX)

    def test_case_preserving(self) -> None:
        lower = encode_password("testpw1")
        upper = encode_password("TESTPW1")
        mixed = encode_password("TestPw1")
        assert lower != upper
        assert decode_password(lower) == "testpw1"
        assert decode_password(upper) == "TESTPW1"
        assert decode_password(mixed) == "TestPw1"

    def test_decode_encode_identity(self) -> None:
        for password in ["Hello", "x", "LongPassword20ch"]:
            field = encode_password(password)
            decoded = decode_password(field)
            assert decoded == password


class TestJet3Password:
    """Verify Jet 3 (Access 95/97) password decode with 16-byte fields."""

    def test_jet3_roundtrip(self) -> None:
        for password in ["HELLO", "test", "x"]:
            encoded = encode_password(password, jet3=True)
            assert len(encoded) == 16
            decoded = decode_password(encoded, jet3=True)
            assert decoded == password

    def test_jet3_blank(self) -> None:
        blank = WORKGROUP_KEY * 2
        assert decode_password(blank, jet3=True) == ""


class TestWorkgroupIdentity:
    """Verify workgroup identity 3DES decode."""

    def test_decode_returns_dataclass(self) -> None:
        fake_sid = b"\x01\x00" + b"\x00" * (_WORKGROUP_BLOCKS_COUNT * 8)
        result = decode_workgroup_identity(fake_sid)
        assert result is not None
        assert isinstance(result, WorkgroupIdentity)

    def test_short_sid_returns_none(self) -> None:
        assert decode_workgroup_identity(b"\x01\x02") is None


# Constant for test use.
_WORKGROUP_BLOCKS_COUNT = 12


class TestPidDecode:
    """Verify PID recovery from SID fields."""

    def test_builtin_short_sid(self) -> None:
        assert decode_pid(b"\x03\x01") == ""

    def test_empty_input(self) -> None:
        assert decode_pid(b"") == ""

    def test_real_corpus_user_pid(self) -> None:
        sid = bytes.fromhex("fe0d6c45be36ae669bf6ee043efe666e76700982de968e463d70")
        assert decode_pid(sid) == "CorpusPID1234"

    def test_real_test_user_pid(self) -> None:
        sid = bytes.fromhex("fe0c2aee39ccaf2335b0f39e938e25589f21f257e9149f")
        assert decode_pid(sid) == "TestPID45678"


class TestSidEncode:
    """Verify full SID generation from PID + account name (forward direction)."""

    def test_byte_identical_ua(self) -> None:
        from office_password_toolkit.crypto.uls import encode_sid

        expected = bytes.fromhex("fe0822143fb17177ad037a44")
        assert encode_sid("PIDA1234", "ua") == expected

    def test_byte_identical_corpus_user(self) -> None:
        from office_password_toolkit.crypto.uls import encode_sid

        expected = bytes.fromhex("fe0d6c45be36ae669bf6ee043efe666e76700982de968e463d70")
        assert encode_sid("CorpusPID1234", "corpus_user") == expected

    def test_byte_identical_test_user(self) -> None:
        from office_password_toolkit.crypto.uls import encode_sid

        expected = bytes.fromhex("fe0c2aee39ccaf2335b0f39e938e25589f21f257e9149f")
        assert encode_sid("TestPID45678", "test_user") == expected

    def test_roundtrip_encode_decode(self) -> None:
        from office_password_toolkit.crypto.uls import encode_sid

        for pid, name in [("MyPID1234", "admin"), ("ABCDE", "testuser"), ("LongPID567890", "user1")]:
            sid = encode_sid(pid, name)
            assert decode_pid(sid) == pid


class TestMdwDetection:
    """Verify MDW file signature detection."""

    def test_valid_signature(self) -> None:
        header = b"\x00\x01\x00\x00Jet System DB" + b"\x00" * 200
        assert is_mdw(header) is True

    def test_invalid_signature(self) -> None:
        header = b"\x00\x01\x00\x00Standard Jet DB" + b"\x00" * 200
        assert is_mdw(header) is False

    def test_too_short(self) -> None:
        assert is_mdw(b"\x00\x01") is False


_CORPUS = Path(__file__).parent / "corpus"
_MDW_PLAIN = _CORPUS / "lab" / "o2003__system_plain.mdw"
_MDW_ULS = _CORPUS / "lab" / "o2003__system_uls_pw.mdw"


class TestJet3Mdw:
    """Verify the Jet 3 MDW parsing path with a synthetic workgroup file."""

    @staticmethod
    def _build_jet3_mdw() -> bytes:
        """Construct a minimal synthetic Jet 3 MDW with one user account."""
        from office_password_toolkit.crypto.uls import (
            _ACCOUNT_SECTION_SIZE,
            _JET3_ACCOUNT_SECTION_OFFSET,
            _MDW_ENCODING_KEY_OFFSET,
            _MDW_RC4_KEY,
            _MDW_RC4_REGION_LEN,
            _MDW_RC4_REGION_START,
            _rc4,
        )

        mdw_size = _JET3_ACCOUNT_SECTION_OFFSET + _ACCOUNT_SECTION_SIZE + 0x100
        mdw = bytearray(mdw_size)
        mdw[0x04 : 0x04 + 13] = b"Jet System DB"

        region_plain = bytearray(_MDW_RC4_REGION_LEN)
        key_off = _MDW_ENCODING_KEY_OFFSET - _MDW_RC4_REGION_START
        enc_key = b"\x42\x42\x42\x42"
        region_plain[key_off : key_off + 4] = enc_key
        mdw[_MDW_RC4_REGION_START : _MDW_RC4_REGION_START + _MDW_RC4_REGION_LEN] = _rc4(_MDW_RC4_KEY, bytes(region_plain))

        section = bytearray(_ACCOUNT_SECTION_SIZE)
        section[0:2] = b"\x01\x01"
        section[4:6] = (4).to_bytes(2, "little")
        section[0x08:0x0A] = (1).to_bytes(2, "little")
        section[0x0A:0x0C] = (0x100).to_bytes(2, "little")
        section[0x100] = 0x00
        section[0x101:0x105] = b"root"

        encrypted = _rc4(enc_key, bytes(section))
        mdw[_JET3_ACCOUNT_SECTION_OFFSET : _JET3_ACCOUNT_SECTION_OFFSET + _ACCOUNT_SECTION_SIZE] = encrypted
        return bytes(mdw)

    def test_jet3_mdw_parses(self) -> None:
        result = parse_mdw(self._build_jet3_mdw())
        assert result is not None
        assert result.jet3 is True

    def test_jet3_mdw_has_accounts(self) -> None:
        result = parse_mdw(self._build_jet3_mdw())
        assert result is not None
        assert len(result.accounts) >= 1


class TestJet3Vba:
    """Verify DPB scanning works on Jet 3 format databases."""

    def test_dpb_scan_on_jet3_mdb(self, tmp_path: Path) -> None:
        from office_password_toolkit.formats.access import _scan_vba_dpb

        mdb = bytearray(0x1000)
        mdb[0x04 : 0x04 + 15] = b"Standard Jet DB"
        mdb[0x14] = 0x00
        dpb_line = b'\r\nDPB="D0D224C725C725C7"\r\n'
        mdb[0x200 : 0x200 + len(dpb_line)] = dpb_line
        p = tmp_path / "jet3_vba.mdb"
        p.write_bytes(bytes(mdb))
        assert _scan_vba_dpb(p) == "D0D224C725C725C7"


class TestMdwCorpus:
    """Verify MDW parsing against the two real .mdw files in tests/corpus/lab/."""

    def test_plain_mdw_parses(self) -> None:
        result = parse_mdw(_MDW_PLAIN.read_bytes())
        assert result is not None
        assert not result.jet3

    def test_plain_mdw_has_builtin_accounts(self) -> None:
        result = parse_mdw(_MDW_PLAIN.read_bytes())
        assert result is not None
        names = {a.name.lower() for a in result.accounts}
        assert "admin" in names

    def test_plain_mdw_no_passwords(self) -> None:
        result = parse_mdw(_MDW_PLAIN.read_bytes())
        assert result is not None
        pw_accounts = [a for a in result.accounts if a.password]
        assert pw_accounts == []

    def test_uls_mdw_parses(self) -> None:
        result = parse_mdw(_MDW_ULS.read_bytes())
        assert result is not None
        assert not result.jet3

    def test_uls_mdw_recovers_all_passwords(self) -> None:
        result = parse_mdw(_MDW_ULS.read_bytes())
        assert result is not None
        passwords = {a.name: a.password for a in result.accounts if a.password}
        assert passwords == {"admin": "TestPw1", "corpus_user": "UserPw2", "test_user": "P@ss!"}

    def test_uls_mdw_recovers_pids(self) -> None:
        result = parse_mdw(_MDW_ULS.read_bytes())
        assert result is not None
        pids = {a.name: a.pid for a in result.accounts if a.pid}
        assert pids["corpus_user"] == "CorpusPID1234"
        assert pids["test_user"] == "TestPID45678"

    def test_uls_mdw_classifies_groups(self) -> None:
        result = parse_mdw(_MDW_ULS.read_bytes())
        assert result is not None
        groups = {a.name for a in result.accounts if a.is_group}
        assert "Users" in groups
        assert "admin" not in groups

    def test_uls_mdw_identifies_builtins(self) -> None:
        result = parse_mdw(_MDW_ULS.read_bytes())
        assert result is not None
        builtins = {a.name for a in result.accounts if a.is_builtin}
        assert "admin" in builtins
        assert "corpus_user" not in builtins

    def test_plain_mdw_workgroup_identity_is_default(self) -> None:
        result = parse_mdw(_MDW_PLAIN.read_bytes())
        assert result is not None
        assert result.workgroup is not None
        assert result.workgroup.workgroup_id.strip() == ""
        assert result.workgroup.owner_name.strip() == ""
        assert result.workgroup.organisation.strip() == ""


class TestMdwParseExtended:
    """Verify MDW file parsing with extra .mdw files from lab VMs (skipped if absent)."""

    def test_parse_fresh_mdw(self) -> None:
        mdw_path = Path("/tmp/mdw_vectors/corpus/gen/Fresh.mdw")
        if not mdw_path.exists():
            pytest.skip("Lab MDW file not available")
        result = parse_mdw(mdw_path.read_bytes())
        assert result is not None
        assert not result.jet3
        passwords = {a.name: a.password for a in result.accounts if a.password}
        assert len(passwords) >= 16


class TestWorkgroupKey:
    """Verify workgroup key constant matches msjet40.dll."""

    def test_length(self) -> None:
        assert len(WORKGROUP_KEY) == 8

    def test_value(self) -> None:
        assert WORKGROUP_KEY == bytes.fromhex("6952ad67f3d5e1e6")
