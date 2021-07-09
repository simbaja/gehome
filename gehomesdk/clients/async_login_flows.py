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

async def async_get_oauth2_token(session: ClientSession, account_username: str, account_password: str):
    """Hackily get an oauth2 token until I can be bothered to do this correctly"""

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
            raise GeAuthFailedError(await resp.text())
        if resp.status >= 500:
            raise GeGeneralServerError(await resp.text())
        try:
            code = parse_qs(urlparse(resp.headers['Location']).query)['code'][0]
        except:
            _LOGGER.exception(f"There was a problem getting the authorization code, full response: {resp}")
            raise GeAuthFailedError(f'Could not obtain authorization code')

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
                raise GeAuthFailedError(await resp.text())
            if resp.status >= 500:
                raise GeGeneralServerError(await resp.text())
            oauth_token = await resp.json()
        try:
            access_token = oauth_token['access_token']
            return oauth_token
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')
    except:
        _LOGGER.exception("Could not get OAuth token")
        raise GeAuthFailedError(f'Could not get OAuth token')

async def async_refresh_oauth2_token(session: ClientSession, refresh_token: str):
    """ Refreshes an OAuth2 Token based on a refresh token """

    post_data = {
        'redirect_uri': OAUTH2_REDIRECT_URI,
        'client_id': OAUTH2_CLIENT_ID,
        'client_secret': OAUTH2_CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    auth = BasicAuth(OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)
    async with session.post(f'{LOGIN_URL}/oauth2/token', data=post_data, auth=auth) as resp:
        if 400 <= resp.status < 500:
            raise GeAuthFailedError(await resp.text())
        if resp.status >= 500:
            raise GeGeneralServerError(await resp.text())
        oauth_token = await resp.json()
    try:
        access_token = oauth_token['access_token']
        return oauth_token
    except KeyError:
        raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')
