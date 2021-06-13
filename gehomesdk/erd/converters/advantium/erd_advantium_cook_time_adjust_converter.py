from ..abstract import ErdReadWriteConverter
from ..primitives import *

class ErdAdvantiumCookTimeAdjustConverter(ErdReadWriteConverter[int]):
    def erd_decode(self, value: str) -> int:
        return erd_decode_int(value)
    def erd_encode(self, value: any) -> str:
        return erd_encode_int(value, 3)