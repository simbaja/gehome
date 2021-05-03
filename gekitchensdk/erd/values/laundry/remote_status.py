import enum

@enum.unique
class RemoteStatus(enum.Enum):
    STATUS_DISABLED = "status_disabled"
    STATUS_ENABLED = "status_enabled"
    STATUS_NOTSUPPORTED = "status_notsupported"
    
    def stringify(self, **kwargs):
        return self.name.replace("SOIL_","").replace("_"," ").title()
