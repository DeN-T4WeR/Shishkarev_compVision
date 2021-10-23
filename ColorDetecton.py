import cv2
import numpy

img: numpy.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)

h, w, _ = img.shape
shirink_koeff = 2
img = cv2.resize(img, (w//shirink_koeff, h//shirink_koeff), cv2.shirink_koeff)
cv2. imshow("orog", img)
cv2.waitKey(0)