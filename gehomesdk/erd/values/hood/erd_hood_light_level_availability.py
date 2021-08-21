from typing import NamedTuple

class ErdHoodLightLevelAvailability(NamedTuple):
    off_available: bool = False
    dim_available: bool = False
    high_available: bool = False
    raw_value: str = None

    @property
    def is_available(self):
        return (
            self.off_available |
            self.dim_available |
            self.high_available
        )