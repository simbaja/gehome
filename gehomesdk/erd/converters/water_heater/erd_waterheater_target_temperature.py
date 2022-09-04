from gehomesdk.erd.values import ErdWaterHeaterTargetTemperature

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterTargetTemperatureConverter(
    ErdReadWriteConverter[ErdWaterHeaterTargetTemperature]
):
    def erd_decode(self, value) -> ErdWaterHeaterTargetTemperature:
        try:
            return ErdWaterHeaterTargetTemperature(int(value, 16) / 10)
        except ValueError:
            return ErdWaterHeaterTargetTemperature.OK

    def erd_encode(self, value: ErdWaterHeaterTargetTemperature) -> str:
        return erd_encode_int(int(value.temperature * 10))
