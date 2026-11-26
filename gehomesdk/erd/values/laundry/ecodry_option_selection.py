import enum
from typing import NamedTuple

class ErdEcoDryOptionStatus(enum.Enum):
    DISABLED = 0
    ENABLED = 1
    
    def stringify(self, **kwargs):
        return self.name.title()


class ErdEcoDryOptionSelection (NamedTuple):
    option_status: ErdEcoDryOptionStatus = ErdEcoDryOptionStatus.DISABLED
    raw_value: str | None = None
    
    def stringify(self, **kwargs):
        return self.option_status.stringify()
