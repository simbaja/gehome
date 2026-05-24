from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.cooktop import CooktopStatus, ErdCooktopStatus, Burner

class CooktopStatusConverter(ErdReadOnlyConverter[CooktopStatus]):
    def erd_decode(self, value: str) -> CooktopStatus:
        if not value:
            return CooktopStatus.DEFAULT()
        
        try:
            # break the string into two character segments and parse as ints
            vals = [erd_decode_int(value[i:i + 2]) for i in range(0, len(value), 2)]
            status = ErdCooktopStatus(vals[0])
            burners = {}

            if vals[1] != 255:
                burners["leftFront"] = Burner(vals[1], vals[2])
            if vals[3] != 255:
                burners["leftRear"] = Burner(vals[3], vals[4])
            if vals[5] != 255:
                burners["centerFront"] = Burner(vals[5], vals[6])
            if vals[7] != 255:
                burners["centerRear"] = Burner(vals[7], vals[8])
            if vals[9] != 255:
                burners["rightFront"] = Burner(vals[9], vals[10])
            if vals[11] != 255:
                burners["rightRear"] = Burner(vals[11], vals[12])

            return CooktopStatus(status, burners, value)
        except:
            return CooktopStatus.DEFAULT()
