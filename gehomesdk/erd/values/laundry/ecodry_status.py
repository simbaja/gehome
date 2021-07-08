import enum

@enum.unique
class EcoDryStatus(enum.Enum):
    STATUS_UNKNOWN = "Unknown"
    STATUS_ENABLED = "Enabled"
    STATUS_DISABLE = "Disabled"
    
    def stringify(self, **kwargs):
        return self.value
