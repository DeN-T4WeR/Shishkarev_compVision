import cv2
import numpy

img: numpy.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)
h, w, _ = img.shape
shirink_koeff = 2
img = cv2.resize(img, (w//shirink_koeff, h//shirink_koeff), cv2.INTER_NEAREST)

while True:

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2. imshow("orog", img)
    cv2. imshow("imgHSV", imgHSV)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break