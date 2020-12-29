import enum
from .available_cook_mode import AvailableCookMode
from .erd_oven_cook_mode import ErdOvenCookMode

@enum.unique
class ErdAvailableCookMode(enum.Enum):
    """
    Available cooking modes.
    In the XMPP API, they are represented as an index into an array of bytes and a bitmask.
    Thus these take the form (byte: int, mask: int, cook_mode: ErdOvenCookMode).  See ErdAvailableCookMode.smali
    in the Android app.
    """
    OVEN_BAKE = AvailableCookMode(byte=9, mask=2, cook_mode=ErdOvenCookMode.BAKE_NOOPTION)
    OVEN_CONVECTION_BAKE = AvailableCookMode(byte=7, mask=4, cook_mode=ErdOvenCookMode.CONVBAKE_NOOPTION)
    OVEN_CONVECTION_MULTI_BAKE = AvailableCookMode(byte=6, mask=8, cook_mode=ErdOvenCookMode.CONVMULTIBAKE_NOOPTION)
    OVEN_CONVECTION_ROAST = AvailableCookMode(byte=5, mask=16, cook_mode=ErdOvenCookMode.CONVROAST_NOOPTION)
    OVEN_FROZEN_SNACKS = AvailableCookMode(byte=2, mask=1, cook_mode=ErdOvenCookMode.FROZEN_SNACKS)
    OVEN_FROZEN_SNACKS_MULTI = AvailableCookMode(byte=2, mask=2, cook_mode=ErdOvenCookMode.FROZEN_SNACKS_MULTI)
    OVEN_FROZEN_PIZZA = AvailableCookMode(byte=2, mask=4, cook_mode=ErdOvenCookMode.FROZEN_PIZZA)
    OVEN_FROZEN_PIZZA_MULTI = AvailableCookMode(byte=2, mask=8, cook_mode=ErdOvenCookMode.FROZEN_PIZZA_MULTI)
    OVEN_BAKED_GOODS = AvailableCookMode(byte=2, mask=16, cook_mode=ErdOvenCookMode.BAKED_GOODS)
