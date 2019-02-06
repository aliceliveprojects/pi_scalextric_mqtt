import RPi.GPIO as GPIO
import time
import random
import argparse


# Define Command Line Arguments
parser = argparse.ArgumentParser(description='Deploys special weapon to a specific channel')
parser.add_argument('targetChannel',help='Which channel to target the special weapon',type=int)

args = parser.parse_args()
targetChannel = args.targetChannel


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(targetChannel,GPIO.OUT)



p = GPIO.PWM(targetChannel, 50)
p.start(0)
start = time.time()
elapsedTime = 0

high = False

while elapsedTime < 5:
    if high:
        print()
        p.ChangeDutyCycle(random.uniform(70,100))
        high = False
    else:
        p.ChangeDutyCycle(random.uniform(10,40))
        high = True

    time.sleep(1)
    end= time.time()
    elapsedTime = end - start

