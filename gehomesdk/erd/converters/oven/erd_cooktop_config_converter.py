from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import ErdCooktopConfig


class ErdCooktopConfigConverter(ErdReadOnlyConverter[ErdCooktopConfig]):
    def erd_decode(self, value: str):       
        if value:
            try:
                present = erd_decode_int(value[:2])
                return ErdCooktopConfig.NONE if present == 0 else ErdCooktopConfig.PRESENT 
            except ValueError:
                return ErdCooktopConfig.NONE
        else:
            return ErdCooktopConfig.NONE
