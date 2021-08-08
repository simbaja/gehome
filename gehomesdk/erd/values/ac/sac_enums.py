from typing import Optional, NamedTuple

class ErdSacAvailableModes(NamedTuple):
    has_heat: bool
    has_dry: bool
    has_eco: bool
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"heat: {self.has_heat}, dry: {self.has_dry}, eco: {self.has_eco}"

class ErdSacTargetTemperatureRange(NamedTuple):
    min: int
    max: int
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"min: {self.min}, max: {self.max}"
