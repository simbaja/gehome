from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.hood import *

class ErdHoodFanSettingConverter(ErdReadWriteConverter[ErdHoodFanSetting]):
    def erd_decode(self, value: str) -> ErdHoodFanSetting:
        try:
            return ErdHoodFanSetting(erd_decode_int(value))
        except:
            return ErdHoodFanSetting.OFF

    def erd_encode(self, value: ErdHoodFanSetting) -> str:
        return erd_encode_int(value.value, 1)
