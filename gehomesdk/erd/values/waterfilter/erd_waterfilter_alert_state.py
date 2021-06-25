from datetime import timedelta
from typing import NamedTuple, Optional

class ErdWaterFilterAlertState(NamedTuple):
    value: int

    # TODO: I'm unsure which bits mean low, medium, high
    '''Detect if an alert is active'''
    def has_alert(self):
        if self.value & 1 == 1 or self.value & 2 == 1 or self.value & 4 == 1:
            return True
        return False