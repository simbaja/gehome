""" ERD Converters for dishwasher """

__all__ = (
    "ErdCycleStateConverter",
    "ErdOperatingModeConverter",
    "ErdRinseAgentConverter"
)

import logging
from .abstract import ErdReadOnlyConverter, ErdValueConverter
from .primitives import *
from gekitchen.erd.values.dishwasher import *

_LOGGER = logging.getLogger(__name__)

class ErdCycleStateConverter(ErdReadOnlyConverter[ErdCycleState]):
    def erd_decode(self, value: str) -> ErdCycleState:
        """ Decodes the dishwasher cycle state """    
        try:
            raw = ErdCycleStateRaw(value)
            _LOGGER.debug(f'Cycle State Value: {raw}')
            return ErdCycleState(CYCLE_STATE_RAW_MAP[raw])
        except (ValueError, KeyError):
            return ErdCycleState.NA

class ErdOperatingModeConverter(ErdReadOnlyConverter[ErdOperatingMode]):
    def erd_decode(self, value: str) -> ErdOperatingMode:
        """Decode the dishwasher operating state """
        try:
            return ErdOperatingMode(value)
        except ValueError:
            return ErdOperatingMode.NA

class ErdRinseAgentConverter(ErdReadOnlyConverter[ErdRinseAgent]):
    def erd_decode(self, value: str) -> ErdRinseAgent:
        """ Decodes the dishwasher rinse agent status """
        try:
            raw = ErdRinseAgentRaw(value)
            _LOGGER.debug(f'Rinse Agent Value: {raw}')
            return ErdRinseAgent(RINSE_AGENT_RAW_MAP[raw])
        except (ValueError, KeyError):
            return ErdRinseAgent.NA
