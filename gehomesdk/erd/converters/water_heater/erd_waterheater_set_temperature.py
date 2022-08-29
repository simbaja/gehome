from gehomesdk.erd.values import ErdWaterHeaterSetTemperature

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterSetTemperatureConverter(
    ErdReadWriteConverter[ErdWaterHeaterSetTemperature]
):
    def erd_decode(self, value) -> ErdWaterHeaterSetTemperature:
        try:
            return ErdWaterHeaterSetTemperature(int(value, 16) / 10)
        except ValueError:
            return ErdWaterHeaterSetTemperature.OK

    def erd_encode(self, value: ErdWaterHeaterSetTemperature) -> str:
        return erd_encode_int(int(value.temperature * 10))
