from gehomesdk.erd.values import ErdWaterHeaterBoostMode

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterBoostModeConverter(ErdReadWriteConverter[ErdWaterHeaterBoostMode]):
    def erd_decode(self, value) -> ErdWaterHeaterBoostMode:
        try:
            return ErdWaterHeaterBoostMode(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterBoostMode.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterBoostMode) -> str:
        return value.value
