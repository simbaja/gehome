from gehomesdk.erd.values import ErdWaterHeaterMinMaxTemperature

from ..abstract import ErdReadOnlyConverter
from ..primitives import *


class ErdWaterHeaterMinMaxTemperatureConverter(
    ErdReadOnlyConverter[ErdWaterHeaterMinMaxTemperature]
):
    def erd_decode(self, value: str) -> ErdWaterHeaterMinMaxTemperature:
        raw_bytes = bytes.fromhex(value)
        lower_temp = int.from_bytes(raw_bytes[:2], "big") / 10
        upper_temp = int.from_bytes(raw_bytes[-2:], "big") / 10
        return ErdWaterHeaterMinMaxTemperature(lower=lower_temp, upper=upper_temp)
