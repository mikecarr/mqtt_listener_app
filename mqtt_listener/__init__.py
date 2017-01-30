from flask import Flask, make_response, jsonify, abort
from mqtt import MqttListener

app = Flask(__name__)


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

    print(task)
    return task


def main():

    # start topic listeners
    try:
        print("Starting Thread")
        mqttla = MqttListener('home/sample/a')
        mqttla.start()

        mqttlb = MqttListener('home/sample/b')
        mqttlb.start()

    except:
        print("Error: unable to start listener threads!")

    # launch Flask server
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
