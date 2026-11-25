from datetime import timedelta

import pytest

from gehomesdk.erd import ErdCode, ErdDataType
from gehomesdk.erd.converters.ac import (
    ErdSacAlertsConverter,
    ErdSacSelfCleanReminderDurationConverter,
    ErdSacSelfCleanSupportConverter,
)
from gehomesdk.erd.erd_configuration import _configuration as erd_config
from gehomesdk.erd.values.ac import (
    ErdSacSelfCleanReminderDuration,
    ErdSacSelfCleanSupport,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", ErdSacSelfCleanSupport.NOT_SUPPORTED),
        ("01", ErdSacSelfCleanSupport.SUPPORTED),
        ("FF", ErdSacSelfCleanSupport.UNKNOWN),
    ],
)
def test_sac_self_clean_support_decode(raw: str, expected: ErdSacSelfCleanSupport) -> None:
    converter = ErdSacSelfCleanSupportConverter()
    assert converter.erd_decode(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", ErdSacSelfCleanReminderDuration.HOURS_250),
        ("01", ErdSacSelfCleanReminderDuration.HOURS_500),
        ("02", ErdSacSelfCleanReminderDuration.HOURS_1000),
        ("03", ErdSacSelfCleanReminderDuration.HOURS_1500),
        ("04", ErdSacSelfCleanReminderDuration.NEVER),
    ],
)
def test_sac_self_clean_reminder_duration_round_trip(
    raw: str, expected: ErdSacSelfCleanReminderDuration
) -> None:
    converter = ErdSacSelfCleanReminderDurationConverter()
    assert converter.erd_decode(raw) == expected
    assert converter.erd_encode(expected) == raw


def test_sac_alerts_decode() -> None:
    converter = ErdSacAlertsConverter()
    none_active = converter.erd_decode("0000")
    assert none_active.boolify() is False
    assert none_active.stringify() == "None"

    first_and_banner = converter.erd_decode("0900")  # bits 8 and 11
    assert first_and_banner.self_clean_first_alert is True
    assert first_and_banner.self_clean_second_alert is False
    assert first_and_banner.self_clean_third_alert is False
    assert first_and_banner.self_clean_in_app_banner_alert is True
    assert first_and_banner.boolify() is True


def test_sac_dishwasher_and_ccm_erds_configured() -> None:
    configured = {entry.erd_code: entry for entry in erd_config}
    assert ErdCode.DISHWASHER_LEAK_DETECTED in configured
    assert ErdCode.CCM_DESCALE_REMAINING_CYCLES in configured
    for code in (
        ErdCode.SAC_SELF_CLEAN_OUTDOOR_TEMP_PERMITS,
        ErdCode.SAC_SELF_CLEAN_SUPPORT,
        ErdCode.SAC_SELF_CLEAN_STATUS,
        ErdCode.SAC_SELF_CLEAN_REQUEST,
        ErdCode.SAC_SELF_CLEAN_REMINDER_DURATION,
        ErdCode.SAC_SELF_CLEAN_ALERT_COUNTDOWN,
        ErdCode.SAC_ALERTS,
    ):
        assert code in configured

    countdown_entry = configured[ErdCode.SAC_SELF_CLEAN_ALERT_COUNTDOWN]
    assert countdown_entry.data_type == ErdDataType.TIMESPAN
    assert countdown_entry.erd_decode("00015f90") == timedelta(minutes=90000)
    assert countdown_entry.erd_decode("0000ffff") == timedelta(minutes=65535)
    assert countdown_entry.erd_decode("ffffffff") is None
