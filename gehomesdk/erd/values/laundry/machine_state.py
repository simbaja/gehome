import enum

@enum.unique
class MachineState(enum.Enum):
    STATUS_DASH = "---"
    STATUS_OFF = "Off"
    STATUS_STANDBY = "Standby"
    STATUS_RUN = "Run"
    STATUS_CYCLE_COMPLETE = "Finished"
    STATUS_PAUSED = "Paused"
    STATUS_DELAY_RUN = "Delay Run"
    STATUS_DELAY_PAUSED = "Delay Paused"
    STATUS_DRAIN_TIMEOUT = "Drain Timeout"
    STATUS_COMMISSIONING = "Commissioning"
    STATUS_BULK_FLUSH = "Bulk Flush"
    STATUS_CLEAN_SPEAK = "Clean Speak"
    
    def stringify(self, **kwargs):
        return self.value
