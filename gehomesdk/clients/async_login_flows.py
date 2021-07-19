from aiohttp import BasicAuth, ClientSession
from lxml import etree
from urllib.parse import urlparse, parse_qs
import logging

from ..exception import *
from .const import (
    LOGIN_URL, 
    OAUTH2_CLIENT_ID, 
    OAUTH2_CLIENT_SECRET,
    OAUTH2_REDIRECT_URI
)

try:
    import re2 as re
except ImportError:
    import re

_LOGGER = logging.getLogger(__name__)  

async def async_get_authorization_code(session, account_username, account_password):
    params = {
        'client_id': OAUTH2_CLIENT_ID,
        'response_type': 'code',
        'access_type': 'offline',
        'redirect_uri': OAUTH2_REDIRECT_URI,
    }

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

    etr = etree.HTML(resp_text)
    post_data = {
        i.attrib['name']: i.attrib['value']
        for i in etr.xpath("//form[@id = 'frmsignin']//input")
        if 'value' in i.keys()
    }
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

    #parse the response into html
    etr = etree.HTML(resp_text)
    post_data = {}

    try:
        #first try to pull all the form values    
        post_data = {
            i.attrib['name']: i.attrib['value']
            for i in etr.xpath("//form[@id = 'frmsignin']//input")
            if 'value' in i.keys()
        }
    except:
        pass

    #if we have an authorized key, try to authorize the application
    if "authorized" in post_data:
        code = await async_authorize_application(session, post_data)
        return code

    #try to get the error based on the known responses
    try:
        reason = etr.find(".//div[@id='alert_pane']").text.translate({ord(c):"" for c in "\t\n"})
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

async def async_get_oauth2_token(session: ClientSession, account_username: str, account_password: str):
    """Hackily get an oauth2 token until I can be bothered to do this correctly"""

    #attempt to get the authorization code
    code = await async_get_authorization_code(session, account_username, account_password)

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
            access_token = oauth_token['access_token']
            return oauth_token
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')
    except Exception as exc:
        resp_text = await resp.text()
        _LOGGER.exception(f"Could not get OAuth token, response details: {resp.__dict__}")
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
            access_token = oauth_token['access_token']
            return oauth_token
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')
    except Exception as exc:
        resp_text = await resp.text()
        _LOGGER.exception(f"Could not refresh OAuth token, response details: {resp.__dict__}")
        raise GeAuthFailedError(f'Could not refresh OAuth token') from exc        