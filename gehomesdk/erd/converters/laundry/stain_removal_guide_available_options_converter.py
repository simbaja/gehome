import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdStainRemovalGuideAvailableOptions

_LOGGER = logging.getLogger(__name__)

class ErdStainRemovalGuideAvailableOptionsConverter(ErdReadOnlyConverter[ErdStainRemovalGuideAvailableOptions]):
    def erd_decode(self, value: str) -> ErdStainRemovalGuideAvailableOptions:
        if not value:
            return ErdStainRemovalGuideAvailableOptions()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdStainRemovalGuideAvailableOptions(
                off_allowed = bool((i >> 8) & 1),
                blood_allowed = bool((i >> 9) & 1),
                grass_allowed = bool((i >> 10) & 1),
                dirt_allowed = bool((i >> 11) & 1),
                tomato_allowed = bool((i >> 12) & 1),
                beverages_allowed = bool((i >> 13) & 1),
                oily_allowed = bool((i >> 14) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct stain removal guide available options, using default.")
            return ErdStainRemovalGuideAvailableOptions(raw_value=value)
