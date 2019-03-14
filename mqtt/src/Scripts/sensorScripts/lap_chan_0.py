import time
import grovepi

id = 0

# Connect the Grove IR Reflective Sensor to digital port D3
light_sensor = 3

# default threshold value
threshold = 1

grovepi.pinMode(light_sensor,"INPUT")

stop = False

def changeTriggerPercent(triggerPercent):
    global threshold
    threshold = int(triggerPercent)

def stopSensor():
    print("stopped")
    global stop
    stop = True

def startSensor(triggerPercent,callback, callbackId):
    global threshold
    threshold = int(triggerPercent)
    id =  int(callbackId)
    
    triggered = False
    while not stop:
        try:
            light_value = grovepi.digitalRead(light_sensor)
            if(light_value >= threshold):
                if not triggered:
                    triggered = True
                    callback(id,light_value)

            if(triggered and light_value < threshold):
                triggered = False
            
            time.sleep(.05)
        except IOError:
            stopSensor()
            print("Error")



