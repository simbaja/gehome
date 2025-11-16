import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from ...values.advantium import ErdAdvantiumRemoteCookModeConfig

_LOGGER = logging.getLogger(__name__)

class ErdAdvantiumRemoteCookModeConfigConverter(ErdReadOnlyConverter[ErdAdvantiumRemoteCookModeConfig]):
    def erd_decode(self, value: str) -> ErdAdvantiumRemoteCookModeConfig:
        if not value:
            return ErdAdvantiumRemoteCookModeConfig(None, None)
        
        try:
            # break the string into two character segments
            values = [erd_decode_int(value[i:i + 2]) for i in range(0, len(value), 2)]

            remote_cookmode_config = ErdAdvantiumRemoteCookModeConfig(values, value)
            _LOGGER.debug("Remote Cook Mode Config for value %s is: %s", value, remote_cookmode_config)
            return remote_cookmode_config
        except:
            _LOGGER.exception("Could not construct remote cook mode config (value: %s), using default.")
            return ErdAdvantiumRemoteCookModeConfig(None, value)
