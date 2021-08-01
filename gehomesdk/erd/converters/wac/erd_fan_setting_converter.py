from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.wac import *

class ErdFanSettingConverter(ErdReadWriteConverter[ErdFanSetting]):
    def erd_decode(self, value: str) -> ErdFanSetting:
        try:
            return ErdFanSetting(erd_decode_int(value))
        except:
            return ErdFanSetting.DEFAULT

    def erd_encode(self, value: ErdFanSetting) -> str:
        return erd_encode_int(value.value, 1)
