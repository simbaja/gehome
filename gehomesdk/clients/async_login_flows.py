from http.cookies import SimpleCookie
from aiohttp import BasicAuth, ClientSession
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import logging
from typing import Any, Dict

from ..exception import *
from .const import (
    LOGIN_COOKIE_DOMAIN,
    LOGIN_REGION_COOKIE_NAME,
    LOGIN_REGIONS,
    LOGIN_URL, 
    OAUTH2_CLIENT_ID, 
    OAUTH2_CLIENT_SECRET,
    OAUTH2_REDIRECT_URI
)

try:
    import re2 as re # pyright: ignore[reportMissingImports]
except ImportError:
    import re

_LOGGER = logging.getLogger(__name__)  

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
    """
    Parse `html`, find form with id `form_id`, and return a mapping of input name -> value.
    """
    soup = BeautifulSoup(html, "html.parser")
    form = soup.find("form", id=form_id)
    if not form:
        return {}

    result: Dict[str, str] = {}
    for i in form.find_all("input"):
        
        name = normalize_html_attr_value(i.get("name"))
        if not name:
            continue

        # use empty string if no value attribute present
        value = i.get("value", "")
        result[name] = normalize_html_attr_value(value)
    return result


async def async_get_authorization_code(session: ClientSession, account_username: str, account_password: str, account_region: str):
    params = {
        'client_id': OAUTH2_CLIENT_ID,
        'response_type': 'code',
        'access_type': 'offline',
        'redirect_uri': OAUTH2_REDIRECT_URI,
    }

    set_login_cookie(session, account_region)

    async with session.get(f'{LOGIN_URL}/oauth2/auth', params=params) as resp:
        if 400 <= resp.status < 500:
            raise GeAuthFailedError(await resp.text())
        if resp.status >= 500:
            raise GeGeneralServerError(await resp.text())
        resp_text = await resp.text()

    email_regex = (
        r'^\s*(\w+(?:(?:-\w+)|(?:\.\w+)|(?:\+\w+))*\@'
        r'[A-Za-z0-9]+(?:(?:\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9][A-Za-z0-9]+)\s*$'
    )
    clean_username = re.sub(email_regex, r'\1', account_username)

    post_data = extract_form_inputs(resp_text, 'frmsignin')
    post_data['username'] = clean_username
    post_data['password'] = account_password

    async with session.post(f'{LOGIN_URL}/oauth2/g_authenticate', data=post_data, allow_redirects=False) as resp:
        if 400 <= resp.status < 500:
            raise GeAuthFailedError(f"Problem with request, code: {resp.status}")
        if resp.status >= 500:
            raise GeGeneralServerError(f"Server error, code: {resp.status}")
        try:
            if resp.status == 200:
                #if we have an OK response, probably need to "authorize", but could also
                #be an authentication issue
                code = await async_handle_ok_response(session, await resp.text())
            else:
                #assume response has a location header from which we can get a code
                code = parse_qs(urlparse(resp.headers['Location']).query)['code'][0]
        except Exception as exc:
            resp_text = await resp.text()
            _LOGGER.exception(f"There was a problem getting the authorization code, response details: {resp.__dict__}")
            raise GeAuthFailedError(f'Could not obtain authorization code') from exc
    return code

async def async_handle_ok_response(session: ClientSession, resp_text: str) -> str:
    """Handles an OK 200 response from the login process"""
    
    # Check if this is an MFA enrollment page
    if "Add Multi-Factor Authentication" in resp_text or "addMfaForm" in resp_text:
        _LOGGER.info("MFA enrollment page detected, attempting to skip MFA automatically...")
        
        try:
            soup = BeautifulSoup(resp_text, "html.parser")
            mfa_form = soup.find("form", id="addMfaForm")
            
            if not mfa_form:
                _LOGGER.error("Could not find MFA form in the response")
                raise GeAuthFailedError("MFA enrollment page detected but could not find the form. Please log into the SmartHQ app and skip or complete MFA setup manually.")
            
            # Extract CSRF token from the form
            form_data = {}
            csrf_input = mfa_form.find("input", {"name": "_csrf"})
            if csrf_input:
                form_data["_csrf"] = csrf_input.get("value", "")
            
            # Also try to get CSRF from meta tag
            csrf_meta = soup.find("meta", {"name": "_csrf"})
            if csrf_meta and not form_data.get("_csrf"):
                form_data["_csrf"] = csrf_meta.get("content", "")
            
            _LOGGER.debug(f"Submitting MFA skip with CSRF token: {form_data.get('_csrf', 'none')[:20]}...")
            
            # Submit the skip action (POST to /account/active/redirect)
            async with session.post(
                f"{LOGIN_URL}/account/active/redirect",
                data=form_data,
                allow_redirects=False
            ) as skip_resp:
                skip_status = skip_resp.status
                _LOGGER.debug(f"MFA skip response status: {skip_status}")
                
                # Check if we got a redirect (success case)
                if skip_status in (301, 302, 303, 307, 308):
                    location = skip_resp.headers.get('Location', '')
                    _LOGGER.debug(f"MFA skip redirect location: {location}")
                    
                    # Check if the redirect contains the auth code
                    if 'code=' in location:
                        code = parse_qs(urlparse(location).query).get('code', [None])[0]
                        if code:
                            _LOGGER.info("Successfully skipped MFA and obtained authorization code")
                            return code
                    
                    # Follow the redirect manually
                    # Handle relative URLs
                    if location.startswith('/'):
                        location = f"{LOGIN_URL}{location}"
                    
                    async with session.get(location, allow_redirects=False) as redirect_resp:
                        _LOGGER.debug(f"Redirect response status: {redirect_resp.status}")
                        if redirect_resp.status in (301, 302, 303, 307, 308):
                            final_location = redirect_resp.headers.get('Location', '')
                            if 'code=' in final_location:
                                code = parse_qs(urlparse(final_location).query).get('code', [None])[0]
                                if code:
                                    _LOGGER.info("Successfully skipped MFA and obtained authorization code")
                                    return code
                        # Recursively handle the response
                        redirect_text = await redirect_resp.text()
                        return await async_handle_ok_response(session, redirect_text)
                
                # If we got a 200, recursively handle it
                if skip_status == 200:
                    skip_resp_text = await skip_resp.text()
                    return await async_handle_ok_response(session, skip_resp_text)
                
                # Handle error responses
                resp_body = await skip_resp.text()
                _LOGGER.error(f"MFA skip failed with status {skip_status}")
                _LOGGER.debug(f"MFA skip response body: {resp_body[:2000]}")
                raise GeAuthFailedError(f"MFA skip failed with status {skip_status}. Please log into the SmartHQ app and skip or complete MFA setup manually.")
                
        except GeAuthFailedError:
            raise
        except Exception as e:
            _LOGGER.exception(f"Error during MFA skip: {e}")
            raise GeAuthFailedError(f"MFA skip failed: {e}. Please log into the SmartHQ app and skip or complete MFA setup manually.") from e
    
    # Check if this is a terms acceptance page
    if "Almost Finished" in resp_text and "/oauth2/terms/accept" in resp_text:
        _LOGGER.info("Terms acceptance page detected, attempting to accept terms automatically...")
        
        try:
            # Parse the form fields from the HTML using BeautifulSoup for reliability
            soup = BeautifulSoup(resp_text, "html.parser")
            # Try finding by id first, then by name
            terms_form = soup.find("form", id="termsform")
            if not terms_form:
                terms_form = soup.find("form", {"name": "termsform"})
            
            if not terms_form:
                _LOGGER.error("Could not find terms form in the response")
                _LOGGER.debug(f"Response preview: {resp_text[:1000]}")
                raise GeAuthFailedError("Terms acceptance page detected but could not find the form")
            
            _LOGGER.debug("Found terms form in HTML")
            
            # Extract all hidden input values from the form using regex for reliability
            # The HTML has malformed attributes (no quotes around some values)
            form_data = {}
            
            # Extract signature (properly quoted)
            sig_match = re.search(r'name="signature"\s+value="([^"]+)"', resp_text)
            if sig_match:
                form_data["signature"] = sig_match.group(1)
                _LOGGER.debug(f"Found signature: {form_data['signature'][:50]}...")
            
            # Extract login_actions_signature (NOT quoted - value=XXX>)
            las_match = re.search(r'name="login_actions_signature"[^>]*value=([^>\s]+)>', resp_text)
            if las_match:
                # Remove trailing > if present
                las_value = las_match.group(1).rstrip('>')
                form_data["login_actions_signature"] = las_value
                _LOGGER.debug(f"Found login_actions_signature: {las_value[:50]}...")
            
            # Extract isDeveloper
            dev_match = re.search(r'name="isDeveloper"\s+value="([^"]+)"', resp_text)
            if dev_match:
                form_data["isDeveloper"] = dev_match.group(1)
            
            # Extract _csrf from form
            csrf_match = re.search(r'name="_csrf"\s+value="([^"]+)"', resp_text)
            if csrf_match:
                form_data["_csrf"] = csrf_match.group(1)
                _LOGGER.debug(f"Found _csrf: {form_data['_csrf']}")
            
            _LOGGER.info(f"Extracted form fields via regex: {list(form_data.keys())}")
            
            # Set the checkbox values to indicate acceptance
            # The HTML shows checkboxes with names "developerTerms" and "connected_terms"
            # When checked, browsers send "on" as the value
            form_data["developerTerms"] = "on"
            form_data["connected_terms"] = "on"
            
            # Use the CSRF token from the form data for the header
            csrf_token = form_data.get("_csrf", "")
            
            # Build headers with CSRF token
            headers = {}
            if csrf_token:
                headers["X-CSRF-TOKEN"] = csrf_token
            
            _LOGGER.debug(f"Submitting terms acceptance with {len(form_data)} fields: {list(form_data.keys())}")
            
            async with session.post(
                f"{LOGIN_URL}/oauth2/terms/accept",
                data=form_data,
                headers=headers,
                allow_redirects=False  # Don't auto-follow to capture redirect
            ) as terms_resp:
                terms_status = terms_resp.status
                _LOGGER.debug(f"Terms acceptance response status: {terms_status}")
                
                # Check if we got a redirect (success case)
                if terms_status in (301, 302, 303, 307, 308):
                    location = terms_resp.headers.get('Location', '')
                    _LOGGER.debug(f"Terms acceptance redirect location: {location}")
                    
                    # Check if the redirect contains the auth code
                    if 'code=' in location:
                        code = parse_qs(urlparse(location).query).get('code', [None])[0]
                        if code:
                            _LOGGER.info("Successfully accepted terms and obtained authorization code")
                            return code
                    
                    # Follow the redirect manually
                    async with session.get(location, allow_redirects=False) as redirect_resp:
                        _LOGGER.debug(f"Redirect response status: {redirect_resp.status}")
                        if redirect_resp.status in (301, 302, 303, 307, 308):
                            final_location = redirect_resp.headers.get('Location', '')
                            if 'code=' in final_location:
                                code = parse_qs(urlparse(final_location).query).get('code', [None])[0]
                                if code:
                                    _LOGGER.info("Successfully accepted terms and obtained authorization code")
                                    return code
                        # Recursively handle the response
                        redirect_text = await redirect_resp.text()
                        return await async_handle_ok_response(session, redirect_text)
                
                # If we got a 200, recursively handle it
                if terms_status == 200:
                    terms_resp_text = await terms_resp.text()
                    return await async_handle_ok_response(session, terms_resp_text)
                
                # Handle error responses
                resp_body = await terms_resp.text()
                _LOGGER.error(f"Terms acceptance failed with status {terms_status}")
                _LOGGER.debug(f"Terms response body: {resp_body[:2000]}")
                raise GeAuthFailedError(f"Terms acceptance failed with status {terms_status}")
                
        except GeAuthFailedError:
            raise
        except Exception as e:
            _LOGGER.exception(f"Error during terms acceptance: {e}")
            raise GeAuthFailedError(f"Terms acceptance failed: {e}") from e

    post_data = {}

    try:
        #first try to pull all the form values    
        post_data = extract_form_inputs(resp_text, 'frmsignin')
    except:
        pass

    #if we have an authorized key, try to authorize the application
    if "authorized" in post_data:
        code = await async_authorize_application(session, post_data)
        return code

    #try to get the error based on the known responses
    try:
        soup = BeautifulSoup(resp_text, "html.parser")
        pane = soup.find("div", id="alert_pane")
        if pane is not None:
            text = pane.get_text()
            if text:
                reason = text.translate({ord(c): "" for c in "\t\n"})
                raise GeAuthFailedError(f"Authentication failed, reason: {reason}")
    except GeAuthFailedError:
        raise #re-raise only auth failed errors, all others are irrelevant at this point
    except:
        pass

    #throw an exception by default
    raise GeAuthFailedError("Authentication failed for unknown reason, please review response text for clues.")

async def async_authorize_application(session: ClientSession, post_data: dict) -> str:
    """Authorizes the application if needed"""

    _LOGGER.info(
        "The application requires authentication and will attempt to grant consent automatically. " + \
        "Visit https://accounts.brillion.geappliances.com/consumer/active/applications to deauthorize.")

    post_data["authorized"] = "yes"

    async with session.post(f'{LOGIN_URL}/oauth2/code', data=post_data, allow_redirects=False) as resp:
        if 400 <= resp.status < 500:
            raise GeAuthFailedError(f"Problem with request, code: {resp.status}")
        if resp.status >= 500:
            raise GeGeneralServerError(f"Server error, code: {resp.status}")
        try:
            #oauth2/code appears to give the same header as we expect in the normal case, so let's try to use it
            code = parse_qs(urlparse(resp.headers['Location']).query)['code'][0]
        except Exception as exc:
            resp_text = await resp.text()
            _LOGGER.exception(f"There was a problem authorizing the application, response details: {resp.__dict__}")
            raise GeAuthFailedError(f'Could not authorize application') from exc
    return code    

async def async_get_oauth2_token(session: ClientSession, account_username: str, account_password: str, account_region: str):
    """Hackily get an oauth2 token until I can be bothered to do this correctly"""

    #attempt to get the authorization code
    code = await async_get_authorization_code(session, account_username, account_password, account_region)

    #get the token
    post_data = {
        'code': code,
        'client_id': OAUTH2_CLIENT_ID,
        'client_secret': OAUTH2_CLIENT_SECRET,
        'redirect_uri': OAUTH2_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }
    try:
        auth = BasicAuth(OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)
        async with session.post(f'{LOGIN_URL}/oauth2/token', data=post_data, auth=auth) as resp:
            if 400 <= resp.status < 500:
                raise GeAuthFailedError(f"Problem with request, code: {resp.status}")
            if resp.status >= 500:
                raise GeGeneralServerError(f"Server error, code: {resp.status}")
            oauth_token = await resp.json()
        try:
            _ = oauth_token['access_token']
            return oauth_token
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')
        except Exception as exc:
            resp_text = await resp.text()
            _LOGGER.exception(f"Could not get OAuth token, response details: {resp.__dict__}")
            raise GeAuthFailedError(f'Could not get OAuth token') from exc
    except Exception as exc:
        raise GeAuthFailedError(f'Could not get OAuth token') from exc

async def async_refresh_oauth2_token(session: ClientSession, refresh_token: str):
    """ Refreshes an OAuth2 Token based on a refresh token """

    post_data = {
        'redirect_uri': OAUTH2_REDIRECT_URI,
        'client_id': OAUTH2_CLIENT_ID,
        'client_secret': OAUTH2_CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    try:
        auth = BasicAuth(OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)
        async with session.post(f'{LOGIN_URL}/oauth2/token', data=post_data, auth=auth) as resp:
            if 400 <= resp.status < 500:
                raise GeAuthFailedError(f"Problem with request, code: {resp.status}")
            if resp.status >= 500:
                raise GeGeneralServerError(f"Server error, code: {resp.status}")
            oauth_token = await resp.json()
        try:
            _ = oauth_token['access_token']
            return oauth_token
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')
        except Exception as exc:
            _ = await resp.text()
            _LOGGER.exception(f"Could not refresh OAuth token, response details: {resp.__dict__}")
            raise GeAuthFailedError(f'Could not refresh OAuth token') from exc
    except Exception as exc:
        raise GeAuthFailedError(f'Could not refresh OAuth token') from exc

