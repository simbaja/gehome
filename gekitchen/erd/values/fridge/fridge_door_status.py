from typing import NamedTuple
from .erd_door_status import ErdDoorStatus

class FridgeDoorStatus(NamedTuple):
    fridge_right: ErdDoorStatus
    fridge_left: ErdDoorStatus
    freezer: ErdDoorStatus
    drawer: ErdDoorStatus
    status: str
