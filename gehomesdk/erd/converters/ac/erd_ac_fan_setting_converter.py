from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.ac import *

class ErdAcFanSettingConverter(ErdReadWriteConverter[ErdAcFanSetting]):
    def erd_decode(self, value: str) -> ErdAcFanSetting:
        try:
            return ErdAcFanSetting(erd_decode_int(value))
        except:
            return ErdAcFanSetting.DEFAULT

    def erd_encode(self, value: ErdAcFanSetting) -> str:
        return erd_encode_int(value.value, 1)
