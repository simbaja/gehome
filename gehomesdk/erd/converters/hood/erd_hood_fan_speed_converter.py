from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.hood import *

class ErdHoodFanSpeedConverter(ErdReadWriteConverter[ErdHoodFanSpeed]):
    def erd_decode(self, value: str) -> ErdHoodFanSpeed:
        try:
            return ErdHoodFanSpeed(erd_decode_int(value))
        except:
            return ErdHoodFanSpeed.OFF

    def erd_encode(self, value: ErdHoodFanSpeed) -> str:
        return erd_encode_int(value.value, 1)
