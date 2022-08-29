from gehomesdk.erd.values import ErdWaterHeaterModeHoursRemaining

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterModeHoursRemainingConverter(
    ErdReadWriteConverter[ErdWaterHeaterModeHoursRemaining]
):
    def erd_decode(self, value) -> ErdWaterHeaterModeHoursRemaining:
        try:
            return ErdWaterHeaterModeHoursRemaining(hours=int(value, 16))
        except ValueError:
            return ErdWaterHeaterModeHoursRemaining.OK

    def erd_encode(self, value: ErdWaterHeaterModeHoursRemaining) -> str:
        return erd_encode_int(value.hours)
