import time
import grovepi

id = 0

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

stop = False

def startSensor(triggerPercent,callback):
    global threshold
    threshold = int(triggerPercent)
    
    tiggered = False
    while not stop:
        try:
            light_value = grovepi.analogRead(light_sensor)
            if(light_value <= threshold):
                if not tiggered:
                    tiggered = True
                    callback(id,light_value)

            if(tiggered and light_value > threshold):
                tiggered = False
            print(light_value)
            time.sleep(.5)
        except IOError:
            print("Error")

def changeTriggerPercent(triggerPercent):
    global threshold
    threshold = int(triggerPercent)

def stopSensor():
    print("stopped")
    global stop
    stop = True