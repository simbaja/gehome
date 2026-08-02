from ..abstract import ErdReadOnlyConverter
from ...values.fridge import FridgeAlertNotifications

class FridgeAlertNotificationsConverter(ErdReadOnlyConverter[FridgeAlertNotifications]):
    def erd_decode(self, value: str) -> FridgeAlertNotifications:
        """Decode the "Notifications" half of the bit-mapped alert ERD.

        The payload is two 16 byte (128 bit) bitfields: "Supported Notifications"
        (offset 0) then "Notifications" (offset 16), each treated as a single
        big-endian integer, with individual alerts addressed by bit number. Only
        the actual "Notifications" half is decoded here; supported/equipped
        checks should use the appliance's feature list instead.
        """
        if not value or len(value) < 64:
            notifications = 0
        else:
            notifications = int(value[32:64], 16)

        def bit(offset: int) -> bool:
            return bool((notifications >> offset) & 1)

        return FridgeAlertNotifications(
            fresh_food_door_alert=bit(120),
            freezer_door_alert=bit(121),
            filter_order_alert=bit(122),
            filter_replace_alert=bit(123),
            fresh_food_high_temperature_alert=bit(124),
            freezer_high_temperature_alert=bit(125),
            ice_maker_1_full_alert=bit(126),
            ice_maker_0_full_alert=bit(127),
            leak_detected_alert=bit(112),
            potential_pitcher_leak_alert=bit(113),
            pitcher_low_flow_alert=bit(114),
            drawer_temperature_met_alert=bit(115),
            freezer_door_opened_alert=bit(116),
            ice_maker_2_full_alert=bit(117),
            convertible_compartment_door_opened_alert=bit(118),
            bottle_chill_alarm_alert=bit(119),
            secondary_drawer_temperature_met_alert=bit(104),
            secondary_convertible_compartment_door_opened_alert=bit(105),
        )
