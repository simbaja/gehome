from typing import NamedTuple, Optional


class ErdWaterHeaterSetTemperature(NamedTuple):
    temperature: float

    def stringify(self, **kwargs) -> Optional[str]:
        return f"{self.temperature:.2f}"
