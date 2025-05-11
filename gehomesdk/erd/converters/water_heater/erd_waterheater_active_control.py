from gehomesdk.erd.values import ErdWaterHeaterActiveControl

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterActiveControlConverter(ErdReadWriteConverter[ErdWaterHeaterActiveControl]):
    def __init__(self, erd_code: str = "Unknown", length: int = 1):
        super().__init__(erd_code)
        self.length = length    
        
    def erd_decode(self, value) -> ErdWaterHeaterActiveControl:
        try:
            return ErdWaterHeaterActiveControl(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterActiveControl.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterActiveControl) -> str:
        return erd_encode_int(value.value, self.length)
