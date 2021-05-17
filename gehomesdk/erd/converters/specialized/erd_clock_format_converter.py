from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values import ErdClockFormat

class ErdClockFormatConverter(ErdReadWriteConverter[ErdClockFormat]):
    def erd_decode(self, value: str) -> ErdClockFormat:
        return ErdClockFormat(value)
    def erd_encode(self, value: ErdClockFormat) -> str:
        return value.value    
