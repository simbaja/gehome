from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.advantium import ErdAdvantiumKitchenTimerMinMax

class ErdAdvantiumKitchenTimerMinMaxConverter(ErdReadOnlyConverter[ErdAdvantiumKitchenTimerMinMax]):
    def erd_decode(self, value: str) -> ErdAdvantiumKitchenTimerMinMax:
        return ErdAdvantiumKitchenTimerMinMax(
            min_time=erd_decode_int(value[0:4]),
            max_time=erd_decode_int(value[4:8]),
            raw_value=value
        )