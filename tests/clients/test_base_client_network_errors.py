import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest

from gehomesdk.clients.base_client import GeBaseClient
from gehomesdk.exception import GeAuthFailedError


class _DummyClient(GeBaseClient):
    async def _async_run_client(self) -> None:
        return None

    async def async_set_erd_value(self, appliance, erd_code, erd_value) -> None:
        return None

    async def async_request_update(self, appliance) -> None:
        return None

    async def _async_do_full_login_flow(self):
        return {"userId": "u1"}

    async def _async_do_refresh_login_flow(self):
        return {"userId": "u1"}

    async def _disconnect(self) -> None:
        return None


def test_refresh_oauth2_token_propagates_network_error_without_full_login() -> None:
    async def _run() -> None:
        client = _DummyClient("user", "pass", refresh_token="valid-refresh")
        client._session = MagicMock()
        full_login = AsyncMock()
        client._async_get_oauth2_token = full_login  # type: ignore[method-assign]

        with patch(
            "gehomesdk.clients.base_client.async_refresh_oauth2_token",
            new=AsyncMock(side_effect=aiohttp.ClientConnectionError("DNS timeout")),
        ):
            with pytest.raises(aiohttp.ClientConnectionError):
                await client._async_refresh_oauth2_token()

        full_login.assert_not_called()
        assert client.refresh_token == "valid-refresh"

    asyncio.run(_run())


def test_refresh_oauth2_token_falls_back_on_auth_failure() -> None:
    async def _run() -> None:
        client = _DummyClient("user", "pass", refresh_token="expired-refresh")
        client._session = MagicMock()
        client._async_get_oauth2_token = AsyncMock(  # type: ignore[method-assign]
            return_value={
                "access_token": "new-access",
                "refresh_token": "new-refresh",
                "expires_in": 3600,
            }
        )

        with patch(
            "gehomesdk.clients.base_client.async_refresh_oauth2_token",
            new=AsyncMock(side_effect=GeAuthFailedError("Refresh failed (400)")),
        ):
            await client._async_refresh_oauth2_token()

        client._async_get_oauth2_token.assert_awaited_once()
        assert client.refresh_token == "new-refresh"

    asyncio.run(_run())


def test_get_credentials_propagates_timeout_without_full_login() -> None:
    async def _run() -> None:
        client = _DummyClient("user", "pass", refresh_token="valid-refresh")
        client.async_do_refresh_login_flow = AsyncMock(side_effect=asyncio.TimeoutError())  # type: ignore[method-assign]
        client.async_do_full_login_flow = AsyncMock()  # type: ignore[method-assign]

        with pytest.raises(asyncio.TimeoutError):
            await client.async_get_credentials(MagicMock())

        client.async_do_full_login_flow.assert_not_called()

    asyncio.run(_run())


def test_run_client_retries_transient_refresh_error() -> None:
    async def _run() -> None:
        client = _DummyClient("user", "pass", refresh_token="valid-refresh")
        run_calls = 0

        async def _fake_run() -> None:
            nonlocal run_calls
            run_calls += 1
            if run_calls == 1:
                raise ConnectionError("dropped")
            await client.disconnect()

        client._async_run_client = _fake_run  # type: ignore[method-assign]
        client._has_successful_connect = True
        client.async_do_refresh_login_flow = AsyncMock(  # type: ignore[method-assign]
            side_effect=[aiohttp.ClientConnectionError("DNS timeout"), {"userId": "u1"}]
        )

        with patch("gehomesdk.clients.base_client.asyncio.sleep", new=AsyncMock()):
            await client.async_run_client()

        assert run_calls == 2
        assert client.async_do_refresh_login_flow.await_count == 2

    asyncio.run(_run())
