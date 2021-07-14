import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdSmartDispense, ErdSmartDispenseSetting

_LOGGER = logging.getLogger(__name__)

class SmartDispenseConverter(ErdReadOnlyConverter[ErdSmartDispense]):
    def erd_decode(self, value: str) -> ErdSmartDispense:
        if not value:
            return ErdSmartDispense()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))
            return ErdSmartDispense(
                setting = ErdSmartDispenseSetting(int_values[0]),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct smart dispense settings, using default.")
            return ErdSmartDispense(raw_value=value)
