
from .ge_auth_failed_error import GeAuthFailedError

class GeAuthMfaRequiredError(GeAuthFailedError):
    """Raised when multi-factor authentication is required before
    authentication can proceed.

    This covers two distinct situations:

    - MFA *enrollment* is being requested (the account has no MFA method
      configured yet, and there is no automatic "skip" option). The user
      must configure MFA in the SmartHQ app or at
      https://accounts.brillion.geappliances.com.
    - An MFA verification *code challenge* was presented (the account
      already has MFA enabled). In this case, `mfa_methods` will contain
      the available verification methods (e.g. ``["email"]``) and the
      challenge can be completed interactively using `GeSmartHqLogin`
      instead of the simple `async_get_oauth2_token` helper. `csrf_token`
      carries the session token needed to resume the challenge (send/submit
      the code) without re-parsing the challenge page.
    """

    def __init__(
        self,
        *args,
        mfa_methods: list[str] | None = None,
        csrf_token: str | None = None,
    ):
        super().__init__(*args)
        self.mfa_methods: list[str] = mfa_methods or []
        self.csrf_token: str | None = csrf_token
