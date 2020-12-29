from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gekitchensdk.erd.values.fridge import FridgeSetPoints

class FridgeSetPointsConverter(ErdReadWriteConverter[FridgeSetPoints]):
    def erd_decode(self, value: str) -> FridgeSetPoints:
        return FridgeSetPoints(
            fridge=ErdSignedByteConverter.erd_decode(value[0:2]),
            freezer=ErdSignedByteConverter.erd_decode(value[2:4]),
        )
    @staticmethod    
    def erd_encode(value: FridgeSetPoints):
        return ErdSignedByteConverter.erd_encode(value.fridge) + ErdSignedByteConverter.erd_encode(value.freezer)
