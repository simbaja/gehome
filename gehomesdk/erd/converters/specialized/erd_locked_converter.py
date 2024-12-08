from typing import Optional
from ..abstract import ErdReadWriteConverter
from gehomesdk.erd.values.common import ErdInterfaceLocked
#user interface locked state

class ErdLockedConverter(ErdReadWriteConverter[ErdInterfaceLocked]):
    def erd_decode(self, value: str) -> ErdInterfaceLocked:
        try:
            return ErdInterfaceLocked(int(value))
        except ValueError:
            return ErdInterfaceLocked.DEFAULT

    def erd_encode(self, value: ErdInterfaceLocked) -> str:
        try:
            value = value.value
        except AttributeError:
            pass
        return '{:02X}'.format(value)
        
class ErdLockedBoolConverter(ErdReadWriteConverter[Optional[bool]]):
    def erd_decode(self, value: str) -> bool:
        try:
            return bool(ErdInterfaceLocked(int(value)) == ErdInterfaceLocked.LOCKED)
        except ValueError:
            return False

    def erd_encode(self, value: ErdInterfaceLocked) -> str:
        try:
            value = value.value
        except AttributeError:
            pass
        return '{:02X}'.format(value)
