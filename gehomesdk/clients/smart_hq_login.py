"""Interactive (MFA-aware) SmartHQ login.

This module is a thin, stateful wrapper around the composable building
blocks in `async_login_flows` (`async_get_authorization_code`,
`_handle_response`, `async_exchange_authorization_code`, etc.). It adds no
duplicate HTML/redirect handling of its own; it just resumes the same
login flow when an MFA verification-code challenge is raised, and drives
the SmartHQ-specific "send code"/"submit code" endpoints.
"""

import logging
from aiohttp import ClientSession
from dataclasses import dataclass, field
from urllib.parse import urljoin
from typing import List, Optional

from ..exception import *
from .const import (
    LOGIN_URL,
    MFA_SENDTOTP_PATH,
    MFA_SENDTOTP_PROCESS_PATH,
    MFA_VERIFY_PATH,
)
from .async_login_flows import (
    _handle_response,
    _raise_for_status,
    async_exchange_authorization_code,
    async_get_authorization_code,
    extract_csrf_token,
)

_LOGGER = logging.getLogger(__name__)

@dataclass
class GeLoginResult:
    """Outcome of an authentication attempt against the SmartHQ login
    pages, used by `GeSmartHqLogin`.

    If `mfa_required` is True, `token` is None and the caller must
    complete the challenge via `GeSmartHqLogin.async_send_code` and
    `GeSmartHqLogin.async_submit_code` before a token is available.
    """

    token: Optional[dict] = None
    mfa_required: bool = False
    mfa_methods: List[str] = field(default_factory=list)


class GeSmartHqLogin:
    """Drives the SmartHQ OAuth login, including the multi-factor
    authentication (MFA) one-time-code challenge.

    Some SmartHQ accounts require an emailed (or SMS) verification code
    during login. `async_get_oauth2_token` has no way to satisfy that
    challenge, since it requires interactively prompting the user for the
    code, so it simply raises `GeAuthMfaRequiredError`. Applications that
    want to complete the challenge (e.g. a Home Assistant config flow)
    should use this class instead::

        login = GeSmartHqLogin(session)
        result = await login.async_login(username, password, region)
        if result.mfa_required:
            await login.async_send_code(result.mfa_methods[0])
            # ... prompt the user for the emailed/texted code ...
            token = await login.async_submit_code(code)
        else:
            token = result.token

    The resulting token dict includes a ``refresh_token`` that can be
    passed to a client (e.g. via the `refresh_token` constructor argument
    of `GeBaseClient`) so future reconnects don't repeat the MFA challenge.

    Instances are single-use per login attempt, but survive across steps:
    the aiohttp session's cookie jar carries the server-side session, and
    the CSRF token is cached on the instance between calls.
    """

    def __init__(self, session: ClientSession):
        self._session = session
        self._csrf: Optional[str] = None
        self._mfa_type: str = "email"

    async def async_login(
        self,
        account_username: str,
        account_password: str,
        account_region: str,
    ) -> GeLoginResult:
        """Submit credentials. Returns a token, or signals that an MFA
        verification code challenge is required.

        This reuses `async_get_authorization_code` for the entire
        credentials/redirect/HTML walk; the only difference from the
        non-interactive flow is that a `GeAuthMfaRequiredError` is caught
        here (instead of propagating) so the challenge can be resumed.
        """
        try:
            auth_code = await async_get_authorization_code(
                self._session, account_username, account_password, account_region
            )
        except GeAuthMfaRequiredError as err:
            self._csrf = err.csrf_token
            return GeLoginResult(mfa_required=True, mfa_methods=err.mfa_methods or ["email"])

        return GeLoginResult(token=await async_exchange_authorization_code(self._session, auth_code))

    async def async_send_code(self, method: str = "email") -> None:
        """Trigger delivery of the one-time verification code for the
        chosen method (must be called after `async_login` returns a result
        with `mfa_required` set)."""
        if not self._csrf:
            raise GeAuthFailedError("Missing session token for MFA; call async_login first")
        self._mfa_type = method
        data = {"mfaType": method, "_csrf": self._csrf}

        # Interstitial "send code" page.
        async with self._session.post(
            urljoin(LOGIN_URL, MFA_SENDTOTP_PATH), data=data, allow_redirects=False
        ) as resp:
            _raise_for_status(resp.status)
            html = await resp.text()
        self._csrf = extract_csrf_token(html) or self._csrf

        # Actually send the code (email/SMS).
        data["_csrf"] = self._csrf
        async with self._session.post(
            urljoin(LOGIN_URL, MFA_SENDTOTP_PROCESS_PATH), data=data, allow_redirects=False
        ) as resp:
            _raise_for_status(resp.status)
            html = await resp.text()
        self._csrf = extract_csrf_token(html) or self._csrf

    async def async_submit_code(self, code: str) -> dict:
        """Submit the verification code; returns the OAuth token dict
        (including ``refresh_token``) on success.

        Delegates redirect/HTML handling after submission to the shared
        `_handle_response` building block; only the SmartHQ-specific
        "invalid code re-renders the page with status 200" case is handled
        here.
        """
        if not self._csrf:
            raise GeAuthFailedError("Missing session token for MFA; call async_login first")
        data = {"mfaType": self._mfa_type, "totpCode": code.strip(), "_csrf": self._csrf}

        async with self._session.post(
            urljoin(LOGIN_URL, MFA_VERIFY_PATH), data=data, allow_redirects=False
        ) as resp:
            if resp.status == 200:
                # Wrong/expired code re-renders the entry page; refresh CSRF for retry.
                html = await resp.text()
                self._csrf = extract_csrf_token(html) or self._csrf
                raise GeAuthFailedError("Invalid or expired verification code")

            if resp.status not in (301, 302, 303, 307, 308):
                _raise_for_status(resp.status)

            auth_code = await _handle_response(self._session, resp)

        return await async_exchange_authorization_code(self._session, auth_code)

