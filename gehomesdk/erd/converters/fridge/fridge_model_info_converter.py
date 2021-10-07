from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.fridge import FridgeModelInfo

class FridgeModelInfoConverter(ErdReadOnlyConverter[FridgeModelInfo]):
    def erd_decode(self, value: str) -> FridgeModelInfo:
        doors = 2
        has_fridge = True
        has_freezer = True
        has_convertable_drawer = False

        type_code = erd_decode_int(value[:2])
        if(type_code == 3):
            has_freezer = False
            doors = 1
        if(type_code == 4):
            has_fridge = False
            doors = 1
        if(type_code in [6,7]):
            doors = 4
            has_convertable_drawer = True
        
        return FridgeModelInfo(
            has_fridge=has_fridge,
            has_freezer=has_freezer,
            doors=doors,
            has_convertable_drawer=has_convertable_drawer,
            raw_value=value
        )

