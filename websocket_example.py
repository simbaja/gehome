#!/usr/bin/env python3

"""
Websocket client example

We're going to run the client in a pre-existing event loop.  We're also going to register some event callbacks
to update appliances every five minutes and to turn on our oven the first time we see it.  Because that is safe!
"""

import aiohttp
import asyncio
import logging
from logging.handlers import RotatingFileHandler
import sys
from datetime import timedelta
from typing import * #Any, Dict, Tuple
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
__version__ = '1.0.0'
KEEPALIVE_TIMEOUT = 30
LIST_APPLIANCES_FREQUENCY = 600

class GeWSClient(GeWebsocketClient):

    __version__ = __version__

    def __init__(self, username: str, password: str, region: str = "US", event_loop: Optional[asyncio.AbstractEventLoop] = None, keepalive: Optional[int] = KEEPALIVE_TIMEOUT, list_frequency: Optional[int] = LIST_APPLIANCES_FREQUENCY):
        super().__init__(username, password, region, event_loop, keepalive, list_frequency)
        self.log = logging.getLogger(__class__.__name__)
        self.log.info('INIT Class')
        self.add_event_handler(EVENT_APPLIANCE_INITIAL_UPDATE, self.detect_appliance_type)
        self.add_event_handler(EVENT_APPLIANCE_STATE_CHANGE, self.log_state_change)
        #self.add_event_handler(EVENT_APPLIANCE_STATE_CHANGE, self.log_state_update)
        #self.add_event_handler(EVENT_ADD_APPLIANCE, self.do_periodic_update)
        
    async def start(self):
        session = aiohttp.ClientSession()
        await self.async_get_credentials(session)
        await self.async_run_client()
        
    async def stop(self):
        await self.disconnect()
        
    async def log_state_change(self, data: Tuple[GeAppliance, Dict[ErdCodeType, Any]]):
        """Log changes in appliance state"""
        appliance, state_changes = data
        updated_keys = ', '.join([str(s) for s in state_changes])
        self.log.info(f'Appliance state change detected in {appliance}. Updated keys: {updated_keys}')
        for k, v in state_changes.items():
            self.log.info('{}: {}'.format(k, v))
        
    async def log_state_update(self, data: Tuple[GeAppliance, Dict[ErdCodeType, Any]]):
        """Log changes in appliance state"""
        appliance, state_changes = data
        updated_keys = ', '.join([str(s) for s in state_changes])
        self.log.info(f'Appliance state update in {appliance}. Updated keys: {updated_keys}')
    
    async def detect_appliance_type(self, appliance: GeAppliance):
        """
        Detect the appliance type.
        This should only be triggered once since the appliance type should never change.

        Also, let's turn on ovens!
        """
        self.log.info(f'Appliance state change detected in {appliance}')
        if appliance.appliance_type == ErdApplianceType.OVEN:
            self.log.info('Turning on the oven!')
            await appliance.async_set_erd_value(
                ErdCode.UPPER_OVEN_COOK_MODE,
                OvenCookSetting(OVEN_COOK_MODE_MAP[ErdOvenCookMode.BAKE_NOOPTION], 350)
            )
            self.log.info('Set the timer!')
            await appliance.async_set_erd_value(ErdCode.UPPER_OVEN_KITCHEN_TIMER, timedelta(minutes=45))
            pass


    async def do_periodic_update(self, appliance: GeAppliance):
        """Request a full state update every minute forever"""
        self.log.info(f'Registering update callback for {appliance:s}')
        while True:
            await asyncio.sleep(60 * 1)
            self.log.info(f'Requesting update for {appliance:s}')
            await appliance.async_request_update()
        
def setup_logger(logger_name, log_file, level=logging.DEBUG, console=False):
    try:
        if logger_name:
            l = logging.getLogger(logger_name)
        else:
            l = logging.getLogger()
        formatter = logging.Formatter('[%(asctime)s][%(levelname)5.5s](%(name)-20s) %(message)s')
        if log_file is not None:
            fileHandler = logging.handlers.RotatingFileHandler(log_file, mode='a', maxBytes=10000000, backupCount=10)
            fileHandler.setFormatter(formatter)
        if console == True:
            #formatter = logging.Formatter('[%(levelname)1.1s %(name)-20s] %(message)s')
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)

        l.setLevel(level)
        if log_file is not None:
            l.addHandler(fileHandler)
        if console == True:
          l.addHandler(streamHandler)
             
    except Exception as e:
        print("Error in Logging setup: %s - do you have permission to write the log file??" % e)
        sys.exit(1)
        
def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Forward MQTT data from GE Appliance MQTT broker')
    parser.add_argument("--version", action="version",
                        version="%(prog)s {0}".format(__version__))
    
    #parser.add_argument("--host", help="TV hostname or IP address")
    #parser.add_argument("--port", type=int, help="TV port number (TCP)")
    #parser.add_argument("--token",type=int, help="security token")
    #parser.add_argument("--name", help="device name")
    parser.add_argument('-t', '--topic',action='store',type=str,default="/samsungtv/command",help=  'MQTT Topic to send commands to, (can use # '
                                                                                                    'and +) default: %(default)s)')
    parser.add_argument('-T', '--pubtopic',action='store',type=str,default="/samsungtv/feedback",help=  'Topic on broker to publish feedback to (default: '
                                                                                                        '%(default)s)')
    parser.add_argument('-b', '--broker',action='store',type=str,default=None,help='ipaddress of MQTT broker (default: %(default)s)')
    parser.add_argument('-p', '--mqtt_port',action='store',type=int,default=1883,help='MQTT broker port number (default: %(default)s)')
    parser.add_argument('-U', '--user',action='store',type=str,default=None,help='MQTT broker user name (default: %(default)s)')
    parser.add_argument('-P', '--password',action='store',type=str,default=None,help='MQTT broker password (default: %(default)s)')
    parser.add_argument("--file", default='./samsungws.conf', help="config file name")
    parser.add_argument("--timeout", type=float, default=None,
                        help="socket timeout in seconds (1 is minnimum timeout, default: 20s")
    parser.add_argument("-L", "--log", default='./GEAppliance.log', help="log file name")
    parser.add_argument("-K", "--keys", action="store_true",default = False,
                        help="List possible Remote Keys")
    parser.add_argument("-D", "--debug", action="store_true",default = False,
                        help="Debug Mode")
    parser.add_argument("-W", "--wsdebug", action="store_true",default = False,
                        help="Websocket Debug Mode")
                        
    return parser.parse_args()
    
async def main():
    global log, client
    arg = parse_args()
    if arg.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    #logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname)-8s %(message)s')
    
    #setup logging
    setup_logger(None, arg.log, level=log_level,console=True)
    log = logging.getLogger(__name__)

    client = GeWSClient(USERNAME, PASSWORD, REGION)
    await client.start()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.info("System exit Received - Exiting program")
        #asyncio.run(client.disconnect())
    log.info('Program Exited')
