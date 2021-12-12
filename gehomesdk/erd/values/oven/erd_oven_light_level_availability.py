from typing import NamedTuple

class ErdOvenLightLevelAvailability(NamedTuple):
    z1: bool = False
    z2: bool = False
    z3: bool = False
    z4: bool = False
    z5: bool = True
    raw_value: str = None

    @property
    def dim_available(self):
        return self.z1

    @property
    def high_available(self):
        return self.z2
    
    @property
    def is_available(self):
        return self.z5 | self.z1, self.z2

        