from typing import NamedTuple


class ErdWaterHeaterSetTemperature(NamedTuple):
    temperature: float

    def stringify(self, **kwargs) -> str | None:
        return f"{self.temperature:.2f}"
