import argparse
import json
import time
import paho.mqtt.client as mqttClient
import sensorsMqtt
import importlib
import subprocess
import threading, time



def my_threaded_func(arg, arg2):
    print "Running thread! Args:", (arg, arg2)
    time.sleep(10)
    print "Done!"




def sensorCallback(id,percent):
    sensorsMqtt.publishSensorEvent(id)
    


def sensorDetails(sensorDetails):
    print(sensorDetails)
    
    
    for sensorId in sensorDetails:
        triggerPercent = 0
        sensor = sensorDetails[sensorId]
        if 'trigger' in sensor:
            triggerPercent = sensor['trigger']
        else:
            triggerPercent = sensor['default_trigger']
        sensor = importlib.import_module(sensor['name'])
        thread = threading.Thread(target=sensor.startSensor, args=(10,sensorCallback))
        thread.start()
        



# Define Command Line Arguments
parser = argparse.ArgumentParser(description='Publishes to Sensor Event once a sensor is above the specified threshold')
parser.add_argument('piUUID',help='UUID of the pi')
parser.add_argument('broker_address', help='Broker address, not including port example: m15.cloudmqtt.com')
parser.add_argument('broker_port',help='Port for broker',type=int)
parser.add_argument('sensorFilePath', help='Absolute path to the sensor.json file')
parser.add_argument('--username',nargs='?', help='Username for broker (username must not be "None")')
parser.add_argument('--password',nargs='?', help='Password for broker (password must not be "None")')

args = parser.parse_args()



# Broker Details Taken From Command Line Args
piID = args.piUUID
broker_address = args.broker_address
port = args.broker_port
username = args.username
password = args.password

sensorsMqtt.on_sensorDetails = sensorDetails
sensorsMqtt.connect(piID,broker_address,port,username=username,password=password)
