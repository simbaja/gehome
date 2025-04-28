from gehomesdk.erd.values import ErdWaterHeaterBoostControl

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterBoostControlConverter(ErdReadWriteConverter[ErdWaterHeaterBoostControl]):
    def __init__(self, erd_code: str = "Unknown", length: int = 1):
        super().__init__(erd_code)
        self.length = length
        
    def erd_decode(self, value) -> ErdWaterHeaterBoostControl:
        try:
            return ErdWaterHeaterBoostControl(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterBoostControl.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterBoostControl) -> str:
        return value.value
