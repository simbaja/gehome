import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.dishwasher import ErdOperatingMode, OperatingMode, OPERATING_MODE_MAP

_LOGGER = logging.getLogger(__name__)

class OperatingModeConverter(ErdReadOnlyConverter[OperatingMode]):
    def erd_decode(self, value: str) -> OperatingMode:
        """Decode the dishwasher operating state """
        try:
            om = ErdOperatingMode(erd_decode_int(value))
            _LOGGER.debug("raw operating mode value: %s", om)
            return OPERATING_MODE_MAP[om]
        except (KeyError, ValueError):
            return OPERATING_MODE_MAP[ErdOperatingMode.INVALID]
