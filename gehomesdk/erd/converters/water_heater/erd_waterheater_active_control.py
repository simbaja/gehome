from gehomesdk.erd.values import ErdWaterHeaterActiveControl

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterActiveControlConverter(ErdReadWriteConverter[ErdWaterHeaterActiveControl]):
    def erd_decode(self, value) -> ErdWaterHeaterActiveControl:
        try:
            return ErdWaterHeaterActiveControl(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterActiveControl.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterActiveControl) -> str:
        return value.value
