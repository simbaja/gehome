from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int

class ErdCumulativeGasCubicFeetConverter(ErdReadOnlyConverter[float]):
    def erd_decode(self, value: str) -> float:
        return erd_decode_int(value) / 10.0
