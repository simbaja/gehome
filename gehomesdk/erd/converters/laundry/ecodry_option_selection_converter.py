import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdEcoDryOptionSelection

_LOGGER = logging.getLogger(__name__)

class ErdEcoDryOptionSelectionConverter(ErdReadOnlyConverter[ErdEcoDryOptionSelection]):
    def erd_decode(self, value: str) -> ErdEcoDryOptionSelection:
        if not value:
            return ErdRemoteCycleSelectionSelection()
        
        try:
            i = erd_decode_int(value)
            
            return ErdEcoDryOptionSelection(
                option_enabled = bool(i & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct eco dry option selection, using default.")
            return ErdEcoDryOptionSelection(raw_value=value)
