from typing import Optional, NamedTuple

class ErdSacAvailableModes(NamedTuple):
    has_heat: bool
    has_dry: bool
    has_auto: bool
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"heat: {self.has_heat}, dry: {self.has_dry}, auto: {self.has_auto}"

class ErdSacTargetTemperatureRange(NamedTuple):
    min: int
    max: int

    def stringify(self, **kwargs) -> Optional[str]:
        return f"min: {self.min}, max: {self.max}"
