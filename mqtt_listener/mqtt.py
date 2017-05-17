import paho.mqtt.client as mqtt
from threading import Thread
from pi_switch import RCSwitchSender
import logging

MQTT_HOST = '10.0.1.5'
mk2_printer_power_topic = 'home/garage/printer/mk2/power'
mk2_printer_light_topic = 'home/garage/printer/mk2/light/power'
mk2s_printer_power_topic = 'home/garage/printer/mk2s/power'
mk2s_printer_light_topic = 'home/garage/printer/mk2s/light/power'

sender = RCSwitchSender()
sender.enableTransmit(0) # use WiringPi pin 0
sender.setPulseLength(189)


class MqttListener(Thread):
    """ MQTT listener """
    logger = logging.getLogger('MqttListenerApp.MqttListener')

    def __init__(self, topic, client_id=None):
        ''' Constructor '''
        Thread.__init__(self)
        self.logger.debug("Init: Topic: {}, Client Id: {}".format(topic, client_id))
        self.mqttc = mqtt.Client(client_id)
        self.mqttc.on_connect = self.mqtt_on_connect
        self.mqttc.on_message = self.mqtt_on_message
        self.topic = topic

        try:
            self.logger.info("connecting to %s" % MQTT_HOST)
            self.mqttc.username_pw_set('mqtt_listener')
            self.mqttc.connect(MQTT_HOST, 1883, 60)

        except Exception,e:
            self.logger.error("Error, %s" % str(e))

    def mqtt_on_connect(self, client, obj, flags, rc):
        self.logger.debug("Connected with result code " + str(rc))

        self.logger.debug("subscribing to %s" % self.topic)
        self.mqttc.subscribe(self.topic)

    def mqtt_on_message(self, client, obj, msg):
        self.logger.info("Topic: %s , Message: %s" % (str(msg.topic),str(msg.payload)))

        if msg.topic == mk2_printer_power_topic:
            if int(msg.payload) == 1:
		#  turn power on
                sender.sendDecimal(87347, 24)
            elif int(msg.payload) == 0:
                sender.sendDecimal(87356, 24)
            else:
                self.logger.error("Oops error, don't know how to do that.")

        elif msg.topic == mk2_printer_light_topic:
            if int(msg.payload) == 1:
		#  turn power on
                sender.sendDecimal(87491, 24)
            elif int(msg.payload) == 0:
                sender.sendDecimal(87500, 24)
            else:
                self.logger.error("Oops error, don't know how to do that.")
        
        elif msg.topic == mk2s_printer_power_topic:
            if int(msg.payload) == 1:
		#  turn power on
                sender.sendDecimal(87811, 24)
            elif int(msg.payload) == 0:
                sender.sendDecimal(87820, 24)
            else:
                self.logger.error("Oops error, don't know how to do that.")


    def mqtt_on_log(self, mqttc, obj, level, string):
        self.logger.debug(string)

    def start(self):
        self.logger.debug("** Start Loop **")
        self.mqttc.loop_start()


