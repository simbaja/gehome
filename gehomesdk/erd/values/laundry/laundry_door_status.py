import enum

@enum.unique
class LaundryDoorStatus(enum.Enum):
    STATUS_NA = "---"
    STATUS_OPEN = "Open"
    STATUS_CLOSED = "Closed"
    
    def stringify(self, **kwargs):
        return self.name.replace("STATUS_","").replace("_"," ").title()
