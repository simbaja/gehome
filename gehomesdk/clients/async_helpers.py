from typing import AsyncIterable, AsyncIterator, TypeVar
import asyncio
import contextlib

T = TypeVar("T")


async def CancellableAsyncIterator(source: AsyncIterable[T], cancel_event: asyncio.Event) -> AsyncIterator[T]:
    """
    Yield items from `source` until `cancel_event` is set.
    """
    aiter = source.__aiter__()
    # create one cancel waiter and reuse it inside the loop
    cancel_task = asyncio.ensure_future(cancel_event.wait())
    try:
        while True:
            # fast-path: if cancellation already requested, stop
            if cancel_task.done():
                break

            # __anext__ returns an Awaitable; ensure_future accepts Awaitable
            next_fut = asyncio.ensure_future(aiter.__anext__())

            try:
                done, _ = await asyncio.wait(
                    {next_fut, cancel_task}, return_when=asyncio.FIRST_COMPLETED
                )

                # cancellation won
                if cancel_task in done:
                    # cancel the pending next future (if any) and await it to avoid warnings
                    if not next_fut.done():
                        next_fut.cancel()
                        with contextlib.suppress(asyncio.CancelledError):
                            await next_fut
                    break

                # next completed first: propagate result
                try:
                    item = next_fut.result()
                except StopAsyncIteration:
                    break
                yield item

            finally:
                # defensive: ensure next_fut is not left pending
                if not next_fut.done():
                    next_fut.cancel()
                    with contextlib.suppress(asyncio.CancelledError):
                        await next_fut

    finally:
        # ensure underlying iterator is closed if it supports aclose()
        if hasattr(aiter, "aclose"):
            with contextlib.suppress(Exception):
                await aiter.aclose() # type: ignore
        # make sure the shared cancel_task is cleaned up if still pending
        if not cancel_task.done():
            cancel_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await cancel_task