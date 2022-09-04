from typing import NamedTuple, Optional


class ErdWaterHeaterTargetTemperature(NamedTuple):
    temperature: float

    def stringify(self, **kwargs) -> Optional[str]:
        return f"{self.temperature:.2f}"
