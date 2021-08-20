import enum
from .available_cook_mode import AvailableCookMode
from .erd_oven_cook_mode import ErdOvenCookMode

@enum.unique
class ErdExtendedCookMode(enum.Enum):
    """
    These represent extended cook modes (similar to but different from available cook modes)
    """
    OVEN_AIRFRY = AvailableCookMode(byte=1, mask=1, cook_mode=ErdOvenCookMode.AIRFRY)
