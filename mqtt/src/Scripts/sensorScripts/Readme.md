# Sensor Scripts

This readme is intended for developers only not for deployment

## How It Works
Well thats simple. Node-red reads where sensors.py is located from the config.json file and deploys the script.

Sensors.py subscribes to the sensors topic to retrieve sensor.json details and starts up each sensor. For sensors.py to start-up each sensor each script file must be in sensors.py folder and must be named the same as in the sensors.json file.

Each sensor runs on an independant thread and can publish to the sensor event topic when triggered.

If you wish to change the trigger percentage for a sensor once everything has been deployed, a trigger_percent topic is exposed. Publish the new trigger percentage to trigger_percent topic and the sensor.py will handle the rest. 