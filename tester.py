#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
from squid import *
import time
reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

try:
    rgb = Squid(18,23,24)
    while True:
        id, text = reader.read()
	rgb.set_color(RED)
	time.sleep(1)
	rgb.set_color(GREEN)
        

finally:
    print("cleaning up")
    GPIO.cleanup()
