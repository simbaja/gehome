import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdDryerReduceStaticOptionAllowables

_LOGGER = logging.getLogger(__name__)

class ErdDryerReduceStaticOptionAllowablesConverter(ErdReadOnlyConverter[ErdDryerReduceStaticOptionAllowables]):
    def erd_decode(self, value: str) -> ErdDryerReduceStaticOptionAllowables:
        if not value:
            return ErdDryerReduceStaticOptionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdDryerReduceStaticOptionAllowables(
                dryer_reduce_static_disable_allowed = bool((i >> 8) & 1),
                dryer_reduce_static_enable_allowed = bool((i >> 9) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct dryer reduce static option allowables, using default.")
            return ErdDryerReduceStaticOptionAllowables(raw_value=value)
