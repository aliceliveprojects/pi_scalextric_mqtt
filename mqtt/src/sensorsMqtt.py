import paho.mqtt.client as mqttClient
import json

UUID = None

on_sensorDetails = None

def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        print("connected to broker")
          
        client.message_callback_add("testUUID/sensors",sensorDetailsSub)
        client.subscribe("testUUID/sensors")

def sensorDetailsSub(client, userdata, message):
    # change the sensor string to JSON
    sensorJSON = json.loads(message.payload)

    try:
        global sensorDetails
        sensorDetails(sensorJSON)
    except:
        pass
  
    
    
   

def connect(piUUID,broker_address,port,username='None',password='None'):
    global UUID
    UUID = piUUID
    
    client = mqttClient.Client(client_id="",clean_session=True)

    if username != 'None':
        if password != 'None':
            client.username_pw_set(username, password=password)
        else:
            client.username_pw_set(username)


    client.on_connect= on_connect
    
    # Establish Connection To Broker
    client.connect(broker_address, port=port)
    client.loop_forever()