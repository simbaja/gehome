from typing import NamedTuple, Optional

class ErdMicrowaveCookSetting(NamedTuple):
    target_power_level: Optional[int] = None
    cook_minutes: Optional[int] = 0
    cook_seconds: Optional[int] = 0
    raw_value: Optional[str] = None