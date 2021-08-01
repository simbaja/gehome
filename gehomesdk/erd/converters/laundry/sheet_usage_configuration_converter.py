import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdSheetUsageConfiguration

_LOGGER = logging.getLogger(__name__)

class SheetUsageConfigurationConverter(ErdReadOnlyConverter[ErdSheetUsageConfiguration]):
    def erd_decode(self, value: str) -> ErdSheetUsageConfiguration:
        if not value:
            return ErdSheetUsageConfiguration()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))
            
            return ErdSheetUsageConfiguration(
                extra_large_load_size = int_values[0],
                large_load_size = int_values[1],
                medium_load_size = int_values[2],
                small_load_size = int_values[3],
                timed_dryer_sheets_load_size = int_values[4],
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct sheet usage configuration, using default.")
            return ErdSheetUsageConfiguration(raw_value=value)
