from typing import NamedTuple, Optional


class ErdWaterHeaterModeHoursRemaining(NamedTuple):
    hours: int

    def stringify(self, **kwargs) -> Optional[str]:
        return str(self.hours)
