from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values.common import ErdOnOff

class ErdOnOffConverter(ErdReadWriteConverter[ErdOnOff]):
    def erd_decode(self, value: str) -> ErdOnOff:
        try:
            return ErdOnOff(value)
        except ValueError:
            return ErdOnOff.NA

    def erd_encode(self, value: ErdOnOff) -> str:
        return value.value
