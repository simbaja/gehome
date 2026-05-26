from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.common import ErdDemandResponseState


class ErdDemandResponseStateConverter(ErdReadOnlyConverter[ErdDemandResponseState]):
    def erd_decode(self, value: str) -> ErdDemandResponseState:
        try:
            return ErdDemandResponseState(erd_decode_int(value))
        except:
            return ErdDemandResponseState.NOT_AVAILABLE
