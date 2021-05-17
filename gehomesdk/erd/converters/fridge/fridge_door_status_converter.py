from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.fridge import FridgeDoorStatus, ErdDoorStatus

class FridgeDoorStatusConverter(ErdReadOnlyConverter[FridgeDoorStatus]):
    def erd_decode(self, value: str) -> FridgeDoorStatus:
        def get_door_status(val: str) -> ErdDoorStatus:
            try:
                return ErdDoorStatus(val)
            except ValueError:
                return ErdDoorStatus.NA

        fridge_right = get_door_status(value[:2])
        fridge_left = get_door_status(value[2:4])
        freezer = get_door_status(value[4:6])
        drawer = get_door_status(value[6:8])
        if (fridge_right != ErdDoorStatus.OPEN) and (fridge_left != ErdDoorStatus.OPEN):
            if freezer == ErdDoorStatus.OPEN:
                status = "Freezer Open"
            else:
                status = "Closed"
        elif freezer == ErdDoorStatus.OPEN:
            status = "All Open"
        else:
            status = "Fridge Open"
        return FridgeDoorStatus(
            fridge_right=fridge_right,
            fridge_left=fridge_left,
            freezer=freezer,
            drawer=drawer,
            status=status,
        )
