from http.cookies import SimpleCookie
from aiohttp import BasicAuth, ClientSession
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urljoin
import logging
from typing import Any, Dict, List, Optional

from ..exception import *
from .const import (
    LOGIN_COOKIE_DOMAIN,
    LOGIN_REGION_COOKIE_NAME,
    LOGIN_REGIONS,
    LOGIN_URL,
    MFA_OPTIONS_PATH,
    OAUTH2_CLIENT_ID,
    OAUTH2_CLIENT_SECRET,
    OAUTH2_REDIRECT_URI,
)

try:
    import re2 as re  # pyright: ignore
except ImportError:
    import re

_LOGGER = logging.getLogger(__name__)

MAX_REDIRECTS = 10


# ---------------------------------------------------------------------------
# Utility Helpers
# ---------------------------------------------------------------------------

def set_login_cookie(session: ClientSession, account_region: str):
    c = SimpleCookie()
    c[LOGIN_REGION_COOKIE_NAME] = LOGIN_REGIONS[account_region]
    c[LOGIN_REGION_COOKIE_NAME]["domain"] = LOGIN_COOKIE_DOMAIN
    c[LOGIN_REGION_COOKIE_NAME]["path"] = "/"
    c[LOGIN_REGION_COOKIE_NAME]["httponly"] = True
    c[LOGIN_REGION_COOKIE_NAME]["secure"] = True
    session.cookie_jar.update_cookies(c)


def normalize_html_attr_value(raw: Any) -> str:
    if isinstance(raw, (list, tuple)):
        return " ".join(str(x) for x in raw)
    if raw is None:
        return ""
    return str(raw)


def extract_form_inputs(html: str, form_id: str) -> Dict[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    form = soup.find("form", id=form_id)
    if not form:
        return {}

    result: Dict[str, str] = {}
    for i in form.find_all("input"):
        name = normalize_html_attr_value(i.get("name"))
        if not name:
            continue
        value = i.get("value", "")
        result[name] = normalize_html_attr_value(value)
    return result


def extract_code_from_location(location: str) -> Optional[str]:
    if not location:
        return None
    parsed = urlparse(location)
    qs = parse_qs(parsed.query)
    return qs.get("code", [None])[0]


def extract_mfa_methods(html: str) -> List[str]:
    """Extract the available MFA verification methods from the method
    chooser page (e.g. buttons named ``email_btn``/``sms_btn`` with the
    method as their value)."""
    soup = BeautifulSoup(html, "html.parser")
    methods: List[str] = []
    for btn in soup.find_all("button"):
        name = normalize_html_attr_value(btn.get("name"))
        value = normalize_html_attr_value(btn.get("value"))
        if name.endswith("_btn") and value:
            methods.append(value)
    return methods


def extract_csrf_token(html: str) -> Optional[str]:
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find("input", attrs={"name": "_csrf"})
    if tag and tag.get("value"):
        return normalize_html_attr_value(tag.get("value"))
    meta = soup.find("meta", attrs={"name": "_csrf"})
    if meta and meta.get("content"):
        return normalize_html_attr_value(meta.get("content"))
    return None


def _raise_for_status(status: int, text: str = "") -> None:
    if 400 <= status < 500:
        raise GeAuthFailedError(f"Login failed ({status}) {text[:200]}")
    if status >= 500:
        raise GeGeneralServerError(f"Server error ({status})")

# ---------------------------------------------------------------------------
# Core OAuth Flow
# ---------------------------------------------------------------------------

async def async_get_authorization_code(
    session: ClientSession,
    account_username: str,
    account_password: str,
    account_region: str,
) -> str:

    params = {
        "client_id": OAUTH2_CLIENT_ID,
        "response_type": "code",
        "access_type": "offline",
        "redirect_uri": OAUTH2_REDIRECT_URI,
    }

    set_login_cookie(session, account_region)

    async with session.get(f"{LOGIN_URL}/oauth2/auth", params=params) as resp:
        if 400 <= resp.status < 500:
            raise GeAuthFailedError(await resp.text())
        if resp.status >= 500:
            raise GeGeneralServerError(await resp.text())
        login_page = await resp.text()

    email_regex = (
        r'^\s*(\w+(?:(?:-\w+)|(?:\.\w+)|(?:\+\w+))*\@'
        r'[A-Za-z0-9]+(?:(?:\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9][A-Za-z0-9]+)\s*$'
    )
    clean_username = re.sub(email_regex, r"\1", account_username)

    post_data = extract_form_inputs(login_page, "frmsignin")
    post_data["username"] = clean_username
    post_data["password"] = account_password

    async with session.post(
        f"{LOGIN_URL}/oauth2/g_authenticate",
        data=post_data,
        allow_redirects=False,
    ) as resp:

        if 400 <= resp.status < 500:
            raise GeAuthFailedError(f"Login failed ({resp.status})")
        if resp.status >= 500:
            raise GeGeneralServerError(f"Server error ({resp.status})")

        return await _handle_response(session, resp)


async def _handle_response(
    session: ClientSession,
    resp,
    redirect_count: int = 0,
) -> str:

    if redirect_count > MAX_REDIRECTS:
        raise GeAuthFailedError("Too many redirects during login")

    # -----------------------------------
    # REDIRECT HANDLING
    # -----------------------------------
    if resp.status in (301, 302, 303, 307, 308):
        location = resp.headers.get("Location", "")

        code = extract_code_from_location(location)
        if code:
            _LOGGER.info("OAuth authorization code obtained via redirect")
            return code

        next_url = urljoin(LOGIN_URL, location)
        _LOGGER.debug(f"Following redirect to {next_url}")

        async with session.get(next_url, allow_redirects=False) as next_resp:
            return await _handle_response(
                session, next_resp, redirect_count + 1
            )

    # -----------------------------------
    # HTML HANDLING (200)
    # -----------------------------------
    if resp.status == 200:
        text = await resp.text()
        return await _handle_html(session, text)

    raise GeAuthFailedError(
        f"Unexpected response status {resp.status}"
    )


# ---------------------------------------------------------------------------
# HTML Page Handlers
# ---------------------------------------------------------------------------

async def _handle_html(session: ClientSession, html: str) -> str:

    # -------------------------------------------------
    # MFA Verification Code Challenge
    # -------------------------------------------------
    # The account already has MFA enabled and the login is being asked to
    # complete a one-time-code challenge. This can't be completed here
    # (it requires interactively prompting the user for the code), so
    # surface it as an exception with the available methods. Callers that
    # want to complete the challenge should use `GeSmartHqLogin` instead
    # of `async_get_oauth2_token`.
    if (
        MFA_OPTIONS_PATH in html
        or "verifyOptionForm" in html
    ):
        methods = extract_mfa_methods(html) or ["email"]
        csrf = extract_csrf_token(html)
        _LOGGER.info("SmartHQ MFA verification challenge detected; methods=%s", methods)
        raise GeAuthMfaRequiredError(
            "Multi-factor authentication verification code required. Use "
            "GeSmartHqLogin to complete the MFA challenge interactively.",
            mfa_methods=methods,
            csrf_token=csrf,
        )

    # -------------------------------------------------
    # MFA Enrollment Page
    # -------------------------------------------------
    if (
        "addMfaForm" in html
        or "Multi-Factor Authentication" in html
        or "/account/active/security/add/mfamethod" in html
    ):
        _LOGGER.info("MFA enrollment page detected")

        soup = BeautifulSoup(html, "html.parser")
        form = soup.find("form", id="addMfaForm")

        if not form:
            raise GeAuthMfaRequiredError(
                "MFA enrollment required. Please configure multi-factor authentication "
                "in the SmartHQ app or at https://accounts.brillion.geappliances.com "
                "and then retry."
            )

        form_data = {}
        for i in form.find_all("input"):
            name = i.get("name")
            if name:
                form_data[name] = i.get("value", "")

        async with session.post(
            f"{LOGIN_URL}/account/active/redirect",
            data=form_data,
            allow_redirects=False,
        ) as resp:
            return await _handle_response(session, resp)

    # -------------------------------------------------
    # Terms Acceptance
    # -------------------------------------------------
    if "/oauth2/terms/accept" in html:
        _LOGGER.info("Terms acceptance page detected")

        soup = BeautifulSoup(html, "html.parser")
        form = soup.find("form")

        if not form:
            raise GeAuthTermsRequiredError(
                "Terms acceptance required. Please accept the updated Terms of Service "
                "in the SmartHQ app or at https://accounts.brillion.geappliances.com "
                "and then retry."
            )

        form_data = {}
        for i in form.find_all("input"):
            name = i.get("name")
            if name:
                form_data[name] = i.get("value", "")

        form_data["developerTerms"] = "on"
        form_data["connected_terms"] = "on"

        async with session.post(
            f"{LOGIN_URL}/oauth2/terms/accept",
            data=form_data,
            allow_redirects=False,
        ) as resp:
            return await _handle_response(session, resp)

    # -------------------------------------------------
    # App Authorization
    # -------------------------------------------------
    form_data = extract_form_inputs(html, "frmsignin")
    if "authorized" in form_data:
        _LOGGER.info("Authorizing application automatically")
        form_data["authorized"] = "yes"

        async with session.post(
            f"{LOGIN_URL}/oauth2/code",
            data=form_data,
            allow_redirects=False,
        ) as resp:
            return await _handle_response(session, resp)

    # -------------------------------------------------
    # Login Error
    # -------------------------------------------------
    soup = BeautifulSoup(html, "html.parser")
    pane = soup.find("div", id="alert_pane")
    if pane:
        reason = pane.get_text(strip=True)
        raise GeAuthFailedError(f"Authentication failed: {reason}")

    raise GeAuthFailedError(
        "Authentication failed for unknown reason."
    )


# ---------------------------------------------------------------------------
# Token Exchange
# ---------------------------------------------------------------------------

async def async_exchange_authorization_code(
    session: ClientSession,
    code: str,
) -> dict:
    """Exchange an OAuth2 authorization code for an access/refresh token pair."""

    post_data = {
        "code": code,
        "client_id": OAUTH2_CLIENT_ID,
        "client_secret": OAUTH2_CLIENT_SECRET,
        "redirect_uri": OAUTH2_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    auth = BasicAuth(OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)

    async with session.post(
        f"{LOGIN_URL}/oauth2/token",
        data=post_data,
        auth=auth,
    ) as resp:
        _raise_for_status(resp.status, f"Token request failed ({resp.status})")
        token = await resp.json()

    if "access_token" not in token:
        raise GeAuthFailedError(f"Invalid token response: {token}")

    return token


async def async_get_oauth2_token(
    session: ClientSession,
    account_username: str,
    account_password: str,
    account_region: str,
):

    code = await async_get_authorization_code(
        session,
        account_username,
        account_password,
        account_region,
    )

    return await async_exchange_authorization_code(session, code)


async def async_refresh_oauth2_token(
    session: ClientSession,
    refresh_token: str,
):

    post_data = {
        "redirect_uri": OAUTH2_REDIRECT_URI,
        "client_id": OAUTH2_CLIENT_ID,
        "client_secret": OAUTH2_CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    auth = BasicAuth(OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)

    async with session.post(
        f"{LOGIN_URL}/oauth2/token",
        data=post_data,
        auth=auth,
    ) as resp:

        if 400 <= resp.status < 500:
            raise GeAuthFailedError(f"Refresh failed ({resp.status})")
        if resp.status >= 500:
            raise GeGeneralServerError(f"Server error ({resp.status})")

        token = await resp.json()

    if "access_token" not in token:
        raise GeAuthFailedError(f"Invalid refresh response: {token}")

    return token