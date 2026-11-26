"""Value types for range/oven accent lighting ERDs (0x5023, 0x5024, 0x5025)."""

from typing import NamedTuple


class ErdAccentLightSettings(NamedTuple):
    """Decoded accent lighting request/status (ERD 0x5023 / 0x5024)."""

    custom_color_active: bool = False
    brightness: int = 0
    color_temperature: int = 0
    custom_color_code: int = 0
    reserved: bytes = b"\x00\x00\x00\x00"
    raw_value: str | None = None

    @property
    def rgb(self) -> tuple[int, int, int]:
        """Return the (R, G, B) tuple extracted from custom_color_code."""
        return (
            (self.custom_color_code >> 16) & 0xFF,
            (self.custom_color_code >> 8) & 0xFF,
            self.custom_color_code & 0xFF,
        )

    def stringify(self, **kwargs) -> str:
        """Return a human-readable summary of the accent light settings."""
        if self.custom_color_active:
            return f"Custom #{self.custom_color_code & 0xFFFFFF:06X} ({self.brightness}%)"
        return f"{self.color_temperature}K ({self.brightness}%)"


class ErdAccentLightCapabilities(NamedTuple):
    """Decoded accent lighting limits/capabilities (ERD 0x5025)."""

    brightness_min: int = 0
    brightness_max: int = 0
    color_temperature_min: int = 0
    color_temperature_max: int = 0
    custom_colors_available: bool = False
    raw_value: str | None = None

    def stringify(self, **kwargs) -> str:
        """Return a human-readable summary of the accent light capabilities."""
        return (
            f"Brightness {self.brightness_min}-{self.brightness_max}%, "
            f"Temp {self.color_temperature_min}-{self.color_temperature_max}K, "
            f"Custom={self.custom_colors_available}"
        )
