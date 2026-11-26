import asyncio
from typing import Any
from unittest.mock import AsyncMock, patch

from websockets.protocol import State

from gehomesdk.clients.states import GeClientState
from gehomesdk.clients.websocket_client import GeWebsocketClient


class _FakeWebSocket:
    """Minimal async-iterable websocket stub that stays open until cancelled."""

    def __init__(self) -> None:
        self.state = State.OPEN
        self.send = AsyncMock()
        self.close = AsyncMock()
        self._block = asyncio.Event()

    async def __aenter__(self) -> "_FakeWebSocket":
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.state = State.CLOSED

    def __aiter__(self) -> "_FakeWebSocket":
        return self

    async def __anext__(self) -> str:
        await self._block.wait()
        raise StopAsyncIteration


def test_cancelling_connected_run_client_task_ends_immediately() -> None:
    """Cancelling the task running async_run_client must terminate it instead of reconnecting."""

    async def _run() -> None:
        client = GeWebsocketClient("user", "pass")
        client._async_ensure_ssl_context = AsyncMock(return_value=None)  # type: ignore[method-assign]
        client.credentials = {"endpoint": "wss://example.invalid", "userId": "u1"}
        client._has_successful_connect = True

        fake_ws = _FakeWebSocket()
        with patch("gehomesdk.clients.websocket_client.connect", return_value=fake_ws):
            task = asyncio.create_task(client.async_run_client())
            for _ in range(100):
                if client.state == GeClientState.CONNECTED:
                    break
                await asyncio.sleep(0.01)
            assert client.state == GeClientState.CONNECTED

            task.cancel()
            done, _ = await asyncio.wait({task}, timeout=1.0)

            assert task in done
            assert task.cancelled()

    asyncio.run(_run())


def test_internal_cancelled_error_is_absorbed_when_task_not_cancelling() -> None:
    """An internal CancelledError not aimed at the outer task should still be absorbed."""

    async def _run() -> None:
        client = GeWebsocketClient("user", "pass")
        client._async_ensure_ssl_context = AsyncMock(  # type: ignore[method-assign]
            side_effect=asyncio.CancelledError()
        )

        # Should return cleanly without raising CancelledError.
        await client._async_run_client()

    asyncio.run(_run())
