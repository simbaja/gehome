from typing import NamedTuple

class ErdHoodFanSpeedAvailability(NamedTuple):
    off_available: bool = False
    low_available: bool = False
    med_available: bool = False
    high_available: bool = False
    boost_available: bool = False
    raw_value: str | None = None

    @property
    def is_available(self):
        return (
            self.off_available |
            self.low_available |
            self.med_available |
            self.high_available |
            self.boost_available
        )

    @classmethod
    def from_count(cls, levels: int) -> "ErdHoodFanSpeedAvailability":
        """Construct availability based on number of supported fan speed levels (0–5)."""
        # clamp to valid range
        levels = max(0, min(levels, 5))

        return cls(
            off_available   = levels >= 1,
            low_available   = levels >= 2,
            med_available   = levels >= 3,
            high_available  = levels >= 4,
            boost_available = levels >= 5,
            raw_value       = str(levels),
        )