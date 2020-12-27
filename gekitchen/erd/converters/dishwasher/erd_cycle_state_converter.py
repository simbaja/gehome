import logging

from gekitchen.erd.converters.abstract import ErdReadOnlyConverter
from gekitchen.erd.converters.primitives import *
from gekitchen.erd.values.dishwasher import ErdCycleState, ErdCycleStateRaw, CYCLE_STATE_RAW_MAP

_LOGGER = logging.getLogger(__name__)

class ErdCycleStateConverter(ErdReadOnlyConverter[ErdCycleState]):
    def erd_decode(self, value: str) -> ErdCycleState:
        """ Decodes the dishwasher cycle state """    
        try:
            raw = ErdCycleStateRaw(value)
            _LOGGER.debug(f'raw cycle state value: {raw}')
            return ErdCycleState(CYCLE_STATE_RAW_MAP[raw])
        except (ValueError, KeyError):
            return ErdCycleState.NA
