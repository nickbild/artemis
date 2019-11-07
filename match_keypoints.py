import cv2
import numpy as np
import pickle


max_distance = 1000000      # Max distance measurement for a match to be considered valid.


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

surf = cv2.xfeatures2d.SURF_create()
cap = cv2.VideoCapture(0)

while True:
    # Load image to find KP in.
    # frame = cv2.imread("file_2.jpg")
    ret, frame = cap.read()

    # Detect keypoints.
    kp2 = surf.detect(frame, None)
    kp2, desc2 = surf.compute(frame, kp2)

    # Search for a keypoint matching the target.
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
    matches = bf.match(desc1, desc2)

    if len(matches) > 0:
        matches = sorted(matches, key = lambda x:x.distance)
        if matches[0].distance < max_distance:
            kp2_idx = matches[0].trainIdx
            (x, y) = kp2[kp2_idx].pt

            print("Found at x:{} y:{} score:{}".format(x, y, matches[0].distance))

            # img_orig = cv2.imread("file_2.jpg")
            # img = cv2.drawMatches(img_orig, kp1, frame, kp2, matches[:10], flags=2, outImg=np.array([]))
            # cv2.imshow('KP', img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
