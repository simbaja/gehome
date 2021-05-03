from .erd_state_detail import ErdLaundryStateDetail
from .laundry_const import *

LAUNDRY_STATE_DETAIL_MAP = {
    ErdLaundryOperatingMode.IDLE: LAUNDRY_STATE_OFF,
    ErdLaundryOperatingMode.STANDBY: LAUNDRY_STATE_STANDBY,
    ErdLaundryOperatingMode.RUN: LAUNDRY_STATE_RUN,
    ErdLaundryOperatingMode.PAUSE: LAUNDRY_STATE_PAUSE,
    ErdLaundryOperatingMode.END_OF_CYCLE: LAUNDRY_STATE_END_OF_CYCLE,
    ErdLaundryOperatingMode.DSM_DELAY_RUN: LAUNDRY_STATE_DSM_DELAY_RUN,
    ErdLaundryOperatingMode.DELAY_RUN: LAUNDRY_STATE_DELAY_RUN,
    ErdLaundryOperatingMode.DELAY_PAUSE: LAUNDRY_STATE_DELAY_PAUSE,
    ErdLaundryOperatingMode.DRAIN_TIMEOUT: LAUNDRY_STATE_DRAIN_TIMEOUT,
    ErdLaundryOperatingMode.CLEAN_SPEAK: LAUNDRY_STATE_CLEAN_SPEAK
}
