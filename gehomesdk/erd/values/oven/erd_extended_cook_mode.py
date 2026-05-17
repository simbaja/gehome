import enum
from .available_cook_mode import AvailableCookMode
from .erd_oven_cook_mode import ErdOvenCookMode

@enum.unique
class ErdExtendedCookMode(enum.Enum):
    """
    These represent extended cook modes (similar to but different from available cook modes)
    """
    # Extended cook-mode ERDs arrive with the bytes ordered from highest spec
    # offset to lowest, matching the existing available cook-mode tables.
    OVEN_AIRFRY = AvailableCookMode(byte=2, mask=0x40, cook_mode=ErdOvenCookMode.AIRFRY)
    OVEN_AIRFRY_PROBE = AvailableCookMode(byte=2, mask=0x80, cook_mode=ErdOvenCookMode.AIRFRY_PROBE)
    OVEN_AIRFRY_DELAY_START = AvailableCookMode(byte=1, mask=0x01, cook_mode=ErdOvenCookMode.AIRFRY_DELAYSTART)
    OVEN_AIRFRY_PROBE_DELAY_START = AvailableCookMode(byte=1, mask=0x02, cook_mode=ErdOvenCookMode.AIRFRY_PROBE_DELAYSTART)
