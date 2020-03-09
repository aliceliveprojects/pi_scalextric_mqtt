import paho.mqtt.client as mqttClient
import json

UUID = None

sensorDetails = {}

recievedTriggers = 0

on_sensorDetails = None

client = None


def on_connect(client, userdata, flags, rc):
    print("connect")
    print("rc = ",rc)
    if(rc == 0):
        print("connected to broker")
        
        # retrieve sensor details
        client.message_callback_add(UUID + '/sensors', sensorDetailsSub)
        client.subscribe(UUID + '/sensors')
        # unsubscribe
        client.unsubscribe(UUID + '/sensors')
    else:
        print("connection returned rc of: " + rc)

def sensorTriggerPercentSub(client, userdata, message):
    global sensorDetails, recievedTriggers

    recievedTriggers = 1+recievedTriggers
    
    topicParts = message.topic.split('/')
    sensorId = int(topicParts[2])
    
    
    sensor = sensorDetails[sensorId]
    sensor['trigger'] = message.payload

    # check if all sensor trigger percents have been recieved, then notify 
    if(recievedTriggers == len(sensorDetails)):
            recievedTriggers = 0
            try:
                on_sensorDetails(sensorDetails)
            except:
                    pass
            
  



def sensorDetailsSub(client, userdata, message):
    # change the sensor string to JSON
    sensorJSON = json.loads(message.payload)

    global sensorDetails

    # fill sensor dic, key is sensor id
    for sensor in sensorJSON:
        sensorDetails[sensor['id']] = sensor

    
    # once sensor details have been retrieved, retireve sensor trigger percentages 
    client.message_callback_add(UUID + '/sensors/+/trigger_percent', sensorTriggerPercentSub)
    client.subscribe(UUID + '/sensors/+/trigger_percent')


def connect(piUUID, broker_address, port, username='None', password='None'):
    
    global UUID,client
    UUID = piUUID

    client = mqttClient.Client(client_id="", clean_session=True, transport="websockets")

    client.tls_set() 
    
    if username != 'None':
        print("username: ", username)
        if password != 'None':
            print("password", password)
            client.username_pw_set(username, password=password)
        else:
            client.username_pw_set(username)

    client.on_connect = on_connect

    # Establish Connection To Broker
    
    client.connect(broker_address, port=port)
    client.loop_forever()
    

def publishSensorEvent(sensorId):
    topic = UUID + '/sensors/' + str(sensorId)
    client.publish(topic)
    client.loop()

def disconnect():
    client.disconnect()
