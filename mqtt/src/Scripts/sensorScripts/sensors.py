import argparse
import json
import time
import paho.mqtt.client as mqttClient
import sensorsMqtt
import importlib
import subprocess
import threading, time


sensorThreads= []

def sensorCallback(id,percent):
    print("H")
    sensorsMqtt.publishSensorEvent(id)
    


def sensorDetails(sensorDetails):
    print(sensorDetails)
    
    stopSensor(sensorThreads)
    
    for sensorId in sensorDetails:
        startSensor(sensorDetails[sensorId])

def stopSensor(sensors):
    for sensor in sensors:
        sensor.stop()
        
def startSensor(sensor):
    triggerPercent = 0
    
    name = "un-named"
    if 'name' in sensor:
        name = sensor['name']
        
    if 'trigger' in sensor:
        triggerPercent = sensor['trigger']
    else:
        triggerPercent = sensor['default_trigger']
    
    if 'id' in sensor:
        callbackId = sensor['id']
    else:
        callbackId = 0
    
    enabled = False

    if 'enabled' in sensor:
        enabled = sensor['enabled']

    if enabled != False:
        print("Enabling sensor: ", sensor['name'])
        sensor = importlib.import_module(sensor['name'])
        thread = threading.Thread(target=sensor.startSensor, args=(triggerPercent,sensorCallback, callbackId))
        sensorThreads.append(sensor)
        thread.start()
    


# Define Command Line Arguments
parser = argparse.ArgumentParser(description='Publishes to Sensor Event once a sensor is above the specified threshold')
parser.add_argument('piUUID',help='UUID of the pi')
parser.add_argument('broker_address', help='Broker address, not including port example: m15.cloudmqtt.com')
parser.add_argument('broker_port',help='Port for broker',type=int)
parser.add_argument('--username',nargs='?', help='Username for broker (username must not be "None")')
parser.add_argument('--password',nargs='?', help='Password for broker (password must not be "None")')

args = parser.parse_args()



# Broker Details Taken From Command Line Args
piID = args.piUUID
broker_address = args.broker_address
port = args.broker_port
username = args.username
password = args.password



def execute():
        sensorsMqtt.on_sensorDetails = sensorDetails
        sensorsMqtt.connect(piID,broker_address,port,username=username,password=password)

def main():
    try:
        execute()
    finally:
        stopSensor(sensorThreads)
        sensorsMqtt.disconnect()

if __name__=='__main__':
    main()

