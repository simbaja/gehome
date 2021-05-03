import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdSpinTimeLevel, SpinTimeLevel, SPINTIME_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class SpinTimeLevelConverter(ErdReadOnlyConverter[SpinTimeLevel]):
    def erd_decode(self, value: str) -> SpinTimeLevel:
        """Decode the dishwasher operating state """
        try:
            om = ErdSpinTimeLevel(erd_decode_int(value))
            ###_LOGGER.debug(f'raw operating mode value: {om}')
            return SPINTIME_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdSpinTimeLevel.NA
