from .laundry_enums import ErdLaundryDoorLockStatus
from .laundry_door_lock_status import LaundryDoorLockStatus

LAUNDRY_DOOR_LOCK_STATUS_MAP = {
    ErdLaundryDoorLockStatus.LOCKED: LaundryDoorLockStatus.STATUS_LOCKED,
    ErdLaundryDoorLockStatus.UNLOCKED: LaundryDoorLockStatus.STATUS_UNLOCKED
}
