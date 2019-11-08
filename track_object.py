import cv2
import numpy as np
import pickle
import infer
import servo


max_distance = 1000000              # Max distance measurement for a keypoint match to be considered valid.
obj_of_interest = "person"          # Object to locate.  COCO class label.

surf = cv2.xfeatures2d.SURF_create()
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)

cap = cv2.VideoCapture(0)
cap.set(3, 300)
cap.set(4, 300)


def unpickle_keypoints(array):
    keypoints = []
    descriptors = []
    for point in array:
        temp_feature = cv2.KeyPoint(x=point[0][0], y=point[0][1], _size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        temp_descriptor = point[6]
        keypoints.append(temp_feature)
        descriptors.append(temp_descriptor)
    return keypoints, np.array(descriptors)


# Load previously determined KPs.
keypoints_database = pickle.load(open("keypoints_database.dat", "rb"))
kp1, desc1 = unpickle_keypoints(keypoints_database[0])
kp1, desc1 = unpickle_keypoints(keypoints_database[1])

# Initialize DL model.
ssd_model, utils, classes_to_labels = infer.init_model()

while True:
    ret, frame = cap.read()

    # Locate the object of interest in the current frame.
    obj_x, obj_y, obj_w, obj_h = infer.locate_object(frame, obj_of_interest, ssd_model, utils, classes_to_labels)

    # If the object was found...
    if obj_x is not None:
        # Detect keypoints in curent frame.
        kp2 = surf.detect(frame, None)
        kp2, desc2 = surf.compute(frame, kp2)

        # Search for keypoints that match the saved keypoints.
        matches = bf.match(desc1, desc2)

        # If the top keypoint is a close enough match...
        if len(matches) > 0:
            matches = sorted(matches, key = lambda x:x.distance)
            if matches[0].distance < max_distance:
                kp2_idx = matches[0].trainIdx
                (x, y) = kp2[kp2_idx].pt

                print("Object at x:{} y:{}".format(obj_x, obj_y))
                print("Laser at x:{} y:{} score:{}".format(x, y, matches[0].distance))
                # Move laser point closer to object via servo motion.
                servo.move_laser(obj_x, obj_y, x, y)
