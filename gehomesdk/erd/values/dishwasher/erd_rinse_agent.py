import enum

#I might be doing something wrong, but I saw an "02" value come through
#which doesn't seem to be in any of the documentation I saw... it registered
#as low on the interface, so I'll just assume there's two codes
#Saw a 04 code - which seemed to correspond to dispensing (during wash). Don't know what 03 is though.
@enum.unique
class ErdRinseAgentRaw(enum.Enum):
    RINSE_AGENT_GOOD = "00"
    RINSE_AGENT_LOW1 = "01"
    RINSE_AGENT_LOW2 = "02"
    RINSE_AGENT_EMPTY = "03"
    RINSE_AGENT_DISPENSING = "04"

@enum.unique
class ErdRinseAgent(enum.Enum):
    NA = "FF"
    RINSE_AGENT_GOOD = "00"
    RINSE_AGENT_LOW = "01"
    RINSE_AGENT_LOW2 = "02"
    RINSE_AGENT_EMPTY = "03"
    RINSE_AGENT_DISPENSING = "04"

    def stringify(self, **kwargs):
        return self.name.replace("RINSE_AGENT_","").replace("_"," ").title()

