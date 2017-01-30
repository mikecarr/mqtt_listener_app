import paho.mqtt.client as mqtt
from threading import Thread

MQTT_HOST = "localhost"


class MqttListener(Thread):
    """ MQTT listener """
    topic = ""

    def __init__(self, topic, client_id=None):
        ''' Constructor '''
        Thread.__init__(self)

        self.topic = topic
        self.mqttc = mqtt.Client(client_id)
        self.mqttc.on_connect = self.mqtt_on_connect
        self.mqttc.on_message = self.mqtt_on_message

    def mqtt_on_connect(self, client, obj, flags, rc):
        print("Connected with result code " + str(rc))

    def mqtt_on_message(self, client, obj, msg):
        print("Topic: ", msg.topic + '\nMessage: ' + str(msg.payload))

    def mqtt_on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        print("connecting to %s" % MQTT_HOST)
        self.mqttc.connect(MQTT_HOST, 1883, 60)

        print("subscribing to %s" % self.topic)
        self.mqttc.subscribe(self.topic, 0)

        rc = 0
        while rc == 0:
            rc = self.mqttc.loop()
        return rc
