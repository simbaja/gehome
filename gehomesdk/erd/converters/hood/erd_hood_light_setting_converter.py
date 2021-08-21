from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.hood import *

class ErdHoodLightSettingConverter(ErdReadWriteConverter[ErdHoodLightSetting]):
    def erd_decode(self, value: str) -> ErdHoodLightSetting:
        try:
            return ErdHoodLightSetting(erd_decode_int(value))
        except:
            return ErdHoodLightSetting.OFF

    def erd_encode(self, value: ErdHoodLightSetting) -> str:
        return erd_encode_int(value.value, 1)
