import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdWashTempLevel, WashTempLevel, WASHTEMP_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class WashTempLevelConverter(ErdReadOnlyConverter[WashTempLevel]):
    def erd_decode(self, value: str) -> WashTempLevel:
        """Decode the dishwasher operating state """
        try:
            om = ErdWashTempLevel(erd_decode_int(value))
            ###_LOGGER.debug(f'raw operating mode value: {om}')
            return WASHTEMP_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdWashTempLevel.NA
