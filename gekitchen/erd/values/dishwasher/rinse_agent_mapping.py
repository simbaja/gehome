from .erd_rinse_agent import ErdRinseAgent, ErdRinseAgentRaw

RINSE_AGENT_RAW_MAP = {
    ErdRinseAgentRaw.RINSE_AGENT_GOOD: ErdRinseAgent.RINSE_AGENT_GOOD,
    ErdRinseAgentRaw.RINSE_AGENT_LOW1: ErdRinseAgent.RINSE_AGENT_LOW,
    ErdRinseAgentRaw.RINSE_AGENT_LOW2: ErdRinseAgent.RINSE_AGENT_LOW
}
