from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values import ErdSoundLevel

class ErdSoundLevelConverter(ErdReadWriteConverter[ErdSoundLevel]):    
    def erd_decode(self, value: str) -> ErdSoundLevel:
        sound_level = erd_decode_int(value)
        return ErdSoundLevel(sound_level)
    def erd_encode(self, value: ErdSoundLevel) -> str:
        return erd_encode_int(value.value)
