


API

HTTP METHOD    | URI                                  | Action
===============|======================================|====================|
POST           | http://[hostname]/printer/power/1    | Turn Printer On    |
===============|======================================|====================|
POST           | http://[hostname]/printer/power/0    | Turn Printer Off   |
===============|======================================|====================|
POST           | http://[hostname]/printer/light/1    | Turn Lights On     |
===============|======================================|====================|
POST           | http://[hostname]/printer/light/0    | Turn Lights Off    |
===============|======================================|====================|

Testing
$ mosquitto_pub -h localhost -t 'home/sample/a' -m Hello


## References
* http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/


