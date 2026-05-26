from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.common import ErdResourceMeasurementType


class ErdResourceMeasurementTypeConverter(ErdReadOnlyConverter[ErdResourceMeasurementType]):
    def erd_decode(self, value: str) -> ErdResourceMeasurementType:
        return ErdResourceMeasurementType(erd_decode_int(value))
