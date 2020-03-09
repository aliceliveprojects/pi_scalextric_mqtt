# Sensor Scripts

This readme is intended for developers only not for deployment

Nice installation guide for Eclipse Paho on Python here: http://www.steves-internet-guide.com/into-mqtt-python-client/

1. RPi (Raspbian, Buster) has Python 2.7 and 3 installed
1. Pip installed, and available as pip2 and pip3

We are now explicitly using Python 3

```
pip3 install paho-mqtt
```

1. Grove pi installation. See:  https://pypi.org/project/grovepi/

```
curl -kL dexterindustries.com/update_grovepi | bash
```

1. If you are intending to debug - why not use VSCode on a machine remote to the Pi? To set-up, follow the worklog here: https://github.com/aliceliveprojects/little_blue_pi/blob/master/documentation/worklogs/27.01.2020.md. Once you can see the remote project, use VSCode to install the Python Extensions on the RPi.

1. We're seeing problems with sensors barfing:

```
I/O operation on closed file
```
or

```
argument must be an int, or have a fileno() method.
```

See this for some insight: https://forum.dexterindustries.com/t/grovepi-seems-unstable/6602/2

1. And also reset the firmware with this:

```bash
avrdude -c gpio -p m328p
```

We modified the code to include mutexes around calls to the grovepi functions. We also changed any calls to python programs from within Node-RED to use Python3.  


## How It Works
Note: we're now using websockets exclusively over ssl/tls. The port used on the MQTT server must reflect this - normally, it's 443.

Note: Node-red reads where sensors.py is located from the config.json file and deploys it. The paths to sensors and resources are absolute, not relative, so it's very likely you will need to change them.

Sensors.py subscribes to the sensors topic to retrieve sensor.json details and starts up each sensor. For sensors.py to start-up each sensor each script file must be in sensors.py folder and must be named the same as in the sensors.json file.

For example oli_slick ==> oil_slick.py.

Each sensor runs on an independant thread and can publish to the sensor event topic when triggered.

If you wish to change the trigger percentage for a sensor once everything has been deployed, a trigger_percent topic is exposed. Publish the new trigger percentage to trigger_percent topic and the sensor.py will handle the rest.

## Deploying Sensors.py

### Command Line Arguments

Positional Arguments

| Arguments     | Description  |
| ------------- |:-------------:|
| piUUID        | Pi UUID |
| broker_address    | Broker host|
| broker_port    | Broker port|

Optional Arguments

| Arguments     | Description |
| ------------- |:---------------:|
| --username     | Broker username|
| --password     | Broker password|



To run : 

```python sensors.py [PIUUID] [BROKER_ADDRESS] [BROKER_PORT] --username [USERNAME] --password [PASSWORD]```

For Help :

```python sensors.py -h```

## Sensor Scripts
Each sensor script must contain three functions

---

**changeTriggerPercent**

Must update the trigger percentage

**Parameters**

| Name     | Type | Description |
| --------- |------ |---------------|
| triggerPercent | Number | New trigger percentage |


---

**stopSensor**

Must stop sensor 

---

**startSensor**

Must start the sensor and call callback when triggered

**Parameters**

| Name     | Type | Description |
| ------------- |------ |---------------|
| triggerPercent| Number| Trigger percentage |
| callback| Function| Trigger percentage callback |


