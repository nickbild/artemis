import cv2
import numpy as np
import pickle


frame = cv2.imread("file_2.jpg")

surf = cv2.xfeatures2d.SURF_create()
kp = surf.detect(frame, None)
kp, des = surf.compute(frame, kp)

# Find KP of interest (by coordinates).
i = 0
for keyPoint in kp:
    x = keyPoint.pt[0]
    y = keyPoint.pt[1]
    s = keyPoint.size
    if x > 580 and x < 700:
        print("x:{0} y:{1} size:{2} index:{3}".format(x, y, s, i))
    i += 1

# Limit to KP of interest.
kp_index = 109
kp = [kp[kp_index]]
des = [des[kp_index]]

img = cv2.drawKeypoints(frame, kp, color=(0,255,0), flags=0, outImage=np.array([]))
cv2.imshow('KP', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


def pickle_keypoints(keypoints, descriptors):
    i = 0
    temp_array = []
    for point in keypoints:
        temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id, descriptors[i])
        ++i
        temp_array.append(temp)
    return temp_array


def unpickle_keypoints(array):
    keypoints = []
    descriptors = []
    for point in array:
        temp_feature = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        temp_descriptor = point[6]
        keypoints.append(temp_feature)
        descriptors.append(temp_descriptor)
    return keypoints, np.array(descriptors)


# Save KPs.
temp_array = []
temp = pickle_keypoints(kp, des)
temp_array.append(temp)
pickle.dump(temp_array, open("keypoints_database.dat", "wb"))
