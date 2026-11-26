from typing import NamedTuple
    
class ErdDampAlertOptionAllowables (NamedTuple):
    damp_alert_disable_allowed: bool = False
    damp_alert_enable_allowed: bool = False
    raw_value: str | None = None
    
    def stringify(self, **kwargs):
        return f"DampAlertOptionAllowables: Disabled:{self.damp_alert_disable_allowed}, \
            Enabled:{self.damp_alert_enable_allowed}"
