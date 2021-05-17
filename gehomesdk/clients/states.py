import enum

@enum.unique
class GeClientState(enum.Enum):
    INITIALIZING = enum.auto()
    AUTHORIZING_OAUTH = enum.auto()
    AUTHORIZING_CLIENT = enum.auto()
    CONNECTING = enum.auto()
    CONNECTED = enum.auto()
    DROPPED = enum.auto()
    WAITING = enum.auto()
    DISCONNECTING = enum.auto()
    DISCONNECTED = enum.auto()
