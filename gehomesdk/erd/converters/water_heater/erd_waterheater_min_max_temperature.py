from gehomesdk.erd.values import ErdWaterHeaterMinMaxTemperature

from ..abstract import ErdReadOnlyConverter
from ..primitives import *


class ErdWaterHeaterMinMaxTemperatureConverter(
    ErdReadOnlyConverter[ErdWaterHeaterMinMaxTemperature]
):

    ERD_WATERHEATER_TEMPERATURE_MIN = 100
    ERD_WATERHEATER_TEMPERATURE_MAX = 140

    def erd_decode(self, value: str) -> ErdWaterHeaterMinMaxTemperature:

        try:
            lower_temp = erd_decode_int(value[:4]) / 10
            upper_temp = erd_decode_int(value[-4:]) / 10
        except ValueError:
            return ErdWaterHeaterMinMaxTemperature(
                self.ERD_WATERHEATER_TEMPERATURE_MIN,
                self.ERD_WATERHEATER_TEMPERATURE_MAX,
            )
        if lower_temp == 0 or upper_temp == 0:
            lower_temp = self.ERD_WATERHEATER_TEMPERATURE_MIN
            upper_temp = self.ERD_WATERHEATER_TEMPERATURE_MAX
        return ErdWaterHeaterMinMaxTemperature(lower=lower_temp, upper=upper_temp)
