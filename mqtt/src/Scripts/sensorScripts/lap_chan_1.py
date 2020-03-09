import time
import grovepi
import threading

id = 0

# Connect the Grove IR Reflective Sensor to digital port D4
light_sensor = 4

# default threshold value
threshold = 1

grovepi.pinMode(light_sensor, "INPUT")

stop = False


mutex = threading.Lock()

def changeTriggerPercent(triggerPercent):
    global threshold
    threshold = int(triggerPercent)


def stopSensor():
    print("stopped")
    global stop
    stop = True


def startSensor(triggerPercent, callback, callbackId):
    global threshold
    global mutex
    threshold = int(triggerPercent)
    id = int(callbackId)
    triggered = False
    while not stop:
        mutex.acquire()
        try:
            light_value = grovepi.digitalRead(light_sensor)
            if(light_value >= threshold):
                if not triggered:
                    triggered = True
                    callback(id, light_value)

            if(triggered and light_value < threshold):
                triggered = False

            
        except Exception as e:
            print(e)
            stopSensor()
        finally:
            mutex.release()
            time.sleep(.1)
