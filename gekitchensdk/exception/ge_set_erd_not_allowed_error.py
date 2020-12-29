from .ge_unsupported_operation_error import GeUnsupportedOperationError

class GeSetErdNotAllowedError(GeUnsupportedOperationError):
    """ Exception raised when ERD is not allowed to be set (readonly) """
    def __init__(self, erd_code: str, message="ERD cannot be set, it is readonly"):
        self.erd_code = erd_code
        self.message = message
    
    def __str__(self):
        return f'{self.erd_code} -> {self.message}'
