# SPDX-License-Identifier: Apache-2.0
"""Tests for MSISAM encryption (Microsoft Money 2002+).

Test vectors from ``money2008-pwd.mny`` in the JackcessEncrypt test data,
confirmed with password ``TEST12345`` via thewd-hub ``moneyCrk.cpp`` algorithm
and Jackcess ``MSISAMCryptCodecHandler.java``.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from office_password_toolkit.crypto.msisam import (
    MsisamParams,
    decrypt_file,
    decrypt_page,
    extract_params,
    is_msisam_encrypted,
    msisam_hash_line,
    verify_password,
)

_CORPUS = Path(__file__).parent / "corpus" / "lab"
_MONEY_2008 = _CORPUS / "money2008-pwd.mny"
_MONEY_2001 = _CORPUS / "money2001-pwd.mny"
_MONEY_PLUS = _CORPUS / "money-plus-sample-blank.mny"
_KNOWN_PASSWORD = "TEST12345"


class TestMsisamDetection:
    """Verify MSISAM encryption detection."""

    def test_money_2008_is_msisam(self) -> None:
        data = _MONEY_2008.read_bytes()
        assert is_msisam_encrypted(data)

    def test_money_2001_is_not_msisam(self) -> None:
        data = _MONEY_2001.read_bytes()
        assert not is_msisam_encrypted(data)

    def test_short_data(self) -> None:
        assert not is_msisam_encrypted(b"\x00" * 100)


class TestParamExtraction:
    """Verify MSISAM parameter extraction from the file header."""

    def test_extract_from_money_2008(self) -> None:
        data = _MONEY_2008.read_bytes()
        params = extract_params(data)
        assert params is not None
        assert params.use_sha1 is True
        assert len(params.salt_full) == 8
        assert len(params.salt_check) == 4
        assert len(params.crypt_check) == 4
        assert params.salt_check == params.salt_full[:4]

    def test_extract_from_non_msisam_returns_none(self) -> None:
        data = _MONEY_2001.read_bytes()
        assert extract_params(data) is None


class TestPasswordVerification:
    """Verify MSISAM password checking."""

    def test_correct_password(self) -> None:
        params = extract_params(_MONEY_2008.read_bytes())
        assert params is not None
        assert verify_password(params, _KNOWN_PASSWORD) is True

    def test_wrong_password(self) -> None:
        params = extract_params(_MONEY_2008.read_bytes())
        assert params is not None
        assert verify_password(params, "WRONG") is False

    def test_blank_password_fails(self) -> None:
        params = extract_params(_MONEY_2008.read_bytes())
        assert params is not None
        assert verify_password(params, "") is False

    def test_case_insensitive(self) -> None:
        params = extract_params(_MONEY_2008.read_bytes())
        assert params is not None
        assert verify_password(params, "test12345") is True
        assert verify_password(params, "Test12345") is True


class TestHashExtraction:
    """Verify MSISAM hash line format."""

    def test_hash_line_format(self) -> None:
        params = extract_params(_MONEY_2008.read_bytes())
        assert params is not None
        line = msisam_hash_line(params)
        assert line.startswith("$office-msisam$")
        parts = line.split("$")
        assert parts[0] == ""
        assert parts[1] == "office-msisam"
        assert parts[2] in ("0", "1")
        assert len(parts[3]) == 16
        assert len(parts[4]) == 8


class TestPageDecryption:
    """Verify MSISAM page-level decryption."""

    def test_page_above_max_is_passthrough(self) -> None:
        params = extract_params(_MONEY_2008.read_bytes())
        assert params is not None
        page = b"\xaa" * 0x1000
        assert decrypt_page(params, _KNOWN_PASSWORD, 0x0F, page) == page

    def test_page_1_decrypts(self) -> None:
        data = _MONEY_2008.read_bytes()
        params = extract_params(data)
        assert params is not None
        page1_enc = data[0x1000:0x2000]
        page1_dec = decrypt_page(params, _KNOWN_PASSWORD, 1, page1_enc)
        assert page1_dec != page1_enc


class TestFileDecryption:
    """Verify full MSISAM file decryption."""

    def test_decrypt_with_correct_password(self) -> None:
        data = _MONEY_2008.read_bytes()
        decrypted = decrypt_file(data, _KNOWN_PASSWORD)
        assert len(decrypted) == len(data)
        assert decrypted != data
        assert decrypted[0x1000:0x1004] != data[0x1000:0x1004]

    def test_decrypt_with_wrong_password_raises(self) -> None:
        data = _MONEY_2008.read_bytes()
        with pytest.raises(ValueError, match="Incorrect password"):
            decrypt_file(data, "WRONG")


class TestAccessHandlerIntegration:
    """Verify MSISAM is wired into the Access handler."""

    def test_money_2008_gates(self) -> None:
        from office_password_toolkit.formats.access import AccessHandler

        handler = AccessHandler()
        gates = handler.gates(_MONEY_2008)
        open_gates = [g for g in gates if g.gate.value == "open"]
        assert len(open_gates) == 1
        assert open_gates[0].recovery.value == "crack"

    def test_money_2008_extract(self) -> None:
        from office_password_toolkit.formats.access import AccessHandler

        handler = AccessHandler()
        hashes = handler.extract(_MONEY_2008)
        assert len(hashes) >= 1
        msisam_hashes = [h for h in hashes if h.scheme.value == "msisam"]
        assert len(msisam_hashes) == 1
        assert msisam_hashes[0].value.startswith("$office-msisam$")

    def test_money_2008_decrypt(self, tmp_path: Path) -> None:
        from office_password_toolkit.formats.access import AccessHandler

        handler = AccessHandler()
        out = tmp_path / "decrypted.mny"
        handler.decrypt(_MONEY_2008, out, _KNOWN_PASSWORD)
        assert out.exists()
        assert out.stat().st_size == _MONEY_2008.stat().st_size


class TestMoneyPlusSunset:
    """Verify MSISAM against a real Money Plus Sunset sample file (blank password)."""

    def test_detect_encrypted(self) -> None:
        assert is_msisam_encrypted(_MONEY_PLUS.read_bytes())

    def test_blank_password_verifies(self) -> None:
        params = extract_params(_MONEY_PLUS.read_bytes())
        assert params is not None
        assert verify_password(params, "") is True

    def test_wrong_password_fails(self) -> None:
        params = extract_params(_MONEY_PLUS.read_bytes())
        assert params is not None
        assert verify_password(params, "wrong") is False

    def test_extract_hash(self) -> None:
        from office_password_toolkit.formats.access import AccessHandler

        hashes = AccessHandler().extract(_MONEY_PLUS)
        msisam = [h for h in hashes if h.scheme.value == "msisam"]
        assert len(msisam) == 1

    def test_decrypt(self, tmp_path: Path) -> None:
        out = tmp_path / "sample_dec.mny"
        data = _MONEY_PLUS.read_bytes()
        result = decrypt_file(data, "")
        out.write_bytes(result)
        assert out.stat().st_size == _MONEY_PLUS.stat().st_size
