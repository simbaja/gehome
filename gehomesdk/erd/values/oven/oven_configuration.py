from typing import NamedTuple

class OvenConfiguration(NamedTuple):
    """Cleaner representation of ErdOvenConfiguration"""
    has_knob: bool
    has_warming_drawer: bool
    has_light_bar: bool
    has_lower_oven: bool
    has_lower_oven_kitchen_timer: bool
    raw_value: str | None = None

