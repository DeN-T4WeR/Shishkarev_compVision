import cv2
import numpy as np

img = np.zeros((400, 600, 3), np.uint8)
# img[:] = 255,255,255
# img [200:300, 100:200] = 255, 0, 0

cv2.imshow('image', img)
cv2.waitKey(400)
cv2. line(img, (400,0), (800,800), (0,0,255), 3)
cv2.imshow('image', img)
cv2.waitKey(100)
cv2. line(img, (200,0), (700,700), (255,0,0), 3)
cv2.imshow('image', img)
cv2.waitKey(500)
cv2. line(img, (100,0), (100,700), (0,255,0), 3)
cv2.imshow('image', img)
cv2.waitKey(10)
cv2.rectangle(img, (700,500), (300,200), (0,100,0), cv2.FILLED)
cv2.imshow('image', img)
cv2.waitKey(300)
cv2.rectangle(img, (0,0), (300,200), (0,155,0), 5)
cv2.imshow('image', img)
cv2.waitKey(100)
cv2.circle(img, (300,200), 50, (145,0,200), 5)
cv2.putText(img, "SLAVSE!", (150,200), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255,255,255), 2)

cv2.imshow('image', img)
cv2. waitKey(0)