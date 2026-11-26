from typing import NamedTuple

class ErdWaterFilterAlertState(NamedTuple):
    value: int

    def has_alert(self):
        """Detect if an alert is active"""
        if self.value & 1 == 1 or self.value & 2 == 1 or self.value & 4 == 1:
            return True
        return False

    def has_low_alert(self):
        return self.value & 1 == 1
    def has_medium_alert(self):
        return self.value & 2 == 1
    def has_high_alert(self):
        return self.value & 4 == 1

    def boolify(self) -> bool | None:
        return self.has_alert()

    def stringify(self, **kwargs) -> str | None:
        retVal = ""
        if self.has_high_alert():
            retVal += "| High"
        if self.has_medium_alert():
            retVal += "| Medium"
        if self.has_low_alert():
            retVal += "| Low"
        if retVal != "":
            return retVal[2:]    
        return "Off"
