import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdWashTempLevel, WashTempLevel, WASHTEMP_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class WashTempLevelConverter(ErdReadOnlyConverter[WashTempLevel]):
    def erd_decode(self, value: str) -> WashTempLevel:
        try:
            om = ErdWashTempLevel(erd_decode_int(value))
            return WASHTEMP_LEVEL_MAP[om]
        except (KeyError, ValueError):
            return WASHTEMP_LEVEL_MAP[ErdWashTempLevel.UNKNOWN]
