import argparse
import json
import time
import paho.mqtt.client as mqttClient




def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        print("connected to broker")
        global Connected
        Connected = True
        
        client.message_callback_add("testUUID/sensors",sensorDetails)
        client.subscribe("testUUID/sensors")

def sensorDetails(client, userdata, message):

    print("Received message '" + str(message.payload) + "' on topic '"+ message.topic + "' with QoS " + str(message.qos))
    


# Define Command Line Arguments
parser = argparse.ArgumentParser(description='Publishes to Sensor Event once a sensor is above the specified threshold')
parser.add_argument('piUUID',help='UUID of the pi')
parser.add_argument('broker_address', help='Broker address, not including port example: m15.cloudmqtt.com')
parser.add_argument('broker_port',help='Port for broker',type=int)
parser.add_argument('sensorFilePath', help='Absolute path to the sensor.json file')
parser.add_argument('--username',nargs='?', help='Username for broker (username must not be "None")')
parser.add_argument('--password',nargs='?', help='Password for broker (password must not be "None")')

args = parser.parse_args()
print(args)


Connected = False

# Broker Details Taken From Command Line Args
piID = args.piUUID
broker_address = args.broker_address
port = args.broker_port
username = args.username
password = args.password

# Setup Client	
client = mqttClient.Client(client_id="",clean_session=True)

# Setup Client Username And Password if Specified
if username != 'None':
    if password != 'None':
        client.username_pw_set(username, password=password)
    else:
        client.username_pw_set(username)


client.on_connect= on_connect



# Establish Connection To Broker
client.connect(broker_address, port=port)
client.loop_forever()
