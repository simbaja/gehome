from .laundry_enums import ErdLaundryDoorStatus
from .laundry_door_status import LaundryDoorStatus

LAUNDRY_DOOR_STATUS_MAP = {
    ErdLaundryDoorStatus.OPEN: LaundryDoorStatus.STATUS_OPEN,
    ErdLaundryDoorStatus.CLOSED: LaundryDoorStatus.STATUS_CLOSED
}
