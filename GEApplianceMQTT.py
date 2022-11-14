#!/usr/bin/env python3

"""
Websocket client for GE appliances

This is intended for a dishwasher (Cafe model CDT875P2N7S1), but can be used for any appliance
N Waterton 13/11/2022 V 1.0.0 : Initial Release
"""

import aiohttp
import asyncio
import logging
from logging.handlers import RotatingFileHandler
import sys
from datetime import timedelta
from typing import * #Any, Dict, Tuple
from mqtt import MQTTMixin

from gehomesdk import (
    EVENT_ADD_APPLIANCE,
    EVENT_APPLIANCE_STATE_CHANGE,
    EVENT_APPLIANCE_INITIAL_UPDATE,
    EVENT_GOT_APPLIANCE_LIST,
    ErdApplianceType,
    ErdCode,
    ErdCodeType,
    ErdUserSetting,
    UserCycleSetting,
    UserWashTempSetting,
    UserDryOptionSetting,
    GeAppliance,
    GeWebsocketClient
)

from gehomesdk.clients.const import API_URL

__version__ = '1.0.0'
KEEPALIVE_TIMEOUT = 30
LIST_APPLIANCES_FREQUENCY = 600
API_HOST = API_URL[8:]  # Drop the https://

class GeWSClient(MQTTMixin, GeWebsocketClient):

    __version__ = __version__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = logging.getLogger(__class__.__name__)
        self.log.info(f'{__class__.__name__} library v{__class__.__version__}')
        self.invalid_commands.extend([  'publish', 
                                        'async_do_full_login_flow',
                                        'async_do_refresh_login_flow',
                                        'async_event',
                                        'async_get_credentials',
                                        'async_get_credentials_and_run',
                                        'async_request_features',
                                        'async_request_message',
                                        'async_request_update',
                                        'async_run_client',
                                        'async_send_command',
                                        'async_set_erd_value',
                                        'clear_event_handlers',
                                        'disconnect',
                                        'remove_event_handler',
                                        'add_event_handler'
                                     ])
        #self.add_event_handler(EVENT_APPLIANCE_INITIAL_UPDATE, self._detect_appliance_type)
        self.add_event_handler(EVENT_APPLIANCE_STATE_CHANGE, self._publish_state_change)
        #self.add_event_handler(EVENT_ADD_APPLIANCE, self._do_periodic_update)
        self.add_event_handler(EVENT_GOT_APPLIANCE_LIST, self._publish_status)
        
    async def start(self):
        session = aiohttp.ClientSession()
        await self.async_get_credentials(session)
        await self.async_run_client()
        
    async def stop(self):
        await self._stop()
        await self.disconnect()
        
    def _get_command(self, msg):
        '''
        override MQTTMixin
        get device and insert into args
        '''
        device = msg.topic.split('/')[-2]
        if device in self.appliances.keys():
            command, args = super()._get_command(msg)
            if args is None:
                args = []
            args.insert(0, self.appliances[device])   
            return command, args
        self.log.warning('device: {} not found '.format(device))
        return None, []
        
    def _str2int(self, value):
        return 1 if str(value).lower() in ['true', '1', 't', 'y', 'on', 'open'] else 0
        
    async def refresh(self, appliance, on):
        appliance._property_cache = {}  #clear cache
        await appliance.async_request_update()

    async def _set_user_control_bit(self, appliance, erd, bit, value=1, mask=1):
        '''
        set bits starting at bit to value in erd raw_value and send to appliance
        '''
        value = int(value)
        new_val = int(appliance.get_erd_value(erd).raw_value, 16)
        new_val &= ~(mask << bit)    #clear bits
        if value:
            new_val |= value << bit #set bits
        await appliance.async_set_erd_value(erd, new_val)
        
    async def set_default(self, appliance, on):
        '''
        default 00B900 (Auto, Boost+Sanitize, steam, max dry, both zones, no delay, no bottle jets)
        '''
        self.log.info('Setting {} to {}'.format(ErdCode.DISHWASHER_USER_SETTING, '00B900'))
        await self.async_set_erd_value(appliance, ErdCode.DISHWASHER_USER_SETTING, '00B900')
        
    async def set_lock_controls(self, appliance, on):
        '''
        bit 9
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 9, self._str2int(on))
        
    async def set_sabbath(self, appliance, on):
        '''
        bit 6
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 6, self._str2int(on))
        
    async def set_sound(self, appliance, on):
        '''
        bit 23
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 23, self._str2int(on))
        
    async def set_bottle_jet(self, appliance, on):
        '''
        bit 0
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 0, self._str2int(on))
        
    async def set_presoak(self, appliance, on):
        '''
        called steam on this dishwasher
        '''
        await self.set_steam(appliance, on)
        
    async def set_steam(self, appliance, on):
        '''
        bit 8 (called presoak actually steam)
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 8, self._str2int(on))
        
    async def set_cycle_mode(self, appliance, mode):
        '''
        bit 1
        AUTO = 0
        INTENSE = 1     #Pots
        NORMAL = 2
        DELICATE = 3    #China
        THIRTY_MIN = 4  #Express
        ECO = 5
        RINSE = 6
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 1, mode, 0x7)
        
    async def set_delay_hours(self, appliance, hours):
        '''
        bit 16
        hours 0 to 12
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 16, hours, 0xF)
            
    async def set_dry_option(self, appliance, option):
        '''
        bit 10
        OFF = 0
        POWER_DRY = 1
        MAX_DRY = 2
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 10, option, 0x3)
            
    async def set_wash_temp(self, appliance, option):
        '''
        bit 12
        NORMAL = 0
        BOOST = 1
        SANITIZE = 2
        BOOST_AND_SANITIZE = 3
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 12, option, 0x3)
            
    async def set_wash_zone(self, appliance, option):
        '''
        bit 20
        BOTH = 0
        LOWER = 1
        UPPER = 2
        '''
        await self._set_user_control_bit(appliance, ErdCode.DISHWASHER_USER_SETTING, 20, option, 0x3)
            
    async def set_pods_remaining(self, appliance, value=1):
        '''
        set pods remaining
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_PODS_REMAINING_VALUE, value)
            
    async def set_delay_minutes(self, appliance, value):
        '''
        Set delay start in minutes (max 12 hours)
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_DELAY_START_MINUTES, value)
        
    async def set_dishwasher_cycle(self, appliance, value):
        '''
        AUTO = 0
        INTENSE = 1     #Pots
        NORMAL = 2
        DELICATE = 3    #China
        THIRTY_MIN = 4  #Express
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_CYCLE, UserCycleSetting(value))
        
    async def set_dishwasher_temperature(self, appliance, value):
        '''
        Set Dishwasher Water Temperature
        NORMAL = 0
        BOOST = 1
        SANITIZE = 2
        BOOST_AND_SANITIZE = 3
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_TEMPERATURE, UserWashTempSetting(value))
        
    async def set_dishwasher_drying(self, appliance, value):
        '''
        Set Dishwasher drying
        OFF = 0
        POWER_DRY = 1
        MAX_DRY = 2
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_DRYING, UserDryOptionSetting(value))
        
    async def set_dishwasher_wash_zone(self, appliance, value):
        '''
        Set Dishwasher wash zone
        BOTH = 0
        LOWER = 1
        UPPER = 2
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_WASH_ZONE, UserWashZoneSetting(value))
        
    async def set_dishwasher_steam(self, appliance, value):
        '''
        Set Dishwasher steam
        0 = off
        1 = on
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_STEAM, bool(self._str2int(value)))
        
    async def set_dishwasher_bottle_jets(self, appliance, value):
        '''
        Set Dishwasher bottle jets
        0 = off
        1 = on
        '''
        await appliance.async_set_erd_value(ErdCode.DISHWASHER_BOTTLE_JETS, bool(self._str2int(value)))
        
    async def set_dishwasher_sabbath(self, appliance, value):
        '''
        Set Dishwasher bottle jets
        0 = off
        1 = on
        '''
        await appliance.async_set_erd_value(ErdCode.SABBATH_MODE, bool(self._str2int(value)))
        
    async def send_dishwasher_command(self, appliance, cmd):
        '''
        diswasher commands
        dishwasher-start
        dishwasher-stop
        '''
        if not cmd.startswith('dishwasher'):
            cmd = 'dishwasher-start' if self._str2int(cmd) == 1 else 'dishwasher-stop'
        await self.async_send_command(appliance, cmd)
  
    def _isinstance_namedtuple(self, obj) -> bool:
        return (
                isinstance(obj, tuple) and
                hasattr(obj, '_asdict') and
                hasattr(obj, '_fields')
        )
        
    def publish(self, appliance=None, topic=None, msg=None):
        '''
        adds appliance.mac_addr (if given), and removes leading qualifiers (before .)
        stringifies msg (if possible), and publishes msg enum values
        convertes bytes to hex representation
        handles instances of namedtuple
        '''
        if topic is None or msg is None:
            self.log.debug(f'Not pubishing: {topic}: {msg}')
            return
        if self._isinstance_namedtuple(msg):
            for name, setting in msg._asdict().items():
                self.publish(appliance, '{}/{}'.format(topic, name), setting)
            return
            
        msg_val = None
        if isinstance(msg, (bytes, bytearray)):
            msg_str = msg.hex()
        elif isinstance(msg, (bool, int, float)):
            msg_str = str(msg)
        elif isinstance(msg, str):
           msg_str = msg.strip().split(' ')[-1] #only needed for DISHWASHER_CYCLE_NAME
        else:
            msg_str = appliance.stringify_erd_value(msg)
            if msg_str is None:
                msg_str = msg
            if hasattr(msg, "value"):
                msg_val = msg.value
                   
        topic = str(topic).split('.')[-1]
        topic = '{}/{}'.format(appliance.mac_addr, topic) if appliance else topic
        self._publish(topic, msg_str)
        if msg_val is not None:
            self._publish(topic+'_VAL', msg_val)
        
    async def _publish_state_change(self, data: Tuple[GeAppliance, Dict[ErdCodeType, Any]]):
        """Publish changes in appliance state"""
        appliance, state_changes = data
        updated_keys = ', '.join([str(s) for s in state_changes])
        self.log.debug(f'Appliance state change detected in {appliance}. Updated keys: {updated_keys}')
        self._publish_online_status(appliance)
        for k, v in state_changes.items():
            self.publish(appliance, k, v)
    
    async def _detect_appliance_type(self, appliance: GeAppliance):
        """
        Detect the appliance type.
        This should only be triggered once since the appliance type should never change.
        """
        self.log.info(f'Appliance state change detected in {appliance}')
        
    async def _publish_status(self, items):
        for item in items:
            appliance = self.appliances[item["applianceId"]]
            self._publish_online_status(appliance)
            
    def _publish_online_status(self, appliance: GeAppliance):
        self.publish(appliance, 'online', appliance.available)

    async def _do_periodic_update(self, appliance: GeAppliance):
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
        print("Error in Logging setup: {} - do you have permission to write the log file??".format(e))
        sys.exit(1)
        
def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Forward MQTT data from GE Appliance to MQTT broker')
    parser.add_argument("--version", action="version",
                        version="%(prog)s {0}".format(__version__))
    parser.add_argument('login',action='store',type=str,default=None, help='smartHQ login (default: %(default)s)')
    parser.add_argument('password',action='store', type=str, default=None, help='smartHQ password (default: %(default)s)')
    parser.add_argument('-r', '--region',action='store',type=str,choices=['US', 'EU'],default='US', help='Region (default: %(default)s)')
    parser.add_argument('-n', '--name',action='store',type=str, default=None, help="device name (default: %(default)s)")
    parser.add_argument('-t', '--topic',action='store',type=str,default="/GEAppliance/command",help=  'MQTT Topic to send commands to, (can use # '
                                                                                                    'and +) default: %(default)s)')
    parser.add_argument('-T', '--pubtopic',action='store',type=str,default="/GEAppliance/feedback",help=  'Topic on broker to publish feedback to (default: '
                                                                                                        '%(default)s)')
    parser.add_argument('-b', '--broker',action='store',type=str,default=None,help='ipaddress of MQTT broker (default: %(default)s)')
    parser.add_argument('-p', '--mqtt_port',action='store',type=int,default=1883,help='MQTT broker port number (default: %(default)s)')
    parser.add_argument('-U', '--user',action='store',type=str,default=None,help='MQTT broker user name (default: %(default)s)')
    parser.add_argument('-P', '--mqttpassword',action='store',type=str,default=None,help='MQTT broker password (default: %(default)s)')
    parser.add_argument('-J', '--json-out', action='store_true',default = False, help='Json output (default: %(default)s)')
    parser.add_argument('-poll', '--poll_interval',action='store',type=int,default=0,help='Polling interval (seconds) (0=off) (default: %(default)s)')
    parser.add_argument('-pm', '--poll_methods',nargs='*',action='store',type=str,default='get_status',help='Polling method (default: %(default)s)')
    parser.add_argument('-L', '--log', default='./GEAppliance.log', help='log file name (default: %(default)s)')
    parser.add_argument('-D', '--debug', action='store_true',default = False, help='Debug Mode (default: %(default)s)')
                        
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

    client = GeWSClient(arg.login,
                        arg.password,
                        region=arg.region,
                        event_loop=None,
                        keepalive=KEEPALIVE_TIMEOUT,
                        list_frequency=LIST_APPLIANCES_FREQUENCY,
                        ip=arg.broker,
                        port=arg.mqtt_port,
                        user=arg.user,
                        mqtt_password=arg.mqttpassword,
                        pubtopic=arg.pubtopic,
                        topic=arg.topic,
                        name=arg.name,
                        poll=(arg.poll_interval, arg.poll_methods),
                        json_out=arg.json_out,
                        log=None
                        )

    await client.start()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.info("System exit Received - Exiting program")
        #asyncio.run(client.stop())
    log.info('Program Exited')
