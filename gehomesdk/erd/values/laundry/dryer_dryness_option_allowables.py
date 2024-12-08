from typing import NamedTuple, Optional
    
class ErdDryerDrynessOptionAllowables (NamedTuple):
    dryness_option_disabled_allowed: bool = False
    dryness_option_damp_allowed: bool = False
    dryness_option_lessdry_allowed: bool = False
    dryness_option_dry_allowed: bool = False
    dryness_option_moredry_allowed: bool = False
    dryness_option_extradry_allowed: bool = False
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"DryerDrynessOptionAllowables: Disabled:{self.dryness_option_disabled_allowed}, Damp:{self.dryness_option_damp_allowed}, Less:{self.dryness_option_lessdry_allowed}, Dry:{self.dryness_option_dry_allowed}, More:{self.dryness_option_moredry_allowed}, Extra:{self.dryness_option_extradry_allowed}"
