from dataclasses import dataclass


@dataclass
class ErdDsmPowerUsage:
    """
    DSM (Demand Side Management) power usage snapshot reported by an appliance
    via ERD 0xd005.

    Fields (as defined in the appliance API):
      instantaneous_power_w    - Current draw in watts (u16)
      watt_seconds_since_clear - Cumulative watt-seconds since last clear (u32)
      seconds_since_cleared    - Seconds elapsed since the counter was cleared (u16)
      referenced_to_line       - Which AC line the measurement references (u8, raw)
      water_usage              - Water usage counter, appliance-specific units (u16)
    """
    instantaneous_power_w: int
    watt_seconds_since_clear: int
    seconds_since_cleared: int
    referenced_to_line: int
    water_usage: int
