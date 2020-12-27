""" ERD Converters for dishwasher """

__all__ = (
    "ErdCycleStateConverter",
    "ErdRinseAgentConverter",
    "OperatingModeConverter"
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
            _LOGGER.debug(f'raw cycle state value: {raw}')
            return ErdCycleState(CYCLE_STATE_RAW_MAP[raw])
        except (ValueError, KeyError):
            return ErdCycleState.NA

class OperatingModeConverter(ErdReadOnlyConverter[OperatingMode]):
    def erd_decode(self, value: str) -> OperatingMode:
        """Decode the dishwasher operating state """
        try:
            om = ErdOperatingMode(value)
            _LOGGER.debug(f'raw operating mode value: {raw}')
            return OPERATING_MODE_MAP[om]
        except (KeyError, ValueError):
            return ErdOperatingMode.NA

class ErdRinseAgentConverter(ErdReadOnlyConverter[ErdRinseAgent]):
    def erd_decode(self, value: str) -> ErdRinseAgent:
        """ Decodes the dishwasher rinse agent status """
        try:
            raw = ErdRinseAgentRaw(value)
            _LOGGER.debug(f'raw rinse agent value: {raw}')
            return ErdRinseAgent(RINSE_AGENT_RAW_MAP[raw])
        except (ValueError, KeyError):
            return ErdRinseAgent.NA
