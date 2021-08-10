import logging


import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.common import ErdUnitType

_LOGGER = logging.getLogger(__name__)

class ErdUnitTypeConverter(ErdReadOnlyConverter[ErdUnitType]):
    def erd_decode(self, value: str) -> ErdUnitType:
        try:
            return ErdUnitType(erd_decode_int(value))
        except:
            _LOGGER.warning("Unknown Unit Type: {value}, using default")
            return ErdUnitType.UNKNOWN
