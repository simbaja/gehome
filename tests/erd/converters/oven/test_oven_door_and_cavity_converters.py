import pytest

from gehomesdk.erd import ErdCode
from gehomesdk.erd.converters.oven import (
    ErdOvenDoorStateConverter,
    ErdOvenEstimatedMinutesRemainingConverter,
    OvenRangesConverter,
)
from gehomesdk.erd.erd_configuration import _configuration as erd_config
from gehomesdk.erd.values.oven import (
    ErdOvenDoorState,
    ErdOvenEstimatedTimeStatus,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", ErdOvenDoorState.UNKNOWN),
        ("01", ErdOvenDoorState.OPEN),
        ("02", ErdOvenDoorState.CLOSED),
        ("03", ErdOvenDoorState.INITIAL_INSPECTION),
        ("FF", ErdOvenDoorState.UNKNOWN),
    ],
)
def test_oven_door_state_decode(raw: str, expected: ErdOvenDoorState) -> None:
    state = ErdOvenDoorStateConverter().erd_decode(raw)
    assert state == expected
    if expected == ErdOvenDoorState.OPEN:
        assert state.boolify() is True
    elif expected == ErdOvenDoorState.CLOSED:
        assert state.boolify() is False
    else:
        assert state.boolify() is None


def test_oven_estimated_minutes_remaining_decode() -> None:
    conv = ErdOvenEstimatedMinutesRemainingConverter()
    decoded = conv.erd_decode("001e0200")
    assert decoded.minutes_remaining == 30
    assert decoded.status == ErdOvenEstimatedTimeStatus.ACTIVE
    assert decoded.stringify() == "30 min (Active)"

    invalid = conv.erd_decode("00000000")
    assert invalid.status == ErdOvenEstimatedTimeStatus.INVALID
    assert invalid.stringify() == "Invalid"


def test_air_fry_min_max_temp_uses_oven_ranges() -> None:
    configured = {entry.erd_code: entry for entry in erd_config}
    entry = configured[ErdCode.OVEN_AIR_FRY_MIN_MAX_TEMP]
    assert isinstance(entry.converter, OvenRangesConverter)
    ranges = entry.erd_decode("01c2012c")  # upper=450, lower=300
    assert ranges.upper == 450
    assert ranges.lower == 300


def test_oven_door_and_cavity_erds_configured() -> None:
    configured = {entry.erd_code: entry for entry in erd_config}
    for code in (
        ErdCode.OVEN_AIR_FRY_MIN_MAX_TEMP,
        ErdCode.UPPER_OVEN_REQUEST_DOOR_OPEN,
        ErdCode.UPPER_OVEN_DOOR_STATE,
        ErdCode.UPPER_OVEN_DOOR_OPEN_REMOTE_ENABLED,
        ErdCode.LOWER_OVEN_REQUEST_DOOR_OPEN,
        ErdCode.LOWER_OVEN_DOOR_STATE,
        ErdCode.LOWER_OVEN_DOOR_OPEN_REMOTE_ENABLED,
        ErdCode.UPPER_OVEN_ESTIMATED_MINUTES_REMAINING,
        ErdCode.LOWER_OVEN_ESTIMATED_MINUTES_REMAINING,
    ):
        assert code in configured
