from flask import Flask, make_response, jsonify, abort
from mqtt import MqttListener
import logging
from logging.handlers import RotatingFileHandler
import signal
import sys

mk2_printer_power_topic = 'home/garage/printer/mk2/power'
mk2_printer_light_topic = 'home/garage/printer/mk2/light/power'
mk2s_printer_power_topic = 'home/garage/printer/mk2s/power'
mk2s_printer_light_topic = 'home/garage/printer/mk2s/light/power'
app_name = 'mqtt_listener_app'

app_name = 'mqtt_listener_app'

app = Flask('MqttListenerApp')

# create logger with 'spam_application'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create file handler which logs even debug messages
fh = logging.FileHandler('application.log')
fh.setLevel(logging.INFO)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
app.logger.addHandler(fh)
app.logger.addHandler(ch)
app.logger.setLevel(logging.DEBUG)


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/printer/power/<int:task_id>", methods=['POST'])
def printer_power(task_id):
    
    if len(task_id) == 0:
        abort(404)

    if task_id == 1:
        task = "Turn power On"
    elif task_id == 0:
        task = "Turn power Off"
    else:
        task = "Unknown command"

    print(task)
    return task


@app.route("/printer/light/<int:task_id>", methods=['POST'])
def printer_light(task_id):
    if task_id == 1:
        task = "Turn light On"
    elif task_id == 0:
        task = "Turn light Off"
    else:
        task = "Unknown command"

    app.logger.info(task)
    print(task)
    return task


def main():

    signal.signal(signal.SIGINT, signal_handler)
    logger.debug("======= Application Starting =======")
    # start topic listeners
    try:
        logger.info("Starting Threads")
        mqttla = MqttListener(mk2_printer_power_topic, app_name + "_pp")
        mqttla.start()

        mqttlb = MqttListener(mk2_printer_light_topic, app_name + "_pl")
        mqttlb.start()

        mqttlc = MqttListener(mk2s_printer_power_topic, app_name + "_pp")
        mqttlc.start()

        mqttld = MqttListener(mk2s_printer_power_topic, app_name + "_pp")
        mqttld.start()

    except Exception,e:
        logger.error("Error: unable to start listener threads! %s", str(e))

    # launch Flask server
    app.logger.info("Starting app")
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
