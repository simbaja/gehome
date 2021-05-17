from .ge_exception import GeException

class GeAuthFailedError(GeException):
    """Error raised when the client failed to authenticate"""
    pass
