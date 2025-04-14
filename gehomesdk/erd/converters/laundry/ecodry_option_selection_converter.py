import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdEcoDryOptionSelection, ErdEcoDryOptionStatus

_LOGGER = logging.getLogger(__name__)

class ErdEcoDryOptionSelectionConverter(ErdReadOnlyConverter[ErdEcoDryOptionSelection]):
    def erd_decode(self, value: str) -> ErdEcoDryOptionSelection:
        if not value:
            return ErdEcoDryOptionSelection()
        
        try:
            i = erd_decode_int(value)
            
            return ErdEcoDryOptionSelection(
                option_status = ErdEcoDryOptionStatus(i),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct eco dry option selection, using default.")
            return ErdEcoDryOptionSelection(raw_value=value)
