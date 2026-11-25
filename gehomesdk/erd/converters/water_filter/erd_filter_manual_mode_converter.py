from typing import Union

from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values import ErdWaterFilterManualMode

class ErdFilterManualModeConverter(ErdReadWriteConverter[ErdWaterFilterManualMode]):
    def erd_decode(self, value) -> ErdWaterFilterManualMode:
        try:
            return ErdWaterFilterManualMode(value)
        except ValueError:
            return ErdWaterFilterManualMode.NOT_MANUAL

    def erd_encode(self, value: Union[ErdWaterFilterManualMode, str]) -> str:
        if isinstance(value, ErdWaterFilterManualMode):
            return value.value
        return ErdWaterFilterManualMode(str(value)).value
