import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
#NOTE: reset is actually the number of power cycles

from gehomesdk.erd.values.dishwasher import ErdCycleCount

_LOGGER = logging.getLogger(__name__)

class ErdCycleCountSettingConverter(ErdReadOnlyConverter[ErdCycleCount]):
    def erd_decode(self, value: str) -> ErdCycleCount:
        if not value:
            return ErdCycleCount()
        
        try:
            #convert to int
            i = erd_decode_int(value)

            return ErdCycleCount(
                started = (i & 0xFFFF00000000) >> 32,
                completed = (i & 0xFFFF0000 ) >> 16,
                reset = (i & 0xFFFF),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct cycle counts, using default.")
            return ErdCycleCount(raw_value=value)
