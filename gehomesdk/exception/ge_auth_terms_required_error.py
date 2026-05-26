from .ge_auth_failed_error import GeAuthFailedError

class GeAuthTermsRequiredError(GeAuthFailedError):
    """Raised when the user must accept updated Terms of Service before
    authentication can proceed.  The user must accept the terms in the
    SmartHQ app or at https://accounts.brillion.geappliances.com."""
    pass
