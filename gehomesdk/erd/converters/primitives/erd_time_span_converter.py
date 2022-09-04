import logging

from datetime import timedelta
from typing import Optional

from ..abstract import ErdReadWriteConverter, ErdReadOnlyConverter
from gehomesdk.erd.erd_codes import ErdCodeType

_LOGGER = logging.getLogger(__name__)

def erd_decode_timespan(value: any, uom: str = 'minutes') -> Optional[timedelta]:
    """ 
    Decodes a raw integer as a time span, 65535 is treated as None. 
    UOMs supported: hours, minutes, seconds; default = minutes.
    """
    int_value = int(value, 16)
    if int_value == 65535:
        _LOGGER.debug('Got timespan value of 65535. Treating as None.')
        return None
    if uom == 'seconds':
        return timedelta(seconds=int_value)
    if uom == 'hours':
        return timedelta(hours=int_value)
    return timedelta(minutes=int_value)
def erd_encode_timespan(value: Optional[timedelta], uom: str = 'minutes', length: int = 2) -> str:
    """ 
    Encodes a time span as an erd integer, None is encoded as 65535. 
    UOMs supported: hours, minutes, seconds; default = minutes.
    """
    if value is None:
        int_value = 65535
    else:
        if uom == 'seconds':
            int_value = value.seconds
        if uom == 'hours':
            int_value = value.seconds // 3600
        int_value = value.seconds // 60
    return int_value.to_bytes(length, 'big').hex()

class ErdTimeSpanConverter(ErdReadWriteConverter[Optional[timedelta]]):
    def __init__(self, erd_code: ErdCodeType = "Unknown", uom: str = 'minutes', length: int = 2):
        super().__init__(erd_code)
        self.length = length
        self.uom = uom
    def erd_decode(self, value: str) -> Optional[timedelta]:
        """ Decodes a raw integer as a time span, 65535 is treated as None. """
        return erd_decode_timespan(value, self.uom)
    def erd_encode(self, value: Optional[timedelta]) -> str:
        """ Encodes a time span as an erd integer, None is encoded as 65535. """
        return erd_encode_timespan(value, self.uom, self.length)

class ErdReadOnlyTimeSpanConverter(ErdReadOnlyConverter[Optional[timedelta]]):
    def __init__(self, erd_code: ErdCodeType = "Unknown", uom: str = 'minutes'):
        super().__init__(erd_code)
        self.uom = uom    
    def erd_decode(self, value: str) -> Optional[timedelta]:
        """ Decodes a raw integer as a time span, 65535 is treated as None. """
        return erd_decode_timespan(value, self.uom)