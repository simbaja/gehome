import enum

@enum.unique
class LaundryDoorLockStatus(enum.Enum):
    STATUS_LOCKED = "Locked"
    STATUS_UNLOCKED = "Unlocked"
    
    def stringify(self, **kwargs):
        return self.name.replace("STATUS_","").replace("_"," ").title()
