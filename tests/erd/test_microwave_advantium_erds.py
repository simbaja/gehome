"""Tests for ERDs published by Advantium-style built-in microwaves (e.g. PWB7030)."""
from datetime import timedelta
from unittest.mock import MagicMock

from gehomesdk import ErdCode, ErdDataType
from gehomesdk.ge_appliance import GeAppliance


def _make_appliance(mac: str) -> GeAppliance:
    client = MagicMock()
    client.client_priority = 0
    return GeAppliance(mac, client)


def test_kitchen_time_remaining_is_minutes():
    """0x0050 is u16 minutes; a 1 minute kitchen timer is published as 0001."""
    appliance = _make_appliance("00:00:00:00:00:01")
    appliance.update_erd_value(ErdCode.ADVANTIUM_KITCHEN_TIME_REMAINING, "0001")
    assert appliance.get_erd_value(ErdCode.ADVANTIUM_KITCHEN_TIME_REMAINING) == timedelta(minutes=1)


def test_microwave_power_watts():
    """0x5c12 is u16 watts; a 1000 W microwave publishes 03E8."""
    appliance = _make_appliance("00:00:00:00:00:02")
    appliance.update_erd_value("0x5c12", "03E8")
    assert appliance.get_erd_value(ErdCode.MICROWAVE_POWER_WATTS) == 1000
    assert appliance.get_erd_code_data_type(ErdCode.MICROWAVE_POWER_WATTS) == ErdDataType.INT
