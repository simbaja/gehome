from gehomesdk.erd.values import ErdWaterHeaterBoostState

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterBoostStateConverter(ErdReadWriteConverter[ErdWaterHeaterBoostState]):
    def erd_decode(self, value) -> ErdWaterHeaterBoostState:
        try:
            return ErdWaterHeaterBoostState(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterBoostState.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterBoostState) -> str:
        return value.value
