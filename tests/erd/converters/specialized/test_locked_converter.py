import pytest

from gehomesdk.erd.converters.specialized.erd_locked_converter import (
    ErdLockedBoolConverter,
    ErdLockedConverter,
)
from gehomesdk.erd.values.common import ErdInterfaceLocked


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", False),
        ("01", True),
        ("02", False),
        ("FF", False),
    ],
)
def test_locked_bool_decode(raw: str, expected: bool) -> None:
    converter = ErdLockedBoolConverter()
    assert converter.erd_decode(raw) is expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (True, "01"),
        (False, "02"),
        (None, "FF"),
    ],
)
def test_locked_bool_encode(value, expected: str) -> None:
    converter = ErdLockedBoolConverter()
    assert converter.erd_encode(value) == expected


def test_locked_enum_round_trip() -> None:
    converter = ErdLockedConverter()
    assert converter.erd_decode("01") == ErdInterfaceLocked.LOCKED
    assert converter.erd_decode("02") == ErdInterfaceLocked.UNLOCKED
    assert converter.erd_encode(ErdInterfaceLocked.LOCKED) == "0001"
    assert converter.erd_encode(ErdInterfaceLocked.UNLOCKED) == "0002"
