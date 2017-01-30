

Image
https://hub.docker.com/_/eclipse-mosquitto/


docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/Users/mcarr/workspace/code/python/mqtt_listener_app/mosquitto/mosquitto/config/mosquitto.conf -v $PWD/mosquitto/data -v $PWD/mosquitto/log eclipse-mosquitto
