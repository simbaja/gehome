from gekitchen.erd.values.oven.erd_cooktop_status import ErdCooktopStatus
from typing import NamedTuple, Optional

class CooktopStatus(NamedTuple):
    status: ErdCooktopStatus
    burners: dict
    raw_value: Optional[str]

    @classmethod
    def DEFAULT(cls):
        return cls(ErdCooktopStatus.DASH, {}, None)