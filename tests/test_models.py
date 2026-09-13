"""Tests for Status/Product enums and gate_status/gate_scheme_tag mapping functions."""

from __future__ import annotations

import pytest

from office_password_toolkit.models import (
    DetectResult,
    Gate,
    GateType,
    HashScheme,
    Product,
    RecoveryClass,
    Status,
    _RECOVERY_TO_STATUS,
    ContainerKind,
    gate_scheme_tag,
    gate_status,
)


# --- Status enum -------------------------------------------------------------


class TestStatusEnum:
    """Verify Status enum has all expected members with correct values."""

    def test_status_enum_values(self) -> None:
        assert Status.ENCRYPTED == "encrypted"
        assert Status.REMOVABLE == "removable"
        assert Status.TRIVIAL == "trivial"
        assert Status.INFO == "info"
        assert Status.BLOCKED == "blocked"
        assert Status.OPEN == "open"
        assert len(Status) == 6


# --- Product enum -------------------------------------------------------------


class TestProductEnum:
    """Verify Product enum has all expected members with correct values."""

    def test_product_enum_values(self) -> None:
        expected = {
            "WORD": "Word",
            "EXCEL": "Excel",
            "POWERPOINT": "PowerPoint",
            "ONENOTE": "OneNote",
            "OUTLOOK": "Outlook",
            "ACCESS": "Access",
            "VISIO": "Visio",
            "PROJECT": "Project",
            "PUBLISHER": "Publisher",
            "INFOPATH": "InfoPath",
            "OPENDOCUMENT": "OpenDocument",
            "UNKNOWN": "Unknown",
        }
        for name, value in expected.items():
            member = Product[name]
            assert member.value == value, f"Product.{name} should be {value!r}"
        assert len(Product) == len(expected)


# --- gate_status mapping -----------------------------------------------------


class TestGateStatus:
    """Verify gate_status maps gates to the correct CLI status."""

    def test_gate_status_encrypted(self) -> None:
        gate = Gate(gate=GateType.OPEN, recovery=RecoveryClass.CRACK)
        assert gate_status(gate) is Status.ENCRYPTED

    def test_gate_status_removable(self) -> None:
        gate = Gate(gate=GateType.PROTECT_SHEET, recovery=RecoveryClass.STRIP)
        assert gate_status(gate) is Status.REMOVABLE

    def test_gate_status_trivial(self) -> None:
        gate = Gate(gate=GateType.MAIL_BODY, recovery=RecoveryClass.DECODE)
        # MAIL_BODY is special-cased to INFO regardless of recovery class.
        assert gate_status(gate) is Status.INFO

        # Use a gate type that actually falls through to the recovery mapping.
        gate_modify = Gate(gate=GateType.MODIFY, recovery=RecoveryClass.DECODE)
        assert gate_status(gate_modify) is Status.TRIVIAL

    def test_gate_status_blocked(self) -> None:
        # IRM is always BLOCKED, regardless of the recovery class value.
        for rc in RecoveryClass:
            gate = Gate(gate=GateType.IRM, recovery=rc)
            assert gate_status(gate) is Status.BLOCKED, f"IRM with recovery={rc.name} should be BLOCKED"

    def test_gate_status_info(self) -> None:
        gate = Gate(gate=GateType.SIGNATURE, recovery=RecoveryClass.NONE)
        assert gate_status(gate) is Status.INFO

    def test_gate_status_mail_body_is_info(self) -> None:
        """MAIL_BODY is special-cased to INFO like SIGNATURE."""
        gate = Gate(gate=GateType.MAIL_BODY, recovery=RecoveryClass.DECODE)
        assert gate_status(gate) is Status.INFO


# --- gate_scheme_tag mapping --------------------------------------------------


class TestGateSchemeTag:
    """Verify gate_scheme_tag maps gates to the correct short scheme string."""

    def test_gate_scheme_tag_encrypted(self) -> None:
        gate = Gate(
            gate=GateType.OPEN,
            recovery=RecoveryClass.CRACK,
            scheme=HashScheme.OFFICE_2013,
        )
        assert gate_scheme_tag(gate) == "agile-sha512"

    def test_gate_scheme_tag_protection(self) -> None:
        gate = Gate(gate=GateType.PROTECT_SHEET, recovery=RecoveryClass.STRIP)
        assert gate_scheme_tag(gate) == "sheets"

    def test_gate_scheme_tag_signature(self) -> None:
        gate = Gate(gate=GateType.SIGNATURE, recovery=RecoveryClass.NONE)
        assert gate_scheme_tag(gate) == "signed"

    def test_gate_scheme_tag_vba(self) -> None:
        gate = Gate(
            gate=GateType.VBA_PROJECT,
            recovery=RecoveryClass.CRACK,
            scheme=HashScheme.VBA_SHA1,
        )
        assert gate_scheme_tag(gate) == "macros"

    def test_gate_scheme_tag_irm(self) -> None:
        gate = Gate(gate=GateType.IRM, recovery=RecoveryClass.NONE)
        assert gate_scheme_tag(gate) == "rights-managed"

    def test_gate_scheme_tag_fallback_gap(self) -> None:
        """An OPEN+CRACK gate with no scheme tags as 'gap', not 'open'."""
        gate = Gate(gate=GateType.OPEN, recovery=RecoveryClass.CRACK)
        assert gate_scheme_tag(gate) == "gap"

    def test_gate_scheme_tag_fallback_other(self) -> None:
        """A non-OPEN gate with no scheme falls back to the gate type value."""
        gate = Gate(gate=GateType.OPEN, recovery=RecoveryClass.BYPASS)
        assert gate_scheme_tag(gate) == "open"


# --- Recovery completeness ----------------------------------------------------


class TestRecoveryCoverage:
    """Every RecoveryClass member must have an entry in _RECOVERY_TO_STATUS."""

    def test_all_recovery_classes_have_status(self) -> None:
        missing = [rc for rc in RecoveryClass if rc not in _RECOVERY_TO_STATUS]
        assert missing == [], f"RecoveryClass members missing from _RECOVERY_TO_STATUS: {missing}"


# --- DetectResult accepts product ---------------------------------------------


class TestDetectResult:
    """Verify DetectResult can be constructed with a Product value."""

    def test_detect_result_has_product(self) -> None:
        result = DetectResult(
            path="test.xlsx",
            container=ContainerKind.OOXML_ZIP,
            extension=".xlsx",
            encrypted=False,
            product=Product.EXCEL,
        )
        assert result.product is Product.EXCEL
