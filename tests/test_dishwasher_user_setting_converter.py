import pytest

from gehomesdk.erd.converters.dishwasher.erd_user_setting_converter import (
    ErdUserSettingConverter,
)
from gehomesdk.erd.values.dishwasher.erd_user_setting import (
    ErdUserSetting,
    UserSetting,
    UserCycleSetting,
)


# 30008C and 30028C were observed on a Fisher & Paykel AAFD dishwasher (0x200 is the
# control lock). 043B24 is a GE GDF530PGM0CC with controls locked (simbaja/ha_gehome#59).
# FFFFFF also sets bits the SDK does not model (0x30, 0x4000).
@pytest.mark.parametrize("raw", ["30008C", "30028C", "043B24", "000000", "FFFFFF", "8C"])
def test_round_trip_preserves_raw_value(raw: str) -> None:
    converter = ErdUserSettingConverter()

    assert converter.erd_encode(converter.erd_decode(raw)).upper() == raw.upper().rjust(6, "0")


def test_encode_is_three_bytes() -> None:
    converter = ErdUserSettingConverter()

    # mute is bit 23, in the third byte
    encoded = converter.erd_encode(ErdUserSetting(mute=UserSetting.ENABLE))

    assert encoded.upper() == "800000"


def test_changing_one_field_keeps_other_bits() -> None:
    converter = ErdUserSettingConverter()
    current = converter.erd_decode("30008C")

    locked = converter.erd_encode(current._replace(lock_control=UserSetting.ENABLE))
    unlocked = converter.erd_encode(
        converter.erd_decode(locked)._replace(lock_control=UserSetting.DISABLE)
    )

    assert locked.upper() == "30028C"
    assert unlocked.upper() == "30008C"


def test_out_of_range_field_keeps_reported_bits() -> None:
    converter = ErdUserSettingConverter()
    current = converter.erd_decode("30008C")

    encoded = converter.erd_encode(current._replace(lock_control=UserSetting.INVALID))

    assert encoded.upper() == "30008C"


def test_encode_without_raw_value_uses_fields_only() -> None:
    converter = ErdUserSettingConverter()

    encoded = converter.erd_encode(
        ErdUserSetting(cycle_mode=UserCycleSetting.RINSE, lock_control=UserSetting.ENABLE)
    )

    assert encoded.upper() == "00020C"
