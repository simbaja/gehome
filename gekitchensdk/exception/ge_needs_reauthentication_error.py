from .ge_exception import GeException

class GeNeedsReauthenticationError(GeException):
    """Error raised when the reauthentication is needed"""
    pass