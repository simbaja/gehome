import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdRinseOption, RinseOption, RINSE_OPTION_MAP

_LOGGER = logging.getLogger(__name__)

class RinseOptionConverter(ErdReadOnlyConverter[RinseOption]):
    def erd_decode(self, value: str) -> RinseOption:
        try:
            om = ErdRinseOption(erd_decode_int(value))
            return RINSE_OPTION_MAP[om].value
        except (KeyError, ValueError):
            return ErdRinseOption.NA
