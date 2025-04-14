import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdDryerTemperatureOptionAllowables

_LOGGER = logging.getLogger(__name__)

class ErdDryerTemperatureOptionAllowablesConverter(ErdReadOnlyConverter[ErdDryerTemperatureOptionAllowables]):
    def erd_decode(self, value: str) -> ErdDryerTemperatureOptionAllowables:
        if not value:
            return ErdDryerTemperatureOptionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdDryerTemperatureOptionAllowables(
                temperature_option_disabled_allowed = bool((i >> 8) & 1),
                temperature_option_noheat_allowed = bool((i >> 9) & 1),
                temperature_option_extralow_allowed = bool((i >> 10) & 1),
                temperature_option_low_allowed = bool((i >> 11) & 1),
                temperature_option_medium_allowed = bool((i >> 12) & 1),
                temperature_option_high_allowed = bool((i >> 13) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct dryer temperature option allowables, using default.")
            return ErdDryerTemperatureOptionAllowables(raw_value=value)
