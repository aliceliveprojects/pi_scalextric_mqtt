import time
import grovepi
import threading

id = 0

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10

mutex = threading.Lock()

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

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
    id = int(callbackId)
    
    tiggered = False
    while not stop:
        mutex.acquire()
        try:
            light_value = grovepi.analogRead(light_sensor)
            if(light_value <= threshold):
                if not tiggered:
                    tiggered = True
                    callback(id,light_value)

            if(tiggered and light_value > threshold):
                tiggered = False
            print(light_value)
        except IOError:
            stopSensor()
            print("Error")
        finally:
            mutex.release()
            time.sleep(.5)


