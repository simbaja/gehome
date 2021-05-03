import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.dishwasher import ErdOperatingMode, OperatingMode, OPERATING_MODE_MAP

_LOGGER = logging.getLogger(__name__)

class OperatingModeConverter(ErdReadOnlyConverter[OperatingMode]):
    def erd_decode(self, value: str) -> OperatingMode:
        """Decode the dishwasher operating state """
        try:
            om = ErdOperatingMode(erd_decode_int(value))
            _LOGGER.debug(f'raw operating mode value: {om}')
            return OPERATING_MODE_MAP[om]
        except (KeyError, ValueError):
            return ErdOperatingMode.NA
