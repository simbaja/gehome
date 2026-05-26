from .ge_auth_failed_error import GeAuthFailedError

class GeAuthMfaRequiredError(GeAuthFailedError):
    """Raised when multi-factor authentication enrollment is required before
    authentication can proceed.  The user must configure MFA in the SmartHQ
    app or at https://accounts.brillion.geappliances.com."""
    pass
