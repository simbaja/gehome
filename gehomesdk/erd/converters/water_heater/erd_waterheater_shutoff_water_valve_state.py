from ...values import ErdWaterHeaterShutoffWaterValveState
from ..abstract import ErdReadWriteConverter
from ..primitives import *

class ErdWaterHeaterShutoffWaterValveStateConverter(ErdReadWriteConverter[ErdWaterHeaterShutoffWaterValveState]):
    def erd_decode(self, value) -> ErdWaterHeaterShutoffWaterValveState:
        try:
            return ErdWaterHeaterShutoffWaterValveState(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterShutoffWaterValveState.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterShutoffWaterValveState) -> str:
        return erd_encode_int(value.value)
