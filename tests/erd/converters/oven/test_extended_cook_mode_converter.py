from gehomesdk.erd.converters.oven.erd_extended_cook_mode_converter import (
    ErdExtendedCookModeConverter,
)
from gehomesdk.erd.values.oven import ErdOvenCookMode, OVEN_COOK_MODE_MAP


def test_extended_cook_mode_converter_decodes_airfry_no_option() -> None:
    converter = ErdExtendedCookModeConverter()

    decoded = converter.erd_decode(
        "00 00 40 00 00 00 00 C0 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    )

    assert decoded == {ErdOvenCookMode.AIRFRY}


def test_extended_cook_mode_converter_decodes_all_airfry_variants() -> None:
    converter = ErdExtendedCookModeConverter()

    assert converter.erd_decode(
        "00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    ) == {ErdOvenCookMode.AIRFRY}
    assert converter.erd_decode(
        "00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    ) == {ErdOvenCookMode.AIRFRY_PROBE}
    assert converter.erd_decode(
        "00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    ) == {ErdOvenCookMode.AIRFRY_DELAYSTART}
    assert converter.erd_decode(
        "00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    ) == {ErdOvenCookMode.AIRFRY_PROBE_DELAYSTART}


def test_extended_cook_mode_converter_ignores_non_airfry_bits() -> None:
    converter = ErdExtendedCookModeConverter()

    decoded = converter.erd_decode(
        "00 00 00 00 00 00 00 C0 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    )

    assert decoded == set()


def test_extended_cook_mode_converter_returns_empty_for_zero_value() -> None:
    converter = ErdExtendedCookModeConverter()

    assert converter.erd_decode(
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    ) == set()


def test_airfry_modes_map_to_expected_flags() -> None:
    plain = OVEN_COOK_MODE_MAP[ErdOvenCookMode.AIRFRY]
    probe = OVEN_COOK_MODE_MAP[ErdOvenCookMode.AIRFRY_PROBE]
    delayed = OVEN_COOK_MODE_MAP[ErdOvenCookMode.AIRFRY_DELAYSTART]
    delayed_probe = OVEN_COOK_MODE_MAP[ErdOvenCookMode.AIRFRY_PROBE_DELAYSTART]

    assert not plain.delayed and not plain.probe
    assert not probe.delayed and probe.probe
    assert delayed.delayed and not delayed.probe
    assert delayed_probe.delayed and delayed_probe.probe
