# Sensor Scripts

This readme is intended for developers only not for deployment

## How It Works
Well thats simple. Node-red reads where sensors.py is located from the config.json file and deploys it.

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

```python qrCodeGen.py [PIUUID] [BROKER_ADDRESS] [BROKER_PORT] --username [USERNAME] --password [PASSWORD]```

For Help :

```python qrCodeGen.py -h```