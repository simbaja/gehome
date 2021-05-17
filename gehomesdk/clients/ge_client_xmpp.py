import asyncio
from collections import defaultdict
import os
import logging
import socket
import slixmpp
import ssl
from typing import Any, Dict, List, Callable

try:
    import ujson as json
except ImportError:
    import json

_LOGGER = logging.getLogger(__name__)

# If this isn't done, it'll throw a not implemented exception
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

XMPP_EVENT_MESSAGE = 'message'
XMPP_EVENT_SESSION_START = 'session_start'
XMPP_EVENT_PRESENCE_AVAILABLE = 'presence_available'
XMPP_EVENT_PRESENCE_UNAVAILABLE = 'presence_unavailable'

class GeClientXMPP(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)

        self.add_event_handler(XMPP_EVENT_MESSAGE, self.on_message)
        self.add_event_handler(XMPP_EVENT_SESSION_START, self.on_start)
        self.add_event_handler(XMPP_EVENT_PRESENCE_AVAILABLE, self.on_presence_available)
        self.add_event_handler(XMPP_EVENT_PRESENCE_UNAVAILABLE, self.on_presence_unavailable)
        self.ssl_context.verify_mode = ssl.CERT_NONE

        self._event_handlers = defaultdict(list)

    @property
    def event_handlers(self) -> Dict[str, List[Callable]]:
        return self._event_handlers

    async def async_event(self, event: str, *args, **kwargs):
        """Trigger event callbacks sequentially"""
        for cb in self.event_handlers[event]:
            asyncio.ensure_future(cb(*args, **kwargs), loop=self.loop)

    def add_external_event_handler(self, event: str, callback: Callable, disposable: bool = False):
        if disposable:
            raise NotImplementedError('Support for disposable callbacks not yet implemented')
        self.event_handlers[event].append(callback)

    async def on_presence_available(self, evt: slixmpp.ElementBase):
        await self.async_event(XMPP_EVENT_PRESENCE_AVAILABLE, evt)
    
    async def on_presence_unavailable(self, evt: slixmpp.ElementBase):
        await self.async_event(XMPP_EVENT_PRESENCE_UNAVAILABLE, evt)

    async def on_start(self, evt):
        await self.async_event(XMPP_EVENT_SESSION_START, evt)

    async def on_message(self, evt):
        await self.async_event(XMPP_EVENT_MESSAGE, evt)

    async def _connect_routine(self):
        """
        Override the _connect_routine method from xmlstream.py.
        This is to address the bug corrected in open PR https://github.com/poezio/slixmpp/pull/19.
        """
        self.event_when_connected = "connected"

        if self.connect_loop_wait > 0:
            self.event('reconnect_delay', self.connect_loop_wait)
            await asyncio.sleep(self.connect_loop_wait, loop=self.loop)

        record = await self.pick_dns_answer(self.default_domain)
        if record is not None:
            host, address, dns_port = record
            port = self.address[1] if self.address[1] else dns_port
            self.address = (address, port)
            self._service_name = host
        else:
            # No DNS records left, stop iterating
            # and try (host, port) as a last resort
            self.dns_answers = None

        if self.use_ssl:
            ssl_context = self.get_ssl_context()
        else:
            ssl_context = None

        if self._current_connection_attempt is None:
            return
        try:
            await self.loop.create_connection(
                lambda: self, self.address[0], self.address[1], ssl=ssl_context,
                server_hostname=self.default_domain if self.use_ssl else None
            )
            self.connect_loop_wait = 0
        except socket.gaierror:
            self.event('connection_failed', 'No DNS record available for %s' % self.default_domain)
        except OSError as e:
            _LOGGER.debug('Connection failed: %s', e)
            self.event("connection_failed", e)
            if self._current_connection_attempt is None:
                return
            self.connect_loop_wait = self.connect_loop_wait * 2 + 1
            self._current_connection_attempt = asyncio.ensure_future(
                self._connect_routine(), loop=self.loop,
            )
