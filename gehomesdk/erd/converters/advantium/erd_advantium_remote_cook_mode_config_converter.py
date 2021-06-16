from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.advantium import ErdAdvantiumRemoteCookModeConfig

class ErdAdvantiumRemoteCookModeConfigConverter(ErdReadOnlyConverter[ErdAdvantiumRemoteCookModeConfig]):
    def erd_decode(self, value: str) -> ErdAdvantiumRemoteCookModeConfig:
        if not value:
            return ErdAdvantiumRemoteCookModeConfig(None, None)
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]

            return ErdAdvantiumRemoteCookModeConfig(values, value)
        except:
            return ErdAdvantiumRemoteCookModeConfig(None, value)
