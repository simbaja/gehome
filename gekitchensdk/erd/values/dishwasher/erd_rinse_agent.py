import enum

#I might be doing something wrong, but I saw an "02" value come through
#which doesn't seem to be in any of the documentation I saw... it registered
#as low on the interface, so I'll just assume there's two codes
@enum.unique
class ErdRinseAgentRaw(enum.Enum):
    RINSE_AGENT_GOOD = "00"
    RINSE_AGENT_LOW1 = "01"
    RINSE_AGENT_LOW2 = "02"

@enum.unique
class ErdRinseAgent(enum.Enum):
    NA = "FF"
    RINSE_AGENT_GOOD = "00"
    RINSE_AGENT_LOW = "01"

