"""Tests for GeAppliance.get_raw_erd_value()."""
from unittest.mock import MagicMock

from gehomesdk import ErdCode
from gehomesdk.ge_appliance import GeAppliance


def _make_appliance(mac: str) -> GeAppliance:
    client = MagicMock()
    client.client_priority = 0
    return GeAppliance(mac, client)


def test_raw_value_returns_none_when_never_received():
    appliance = _make_appliance("00:00:00:00:00:01")
    assert appliance.get_raw_erd_value("0x5900") is None
    assert appliance.get_raw_erd_value(ErdCode.USER_INTERFACE_LOCKED) is None


def test_raw_value_round_trip_for_unregistered_code():
    """Unregistered hex codes preserve their raw wire value verbatim."""
    appliance = _make_appliance("00:00:00:00:00:02")
    appliance.update_erd_value("0x5900", "03")
    assert appliance.get_raw_erd_value("0x5900") == "03"


def test_raw_value_round_trip_for_registered_code():
    """Registered codes (decoded by an upstream converter) also preserve
    the raw bytes — the decoded cache and the raw cache live in parallel."""
    appliance = _make_appliance("00:00:00:00:00:03")
    appliance.update_erd_value(ErdCode.USER_INTERFACE_LOCKED, "01")
    assert appliance.get_raw_erd_value(ErdCode.USER_INTERFACE_LOCKED) == "01"
    # lookup by equivalent hex string resolves to the same entry
    assert appliance.get_raw_erd_value("0x0004") == "01"


def test_raw_value_is_overwritten_on_update():
    appliance = _make_appliance("00:00:00:00:00:04")
    appliance.update_erd_value("0x5900", "01")
    appliance.update_erd_value("0x5900", "03")
    assert appliance.get_raw_erd_value("0x5900") == "03"
