from typing import Optional
from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter

def erd_decode_bool(value: any) -> Optional[bool]:
    """ Decodes a raw value to a bool, FF is considered None """
    if value == "FF":
        return None
    return bool(int(value))
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
