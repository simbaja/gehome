from typing import NamedTuple

class ErdMicrowaveCookSetting(NamedTuple):
    target_power_level: int | None = None
    cook_minutes: int | None = 0
    cook_seconds: int | None = 0
    raw_value: str | None = None