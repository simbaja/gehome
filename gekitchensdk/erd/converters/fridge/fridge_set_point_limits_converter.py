from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gekitchensdk.erd.values.fridge import FridgeSetPointLimits

class FridgeSetPointLimitsConverter(ErdReadOnlyConverter[FridgeSetPointLimits]):
    def erd_decode(self, value: str) -> FridgeSetPointLimits:
        return FridgeSetPointLimits(
            fridge_min=ErdSignedByteConverter.erd_decode(value[0:2]),
            fridge_max=ErdSignedByteConverter.erd_decode(value[2:4]),
            freezer_min=ErdSignedByteConverter.erd_decode(value[4:6]),
            freezer_max=ErdSignedByteConverter.erd_decode(value[6:8]),
        )
