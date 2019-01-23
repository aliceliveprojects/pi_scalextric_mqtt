import argparse
import RPi.GPIO as GPIO
import time

parser = argparse.ArgumentParser(description='Channel Throttle')
parser.add_argument('throttle', metavar='N', type=int, nargs='+',
                    help='Throttle')

args = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

for x in range(args.throttle[0]):
	GPIO.output(18,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.1)
GPIO.output(18,GPIO.LOW)

print("[{\"channel\" : 0,\"name\":\"car1\",\"pin\":\"18\",\"percent\":20}]")

