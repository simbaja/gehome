from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.fridge import ErdConvertableDrawerMode

class ErdConvertableDrawerModeConverter(ErdReadWriteConverter[ErdConvertableDrawerMode]):
    def erd_decode(self, value: str) -> ErdConvertableDrawerMode:
        try:
            return ErdConvertableDrawerMode(value[:2])
        except ValueError:
            return ErdConvertableDrawerMode.NA
    def erd_encode(self, value: ErdConvertableDrawerMode) -> str:
        return str(value.value)
