import RPi.GPIO as GPIO


window = 15


def init():
    output_pin = 24 # Pin 18.
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    pwm = GPIO.PWM(output_pin, 50)
    pwm.start(7.5) # Center.  Range 5-10.

    return pwm


def move_laser(obj_x, obj_y, x, y, pwm):
    if (x + window) < obj_x:
        print("Move servo right.")
        pwm.ChangeDutyCycle(6)
    elif (x - window) > obj_x:
        print("Move servo left.")
        pwm.ChangeDutyCycle(8)
    else:
        print("x OK")

    if (y + window) < obj_y:
        print("Move servo down.")
    elif (y - window) > obj_y:
        print("Move servo up.")
    else:
        print("Y OK")
