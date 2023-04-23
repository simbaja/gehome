
import asyncio
from typing import AsyncIterator


async def CancellableAsyncIterator(async_iterator: AsyncIterator, cancellation_event: asyncio.Event) -> AsyncIterator:
    cancellation_task = asyncio.create_task(cancellation_event.wait())
    result_iter = async_iterator.__aiter__()
    while not cancellation_event.is_set():
        done, pending = await asyncio.wait(
            [cancellation_task, asyncio.create_task(result_iter.__anext__())],
            return_when=asyncio.FIRST_COMPLETED
        )
        for done_task in done:
            if done_task == cancellation_task:
                for pending_task in pending:
                    await pending_task
                break
            else:
                yield done_task.result()
