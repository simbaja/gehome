from typing import NamedTuple
    
class ErdDryerExtendedTumbleOptionAllowables (NamedTuple):
    dryer_extended_tumble_disable_allowed: bool = False
    dryer_extended_tumble_enable_allowed: bool = False
    raw_value: str | None = None
    
    def stringify(self, **kwargs):
        return f"DryerExtendedTumbleOptionAllowables: \
            Disable:{self.dryer_extended_tumble_disable_allowed}, \
            Enable:{self.dryer_extended_tumble_enable_allowed}"
