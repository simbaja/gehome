from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int

# A byte-swapped 16-bit value only counts as a setpoint inside this Fahrenheit window.
_PLAUSIBLE_MIN_F = 32
_PLAUSIBLE_MAX_F = 140


class ErdAcTargetTemperatureConverter(ErdReadWriteConverter[int]):
    def erd_decode(self, value: str) -> int:
        try:
            number = erd_decode_int(value)
        except Exception:
            return 86

        # Some AC units report 0x7003 as little-endian 2-byte hex (e.g. "4200" = 66 F)
        # instead of big-endian ("0042"). Swap bytes when that yields a plausible setpoint.
        if 0xFF < number <= 0xFFFF:
            swapped = ((number & 0xFF) << 8) | (number >> 8)
            if _PLAUSIBLE_MIN_F <= swapped <= _PLAUSIBLE_MAX_F:
                return swapped
        return number

    def erd_encode(self, value: int) -> str:
        return erd_encode_int(value, 2)
