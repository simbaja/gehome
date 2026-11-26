import pytest

from gehomesdk.erd.converters.laundry.dryer_extended_tumble_option_request_converter import (
    ErdDryerExtendedTumbleOptionRequestConverter,
)
from gehomesdk.erd.converters.laundry.remote_start_extended_tumble_converter import (
    ErdRemoteStartExtendedTumbleConverter,
)
from gehomesdk.erd.converters.laundry.tumble_status_converter import (
    TumbleStatusConverter,
)
from gehomesdk.erd.values.laundry import (
    ErdDryerExtendedTumbleOptionRequest,
    ErdRemoteStartExtendedTumble,
    ErdTumbleStatus,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (ErdRemoteStartExtendedTumble.START_EXTENDED_TUMBLE, "00"),
        (True, "00"),
        (ErdRemoteStartExtendedTumble.REQUEST_PROCESSED, "ff"),
        (False, "ff"),
    ],
)
def test_remote_start_extended_tumble_encode(value, expected: str) -> None:
    converter = ErdRemoteStartExtendedTumbleConverter()
    assert converter.erd_encode(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (ErdDryerExtendedTumbleOptionRequest.DISABLED, "00"),
        (False, "00"),
        (ErdDryerExtendedTumbleOptionRequest.ENABLED, "01"),
        (True, "01"),
    ],
)
def test_extended_tumble_option_request_encode(value, expected: str) -> None:
    converter = ErdDryerExtendedTumbleOptionRequestConverter()
    assert converter.erd_encode(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (ErdTumbleStatus.DISABLE, "00"),
        (False, "00"),
        (ErdTumbleStatus.ENABLE, "01"),
        (True, "01"),
    ],
)
def test_tumble_status_encode(value, expected: str) -> None:
    converter = TumbleStatusConverter()
    assert converter.erd_encode(value) == expected
