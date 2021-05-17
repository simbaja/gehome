from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.oven import CooktopStatus, ErdCooktopStatus, Burner

class CooktopStatusConverter(ErdReadOnlyConverter[CooktopStatus]):
    def erd_decode(self, value: str) -> CooktopStatus:
        if not value:
            return ErdCooktopStatus.DEFAULT()
        
        try:
            # break the string into two character segments and parse as ints
            vals = [erd_decode_int(value[i:i + 2]) for i in range(0, len(value), 2)]
            status = ErdCooktopStatus(vals[0])
            burners = {}

            burners["leftFront"] = Burner(vals[1], vals[2])
            burners["leftRear"] = Burner(vals[3], vals[4])
            burners["centerFront"] = Burner(vals[5], vals[6])
            burners["centerRear"] = Burner(vals[7], vals[8])
            burners["rightFront"] = Burner(vals[9], vals[10])
            burners["rightRear"] = Burner(vals[11], vals[12])

            return CooktopStatus(status, burners, value)
        except:
            return CooktopStatus.DEFAULT()
