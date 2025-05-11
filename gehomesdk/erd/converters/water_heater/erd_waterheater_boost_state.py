from gehomesdk.erd.values import ErdWaterHeaterBoostState

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterBoostStateConverter(ErdReadWriteConverter[ErdWaterHeaterBoostState]):
    def __init__(self, erd_code: str = "Unknown", length: int = 1):
        super().__init__(erd_code)
        self.length = length
        
    def erd_decode(self, value) -> ErdWaterHeaterBoostState:
        try:
            return ErdWaterHeaterBoostState(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterBoostState.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterBoostState) -> str:
        return erd_encode_int(value.value, self.length)
