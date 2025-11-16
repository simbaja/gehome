"""
Websocket client example

We're going to run the client in a pre-existing event loop.  We're also going to register some event callbacks
to update appliances every five minutes and to turn on our oven the first time we see it.  Because that is safe!
"""

import platform
import aiohttp
import asyncio
import logging
import signal
from datetime import timedelta
from typing import Any, Dict, Tuple, Optional
from credentials import USERNAME, PASSWORD, REGION

from gehomesdk import (
    EVENT_ADD_APPLIANCE,
    EVENT_APPLIANCE_STATE_CHANGE,
    EVENT_APPLIANCE_INITIAL_UPDATE,
    ErdApplianceType,
    ErdCode,
    ErdCodeType,
    ErdOvenCookMode,
    GeAppliance,
    GeWebsocketClient,
    OvenCookSetting,
    OVEN_COOK_MODE_MAP
)

_LOGGER = logging.getLogger(__name__)

async def log_state_change(data: Tuple[GeAppliance, Dict[ErdCodeType, Any]]):
    """Log changes in appliance state"""
    appliance, state_changes = data
    updated_keys = ', '.join([str(s) for s in state_changes])
    _LOGGER.debug(f'Appliance state change detected in {appliance}. Updated keys: {updated_keys}')
    
async def detect_appliance_type(appliance: GeAppliance):
    """
    Detect the appliance type.
    This should only be triggered once since the appliance type should never change.

    Also, let's set a timer!
    """
    _LOGGER.debug(f'Appliance state change detected in {appliance}')
    if appliance.appliance_type == ErdApplianceType.OVEN:
        # _LOGGER.info('Turning on the oven!')
        # await appliance.async_set_erd_value(
        #     ErdCode.UPPER_OVEN_COOK_MODE,
        #     OvenCookSetting(OVEN_COOK_MODE_MAP[ErdOvenCookMode.BAKE_NOOPTION], 350)
        # )
        _LOGGER.info('Set the oven timer!')
        await appliance.async_set_erd_value(ErdCode.UPPER_OVEN_KITCHEN_TIMER, timedelta(minutes=45))
        pass

async def do_periodic_update(appliance: GeAppliance):
    """Request a full state update every minute forever"""
    _LOGGER.debug(f'Registering update callback for {appliance:s}')
    while True:
        await asyncio.sleep(60 * 1)
        _LOGGER.debug(f'Requesting update for {appliance:s}')
        await appliance.async_request_update()

async def shutdown(sig, client: Optional[GeWebsocketClient], client_task: Optional[asyncio.Task[None]]):
    #just exit if we don't have a client or task
    if client is None or client_task is None:
        return

    _LOGGER.info(f"Signal caught: {sig}, shutting down...")

    # create the group to await
    group = asyncio.gather(client_task)
    
    try:
        #disconnect and wait a bit for it to shutdown gracefully
        await client.disconnect()
        _ , _ = await asyncio.wait([client_task], return_when=asyncio.FIRST_COMPLETED, timeout=10)
    except TimeoutError:
        _LOGGER.warning("Client did not shut down gracefully, forcing shutdown.")
        client_task.cancel()

    await group

    _LOGGER.info(f"Shutdown complete.")

async def main():
    loop = asyncio.get_running_loop()
    client: GeWebsocketClient | None = None
    client_task: asyncio.Task[None] | None = None

    try:
        client = GeWebsocketClient(USERNAME, PASSWORD, REGION)
        client.add_event_handler(EVENT_APPLIANCE_INITIAL_UPDATE, detect_appliance_type)
        client.add_event_handler(EVENT_APPLIANCE_STATE_CHANGE, log_state_change)
        client.add_event_handler(EVENT_ADD_APPLIANCE, do_periodic_update)

        async with aiohttp.ClientSession() as session:
            # start up our client
            client_task = asyncio.create_task(client.async_get_credentials_and_run(session))

            # setup signal handlers to catch termination signals (only linux) 
            if platform.system() != "Windows":
                for s in [signal.SIGINT, signal.SIGTERM]:
                    loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(s, client, client_task)))

            # wait for a while...
            await asyncio.sleep(7200)
    except asyncio.exceptions.CancelledError:
        pass
    finally:
        #shutdown gracefully if possible
        await shutdown(signal.SIGTERM, client, client_task)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname)-8s %(message)s')
    asyncio.run(main())
