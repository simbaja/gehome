from typing import NamedTuple
    
class ErdDryerReduceStaticOptionAllowables (NamedTuple):
    dryer_reduce_static_disable_allowed: bool = False
    dryer_reduce_static_enable_allowed: bool = False
    raw_value: str | None = None
    
    def stringify(self, **kwargs):
        return f"DryerReduceStaticOptionAllowables: \
            Disabled:{self.dryer_reduce_static_disable_allowed}, \
            Enabled:{self.dryer_reduce_static_enable_allowed}"
