from typing import Optional, NamedTuple

from .common_enums import ErdAcAvailableModes as ErdSacAvailableModes ### deprecated, use ErdAcAvailableModes

class ErdSacTargetTemperatureRange(NamedTuple):
    min: int
    max: int
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"min: {self.min}, max: {self.max}"
