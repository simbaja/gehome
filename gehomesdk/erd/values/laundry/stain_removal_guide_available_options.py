from typing import NamedTuple, Optional
    
class ErdStainRemovalGuideAvailableOptions (NamedTuple):
    off_allowed: bool = False
    blood_allowed: bool = False
    grass_allowed: bool = False
    dirt_allowed: bool = False
    tomato_allowed: bool = False
    beverages_allowed: bool = False
    oily_allowed: bool = False
    raw_value: Optional[str] = None
    
    def stringify(self, **kwargs):
        return f"StainRemovalGuideAvailableOptions: Off:{self.off_allowed}, Blood:{self.blood_allowed}, Grass:{self.grass_allowed}, Dirt:{self.dirt_allowed}, Tomato:{self.tomato_allowed}, Beverages:{self.beverages_allowed}, Oily:{self.oily_allowed}"
