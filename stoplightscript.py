# A simple scrpt to make the lights on my Pi act like a stoplight.

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
import time
while True :
	GPIO.output(4, True)
	time.sleep(.1)
	GPIO.output(4, False)
	GPIO.output(17, True)
	time.sleep(.1)
	GPIO.output(17, False)
	GPIO.output(22, True)
	time.sleep(.1)
	GPIO.output(22, False)
	GPIO.output(17, True)
	time.sleep(.1)
	GPIO.output(17, False)