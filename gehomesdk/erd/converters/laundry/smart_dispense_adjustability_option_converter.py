import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdSmartDispenseAdjustabilityOption, ErdSmartDispenseSubstanceType, ErdSmartDispenseFlowBucket, ErdSmartDispenseDosageType

_LOGGER = logging.getLogger(__name__)

class ErdSmartDispenseAdjustabilityOptionConverter(ErdReadOnlyConverter[ErdSmartDispenseAdjustabilityOption]):
    def erd_decode(self, value: str) -> ErdSmartDispenseAdjustabilityOption:
        if not value:
            return ErdSmartDispenseAdjustabilityOption()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))

            return ErdSmartDispenseAdjustabilityOption(
                substance = ErdSmartDispenseSubstanceType(int_values[0]),
                bucket = ErdSmartDispenseFlowBucket(int_values[1]),
                dosage = ErdSmartDispenseDosageType(int_values[2]),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct smart dispense adjustability option, using default.")
            return ErdSmartDispenseAdjustabilityOption(raw_value=value)
