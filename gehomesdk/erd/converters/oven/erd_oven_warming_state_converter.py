from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.oven import ErdOvenWarmingState

class ErdOvenWarmingStateConverter(ErdReadWriteConverter[ErdOvenWarmingState]):
    def erd_decode(self, value: str) -> ErdOvenWarmingState:
        try:
            return ErdOvenWarmingState(erd_decode_int(value))
        except Exception:
            return ErdOvenWarmingState.NOT_AVAILABLE

    def erd_encode(self, value: ErdOvenWarmingState) -> str:
        return erd_encode_int(value.value, 1)
