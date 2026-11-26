from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int


class ErdDehumidifierCurrentHumidityConverter(ErdReadOnlyConverter[int]):
    def erd_decode(self, value: str) -> int:
        try:
            return erd_decode_int(value) & 0xFF
        except Exception:
            return 0
