"""Converters for range/oven accent lighting ERDs (0x5023, 0x5024, 0x5025)."""

from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter
from ...values.oven import (
    ErdAccentLightCapabilities,
    ErdAccentLightSettings,
)


def _decode_accent_light_settings(value: str) -> ErdAccentLightSettings:
    """Decode a 12-byte accent light settings payload (0x5023 / 0x5024)."""
    if not value:
        return ErdAccentLightSettings()
    try:
        raw = bytes.fromhex(value)
        if len(raw) < 12:
            return ErdAccentLightSettings(raw_value=value)
        return ErdAccentLightSettings(
            custom_color_active=bool(raw[0]),
            brightness=raw[1],
            color_temperature=int.from_bytes(raw[2:4], "big"),
            custom_color_code=int.from_bytes(raw[4:8], "big"),
            reserved=raw[8:12],
            raw_value=value,
        )
    except ValueError:
        return ErdAccentLightSettings(raw_value=value)


class ErdAccentLightSettingsConverter(ErdReadWriteConverter[ErdAccentLightSettings]):
    """Read/write converter for accent light request ERD (0x5023)."""

    def erd_decode(self, value: str) -> ErdAccentLightSettings:
        return _decode_accent_light_settings(value)

    def erd_encode(self, value: ErdAccentLightSettings) -> str:
        reserved = value.reserved[:4].ljust(4, b"\x00")
        payload = (
            (1 if value.custom_color_active else 0).to_bytes(1, "big")
            + value.brightness.to_bytes(1, "big")
            + value.color_temperature.to_bytes(2, "big")
            + value.custom_color_code.to_bytes(4, "big")
            + reserved
        )
        return payload.hex()


class ErdAccentLightStatusConverter(ErdReadOnlyConverter[ErdAccentLightSettings]):
    """Read-only converter for accent light status ERD (0x5024)."""

    def erd_decode(self, value: str) -> ErdAccentLightSettings:
        return _decode_accent_light_settings(value)


class ErdAccentLightCapabilitiesConverter(
    ErdReadOnlyConverter[ErdAccentLightCapabilities]
):
    """Read-only converter for accent light capabilities ERD (0x5025)."""

    def erd_decode(self, value: str) -> ErdAccentLightCapabilities:
        if not value:
            return ErdAccentLightCapabilities()
        try:
            raw = bytes.fromhex(value)
            if len(raw) < 7:
                return ErdAccentLightCapabilities(raw_value=value)
            return ErdAccentLightCapabilities(
                brightness_min=raw[0],
                brightness_max=raw[1],
                color_temperature_min=int.from_bytes(raw[2:4], "big"),
                color_temperature_max=int.from_bytes(raw[4:6], "big"),
                custom_colors_available=bool(raw[6]),
                raw_value=value,
            )
        except ValueError:
            return ErdAccentLightCapabilities(raw_value=value)
