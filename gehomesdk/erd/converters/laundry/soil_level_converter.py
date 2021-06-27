import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdSoilLevel, SoilLevel, SOIL_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class SoilLevelConverter(ErdReadOnlyConverter[SoilLevel]):
    def erd_decode(self, value: str) -> SoilLevel:
        try:
            om = ErdSoilLevel(erd_decode_int(value))
            return SOIL_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdSoilLevel.INVALID
