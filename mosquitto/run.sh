#!/bin/sh


docker run -it -p 1883:1883 -p 9001:9001 \
-v $PWD/mosquitto/data \
-v $PWD/mosquitto/log \
eclipse-mosquitto