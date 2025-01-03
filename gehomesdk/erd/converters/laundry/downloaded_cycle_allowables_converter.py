import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.laundry import ErdDownloadedCycleAllowables

_LOGGER = logging.getLogger(__name__)

class ErdDownloadedCycleAllowablesConverter(ErdReadOnlyConverter[ErdDownloadedCycleAllowables]):
    def erd_decode(self, value: str) -> ErdDownloadedCycleAllowables:
        if not value:
            return ErdDownloadedCycleAllowables()
        
        try:
            # break the string into two character segments
            values = [value[i:i + 2] for i in range(0, len(value), 2)]
            int_values = list(map(erd_decode_int, values))

            return ErdDownloadedCycleAllowables(
                basket_clean = bool((int_values[0] >> 1) & 1),
                drain_and_spin = bool((int_values[0] >> 2) & 1),
                quick_rinse = bool((int_values[0] >> 3) & 1),
                bulky = bool((int_values[0] >> 4) & 1),
                sanitize = bool((int_values[0] >> 5) & 1),
                towels_or_sheets = bool((int_values[0] >> 6) & 1),
                washer_stream_refresh = bool((int_values[0] >> 7) & 1),
                normal_or_mixed = bool(int_values[1] & 1),
                whites = bool((int_values[1] >> 1) & 1),
                darks = bool((int_values[1] >> 2) & 1),
                jeans = bool((int_values[1] >> 3) & 1),
                hand_wash = bool((int_values[1] >> 4) & 1),
                delicates = bool((int_values[1] >> 5) & 1),
                speed_wash = bool((int_values[1] >> 6) & 1),
                heavy_duty = bool((int_values[1] >> 7) & 1),
                allergen = bool(int_values[2] & 1),
                power_clean = bool((int_values[2] >> 1) & 1),
                rinse_and_spin = bool((int_values[2] >> 2) & 1),
                single_item = bool((int_values[2] >> 3) & 1),
                colors = bool((int_values[2] >> 4) & 1),
                cold_wash = bool((int_values[2] >> 5) & 1),
                water_station = bool((int_values[2] >> 6) & 1),
                tub_clean = bool((int_values[2] >> 7) & 1),
                casuals_steam = bool(int_values[3] & 1),
                stain_wash_with_steam = bool((int_values[3] >> 1) & 1),
                deep_clean = bool((int_values[3] >> 2) & 1),
                bulky_bedding = bool((int_values[3] >> 3) & 1),
                normal = bool((int_values[3] >> 4) & 1),
                quick_wash = bool((int_values[3] >> 5) & 1),
                sanitize_with_oxi = bool((int_values[3] >> 6) & 1),
                self_clean = bool((int_values[3] >> 7) & 1),
                towels = bool(int_values[4] & 1),
                soak = bool((int_values[4] >> 1) & 1),
                wool = bool((int_values[4] >> 2) & 1),
                ultra_fresh_vent = bool((int_values[4] >> 3) & 1),
                sanitize_plus_allergen = bool((int_values[4] >> 4) & 1),
                spin_only = bool((int_values[4] >> 5) & 1),
                everyday = bool((int_values[4] >> 6) & 1),
                soft_toys = bool((int_values[4] >> 7) & 1),
                sneakers = bool(int_values[5] & 1),
                synthetics = bool((int_values[5] >> 1) & 1),
                silk = bool((int_values[5] >> 2) & 1),
                denim = bool((int_values[5] >> 3) & 1),
                drum_clean = bool((int_values[5] >> 4) & 1),
                sheets = bool((int_values[5] >> 5) & 1),
                quick_15 = bool((int_values[5] >> 6) & 1),
                quick_30 = bool((int_values[5] >> 7) & 1),
                easy_iron = bool(int_values[6] & 1),
                sports = bool((int_values[6] >> 1) & 1),
                eco_40_to_60 = bool((int_values[6] >> 2) & 1),
                twency_c = bool((int_values[6] >> 3) & 1),
                warm_wash = bool((int_values[6] >> 4) & 1),
                hot_wash = bool((int_values[6] >> 5) & 1),
                swim_wear = bool((int_values[6] >> 6) & 1),
                eco = bool((int_values[6] >> 7) & 1),
                express = bool(int_values[7] & 1),
                mix = bool((int_values[7] >> 1) & 1),
                quick_cycle = bool((int_values[7] >> 2) & 1),
                duvet = bool((int_values[7] >> 3) & 1),

                cottons = bool(int_values[17] & 1),
                easy_care = bool((int_values[17] >> 1) & 1),
                active_wear = bool((int_values[17] >> 2) & 1),
                timed_dry = bool((int_values[17] >> 3) & 1),
                dewrinkle = bool((int_values[17] >> 4) & 1),
                quick_or_airfluff = bool((int_values[17] >> 5) & 1),
                steam_refresh = bool((int_values[17] >> 6) & 1),
                steam_dewrinkle = bool((int_values[17] >> 7) & 1),
                speed_dry = bool(int_values[18] & 1),
                mixed = bool((int_values[18] >> 1) & 1),
                quick_dry = bool((int_values[18] >> 2) & 1),
                casuals = bool((int_values[18] >> 3) & 1),
                warm_up = bool((int_values[18] >> 4) & 1),
                energy_saver = bool((int_values[18] >> 5) & 1),
                antibacterial = bool((int_values[18] >> 6) & 1),
                rack_dry = bool((int_values[18] >> 7) & 1),
                baby_care = bool(int_values[19] & 1),
                auto_dry = bool((int_values[19] >> 1) & 1),
                auto_extra = bool((int_values[19] >> 2) & 1),
                perm_press = bool((int_values[19] >> 3) & 1),
                washer_link = bool((int_values[19] >> 4) & 1),
                auto_damp = bool((int_values[19] >> 5) & 1),
                smart_vent = bool((int_values[19] >> 6) & 1),
                pre_iron = bool((int_values[19] >> 7) & 1),
                hygiene = bool(int_values[20] & 1),
                cool_air = bool((int_values[20] >> 1) & 1),
                outdoor = bool((int_values[20] >> 2) & 1),
                ultra_delicate = bool((int_values[20] >> 3) & 1),
                scent = bool((int_values[20] >> 4) & 1),
                sanitize_steam = bool((int_values[20] >> 5) & 1),
                durable = bool((int_values[20] >> 6) & 1),
                shoes = bool((int_values[20] >> 7) & 1),
                shirts = bool(int_values[21] & 1),
                refresh = bool((int_values[21] >> 1) & 1),
                freshen = bool((int_values[21] >> 2) & 1),
                ecocool = bool((int_values[21] >> 3) & 1),
                rinse_and_dry = bool((int_values[21] >> 4) & 1),
                leather = bool((int_values[21] >> 5) & 1),
                outerwear = bool((int_values[21] >> 6) & 1),
                mixed_refresh = bool((int_values[21] >> 7) & 1),
                shirts_refresh = bool(int_values[22] & 1),
                delicate_refresh = bool((int_values[22] >> 1) & 1),
                sanitize_refresh = bool((int_values[22] >> 2) & 1),
                light = bool((int_values[22] >> 3) & 1),
                heavy = bool((int_values[22] >> 4) & 1),
                wool_or_knit = bool((int_values[22] >> 5) & 1),
                rain_or_snow = bool((int_values[22] >> 6) & 1),
                kids_item = bool((int_values[22] >> 7) & 1),
                suits_or_coats = bool(int_values[23] & 1),
                pants_crease = bool((int_values[23] >> 1) & 1),
                steam_normal = bool((int_values[23] >> 2) & 1),
                steam_whites = bool((int_values[23] >> 3) & 1),
                steam_towels = bool((int_values[23] >> 4) & 1),
                steam_sanitize = bool((int_values[23] >> 5) & 1),
                down = bool((int_values[23] >> 6) & 1),
                night_dry = bool((int_values[23] >> 7) & 1),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct downloaded cycle allowables, using default.")
            return ErdDownloadedCycleAllowables(raw_value=value)
