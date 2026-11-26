import pytest

from gehomesdk.erd import ErdCode
from gehomesdk.erd.converters.oven import (
    ErdAccentLightCapabilitiesConverter,
    ErdAccentLightSettingsConverter,
    ErdAccentLightStatusConverter,
)
from gehomesdk.erd.erd_configuration import _configuration as erd_config
from gehomesdk.erd.values.oven import (
    ErdAccentLightCapabilities,
    ErdAccentLightSettings,
)
from gehomesdk.exception import GeSetErdNotAllowedError


def test_accent_light_status_decode_custom_color() -> None:
    conv = ErdAccentLightStatusConverter(ErdCode.ACCENT_LIGHT_STATUS)
    decoded = conv.erd_decode("014221980033FF0000000000")

    assert decoded.custom_color_active is True
    assert decoded.brightness == 0x42
    assert decoded.color_temperature == 0x2198
    assert decoded.custom_color_code == 0x0033FF00
    assert decoded.rgb == (0x33, 0xFF, 0x00)
    assert decoded.reserved == b"\x00\x00\x00\x00"
    assert decoded.stringify() == "Custom #33FF00 (66%)"


def test_accent_light_status_decode_color_temp() -> None:
    conv = ErdAccentLightStatusConverter(ErdCode.ACCENT_LIGHT_STATUS)
    decoded = conv.erd_decode("002115180000000000000000")

    assert decoded.custom_color_active is False
    assert decoded.brightness == 33
    assert decoded.color_temperature == 5400
    assert decoded.custom_color_code == 0
    assert decoded.stringify() == "5400K (33%)"


def test_accent_light_request_roundtrip() -> None:
    conv = ErdAccentLightSettingsConverter(ErdCode.ACCENT_LIGHT_REQUEST)
    original = ErdAccentLightSettings(
        custom_color_active=True,
        brightness=0x42,
        color_temperature=0x2198,
        custom_color_code=0x0033FF00,
    )
    encoded = conv.erd_encode(original)
    assert encoded == "014221980033ff0000000000"

    decoded = conv.erd_decode(encoded)
    assert decoded.custom_color_active == original.custom_color_active
    assert decoded.brightness == original.brightness
    assert decoded.color_temperature == original.color_temperature
    assert decoded.custom_color_code == original.custom_color_code


def test_accent_light_capabilities_decode() -> None:
    conv = ErdAccentLightCapabilitiesConverter(ErdCode.ACCENT_LIGHT_CAPABILITIES)
    decoded = conv.erd_decode("21641518219801" + "00" * 9)

    assert decoded == ErdAccentLightCapabilities(
        brightness_min=33,
        brightness_max=100,
        color_temperature_min=5400,
        color_temperature_max=8600,
        custom_colors_available=True,
        raw_value="21641518219801" + "00" * 9,
    )
    assert "33-100%" in decoded.stringify()
    assert "5400-8600K" in decoded.stringify()


@pytest.mark.parametrize("raw", ["", "0102", "zzzz"])
def test_accent_light_invalid_or_short_payloads(raw: str) -> None:
    status_decoded = ErdAccentLightStatusConverter().erd_decode(raw)
    assert status_decoded.brightness == 0

    caps_decoded = ErdAccentLightCapabilitiesConverter().erd_decode(raw)
    assert caps_decoded.brightness_max == 0


def test_accent_light_read_only_erds_reject_encode() -> None:
    with pytest.raises(GeSetErdNotAllowedError):
        ErdAccentLightStatusConverter(ErdCode.ACCENT_LIGHT_STATUS).erd_encode(
            ErdAccentLightSettings()
        )
    with pytest.raises(GeSetErdNotAllowedError):
        ErdAccentLightCapabilitiesConverter(
            ErdCode.ACCENT_LIGHT_CAPABILITIES
        ).erd_encode(ErdAccentLightCapabilities())


def test_accent_light_erds_configured() -> None:
    configured = {entry.erd_code: entry for entry in erd_config}
    assert isinstance(
        configured[ErdCode.ACCENT_LIGHT_REQUEST].converter,
        ErdAccentLightSettingsConverter,
    )
    assert isinstance(
        configured[ErdCode.ACCENT_LIGHT_STATUS].converter,
        ErdAccentLightStatusConverter,
    )
    assert isinstance(
        configured[ErdCode.ACCENT_LIGHT_CAPABILITIES].converter,
        ErdAccentLightCapabilitiesConverter,
    )
