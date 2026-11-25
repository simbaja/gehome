from gehomesdk.erd import ErdCode
from gehomesdk.erd.converters.dishwasher.erd_error_converter import (
    ErdErrorStateConverter,
)
from gehomesdk.erd.erd_configuration import _configuration as erd_config


def test_decode_no_error() -> None:
    converter = ErdErrorStateConverter()
    state = converter.erd_decode("0000")
    assert state.id == 0
    assert state.active is False
    assert state.raw_value == "0000"


def test_decode_preserves_full_error_code() -> None:
    converter = ErdErrorStateConverter()
    state = converter.erd_decode("0103")
    assert state.id == 0x0103
    assert state.active is True
    assert state.raw_value == "0103"


def test_upper_error_erd_is_configured() -> None:
    assert ErdCode.DISHWASHER_UPPER_ERROR.value == "0x3208"
    assert any(
        entry.erd_code == ErdCode.DISHWASHER_UPPER_ERROR
        and isinstance(entry.converter, ErdErrorStateConverter)
        for entry in erd_config
    )
