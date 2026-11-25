import logging

from ..abstract import ErdReadWriteConverter
from ...values.coffee_maker import ErdCcmGrindBrewSettings, ErdCcmGrindBrewStrength

_LOGGER = logging.getLogger(__name__)


class ErdCcmGrindBrewSettingsConverter(ErdReadWriteConverter[ErdCcmGrindBrewSettings]):
    """Converter for the 12-byte Cafe Speciality Grind & Brew settings (ERD 0x9051)."""

    def erd_decode(self, value: str) -> ErdCcmGrindBrewSettings:
        try:
            raw = bytes.fromhex(value)
            if len(raw) < 12:
                raise ValueError(f"Expected 12 bytes, got {len(raw)}")
            try:
                strength = ErdCcmGrindBrewStrength(raw[4])
            except ValueError:
                strength = ErdCcmGrindBrewStrength.UNKNOWN
            return ErdCcmGrindBrewSettings(
                gold_toggle=bool(raw[0]),
                bloom_toggle=bool(raw[1]),
                single_toggle=bool(raw[3]),
                brew_strength=strength,
                brew_temperature=raw[5],
                ounces=raw[6],
                number_of_cups=raw[7],
                bloom_time=raw[11],
                raw_value=value,
            )
        except Exception:
            _LOGGER.exception("Could not construct grind & brew settings, using default.")
            return ErdCcmGrindBrewSettings(raw_value=value)

    def erd_encode(self, value: ErdCcmGrindBrewSettings) -> str:
        payload = bytearray(12)
        if value.raw_value:
            try:
                existing = bytes.fromhex(value.raw_value)
                if len(existing) >= 12:
                    payload = bytearray(existing[:12])
            except ValueError:
                pass

        payload[0] = 1 if value.gold_toggle else 0
        payload[1] = 1 if value.bloom_toggle else 0
        payload[3] = 1 if value.single_toggle else 0
        if value.brew_strength != ErdCcmGrindBrewStrength.UNKNOWN:
            payload[4] = value.brew_strength.value
        payload[5] = int(value.brew_temperature)
        payload[6] = int(value.ounces)
        payload[7] = int(value.number_of_cups)
        payload[11] = int(value.bloom_time)
        return payload.hex()
