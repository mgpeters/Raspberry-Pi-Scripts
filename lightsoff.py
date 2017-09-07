# A simple script for turning off any idling lights hooked up
# to my Pi.

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(4, False)
GPIO.setup(17, False)
GPIO.setup(22, False)