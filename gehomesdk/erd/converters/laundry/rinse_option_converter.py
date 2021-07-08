import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdRinseOption

_LOGGER = logging.getLogger(__name__)

class RinseOptionConverter(ErdReadOnlyConverter[ErdRinseOption]):
    def erd_decode(self, value: str) -> ErdRinseOption:
        try:
            return ErdRinseOption(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdRinseOption.INVALID
