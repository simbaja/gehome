from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.common import ErdGasType


class ErdGasTypeConverter(ErdReadOnlyConverter[ErdGasType]):
    def erd_decode(self, value: str) -> ErdGasType:
        return ErdGasType(erd_decode_int(value))
