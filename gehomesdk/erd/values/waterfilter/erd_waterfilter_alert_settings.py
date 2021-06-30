from datetime import timedelta
from typing import NamedTuple, Optional


class ErdWaterFilterAlertTimeSettings(NamedTuple):
    high_alert_time: int
    low_alert_time: int
    medium_alert_time: int

    def stringify(self, **kwargs) -> Optional[str]:
        return f"high {self.high_alert_time} mins, medium {self.medium_alert_time} mins, low {self.low_alert_time} mins"
