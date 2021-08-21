from typing import NamedTuple

class ErdHoodFanSpeedAvailability(NamedTuple):
    off_available: bool = False
    low_available: bool = False
    med_available: bool = False
    high_available: bool = False
    boost_available: bool = False
    raw_value: str = None

    @property
    def is_available(self):
        return (
            self.off_available |
            self.low_available |
            self.med_available |
            self.high_available |
            self.boost_available
        )
