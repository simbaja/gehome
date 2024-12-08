import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdAdaptiveMyCycleOptionAllowables

_LOGGER = logging.getLogger(__name__)

class ErdAdaptiveMyCycleOptionAllowablesConverter(ErdReadOnlyConverter[ErdAdaptiveMyCycleOptionAllowables]):
    def erd_decode(self, value: str) -> ErdAdaptiveMyCycleOptionAllowables:
        if not value:
            return ErdAdaptiveMyCycleOptionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdAdaptiveMyCycleOptionAllowables(
                adaptive_disable_allowed = bool((i >> 8) & 1),
                adaptive_enable_allowed = bool((i >> 9) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct adaptive my cycle option allowables, using default.")
            return ErdAdaptiveMyCycleOptionAllowables(raw_value=value)
