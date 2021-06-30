from datetime import timedelta
from typing import NamedTuple, Optional


class ErdWaterFilterAlertState(NamedTuple):
    value: int

    # TODO: I'm unsure which bits mean low, medium, high
    """Detect if an alert is active"""

    def has_alert(self):
        if self.value & 1 == 1 or self.value & 2 == 1 or self.value & 4 == 1:
            return True
        return False

    def boolify(self) -> Optional[bool]:
        return self.has_alert()

    def stringify(self, **kwargs) -> Optional[str]:
        if self.has_alert():
            return "ON"
        return "OFF"
