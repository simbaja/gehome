from typing import NamedTuple
from .erd_door_status import ErdDoorStatus

class FridgeDoorStatus(NamedTuple):
    fridge_right: ErdDoorStatus
    fridge_left: ErdDoorStatus
    freezer: ErdDoorStatus
    drawer: ErdDoorStatus
    status: str

    @property
    def any_open(self) -> bool | None:
        if self.status.lower().endswith("open"):
            return True
        return False    

    def stringify(self, **kwargs) -> str | None:
        return self.status
    
    def __str__(self) -> str:
        return self.status or ""