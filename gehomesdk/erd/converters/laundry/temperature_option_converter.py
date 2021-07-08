import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdTemperatureOption, ErdTemperatureNewOption, TemperatureOption, TEMPERATURE_OPTION_MAP, TEMPERATURENEW_OPTION_MAP

_LOGGER = logging.getLogger(__name__)

class TemperatureOptionConverter(ErdReadOnlyConverter[TemperatureOption]):
    def erd_decode(self, value: str) -> TemperatureOption:
        try:
            om = ErdTemperatureOption(erd_decode_int(value))
            return TEMPERATURE_OPTION_MAP[om].value
        except (KeyError, ValueError):
            return TemperatureOption.DASH

class TemperatureNewOptionConverter(ErdReadOnlyConverter[TemperatureOption]):
    def erd_decode(self, value: str) -> TemperatureOption:
        try:
            om = ErdTemperatureNewOption(erd_decode_int(value))
            return TEMPERATURENEW_OPTION_MAP[om].value
        except (KeyError, ValueError):
            return TemperatureOption.DASH
