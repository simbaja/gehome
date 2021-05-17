from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.fridge import FridgeSetPoints

class FridgeSetPointsConverter(ErdReadWriteConverter[FridgeSetPoints]):
    def erd_decode(self, value: str) -> FridgeSetPoints:
        return FridgeSetPoints(
            fridge=erd_decode_signed_byte(value[0:2]),
            freezer=erd_decode_signed_byte(value[2:4]),
        )
    @staticmethod    
    def erd_encode(value: FridgeSetPoints):
        return erd_encode_signed_byte(value.fridge) + erd_encode_signed_byte(value.freezer)
