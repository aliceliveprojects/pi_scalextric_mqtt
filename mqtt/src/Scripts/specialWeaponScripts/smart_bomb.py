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

p.ChangeDutyCycle(100)
time.sleep(5)
p.ChangeDutyCycle(60)

