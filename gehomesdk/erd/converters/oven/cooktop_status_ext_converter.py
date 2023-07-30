import logging

from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import CooktopStatus, ErdCooktopStatus, Burner

_LOGGER = logging.getLogger(__name__)

class CooktopStatusExtConverter(ErdReadOnlyConverter[CooktopStatus]):
    def erd_decode(self, value: str) -> CooktopStatus:
        if not value:
            return CooktopStatus.DEFAULT()
        
        try:
            # break the string into two character segments and parse as ints
            vals = [erd_decode_int(value[i:i + 2]) for i in range(0, len(value), 2)]
            burners = {}

            burners["leftFront"] = Burner(self._convert_to_legacy(vals[0]), 0)
            burners["leftRear"] = Burner(self._convert_to_legacy(vals[3]), 0)
            burners["centerFront"] = Burner(self._convert_to_legacy(vals[6]), 0)
            burners["centerRear"] = Burner(self._convert_to_legacy(vals[9]), 0)
            burners["rightFront"] = Burner(self._convert_to_legacy(vals[12]), 0)
            burners["rightRear"] = Burner(self._convert_to_legacy(vals[15]), 0)

            status = ErdCooktopStatus.OFF
            if(any(x.on for x in burners)):
                status = ErdCooktopStatus.BURNERS_ON

            return CooktopStatus(status, burners, value)
        except Exception as ex:
            _LOGGER.error("Could not convert cooktop status.", exc_info=1)
            return CooktopStatus(ErdCooktopStatus.DASH,{},value)

    def _convert_to_legacy(self, value: int):
        #based on description at: https://github.com/simbaja/ha_gehome/issues/159
        #bit 0 is "exists"
        #bit 2 is "only on/off"
        #bit 6 is "on"
        if value == 1:
            return 1 + self._set_bit(2)
        else:
            return 1 + self._set_bit(2) + self._set_bit(6)

    def _set_bit(self, bit_index):
        return (1 << bit_index)
