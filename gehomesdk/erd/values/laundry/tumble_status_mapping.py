from .laundry_enums import ErdTumbleStatus
from .tumble_status import TumbleStatus

TUMBLE_STATUS_MAP = {
    ErdTumbleStatus.NOT_AVAILABLE: TumbleStatus.NOT_AVAILABLE,
    ErdTumbleStatus.ENABLE: TumbleStatus.ENABLE,
    ErdTumbleStatus.DISABLE: TumbleStatus.DISABLE
}
