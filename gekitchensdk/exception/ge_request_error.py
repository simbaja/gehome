from .ge_exception import GeException

class GeRequestError(GeException):
    """ Exception raised when there is an error processing a message """
    def __init__(self, message: str, code, reason, *args: object) -> None:
        super().__init__(*args)
        self.code = code
        self.reason = reason
        self.message = message
    
    def __str__(self) -> str:
        return f"There was an error while processing a message: Code={self.code}, Reason={self.reason}, Message={self.message}"

