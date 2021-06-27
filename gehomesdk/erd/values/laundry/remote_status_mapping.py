from .laundry_enums import ErdRemoteStatus
from .remote_status import RemoteStatus

REMOTE_STATUS_MAP = {
    ErdRemoteStatus.DISABLE: RemoteStatus.STATUS_DISABLE,
    ErdRemoteStatus.ENABLED: RemoteStatus.STATUS_ENABLED,
    ErdRemoteStatus.NOT_SUPPORTED: RemoteStatus.STATUS_NOT_SUPPORTED
}
