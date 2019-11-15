import RPi.GPIO as GPIO
import time

output_pin = 23 # Pin 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)


def on():
    GPIO.output(output_pin, GPIO.HIGH)

def off():
    GPIO.output(output_pin, GPIO.LOW)

