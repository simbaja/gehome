from typing import Optional
from ..primitives import *
from ..abstract import ErdReadWriteConverter
from ...values.common import ErdInterfaceLocked
#user interface locked state

class ErdLockedConverter(ErdReadWriteConverter[ErdInterfaceLocked]):
    def erd_decode(self, value: str) -> ErdInterfaceLocked:
        try:
            return ErdInterfaceLocked(erd_decode_int(value))
        except ValueError:
            return ErdInterfaceLocked.DEFAULT

    def erd_encode(self, value: ErdInterfaceLocked) -> str:
        iv = 0
        try:
            iv = value.value
        except AttributeError:
            pass
        return erd_encode_int(iv)
        
class ErdLockedBoolConverter(ErdReadWriteConverter[Optional[bool]]):
    def erd_decode(self, value: str) -> bool:
        try:
            return bool(ErdInterfaceLocked(int(value)) == ErdInterfaceLocked.LOCKED)
        except ValueError:
            return False

    def erd_encode(self, value: Optional[bool]) -> str:
        return erd_encode_bool(value)
