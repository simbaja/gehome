'''
MQTT Mixin Client library
8/4/2022 V 1.0.0 N Waterton - Initial Release
26/5/2022 V 1.0.1 N Waterton - Bug fixes
9/11/2022 V 2.0.0 N Waterton - refactored as a Mixin class
'''
import re
from ast import literal_eval
import logging
import asyncio

import paho.mqtt.client as mqtt

__version__ = "2.0.0"

class MQTTMixin():
    '''
    Async MQTT Mixin client intended to be used as a mixin
    all methods not starting with '_' can be sent as commands to MQTT topic
    feedback is published to pubtopic plus name (if given)
    '''
    __version__ = __version__
    invalid_commands = ['start', 'stop', 'subscribe', 'unsubscribe', '']
    
    def __init__(self, *args, **kwargs):
        self._log = kwargs.pop("log", None)
        if self._log is None:
            self._log = logging.getLogger('Main.'+__class__.__name__)
        self._debug = self._log.getEffectiveLevel() <= logging.DEBUG
        self._log.info(f'{__class__.__name__} library v{__class__.__version__}')
        self._broker = kwargs.pop("ip", None)
        self._port = kwargs.pop("port", 1883)
        self._user = kwargs.pop("user", None)
        self._password = kwargs.pop("mqtt_password", None)
        self._pubtopic = kwargs.pop("pubtopic", 'default')
        topic = kwargs.pop("topic", '/default/#')
        self._topic = topic if not topic.endswith('/#') else topic[:-2]
        self._name = kwargs.pop("name", None)
        self._json_out = kwargs.pop("json_out", False)
        self._polling_config = kwargs.pop("poll", None)
        self._polling = []
        self._poll = None
        self._mqttc = None
        self._method_dict = {}  #filled in later
        self._delimiter = '\='
        self._topic_override = None
        self._exit = False
        self._history = {}
        self._tasks = {}
        super().__init__(*args, **kwargs)

        self._loop = asyncio.get_event_loop()
        
        self._q = asyncio.Queue()
        if self._broker is not None:
            self._connect_client()
            self._loop.create_task(self._built_method_dict())
            self._tasks['_process_q'] = self._loop.create_task(self._process_q())
        
    async def _built_method_dict(self):
        '''
        builds the callable methods dict
        need a retry delay, to allow the super class to initialize first
        '''
        await asyncio.sleep(5)  #wait for super class to initialize
        #updated from
        #self._method_dict = {func:getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and not func.startswith("_")}
        retry = 5
        for x in range(retry):
            error = False
            for func in dir(self):
                if not func.startswith('_') and func not in self._method_dict.keys() and func not in self.invalid_commands:
                    try:
                        _func = getattr(self, func)
                        if callable(_func):
                            self._method_dict[func] = _func
                            self._log.debug('Added callable function: {}'.format(func))
                    except Exception as e:
                        self._log.debug('Initialization error: {}, retry: {}'.format(func, x))
                        if x < retry-1:
                            error = True
                            await asyncio.sleep(5)
                            break
                        self._log.debug('No More retries, continuing')
            if not error:
                break
                
        self.log.debug('Callable functions initialized')             
        self._setup_polling()            

    def _setup_polling(self):            
        if self._polling_config:
            self.log.debug('Setting up Polling')
            self._polling = [p for p in self._polling_config[1:] if p in self._method_dict.keys()]
            if self._polling:
                self._poll = self._polling_config[0] if self._polling_config[0] > 0 else None
        if self._poll:
            self._tasks['_poll_status'] = self._loop.create_task(self._poll_status())
        else:
            self._log.debug('Polling is disabled')
        
    def _connect_client(self):
        if not self._broker: return
        if self._MQTT_connected: return
        try:
            # connect to broker
            self._log.info('Connecting to MQTT broker: {}'.format(self._broker))
            self._mqttc = mqtt.Client()
            # Assign event callbacks
            self._mqttc.on_message = self._on_message
            self._mqttc.on_connect = self._on_connect
            self._mqttc.on_disconnect = self._on_disconnect
            if self._user and self._password:
                self._mqttc.username_pw_set(self._user, self._password)
            self._mqttc.will_set(self._get_pubtopic('status'), payload="Offline", qos=0, retain=False)
            self._mqttc.connect(self._broker, self._port, 60)
            self._mqttc.loop_start()
        except socket.error:
            self._log.error("Unable to connect to MQTT Broker")
            self._mqttc = None
        return self._mqttc
        
    def subscribe(self, topic, qos=0):
        '''
        utiltity to subscribe to an MQTT topic
        '''
        if self._MQTT_connected:
            topic = topic.replace('//','/')
            self._log.info('subscribing to: {}'.format(topic))
            self._mqttc.subscribe(topic, qos)
            
    def unsubscribe(self, topic):
        '''
        utiltity to unsubscribe from an MQTT topic
        '''
        if self._MQTT_connected:
            topic = topic.replace('//','/')
            self._log.info('unsubscribing from: {}'.format(topic))
            self._mqttc.unsubscribe(topic)
        
    @property
    def _MQTT_connected(self):
        return bool(self._mqttc.is_connected() if self._mqttc else False)
        
    async def _waitForMQTT(self, timeout=0):
        '''
        Utility to wait for MQTT connection, with optional timeout
        returns false if not broker defined
        '''
        if not self._broker: return False
        timeout = timeout if timeout else 1000000
        count = 0
        while not self._MQTT_connected and count < timeout:
            await asyncio.sleep(1)
            count += 1
        return self._MQTT_connected
        
    def _on_connect(self, client, userdata, flags, rc):
        self._log.info('MQTT broker connected')
        self.subscribe('{}/all/#'.format(self._topic))
        if self._name:
            self.subscribe('{}/{}/#'.format(self._topic, self._name))
        else:
            self.subscribe('{}/#'.format(self._topic))
        self._history = {}
        self._publish('status', 'Online')
        
    def _on_disconnect(self, mosq, obj, rc):
        self._log.warning('MQTT broker disconnected')
        if rc != 0:
            self._log.info('Reconnecting...')
            self._connect_client()
        
    def _on_message(self, mosq, obj, msg):
        #self._log.info(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        asyncio.run_coroutine_threadsafe(self._q.put(msg), self._loop)    #mqtt client is running in a different thread
        
    def _get_pubtopic(self, topic=None):
        pubtopic = self._pubtopic
        if self._name:
            pubtopic = '{}/{}'.format(pubtopic,self._name)
        if topic:
            pubtopic = '{}/{}'.format(pubtopic, topic)
        return pubtopic
            
    def _publish(self, topic=None, message=None):
        if topic is None and message is None:
            self._log.debug(f'Not pubishing: {topic}: {message}')
            return
        try:
            if self._MQTT_connected:
                pubtopic = self._get_pubtopic(topic)
                self._log.info("publishing item: {}: {}".format(pubtopic, message))
                self._mqttc.publish(pubtopic, str(message))
            else:
                self._log.warning(f'MQTT not connected - not publishing {topic}: {message}')
        except Exception as e:
            self._log.exception(e)
            
    async def _poll_status(self):
        '''
        publishes commands in self._polling every self._poll seconds
        '''
        try:
            while not self._exit:
                await asyncio.sleep(self._poll)
                self._log.info('Polling...')
                for cmd in self._polling:
                    if cmd in self._method_dict.keys():
                        result = await self._method_dict[cmd]()
                        if self._json_out:
                            self._publish(cmd, result)
                        else:
                            self._decode_topics(result)
                    else:
                        self._log.warning('Polling command: {cmd} not found')
        except asyncio.CancelledError:
            pass
        self._log.info('Poll loop exited')
               
    def _decode_topics(self, state, prefix=None, override=False):
        '''
        decode json data dict, and _publish as individual topics to
        brokerFeedback/topic the keys are concatenated with _ to make one unique
        topic name strings are expressly converted to strings to avoid unicode
        representations
        '''
        for k, v in state.items():
            if isinstance(v, dict):
                if prefix is None:
                    self._decode_topics(v, k, override=override)
                else:
                    self._decode_topics(v, '{}_{}'.format(prefix, k), override=override)
            else:
                if isinstance(v, list):
                    newlist = []
                    for i in v:
                        if isinstance(i, dict):
                            for ki, vi in i.items():
                                newlist.append((str(ki), vi))
                        else:
                            newlist.append(str(i))
                    v = newlist
                if prefix is not None:
                    k = '{}_{}'.format(prefix, k)
                 
                if override or self._has_changed(k, v):
                    self._publish(k, str(v))
                
    def _has_changed(self, k, v):
        '''
        checks to see if value has changed, returns True/False
        '''
        v = str(v)
        previous = self._history.get(k)
        if previous != v:
            self._history[k] = v
            return True
        return False
        
    async def _process_q(self):
        '''
        Main MQTT command processing loop, run until program exit
        '''
        self._exit = False
        while not self._exit:
            try:
                if self._q.qsize() > 0 and self._debug:
                    self._log.warning('Pending event queue size is: {}'.format(self._q.qsize()))
                msg = await self._q.get()
                
                command, args = self._get_command(msg)
                await self._publish_command(command, args)
                    
                self._q.task_done()
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self._log.exception(e)
                
    def _get_command(self, msg):
        '''
        extract command and args from MQTT msg
        '''
        command = args = None
        topic_command = msg.topic.split('/')[-1]
        msg_command = msg.payload.decode('UTF-8')
            
        if topic_command in self._method_dict.keys():
            command = topic_command
            #parse arg
            args = re.split(self._delimiter, msg_command)
            try:
                args = [literal_eval(v) if re.match('\[|\{|\(|True|False|\d',v) else v for v in args]
            except Exception as e:
                if self._debug:
                    self._log.warning('error parsing args: {}'.format(e))
                
            args = self._filter_list(args)
             
        elif msg_command in self._method_dict.keys():
            command = msg_command
            
        else:
            #undefined
            cmd = topic_command if topic_command not in [self._name, 'all'] else msg_command
            if cmd not in self.invalid_commands:
                self._log.warning('Received invalid command: {}'.format(cmd))
            
        return command, args
             
    async def _publish_command(self, command, args=None):
        try:
            value = await self._execute_command(command, args)
        except Exception as e:
            self._log.error(e)
            value = None
            
        if self._topic_override: #override the topic to publish to
            command = self._topic_override
            self._topic_override = None
            
        if self._json_out or not isinstance(value, dict):
            self._publish(command, value)
        else:
            self._decode_topics(value, override=True)
        
    async def _execute_command(self, command, args):
        '''
        execute the command (if any) with args (if any)
        return value received (if any)
        '''
        value = None
        if command:
            if command in self.invalid_commands:
                self._log.warning("can't run {} from MQTT".format(command))
                return None
            try:
                self._log.info('Received command: {}'.format(command))
                self._log.info('args: {}'.format(args))
                
                if args:
                    value = await self._method_dict[command](*args)
                else:
                    value = await self._method_dict[command]()
            except Exception as e:
                self._log.warning('Command error {} {}: {}'.format(command, args, e))
            self._log.debug('return value: {}'.format(value))
        return value
        
    def _filter_list(self, fl):
        '''
        utility function to strip '' out of lists, and trim leading/trailing spaces
        returns filtered list
        '''
        return list(filter(lambda x: (x !=''), [x.strip() if isinstance(x, str) else x for x in fl]))
        
    async def _stop(self):
        tasks = [t for t in self._tasks.values() if t is not asyncio.current_task()]
        [task.cancel() for task in tasks]
        self._log.info("Cancelling {} outstanding tasks".format(len(tasks)))
        await asyncio.gather(*tasks, return_exceptions=True)
        self._tasks = {}
        if self._MQTT_connected:
            self._mqttc.disconnect()
            self._mqttc.loop_stop()
            self._mqttc = None
        self._log.info('{} stopped'.format(self._name))
