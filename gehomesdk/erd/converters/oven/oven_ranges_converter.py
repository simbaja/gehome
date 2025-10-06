import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import OvenRanges

_LOGGER = logging.getLogger(__name__)

class OvenRangesConverter(ErdReadOnlyConverter[OvenRanges]):  
    def erd_decode(self, value: str) -> OvenRanges:
        raw_bytes = bytes.fromhex(value)
        upper_temp = int.from_bytes(raw_bytes[:2], 'big')
        lower_temp = int.from_bytes(raw_bytes[-2:], 'big')
        _LOGGER.debug("Received value: '%s', translated to upper_temp: '%s' and lower_temp '%s'",value,upper_temp,lower_temp)
        return OvenRanges(
            lower=lower_temp, 
            upper=upper_temp
        )
