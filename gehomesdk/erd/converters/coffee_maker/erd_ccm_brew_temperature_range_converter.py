from gehomesdk.erd.values.coffee_maker.common_enums import ErdCcmBrewTemperatureRange
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

class ErdCcmBrewTemperatureRangeConverter(ErdReadOnlyConverter[ErdCcmBrewTemperatureRange]):

    # Values at the API level are in Fahrenheit regardless of ErdCode.TEMPERATURE_UNIT setting
    ERD_CCM_BREW_TEMPERATURE_MIN = 185
    ERD_CCM_BREW_TEMPERATURE_MAX = 205

    def erd_decode(self, value: str) -> ErdCcmBrewTemperatureRange:
        try:
            min = erd_decode_int(value[0:2])
            max = erd_decode_int(value[2:4])
            if(min == 0 or max == 0):
                min = self.ERD_CCM_BREW_TEMPERATURE_MIN
                max = self.ERD_CCM_BREW_TEMPERATURE_MAX
            return ErdCcmBrewTemperatureRange(min, max, value)
        except:
            return ErdCcmBrewTemperatureRange(self.ERD_CCM_BREW_TEMPERATURE_MIN, self.ERD_CCM_BREW_TEMPERATURE_MAX, value)