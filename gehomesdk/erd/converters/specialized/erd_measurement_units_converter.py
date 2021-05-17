from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values import ErdMeasurementUnits

class ErdMeasurementUnitsConverter(ErdReadWriteConverter[ErdMeasurementUnits]):
    def erd_decode(self, value: str) -> ErdMeasurementUnits:
        return ErdMeasurementUnits(int(value))
    def erd_encode(self, value: ErdMeasurementUnits) -> str:
        return f'{value.value:02d}'
