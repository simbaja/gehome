import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdRinseOption, RinseOption, RINSE_OPTION_MAP

_LOGGER = logging.getLogger(__name__)

class RinseOptionConverter(ErdReadOnlyConverter[RinseOption]):
    def erd_decode(self, value: str) -> RinseOption:
        try:
            om = ErdRinseOption(erd_decode_int(value))
            return RINSE_OPTION_MAP[om].value
        except (KeyError, ValueError):
            return ErdRinseOption.INVALID
