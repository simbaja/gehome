import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdTemperatureOption, TemperatureOption, TEMPERATURE_OPTION_MAP

_LOGGER = logging.getLogger(__name__)

class TemperatureOptionConverter(ErdReadOnlyConverter[TemperatureOption]):
    def erd_decode(self, value: str) -> TemperatureOption:
        try:
            om = ErdTemperatureOption(erd_decode_int(value))
            return TEMPERATURE_OPTION_MAP[om].value
        except (KeyError, ValueError):
            return ErdTemperatureOption.NA
