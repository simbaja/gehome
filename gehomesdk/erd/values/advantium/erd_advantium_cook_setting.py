from datetime import timedelta
from typing import NamedTuple, Optional
from .advantium_enums import *

class ErdAdvantiumCookSetting (NamedTuple):
    d: int = 0  #RANDOM
    cook_action: CookAction = CookAction.STOP
    cook_mode: CookMode = CookMode.NO_MODE
    target_temperature: int = 0
    h: int = 0  #NON-MUTABLE
    i: int = 0  #NON-MUTABLE
    power_level: int = 0
    k: int = 0  #NON-MUTABLE
    cook_time_remaining: timedelta = timedelta(0)  
    m: int = 0  #NON-MUTABLE
    n: int = 0  #NON-MUTABLE  
    o: int = 0  #NON-MUTABLE
    p: int = 0  #NON-MUTABLE
    q: int = 0  #NON-MUTABLE
    r: int = 0  #NON-MUTABLE
    s: int = 0  #NON-MUTABLE
    warm_status: WarmStatus = WarmStatus.OFF
    raw_value: Optional[str] = None
