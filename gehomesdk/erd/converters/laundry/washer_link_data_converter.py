import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdWasherLinkData, BaseCycleType

_LOGGER = logging.getLogger(__name__)

class WasherLinkDataConverter(ErdReadOnlyConverter[ErdWasherLinkData]):
    def erd_decode(self, value: str) -> ErdWasherLinkData:
        if not value:
            return ErdWasherLinkData()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))
            
            return ErdWasherLinkData(
                washer_cycle_count = erd_decode_int(value[0:8], True),
                water_extraction_level_index = int_values[4],
                washer_load_size_index = int_values[5],
                base_cycle_type = BaseCycleType(int_values[6]),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct washer link data, using default.")
            return ErdWasherLinkData(raw_value=value)
