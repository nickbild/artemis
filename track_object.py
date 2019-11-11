import cv2
import numpy as np
import infer
import servo
import laser_tracker


obj_of_interest = "scissors"          # Object to locate.  COCO class label.

cap = cv2.VideoCapture(0)
cap.set(3, 352)
cap.set(4, 288)

# Initialize DL model.
ssd_model, utils, classes_to_labels = infer.init_model()

while True:
    ret, frame = cap.read()

    # Locate the object of interest in the current frame.
    obj_x, obj_y, obj_w, obj_h = infer.locate_object(frame, obj_of_interest, ssd_model, utils, classes_to_labels)

    # If the object was found...
    if obj_x is not None:
        laser_coords = laser_tracker.detect(frame)

        if laser_coords is not None:
            laser_x = laser_coords[0]
            laser_y = laser_coords[1]
            print("Object at x:{} y:{}".format(obj_x, obj_y))
            print("Laser at x:{} y:{}".format(laser_x, laser_y))
            # Move laser point closer to object via servo motion.
            servo.move_laser(obj_x, obj_y, laser_x, laser_y)
