import logging

from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.coffee_maker import *

_LOGGER = logging.getLogger(__name__)

class ErdCcmBrewSettingsConverter(ErdReadWriteConverter[ErdCcmBrewSettings]):

    def erd_decode(self, value: str) -> ErdCcmBrewSettings:
        try:
            brew_strength = ErdCcmBrewStrength(erd_decode_int(value[0:2]))
            brew_temperature = erd_decode_int(value[2:4])
            number_of_cups = erd_decode_int(value[4:6])
            return ErdCcmBrewSettings(number_of_cups, brew_strength, brew_temperature, value)
        except:
            _LOGGER.exception("Could not construct brew settings, using default.")
            return ErdCcmBrewSettings(raw_value=value)

    def erd_encode(self, value: ErdCcmBrewSettings) -> str:
        """
        Encode the brew settings (brew strength, temperatures, # of cups)
        """
        return (
            erd_encode_int(value.brew_strength.value, 1) + 
            erd_encode_int(value.brew_temperature, 1) +
            erd_encode_int(value.number_of_cups, 1)
        )