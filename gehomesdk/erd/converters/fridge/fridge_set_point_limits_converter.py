from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.fridge import FridgeSetPointLimits

class FridgeSetPointLimitsConverter(ErdReadOnlyConverter[FridgeSetPointLimits]):
    def erd_decode(self, value: str) -> FridgeSetPointLimits:
        return FridgeSetPointLimits(
            fridge_min=erd_decode_signed_byte(value[0:2]),
            fridge_max=erd_decode_signed_byte(value[2:4]),
            freezer_min=erd_decode_signed_byte(value[4:6]),
            freezer_max=erd_decode_signed_byte(value[6:8]),
        )
