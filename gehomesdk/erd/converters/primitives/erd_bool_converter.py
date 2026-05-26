import logging
from typing import Optional, Any
from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter

_LOGGER = logging.getLogger(__name__)
_UNEXPECTED_BOOL_VALUES: set = set()

def erd_decode_bool(value: Any) -> Optional[bool]:
    """ Decodes a raw value to a bool, FF is considered None """
    if value == "FF":
        return None
    normalized_value = str(value).upper()
    if normalized_value not in {"00", "01"} and normalized_value not in _UNEXPECTED_BOOL_VALUES:
        _UNEXPECTED_BOOL_VALUES.add(normalized_value)
        _LOGGER.warning(f"Unexpected raw bool value received: {value}; decoding as non-zero truthy/falsey hex")
    return bool(int(value, 16))
def erd_encode_bool(value: Optional[bool]) -> str:
    """ Encodes a raw value to a bool, None is encoded as FF """
    if value is None:
        return "FF"
    return "01" if value else "00"    

class ErdBoolConverter(ErdReadWriteConverter[Optional[bool]]):
    def erd_decode(self, value: str) -> Optional[bool]:
        """ Decodes a raw value to a bool, FF is considered None """
        return erd_decode_bool(value)
    def erd_encode(self, value: Optional[bool]) -> str:
        """ Encodes a raw value to a bool, None is encoded as FF """
        return erd_encode_bool(value)
class ErdReadOnlyBoolConverter(ErdReadOnlyConverter[Optional[bool]]):
    def erd_decode(self, value: str) -> Optional[bool]:
        """ Decodes a raw value to a bool, FF is considered None """
        return erd_decode_bool(value)
