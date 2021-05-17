import enum

@enum.unique
class RemoteStatus(enum.Enum):
    STATUS_NOT_SUPPORTED = "Not Supported"
    STATUS_ENABLED = "Enabled"
    STATUS_DISABLE = "Disabled"
    
    def stringify(self, **kwargs):
        return self.name.replace("STATUS_","").replace("_"," ").title()
