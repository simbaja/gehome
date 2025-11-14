from gehomesdk.erd.values import ErdWaterHeaterMixingValveTankCapacity

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterMixingValveTankCapacityConverter(ErdReadWriteConverter[ErdWaterHeaterMixingValveTankCapacity]):
    def erd_decode(self, value) -> ErdWaterHeaterMixingValveTankCapacity:
        try:
            return ErdWaterHeaterMixingValveTankCapacity(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterMixingValveTankCapacity.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterMixingValveTankCapacity) -> str:
        return value.value
