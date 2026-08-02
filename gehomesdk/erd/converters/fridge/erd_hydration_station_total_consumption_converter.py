from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int

class ErdHydrationStationTotalConsumptionConverter(ErdReadOnlyConverter[float]):
    def erd_decode(self, value: str) -> float:
        return erd_decode_int(value) / 100.0
