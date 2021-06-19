import logging

from datetime import timedelta
from typing import Optional

from ..abstract import ErdReadWriteConverter, ErdReadOnlyConverter

_LOGGER = logging.getLogger(__name__)

def erd_decode_timespan(value: any) -> Optional[timedelta]:
    """ Decodes a raw integer (minutes) as a time span, 65535 is treated as None. """
    minutes = int(value, 16)
    if minutes == 65535:
        _LOGGER.debug('Got timespan value of 65535. Treating as None.')
        return None
    return timedelta(minutes=minutes)
def erd_encode_timespan(value: Optional[timedelta]) -> str:
    """ Encodes a time span as an erd integer (minutes), None is encoded as 65535. """
    if value is None:
        minutes = 65535
    else:
        minutes = value.seconds // 60
    return minutes.to_bytes(4, 'big').hex()

class ErdTimeSpanConverter(ErdReadWriteConverter[Optional[timedelta]]):
    def erd_decode(self, value: str) -> Optional[timedelta]:
        """ Decodes a raw integer as a time span, 65535 is treated as None. """
        return erd_decode_timespan(value)
    def erd_encode(self, value: Optional[timedelta]) -> str:
        """ Encodes a time span as an erd integer, None is encoded as 65535. """
        return erd_encode_timespan(value)

class ErdReadOnlyTimeSpanConverter(ErdReadOnlyConverter[Optional[timedelta]]):
    def erd_decode(self, value: str) -> Optional[timedelta]:
        """ Decodes a raw integer as a time span, 65535 is treated as None. """
        return erd_decode_timespan(value)