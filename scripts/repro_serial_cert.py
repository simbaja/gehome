"""
Repro script for https://github.com/simbaja/ha_gehome/issues/490

Connects to SmartHQ, waits for the initial ERD cache update on each appliance,
then dumps the raw hex and decoded value for ERD 0x0002 (SERIAL_NUMBER) so we
can confirm whether the cloud is sending PEM certificate data in that field.

Usage:
    GE_USERNAME=you@example.com GE_PASSWORD=secret python repro_serial_cert.py
"""

import asyncio
import os
import sys
import platform
import signal
import aiohttp

from gehomesdk import (
    EVENT_ADD_APPLIANCE,
    EVENT_APPLIANCE_INITIAL_UPDATE,
    ErdCode,
    GeAppliance,
    GeWebsocketClient,
)

USERNAME = os.environ.get("GE_USERNAME")
PASSWORD = os.environ.get("GE_PASSWORD")
REGION   = os.environ.get("GE_REGION", "US")

DONE = asyncio.Event()


def _dump_all(appliance: GeAppliance):
    print(f"\n=== Appliance {appliance.mac_addr} — full ERD cache ===")
    cache = appliance._raw_property_cache
    if not cache:
        print("  (empty)")
        return
    for code, raw_hex in sorted(cache.items(), key=lambda x: str(x[0])):
        try:
            decoded = appliance.get_erd_value(code)
        except Exception as e:
            decoded = f"<error: {e}>"
        # Summarise long values
        raw_display = raw_hex if len(raw_hex) <= 40 else raw_hex[:40] + "..."
        print(f"  {str(code):<45} raw={raw_display!r:>45}  decoded={decoded!r}")
    print()


async def on_initial_update(appliance: GeAppliance):
    _dump_all(appliance)


async def on_add_appliance(appliance: GeAppliance):
    # Also dump whatever is already cached at add time (may be empty)
    print(f"\n[add_appliance] {appliance.mac_addr}")


async def main():
    if not USERNAME or not PASSWORD:
        sys.exit("Set GE_USERNAME and GE_PASSWORD environment variables.")

    client = GeWebsocketClient(USERNAME, PASSWORD, REGION)
    client.add_event_handler(EVENT_ADD_APPLIANCE, on_add_appliance)
    client.add_event_handler(EVENT_APPLIANCE_INITIAL_UPDATE, on_initial_update)

    loop = asyncio.get_running_loop()

    async with aiohttp.ClientSession() as session:
        client_task = asyncio.create_task(
            client.async_get_credentials_and_run(session)
        )

        if platform.system() != "Windows":
            for sig in (signal.SIGINT, signal.SIGTERM):
                loop.add_signal_handler(sig, client_task.cancel)

        # Wait up to 60 s for appliances to report in, then exit
        try:
            await asyncio.wait_for(client_task, timeout=60)
        except (asyncio.TimeoutError, asyncio.CancelledError):
            pass
        finally:
            client_task.cancel()
            try:
                await client_task
            except asyncio.CancelledError:
                pass

    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())
