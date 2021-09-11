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

        #get the door status 
        open_doors = []
        if fridge_left == ErdDoorStatus.OPEN or fridge_right == ErdDoorStatus.OPEN:
            open_doors.append('Fridge')
        if freezer == ErdDoorStatus.OPEN:
            open_doors.append('Freezer')
        if drawer == ErdDoorStatus.OPEN:
            open_doors.append('Drawer')
        
        if len(open_doors) > 1:
            status = 'Multiple Open'
        elif len(open_doors) == 1:
            status = open_doors[0] + " Open"
        else:
            status = 'Closed'

        return FridgeDoorStatus(
            fridge_right=fridge_right,
            fridge_left=fridge_left,
            freezer=freezer,
            drawer=drawer,
            status=status,
        )
