from gehomesdk.erd.values import ErdWaterHeaterBoostMode

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterBoostModeConverter(ErdReadWriteConverter[ErdWaterHeaterBoostMode]):
    def __init__(self, erd_code: str = "Unknown", length: int = 1):
        super().__init__(erd_code)
        self.length = length
        
    def erd_decode(self, value) -> ErdWaterHeaterBoostMode:
        try:
            return ErdWaterHeaterBoostMode(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterBoostMode.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterBoostMode) -> str:
        return erd_encode_int(value.value, self.length)
