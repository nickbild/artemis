import RPi.GPIO as GPIO


window = 15


def init():
    output_pin = 27 # Pin 13.
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    p = GPIO.PWM(output_pin, 50)
    p.start(7.5) # Center.  Range 5-10.

    return p


def move_laser(obj_x, obj_y, x, y, p):
    if (x + window) < obj_x:
        print("Move servo right.")
        p.ChangeDutyCycle(6)
    elif (x - window) > obj_x:
        print("Move servo left.")
        p.ChangeDutyCycle(8)
    else:
        print("x OK")

    if (y + window) < obj_y:
        print("Move servo down.")
    elif (y - window) > obj_y:
        print("Move servo up.")
    else:
        print("Y OK")
