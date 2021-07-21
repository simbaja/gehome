from typing import NamedTuple, Optional
from .erd_door_status import ErdDoorStatus

class FridgeDoorStatus(NamedTuple):
    fridge_right: ErdDoorStatus
    fridge_left: ErdDoorStatus
    freezer: ErdDoorStatus
    drawer: ErdDoorStatus
    status: str

    @property
    def any_open(self) -> Optional[bool]:
        if self.status.lower().endswith("open"):
            return True
        return False    

    def stringify(self, **kwargs) -> Optional[str]:
        return self.status
    
    def __str__(self) -> str:
        return self.status or ""