from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdDehumidifierCurrentHumidityConverter(ErdReadWriteConverter[int]):
    def erd_decode(self, value: str) -> int:
        try:
            return erd_decode_int(value) & 0xFF
        except:
            return 0
