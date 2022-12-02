import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.dishwasher import ErdErrorState

_LOGGER = logging.getLogger(__name__)

class ErdErrorStateConverter(ErdReadOnlyConverter[ErdErrorState]):
    def erd_decode(self, value: str) -> ErdErrorState:
        if not value:
            return ErdErrorState()
        
        try:
            #convert to int
            i = erd_decode_int(value)

            return ErdErrorState(
                id = i & 0xF,
                active = bool((i & 0xF0) >> 8),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct error state, using default.")
            return ErdErrorState(raw_value=value)
