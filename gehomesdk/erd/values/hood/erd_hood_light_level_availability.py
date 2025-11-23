from typing import NamedTuple

class ErdHoodLightLevelAvailability(NamedTuple):
    off_available: bool = False
    dim_available: bool = False
    high_available: bool = False
    med_available: bool = False
    raw_value: str | None = None

    @property
    def is_available(self):
        return (
            self.off_available |
            self.dim_available |
            self.high_available |
            self.med_available
        )
    
    @classmethod
    def from_count(cls, levels: int) -> "ErdHoodLightLevelAvailability":
        """Construct availability based on the number of supported light levels (0–3)."""
        levels = max(0, min(levels, 4))

        return cls(
            off_available = levels >= 0,
            dim_available = levels >= 1,
            med_available = levels >= 2,
            high_available = levels >= 3,
            raw_value = str(levels),
        )
