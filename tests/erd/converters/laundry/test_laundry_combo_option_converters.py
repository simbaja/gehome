from datetime import timedelta

import pytest

from gehomesdk.erd import ErdCode, ErdDataType
from gehomesdk.erd.converters.laundry import (
    ErdDeepFillIncrementalOptionConverter,
    ErdLaundryControlLockOptionConverter,
    ErdSoilLevelOptionConverter,
    ErdWashTempOptionConverter,
    SpinTimeLevelConverter,
)
from gehomesdk.erd.erd_configuration import _configuration as erd_config
from gehomesdk.erd.values.laundry import (
    ErdDeepFillIncrementalOption,
    ErdLaundryControlLockOption,
    ErdSoilLevelOption,
    ErdSpinTimeLevel,
    ErdWashTempOption,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", ErdLaundryControlLockOption.DISABLED),
        ("01", ErdLaundryControlLockOption.UNLOCKED),
        ("02", ErdLaundryControlLockOption.LOCKED),
        ("FF", ErdLaundryControlLockOption.UNKNOWN),
    ],
)
def test_control_lock_option_decode(
    raw: str, expected: ErdLaundryControlLockOption
) -> None:
    assert ErdLaundryControlLockOptionConverter().erd_decode(raw) == expected


def test_deep_fill_incremental_option_decode() -> None:
    conv = ErdDeepFillIncrementalOptionConverter()
    assert conv.erd_decode("00") == ErdDeepFillIncrementalOption.OFF
    assert conv.erd_decode("01") == ErdDeepFillIncrementalOption.INCREMENTAL
    assert conv.erd_decode("02") == ErdDeepFillIncrementalOption.MAX_FILL


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", ErdWashTempOption.DISABLE),
        ("01", ErdWashTempOption.TAP_COLD),
        ("05", ErdWashTempOption.WARM),
        ("08", ErdWashTempOption.TEMP_20C),
        ("12", ErdWashTempOption.EXTRA_WARM),
    ],
)
def test_wash_temp_option_decode(raw: str, expected: ErdWashTempOption) -> None:
    assert ErdWashTempOptionConverter().erd_decode(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", ErdSoilLevelOption.DISABLED),
        ("03", ErdSoilLevelOption.NORMAL),
        ("06", ErdSoilLevelOption.AUTO),
    ],
)
def test_soil_level_option_decode(raw: str, expected: ErdSoilLevelOption) -> None:
    assert ErdSoilLevelOptionConverter().erd_decode(raw) == expected


def test_spin_time_level_supports_max() -> None:
    assert SpinTimeLevelConverter().erd_decode("06") == ErdSpinTimeLevel.MAX


def test_combo_option_erds_configured() -> None:
    configured = {entry.erd_code: entry for entry in erd_config}
    for code in (
        ErdCode.LAUNDRY_CONTROL_LOCK_OPTION,
        ErdCode.LAUNDRY_DEEP_FILL_INCREMENTAL_OPTION,
        ErdCode.LAUNDRY_EXTRA_RINSE_OPTION,
        ErdCode.LAUNDRY_WATER_TEMP_OPTION,
        ErdCode.LAUNDRY_SOIL_LEVEL_OPTION,
        ErdCode.LAUNDRY_COMBO_WASH_MODE_STATUS,
        ErdCode.LAUNDRY_COMBO_DRY_MODE_STATUS,
        ErdCode.LAUNDRY_SMART_HQ_REMOTE_OPTION,
        ErdCode.LAUNDRY_REMOTE_SPIN_TIME_LEVEL,
        ErdCode.LAUNDRY_SMART_SOFTENER_DISPENSE_TIME,
        ErdCode.LAUNDRY_WASH_COMPLETE_NOTIFICATION_OPTION,
    ):
        assert code in configured

    softener = configured[ErdCode.LAUNDRY_SMART_SOFTENER_DISPENSE_TIME]
    assert softener.erd_code.value == "0x2140"
    assert softener.data_type == ErdDataType.TIMESPAN
    assert softener.erd_decode("000f") == timedelta(seconds=15)
