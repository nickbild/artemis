import cv2
import numpy as np
import pickle


def pickle_keypoints(keypoints, descriptors):
    i = 0
    temp_array = []
    for point in keypoints:
        temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id, descriptors[i])
        ++i
        temp_array.append(temp)
    return temp_array


kp_array = []
surf = cv2.xfeatures2d.SURF_create()

for num in range(99):
    frame = cv2.imread("img/file_{}.jpg".format(num))

    kp = surf.detect(frame, None)
    kp, des = surf.compute(frame, kp)

    # img = cv2.drawKeypoints(frame, [kp[0]], color=(0,255,0), flags=0, outImage=np.array([]))
    # Find KP of interest (by coordinates).
    # i = 0
    # for keyPoint in kp:
    #     x = keyPoint.pt[0]
    #     y = keyPoint.pt[1]
    #     s = keyPoint.size
    #     cv2.putText(img, str(i), (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200,0,0), 1, cv2.LINE_AA)
    #     # if x > 580 and x < 700:
    #     #     print("x:{0} y:{1} size:{2} index:{3}".format(x, y, s, i))
    #     i += 1
    #     if i == 1:
    #         break
    #
    # cv2.imshow('KP', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Limit to KP of interest.
    kp_index = 0
    kp = [kp[kp_index]]
    des = [des[kp_index]]

    # Save current KP.
    temp = pickle_keypoints(kp, des)
    kp_array.append(temp)

# Save all KPs to file.
pickle.dump(kp_array, open("keypoints_database.dat", "wb"))
