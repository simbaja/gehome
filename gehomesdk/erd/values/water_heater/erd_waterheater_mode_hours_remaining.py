from typing import NamedTuple


class ErdWaterHeaterModeHoursRemaining(NamedTuple):
    hours: int

    def stringify(self, **kwargs) -> str | None:
        return str(self.hours)
