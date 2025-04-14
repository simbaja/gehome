import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdEcoDryOptionAllowables

_LOGGER = logging.getLogger(__name__)

class ErdEcoDryOptionAllowablesConverter(ErdReadOnlyConverter[ErdEcoDryOptionAllowables]):
    def erd_decode(self, value: str) -> ErdEcoDryOptionAllowables:
        if not value:
            return ErdEcoDryOptionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdEcoDryOptionAllowables(
                ecodry_disable_allowed = bool((i >> 8) & 1),
                ecodry_enable_allowed = bool((i >> 9) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct eco dry option allowables, using default.")
            return ErdEcoDryOptionAllowables(raw_value=value)
