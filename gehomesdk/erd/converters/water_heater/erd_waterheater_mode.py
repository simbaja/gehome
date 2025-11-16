from ...values import ErdWaterHeaterMode
from ..abstract import ErdReadWriteConverter
from ..primitives import *

class ErdWaterHeaterModeConverter(ErdReadWriteConverter[ErdWaterHeaterMode]):
    def erd_decode(self, value) -> ErdWaterHeaterMode:
        try:
            return ErdWaterHeaterMode(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterMode.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterMode) -> str:
        return erd_encode_int(value.value)
