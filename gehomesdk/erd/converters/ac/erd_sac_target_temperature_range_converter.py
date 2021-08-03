from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdSacTargetTemperatureRange

class ErdSacTargetTemperatureRangeConverter(ErdReadOnlyConverter[ErdSacTargetTemperatureRange]):
    def erd_decode(self, value: str) -> ErdSacTargetTemperatureRange:
        try:
            min = erd_decode_int(value[0:2])
            max = erd_decode_int(value[2:4])
            if(min == 255 or max == 255):
                min = 60
                max = 86
            return ErdSacTargetTemperatureRange(min, max, value)
        except:
            return ErdSacTargetTemperatureRange(60, 86, value)