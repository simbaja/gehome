import pytest

from gehomesdk.erd.converters.water_filter.erd_filter_manual_mode_converter import (
    ErdFilterManualModeConverter,
)
from gehomesdk.erd.values import ErdWaterFilterManualMode


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (ErdWaterFilterManualMode.NOT_MANUAL, "00"),
        (ErdWaterFilterManualMode.MANUAL, "01"),
        ("00", "00"),
        ("01", "01"),
    ],
)
def test_manual_mode_encode(value, expected: str) -> None:
    converter = ErdFilterManualModeConverter()
    assert converter.erd_encode(value) == expected
