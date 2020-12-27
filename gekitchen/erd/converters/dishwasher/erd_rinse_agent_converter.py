import logging

from gekitchen.erd.converters.abstract import ErdReadOnlyConverter
from gekitchen.erd.converters.primitives import *
from gekitchen.erd.values.dishwasher import ErdRinseAgent, ErdRinseAgentRaw, RINSE_AGENT_RAW_MAP

_LOGGER = logging.getLogger(__name__)

class ErdRinseAgentConverter(ErdReadOnlyConverter[ErdRinseAgent]):
    def erd_decode(self, value: str) -> ErdRinseAgent:
        """ Decodes the dishwasher rinse agent status """
        try:
            raw = ErdRinseAgentRaw(value)
            _LOGGER.debug(f'raw rinse agent value: {raw}')
            return ErdRinseAgent(RINSE_AGENT_RAW_MAP[raw])
        except (ValueError, KeyError):
            return ErdRinseAgent.NA
