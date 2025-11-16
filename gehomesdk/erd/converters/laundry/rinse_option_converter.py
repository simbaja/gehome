import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdRinseOption

_LOGGER = logging.getLogger(__name__)

class RinseOptionConverter(ErdReadOnlyConverter[ErdRinseOption]):
    def erd_decode(self, value: str) -> ErdRinseOption:
        try:
            return ErdRinseOption(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdRinseOption.INVALID
