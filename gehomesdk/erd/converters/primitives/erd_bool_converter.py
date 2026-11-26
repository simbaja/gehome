import logging
from typing import Any
from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter

_LOGGER = logging.getLogger(__name__)
_UNEXPECTED_BOOL_VALUES: set = set()

def erd_decode_bool(value: Any) -> bool | None:
    """ Decodes a raw value to a bool, FF is considered None """
    if value == "FF":
        return None
    normalized_value = str(value).upper()
    if normalized_value not in {"00", "01"} and normalized_value not in _UNEXPECTED_BOOL_VALUES:
        _UNEXPECTED_BOOL_VALUES.add(normalized_value)
        _LOGGER.warning("Unexpected raw bool value received: %s; decoding as non-zero truthy/falsey hex", value)
    return bool(int(value, 16))
def erd_encode_bool(value: bool | None) -> str:
    """ Encodes a raw value to a bool, None is encoded as FF """
    if value is None:
        return "FF"
    return "01" if value else "00"    

class ErdBoolConverter(ErdReadWriteConverter[bool | None]):
    def erd_decode(self, value: str) -> bool | None:
        """ Decodes a raw value to a bool, FF is considered None """
        return erd_decode_bool(value)
    def erd_encode(self, value: bool | None) -> str:
        """ Encodes a raw value to a bool, None is encoded as FF """
        return erd_encode_bool(value)
class ErdReadOnlyBoolConverter(ErdReadOnlyConverter[bool | None]):
    def erd_decode(self, value: str) -> bool | None:
        """ Decodes a raw value to a bool, FF is considered None """
        return erd_decode_bool(value)
