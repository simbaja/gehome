import pytest

from gehomesdk.erd import ErdCode
from gehomesdk.erd.converters.coffee_maker import (
    ErdCcmGrindBrewSettingsConverter,
    ErdCcmGrinderSettingConverter,
)
from gehomesdk.erd.erd_configuration import _configuration as erd_config
from gehomesdk.erd.values.coffee_maker import (
    ErdCcmGrindBrewSettings,
    ErdCcmGrindBrewStrength,
)


def test_grind_brew_settings_decode_and_round_trip() -> None:
    converter = ErdCcmGrindBrewSettingsConverter()
    # Real payload from ha_gehome#251: gold=1, bloom=0, single=0, strength=GOLD(3),
    # temp=200 (0xc8), oz=24 (0x18), cups=10 (0x0a), bloom_time=0
    raw = "0100000003c8180a00000000"
    decoded = converter.erd_decode(raw)

    assert decoded.gold_toggle is True
    assert decoded.bloom_toggle is False
    assert decoded.single_toggle is False
    assert decoded.brew_strength == ErdCcmGrindBrewStrength.GOLD
    assert decoded.brew_temperature == 200
    assert decoded.ounces == 24
    assert decoded.number_of_cups == 10
    assert decoded.bloom_time == 0
    assert decoded.raw_value == raw

    assert converter.erd_encode(decoded) == raw


def test_grind_brew_settings_preserves_unmodeled_bytes() -> None:
    converter = ErdCcmGrindBrewSettingsConverter()
    current = converter.erd_decode("0001aa0001c80c06bbccdd0f")
    updated = current._replace(
        brew_strength=ErdCcmGrindBrewStrength.BOLD,
        brew_temperature=195,
        number_of_cups=8,
        ounces=16,
    )

    encoded = converter.erd_encode(updated)
    assert encoded == "0001aa0002c31008bbccdd0f"


def test_grind_brew_settings_encode_without_raw_value() -> None:
    converter = ErdCcmGrindBrewSettingsConverter()
    encoded = converter.erd_encode(
        ErdCcmGrindBrewSettings(
            brew_strength=ErdCcmGrindBrewStrength.LIGHT,
            brew_temperature=185,
            ounces=12,
            number_of_cups=6,
            bloom_time=15,
        )
    )
    assert encoded == "0000000000b90c060000000f"


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("00", True),
        ("01", False),
        ("FF", None),
    ],
)
def test_grinder_setting_decode_encode(raw: str, expected) -> None:
    converter = ErdCcmGrinderSettingConverter()
    assert converter.erd_decode(raw) is expected
    assert converter.erd_encode(expected) == raw


def test_grind_brew_erds_are_configured() -> None:
    configured = {entry.erd_code: entry for entry in erd_config}
    assert isinstance(
        configured[ErdCode.CCM_GRIND_BREW_SETTINGS].converter,
        ErdCcmGrindBrewSettingsConverter,
    )
    assert isinstance(
        configured[ErdCode.CCM_GRINDER_SETTING].converter,
        ErdCcmGrinderSettingConverter,
    )
    assert ErdCode.CCM_BREW_BASKET_MISSING in configured
    assert ErdCode.CCM_GRIND_BREW_PROFILE_1 in configured
    assert ErdCode.CCM_GRIND_BREW_PROFILE_2 in configured
    assert ErdCode.CCM_GRIND_BREW_PROFILE_3 in configured
