from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values import ErdEndTone

class ErdEndToneConverter(ErdReadWriteConverter[ErdEndTone]):
    def erd_decode(self, value: str) -> ErdEndTone:
        try:
            return ErdEndTone(value)
        except ValueError:
            return ErdEndTone.NA
    def erd_encode(self, value: ErdEndTone) -> str:
        if value == ErdEndTone.NA:
            raise ValueError("Invalid EndTone value")
        return value.value
