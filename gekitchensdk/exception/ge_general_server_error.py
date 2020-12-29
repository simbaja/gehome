from .ge_exception import GeException

class GeGeneralServerError(GeException):
    """Error raised when there is a server error (not 4xx http code)"""
    pass
