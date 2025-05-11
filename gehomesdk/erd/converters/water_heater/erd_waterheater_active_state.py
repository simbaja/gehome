from gehomesdk.erd.values import ErdWaterHeaterActiveState

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterActiveStateConverter(ErdReadWriteConverter[ErdWaterHeaterActiveState]):
    def __init__(self, erd_code: str = "Unknown", length: int = 1):
        super().__init__(erd_code)
        self.length = length
        
    def erd_decode(self, value) -> ErdWaterHeaterActiveState:
        try:
            return ErdWaterHeaterActiveState(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterActiveState.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterActiveState) -> str:
        return erd_encode_int(value.value, self.length)