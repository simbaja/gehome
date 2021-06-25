from datetime import timedelta
from typing import NamedTuple, Optional

class ErdWaterFilterAlertTimeSettings(NamedTuple):
    high_alert_time: int
    low_alert_time: int
    medium_alert_time: int