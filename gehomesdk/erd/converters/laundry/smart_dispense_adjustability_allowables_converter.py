import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdSmartDispenseAdjustabilityAllowables

_LOGGER = logging.getLogger(__name__)

class ErdSmartDispenseAdjustabilityAllowablesConverter(ErdReadOnlyConverter[ErdSmartDispenseAdjustabilityAllowables]):
    def erd_decode(self, value: str) -> ErdSmartDispenseAdjustabilityAllowables:
        if not value:
            return ErdRemoteCycleSelectionAllowables()
        
        try:
            i = erd_decode_int(value, True)
            
            return ErdSmartDispenseAdjustabilityAllowables(
                detergent_bucket_one_allowed = bool((i >> 8) & 1),
                detergent_bucket_two_allowed = bool((i >> 9) & 1),
                detergent_bucket_three_allowed = bool((i >> 10) & 1),
                detergent_bucket_four_allowed = bool((i >> 11) & 1),
                softener_bucket_one_allowed = bool(i & 1),
                softener_bucket_two_allowed = bool((i >> 1) & 1),
                softener_bucket_three_allowed = bool((i >> 2) & 1),
                softener_bucket_four_allowed = bool((i >> 3) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct smart dispense adjustability allowables, using default.")
            return ErdSmartDispenseAdjustabilityAllowables(raw_value=value)
