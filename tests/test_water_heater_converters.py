import pytest

from gehomesdk.erd import ErdCode
from gehomesdk.erd.converters.water_heater import (
    ErdReadOnlyWaterHeaterTemperatureConverter,
)
from gehomesdk.erd.erd_configuration import _configuration as erd_config


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("04B0", 120.0),
        ("0514", 130.0),
        ("0258", 60.0),
    ],
)
def test_readonly_water_heater_temperature_decode(raw: str, expected: float) -> None:
    converter = ErdReadOnlyWaterHeaterTemperatureConverter()
    assert converter.erd_decode(raw) == expected
    assert converter.can_encode is False


@pytest.mark.parametrize(
    ("erd_code", "expected_hex"),
    [
        (ErdCode.WH_HEATER_T1_TEMPERATURE, "0x405f"),
        (ErdCode.WH_HEATER_T2_TEMPERATURE, "0x4060"),
        (ErdCode.WH_HEATER_T6_TEMPERATURE, "0x406e"),
        (ErdCode.WH_HEATER_GROUNDWATER_TEMPERATURE, "0x40b8"),
    ],
)
def test_water_heater_tank_temperature_erds_configured(
    erd_code: ErdCode, expected_hex: str
) -> None:
    assert erd_code.value == expected_hex
    configured = {entry.erd_code: entry for entry in erd_config}
    assert isinstance(
        configured[erd_code].converter,
        ErdReadOnlyWaterHeaterTemperatureConverter,
    )
