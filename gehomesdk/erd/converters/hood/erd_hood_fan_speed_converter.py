from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.hood import ErdHoodFanSpeed

class ErdHoodFanSpeedConverter(ErdReadWriteConverter[ErdHoodFanSpeed]):
    def erd_decode(self, value: str) -> ErdHoodFanSpeed:
        try:
            return ErdHoodFanSpeed(erd_decode_int(value))
        except Exception:
            return ErdHoodFanSpeed.OFF

    def erd_encode(self, value: ErdHoodFanSpeed) -> str:
        return erd_encode_int(value.value, 1)
