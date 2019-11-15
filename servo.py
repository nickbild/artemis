import RPi.GPIO as GPIO
from time import sleep


window = 15

dir1 = 25 # Pin 22.
dir2 = 8 # Pin 24.
servo_select = 24 # Pin 18.

GPIO.setmode(GPIO.BCM)
GPIO.setup(dir1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(dir2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(servo_select, GPIO.OUT, initial=GPIO.LOW)


def move_laser(obj_x, obj_y, x, y, pwm):
    if (x + window) < obj_x:
        # Right.
        GPIO.output(servo_select, GPIO.LOW)

        GPIO.output(dir1, GPIO.LOW)
        sleep(0.01)
        GPIO.output(dir1, GPIO.HIGH)
        sleep(0.01)
        GPIO.output(dir1, GPIO.LOW)

    elif (x - window) > obj_x:
        # Left
        GPIO.output(servo_select, GPIO.LOW)

        GPIO.output(dir2, GPIO.LOW)
        sleep(0.01)
        GPIO.output(dir2, GPIO.HIGH)
        sleep(0.01)
        GPIO.output(dir2, GPIO.LOW)

    if (y + window) < obj_y:
        # Down.
        GPIO.output(servo_select, GPIO.HIGH)

        GPIO.output(dir1, GPIO.LOW)
        sleep(0.01)
        GPIO.output(dir1, GPIO.HIGH)
        sleep(0.01)
        GPIO.output(dir1, GPIO.LOW)

    elif (y - window) > obj_y:
        # Up.
        GPIO.output(servo_select, GPIO.HIGH)

        GPIO.output(dir2, GPIO.LOW)
        sleep(0.01)
        GPIO.output(dir2, GPIO.HIGH)
        sleep(0.01)
        GPIO.output(dir2, GPIO.LOW)
