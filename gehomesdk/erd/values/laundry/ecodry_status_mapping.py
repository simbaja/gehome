from .laundry_enums import ErdEcoDryStatus
from .ecodry_status import EcoDryStatus

ECODRY_STATUS_MAP = {
    ErdEcoDryStatus.STATE_0: EcoDryStatus.STATUS_ENABLED,
    ErdEcoDryStatus.STATE_1: EcoDryStatus.STATUS_UNKNOWN,
    ErdEcoDryStatus.STATE_2: EcoDryStatus.STATUS_UNKNOWN,
    ErdEcoDryStatus.STATE_3: EcoDryStatus.STATUS_DISABLE
}
