from gehomesdk.erd.values import ErdWaterHeaterSetTemperature

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterTemperatureConverter(
    ErdReadWriteConverter[float]
):
    def erd_decode(self, value) -> float:
        try:
            return erd_decode_int(value) / 10
        except ValueError:
            return 0

    def erd_encode(self, value: float) -> str:
        return erd_encode_int(int(value * 10))
