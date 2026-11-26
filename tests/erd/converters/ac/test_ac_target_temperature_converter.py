import pytest

from gehomesdk.erd.converters.ac.erd_ac_target_temperature_converter import (
    ErdAcTargetTemperatureConverter,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("42", 66),
        ("0042", 66),
        ("4200", 66),
        ("4600", 70),
        ("0046", 70),
        ("0100", 256),  # swapped=1, outside plausible window -> keep raw 256
    ],
)
def test_decode_either_byte_order(raw: str, expected: int) -> None:
    converter = ErdAcTargetTemperatureConverter()
    assert converter.erd_decode(raw) == expected


def test_encode() -> None:
    converter = ErdAcTargetTemperatureConverter()
    assert converter.erd_encode(66) == "0042"
