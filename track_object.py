import cv2
import numpy as np
import infer
import servo
import laser_tracker
import laser_control


obj_of_interest = "scissors"          # Object to locate.  COCO class label.
laser_on = False

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize DL model.
ssd_model, utils, classes_to_labels = infer.init_model()

pwm = servo.init()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (300, 300))

    # Locate the object of interest in the current frame.
    obj_x, obj_y, obj_w, obj_h = infer.locate_object(frame, obj_of_interest, ssd_model, utils, classes_to_labels)

    # If the object was found...
    if obj_x is not None:
        # Turn laser on.
        if not laser_on:
            laser_on = True
            laser_control.on()

        laser_coords = laser_tracker.detect(frame)

        if laser_coords is not None:
            laser_x = laser_coords[0]
            laser_y = laser_coords[1]

            obj_x_center = int(obj_x + (obj_w / 2))
            obj_y_center = int(obj_y + (obj_h / 2))

            #print("Object center at x:{} y:{}".format(obj_x_center, obj_y_center))
            #print("Laser at x:{} y:{}".format(laser_x, laser_y))

            # Move laser point closer to object via servo motion.
            servo.move_laser(obj_x_center, obj_y_center, laser_x, laser_y, pwm)
    else:
        # Turn laser off.
        if laser_on:
            laser_on = False
            laser_control.off()
