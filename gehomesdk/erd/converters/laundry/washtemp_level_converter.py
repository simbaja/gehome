import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdWashTempLevel, WashTempLevel, WASHTEMP_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class WashTempLevelConverter(ErdReadOnlyConverter[WashTempLevel]):
    def erd_decode(self, value: str) -> WashTempLevel:
        try:
            om = ErdWashTempLevel(erd_decode_int(value))
            return WASHTEMP_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdWashTempLevel.INVALID
