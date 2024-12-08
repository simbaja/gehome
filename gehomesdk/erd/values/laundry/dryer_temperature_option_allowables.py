from typing import NamedTuple, Optional
    
class ErdDryerTemperatureOptionAllowables (NamedTuple):
    temperature_option_disabled_allowed: bool = False
    temperature_option_noheat_allowed: bool = False
    temperature_option_extralow_allowed: bool = False
    temperature_option_low_allowed: bool = False
    temperature_option_medium_allowed: bool = False
    temperature_option_high_allowed: bool = False
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"DryerTemperatureOptionAllowables: Disabled:{self.temperature_option_disabled_allowed}, NoHeat:{self.temperature_noheat_allowed}, ExtraLow:{self.temperature_option_extralow_allowed}, Low:{self.temperature_option_low_allowed}, Medium:{self.temperature_option_medium_allowed}, High:{self.temperature_option_high_allowed}"
