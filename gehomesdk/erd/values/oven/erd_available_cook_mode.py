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

    The App appears to be a very small subset of the actual modes available.  In addition, based on some older
    documentation, it doesn't even look right.  However, it may be that the modes in the app are the only usable
    ones, so we will just comment out all the other modes... TODO: further testing on which modes are actually
    available.
    """
    # From GE Maker Site
#    BYTE1_BIT0_1 = AvailableCookMode(byte=1, mask=1,   cook_mode=ErdOvenCookMode.BAKE_NOOPTION)
#    BYTE1_BIT1_1 = AvailableCookMode(byte=1, mask=2,   cook_mode=ErdOvenCookMode.BAKE_PROBE)
#    BYTE1_BIT2_1 = AvailableCookMode(byte=1, mask=4,   cook_mode=ErdOvenCookMode.BAKE_DELAYSTART)
#    #BYTE1_BIT3_1 = AvailableCookMode(byte=1, mask=8,   cook_mode=ErdOvenCookMode.BAKETIMED)
#    BYTE1_BIT4_1 = AvailableCookMode(byte=1, mask=16,  cook_mode=ErdOvenCookMode.BAKETIMED_WARM)
#    BYTE1_BIT5_1 = AvailableCookMode(byte=1, mask=32,  cook_mode=ErdOvenCookMode.BAKETIMED_TWOTEMP)
#    BYTE1_BIT6_1 = AvailableCookMode(byte=1, mask=64,  cook_mode=ErdOvenCookMode.BAKE_PROBE_DELAYSTART)
#    #BYTE1_BIT7_1 = AvailableCookMode(byte=1, mask=128, cook_mode=ErdOvenCookMode.BAKETIMED_DELAYSTART)

#    BYTE2_BIT0_1 = AvailableCookMode(byte=2, mask=1,   cook_mode=ErdOvenCookMode.BAKETIMED_WARM_DELAYSTART)
#    BYTE2_BIT1_1 = AvailableCookMode(byte=2, mask=2,   cook_mode=ErdOvenCookMode.BAKETIMED_TWOTEMP_DELAYSTART)
#    BYTE2_BIT2_1 = AvailableCookMode(byte=2, mask=4,   cook_mode=ErdOvenCookMode.BAKE_SABBATH)
#    BYTE2_BIT3_1 = AvailableCookMode(byte=2, mask=8,   cook_mode=ErdOvenCookMode.BROIL_HIGH)
#    BYTE2_BIT4_1 = AvailableCookMode(byte=2, mask=16,  cook_mode=ErdOvenCookMode.BROIL_LOW)
#    BYTE2_BIT5_1 = AvailableCookMode(byte=2, mask=32,  cook_mode=ErdOvenCookMode.PROOF_NOOPTION)
#    BYTE2_BIT6_1 = AvailableCookMode(byte=2, mask=64,  cook_mode=ErdOvenCookMode.WARM_NOOPTION)
#    BYTE2_BIT7_1 = AvailableCookMode(byte=2, mask=128, cook_mode=ErdOvenCookMode.WARM_PROBE)

#    BYTE3_BIT0_1 = AvailableCookMode(byte=3, mask=1,   cook_mode=ErdOvenCookMode.CONVBAKE_NOOPTION)
#    BYTE3_BIT1_1 = AvailableCookMode(byte=3, mask=2,   cook_mode=ErdOvenCookMode.CONVBAKE_PROBE)
#    BYTE3_BIT2_1 = AvailableCookMode(byte=3, mask=4,   cook_mode=ErdOvenCookMode.CONVBAKE_DELAYSTART)
#    #BYTE3_BIT3_1 = AvailableCookMode(byte=3, mask=8,   cook_mode=ErdOvenCookMode.CONVBAKETIMED)
#    BYTE3_BIT4_1 = AvailableCookMode(byte=3, mask=16,  cook_mode=ErdOvenCookMode.CONVBAKETIMED_WARM)
#    BYTE3_BIT5_1 = AvailableCookMode(byte=3, mask=32,  cook_mode=ErdOvenCookMode.CONVBAKETIMED_TWOTEMP)
#    BYTE3_BIT6_1 = AvailableCookMode(byte=3, mask=64,  cook_mode=ErdOvenCookMode.CONVBAKE_PROBE_DELAYSTART)
#    #BYTE3_BIT7_1 = AvailableCookMode(byte=3, mask=128, cook_mode=ErdOvenCookMode.CONVBAKETIMED_DELAYSTART)

#    BYTE4_BIT0_1 = AvailableCookMode(byte=4, mask=1,   cook_mode=ErdOvenCookMode.CONVBAKETIMED_WARM_DELAYSTART)
#    BYTE4_BIT1_1 = AvailableCookMode(byte=4, mask=2,   cook_mode=ErdOvenCookMode.CONVBAKETIMED_TWOTEMP_DELAYSTART)
#    BYTE4_BIT2_1 = AvailableCookMode(byte=4, mask=4,   cook_mode=ErdOvenCookMode.BAKE_SABBATH)
#    BYTE4_BIT3_1 = AvailableCookMode(byte=4, mask=8,   cook_mode=ErdOvenCookMode.BROIL_HIGH)
#    BYTE4_BIT4_1 = AvailableCookMode(byte=4, mask=16,  cook_mode=ErdOvenCookMode.BROIL_LOW)
#    BYTE4_BIT5_1 = AvailableCookMode(byte=4, mask=32,  cook_mode=ErdOvenCookMode.PROOF_NOOPTION)
#    BYTE4_BIT6_1 = AvailableCookMode(byte=4, mask=64,  cook_mode=ErdOvenCookMode.WARM_NOOPTION)
#    BYTE4_BIT7_1 = AvailableCookMode(byte=4, mask=128, cook_mode=ErdOvenCookMode.WARM_PROBE)

#    BYTE5_BIT0_1 = AvailableCookMode(byte=5, mask=1,   cook_mode=ErdOvenCookMode.CONVMULTIBAKE_NOOPTION)
#    BYTE5_BIT1_1 = AvailableCookMode(byte=5, mask=2,   cook_mode=ErdOvenCookMode.CONVMULTIBAKE_PROBE)
#    BYTE5_BIT2_1 = AvailableCookMode(byte=5, mask=4,   cook_mode=ErdOvenCookMode.CONVMULTIBAKE_DELAYSTART)
#    #BYTE5_BIT3_1 = AvailableCookMode(byte=5, mask=8,   cook_mode=ErdOvenCookMode.CONVMULTIBAKETIMED)
#    BYTE5_BIT4_1 = AvailableCookMode(byte=5, mask=16,  cook_mode=ErdOvenCookMode.CONVBAKETIMED_WARM)
#    BYTE5_BIT5_1 = AvailableCookMode(byte=5, mask=32,  cook_mode=ErdOvenCookMode.CONVBAKETIMED_TWOTEMP)
#    BYTE5_BIT6_1 = AvailableCookMode(byte=5, mask=64,  cook_mode=ErdOvenCookMode.CONVMULTIBAKE_PROBE_DELAYSTART)
#    #BYTE5_BIT7_1 = AvailableCookMode(byte=5, mask=128, cook_mode=ErdOvenCookMode.CONVMULTIBAKETIMED_DELAYSTART)

#    BYTE6_BIT0_1 = AvailableCookMode(byte=6, mask=1,   cook_mode=ErdOvenCookMode.CONVMULTIBAKETIMED_WARM_DELAYSTART)
#    BYTE6_BIT1_1 = AvailableCookMode(byte=6, mask=2,   cook_mode=ErdOvenCookMode.CONVMULTIBAKETIMED_TWOTEMP_DELAYSTART)
#    BYTE6_BIT2_1 = AvailableCookMode(byte=6, mask=4,   cook_mode=ErdOvenCookMode.CONVROAST_NOOPTION)
#    BYTE6_BIT3_1 = AvailableCookMode(byte=6, mask=8,   cook_mode=ErdOvenCookMode.CONVROAST_PROBE)
#    BYTE6_BIT4_1 = AvailableCookMode(byte=6, mask=16,  cook_mode=ErdOvenCookMode.CONVROAST_DELAYSTART)
#    #BYTE6_BIT5_1 = AvailableCookMode(byte=6, mask=32,  cook_mode=ErdOvenCookMode.CONVROASTTIMED)
#    BYTE6_BIT6_1 = AvailableCookMode(byte=6, mask=64,  cook_mode=ErdOvenCookMode.CONVBAKETIMED_WARM)
#    BYTE6_BIT7_1 = AvailableCookMode(byte=6, mask=128, cook_mode=ErdOvenCookMode.CONVBAKETIMED_TWOTEMP)    

#    BYTE7_BIT0_1 = AvailableCookMode(byte=7, mask=1,   cook_mode=ErdOvenCookMode.CONVROAST_PROBE_DELAYSTART)
#    #BYTE7_BIT1_1 = AvailableCookMode(byte=7, mask=2,   cook_mode=ErdOvenCookMode.CONVROASTTIMED_DELAYSTART)
#    BYTE7_BIT2_1 = AvailableCookMode(byte=7, mask=4,   cook_mode=ErdOvenCookMode.CONVBROIL_LOW_NOOPTION)
#    BYTE7_BIT3_1 = AvailableCookMode(byte=7, mask=8,   cook_mode=ErdOvenCookMode.CONVBROIL_HIGH_NOOPTION)
#    BYTE7_BIT4_1 = AvailableCookMode(byte=7, mask=16,  cook_mode=ErdOvenCookMode.CONVBROILCRISP_NOOPTION)
#    BYTE7_BIT5_1 = AvailableCookMode(byte=7, mask=32,  cook_mode=ErdOvenCookMode.CONVBROILCRISP_PROBE)
#    #BYTE7_BIT6_1 = AvailableCookMode(byte=7, mask=64,  cook_mode=ErdOvenCookMode.SELFCLEAN)
#    BYTE7_BIT7_1 = AvailableCookMode(byte=7, mask=128, cook_mode=ErdOvenCookMode.STEAMCLEAN) 

    # From SmartHQ App
    OVEN_BAKE = AvailableCookMode(byte=9, mask=2, cook_mode=ErdOvenCookMode.BAKE_NOOPTION)
    OVEN_CONVECTION_BAKE = AvailableCookMode(byte=7, mask=4, cook_mode=ErdOvenCookMode.CONVBAKE_NOOPTION)
    OVEN_CONVECTION_MULTI_BAKE = AvailableCookMode(byte=6, mask=8, cook_mode=ErdOvenCookMode.CONVMULTIBAKE_NOOPTION)
    OVEN_CONVECTION_ROAST = AvailableCookMode(byte=5, mask=16, cook_mode=ErdOvenCookMode.CONVROAST_NOOPTION)
    OVEN_FROZEN_SNACKS = AvailableCookMode(byte=2, mask=1, cook_mode=ErdOvenCookMode.FROZEN_SNACKS)
    OVEN_FROZEN_SNACKS_MULTI = AvailableCookMode(byte=2, mask=2, cook_mode=ErdOvenCookMode.FROZEN_SNACKS_MULTI)
    OVEN_FROZEN_PIZZA = AvailableCookMode(byte=2, mask=4, cook_mode=ErdOvenCookMode.FROZEN_PIZZA)
    OVEN_FROZEN_PIZZA_MULTI = AvailableCookMode(byte=2, mask=8, cook_mode=ErdOvenCookMode.FROZEN_PIZZA_MULTI)
    OVEN_BAKED_GOODS = AvailableCookMode(byte=2, mask=16, cook_mode=ErdOvenCookMode.BAKED_GOODS)
