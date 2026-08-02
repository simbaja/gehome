from typing import NamedTuple

class FridgeAlertNotifications(NamedTuple):
    fresh_food_door_alert: bool
    freezer_door_alert: bool
    filter_order_alert: bool
    filter_replace_alert: bool
    fresh_food_high_temperature_alert: bool
    freezer_high_temperature_alert: bool
    ice_maker_1_full_alert: bool
    ice_maker_0_full_alert: bool
    leak_detected_alert: bool
    potential_pitcher_leak_alert: bool
    pitcher_low_flow_alert: bool
    drawer_temperature_met_alert: bool
    freezer_door_opened_alert: bool
    ice_maker_2_full_alert: bool
    convertible_compartment_door_opened_alert: bool
    bottle_chill_alarm_alert: bool
    secondary_drawer_temperature_met_alert: bool
    secondary_convertible_compartment_door_opened_alert: bool

    @property
    def any_alert(self) -> bool:
        return any(self)
