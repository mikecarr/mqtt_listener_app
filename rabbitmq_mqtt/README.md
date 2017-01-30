

## Build
```
docker build -t rabbit-mqtt .
```

## Run it
```
docker run -it -p 1883:1883 -p 15672:15672 rabbit-mqtt
```

## Admin console
http://localhost:15672/

u/p: guest/guest

https://www.rabbitmq.com/management.html

