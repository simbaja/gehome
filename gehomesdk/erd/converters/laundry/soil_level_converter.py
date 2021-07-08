import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdSoilLevel

_LOGGER = logging.getLogger(__name__)

class SoilLevelConverter(ErdReadOnlyConverter[ErdSoilLevel]):
    def erd_decode(self, value: str) -> ErdSoilLevel:
        try:
            return ErdSoilLevel(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdSoilLevel.INVALID
