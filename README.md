# Artemis

Artemis is an eyeglass-mounted device that can be configured to locate a specific type of object, or a person.  When the target is found, Artemis will track it with a laser.

## How It Works

An eyeglass-mounted camera streams images to a Jetson AGX Xavier.  An SSD300 model is used for object localization within these images.  When the object of interest has been found, a laser diode is turned on.

A servo is also mounted on the eyeglasses for X-axis control of the laser.  A second servo is mounted on top of the first, at a 90 degree angle, to give Y-axis control.  The laser is mounted on the second servo.

Images are thresholded in OpenCV to determine the location of the laser pointer.  With the location of the object, and also the laser, now determined it is possible to adjust the servos to place the laser over the object of interest.

### SSD300 Model

To save time in the prototyping phase, a model pre-trained with the COCO dataset was used ([PyTorch Hub](https://pytorch.org/hub/nvidia_deeplearningexamples_ssd/)).  It is able to recognize and localize [80 different object types](https://github.com/nickbild/artemis/blob/master/category_names.txt).

Any arbitrary model that provides object localization could be inserted in place of this model, and could be trained to detect anything of interest.

### Servo Control

An Adafruit Itsy Bitsy M4 Express microcontroller dev board was used to simplify control of the servos.  The [Arduino sketch is available here](https://github.com/nickbild/artemis/blob/master/servo_handler/servo_handler.ino).

## Media

See it in action.  In this video, Artemis has been directed to find a pair of scissors:  
[YouTube](https://www.youtube.com/watch?v=zOmJOMlqhAQ)

The processing:
![core](https://raw.githubusercontent.com/nickbild/artemis/master/img/core_sm.jpg)

The device:
![core](https://raw.githubusercontent.com/nickbild/artemis/master/img/camera_sm.jpg)

The glasses:
![glasses](https://raw.githubusercontent.com/nickbild/artemis/master/img/glasses_sm.jpg)

## Software

To run the software, you'll need Python3 with the following modules installed:

```
numpy
cv2
RPi.GPIO
torch
skimage
```

Then clone the repo:

`git clone https://github.com/nickbild/artemis.git`

Switch to the `artemis` directory, then run:

`python3 track_object.py`

## Diagrams

![Fritzing Diagram](https://raw.githubusercontent.com/nickbild/artemis/master/diagrams/artemis_bb.png)

The Fritzing file can be [downloaded here](https://github.com/nickbild/artemis/raw/master/diagrams/artemis.fzz).

## Bill of Materials

- NVIDIA Jetson AGX Xavier
- Adafruit Itsy Bitsy M4 Express
- USB Webcam
- 2 x micro servos (e.g. Tower Pro SG92R)
- Laser diode
- NPN transistor
- Half breadboard
- Glasses / sunglasses
- Miscellaneous copper wire

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
