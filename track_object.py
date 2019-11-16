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

loop = 0
obj = []
for i in range(15):
    obj.append({'x': None, 'y': None, 'w': None, 'h': None})

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (300, 300))

    # Locate the object of interest in the current frame.
    obj_x, obj_y, obj_w, obj_h = infer.locate_object(frame, obj_of_interest, ssd_model, utils, classes_to_labels)

    
    obj[loop] = {'x': obj_x, 'y': obj_y, 'w': obj_w, 'h': obj_h}

    loop += 1

    if loop == 15:
        loop = 0

    found = False
    found_at = 0
    for i in range(14, -1, -1):
        if obj[i]['x'] is not None:
            found = True
            found_at = i

    # If the object was found...
    if found:
        obj_x = obj[found_at]['x']
        obj_y = obj[found_at]['y']
        obj_w = obj[found_at]['w']
        obj_h = obj[found_at]['h']

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
            servo.move_laser(obj_x_center, obj_y_center, laser_x, laser_y)
    else:
        # Turn laser off.
        if laser_on:
            laser_on = False
            laser_control.off()
