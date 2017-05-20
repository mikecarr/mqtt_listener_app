from flask_mqtt import Mqtt
from app import app
import logging
from rpi_rf import RFDevice

MK2_PRINTER_POWER_TOPIC = 'home/garage/printer/mk2/power'
MK2_PRINTER_LIGHT_TOPIC = 'home/garage/printer/mk2/light/power'
MK2S_PRINTER_POWER_TOPIC = 'home/garage/printer/mk2s/power'
MK2S_PRINTER_LIGHT_TOPIC = 'home/garage/printer/mk2s/light/power'

mqtt = Mqtt(app)

mqtt.subscribe(MK2_PRINTER_POWER_TOPIC)
mqtt.subscribe(MK2_PRINTER_LIGHT_TOPIC)
mqtt.subscribe(MK2S_PRINTER_POWER_TOPIC)
mqtt.subscribe(MK2S_PRINTER_LIGHT_TOPIC)

rfdevice = RFDevice(17)
rfdevice.enable_tx()

#logger = logging.getLogger('MqttListenerApp.MqttListener')
app.logger.info("***r *MQTT Handler Init... ***")
#sender = RCSwitchSender()
#sender.enableTransmit(0)  # use WiringPi pin 0
#sender.setPulseLength(189)
pulse_length = 189


def send_signal(code, pulse_length=189, protocol=1):
    app.logger.debug("sending")
    rfdevice.tx_code(code, protocol, pulse_length)
    app.logger.debug("sending...done")


@mqtt.on_topic(MK2_PRINTER_POWER_TOPIC)
def handle_mk2_topic(client, userdata, msg):
    app.logger.info('Received msg.on topic {}: {}'
         .format(msg.topic, msg.payload.decode()))

    if int(msg.payload) == 1:
        send_signal(87347)
    elif int(msg.payload) == 0:
        send_signal(87356)
    else:
        app.logger.error("Oops error, don't know how to do that.")

@mqtt.on_topic(MK2_PRINTER_LIGHT_TOPIC)
def handle_mk2_light_topic(client, userdata, msg):
    app.logger.info('Received msg.on topic {}: {}'
         .format(msg.topic, msg.payload.decode()))

    if int(msg.payload) == 1:
        send_signal(87491)
    elif int(msg.payload) == 0:
        send_signal(87500)
    else:
        app.logger.error("Oops error, don't know how to do that.")


@mqtt.on_topic(MK2S_PRINTER_POWER_TOPIC)
def handle_mk2s_power_topic(client, userdata, msg):
    app.logger.info('Received msg.on topic {}: {}'
         .format(msg.topic, msg.payload.decode()))

    if int(msg.payload) == 1:
        send_signal(87811)
    elif int(msg.payload) == 0:
        send_signal(87820)
    else:
        app.logger.error("Oops error, don't know how to do that.")


@mqtt.on_topic(MK2S_PRINTER_LIGHT_TOPIC)
def handle_mk2s_light_topic(client, userdata, msg):
    app.logger.info('Received msg.on topic {}: {}'
         .format(msg.topic, msg.payload.decode()))

    if int(msg.payload) == 1:
        send_signal(89347)
    elif int(msg.payload) == 0:
        send_signal(89356, 183 )
    else:
        app.logger.error("Oops error, don't know how to do that.")



