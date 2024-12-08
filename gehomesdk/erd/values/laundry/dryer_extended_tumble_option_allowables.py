from typing import NamedTuple, Optional
    
class ErdDryerExtendedTumbleOptionAllowables (NamedTuple):
    dryer_extended_tumble_disable_allowed: bool = False
    dryer_extended_tumble_enable_allowed: bool = False
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"DryerExtendedTumbleOptionAllowables: Disable:{self.dryer_extended_tumble_disable_allowed}, Enable:{self.dryer_extended_tumble_enable_allowed}"
