import cv2
import numpy as np
import random as rnd

def getContours(ing):
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgCountours, contours, -1, (255,0,0), 3, cv2.LINE_8, hierarchy)
            peri = cv2.arcLength(cnt, True)
            approx =cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y, w,h = cv2.boundingRect(approx)
            corner_count = len(approx)
            if corner_count == 3:
                object_type = 'Tri'
            elif corner_count == 4:
                side_ratio = w/float(h)
                if 0.98 < side_ratio < 1.03:
                    object_type = 'Kub'
                else: object_type = 'rect'
            elif corner_count == 8:
                object_type = 'Krug'
            else:
                object_type = 'None'
            cv2.rectangle(imgCountours, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(imgCountours, object_type, (x+w//2-10,y+h//2+10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,0,0), 2)


def thresh_callback(val):

    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    imgContours = np.zeros((imgCanny.shape[0], imgCanny.shape[1], 3), np.uint8)
    for i in range(len(contours)):
        color = (rnd.randint(0,256),rnd.randint(0,256),rnd.randint(0,256))
        cv2.drawContours(imgContours, contours, i, color, 2, cv2.LINE_8, hierarchy)
        cv2.imshow('imgContours', imgContours)



img: np.ndarray = cv2.imread('shapes.png', cv2.IMREAD_COLOR)
imgCountours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (11,11),1)
imgCanny = cv2.Canny(imgBlur, 150, 150)
getContours(imgCanny)
# создаем окно
# source_wind = 'source'
# cv2.namedWindow(source_wind)
# cv2.imshow(source_wind, img)
# max_thresh = 500
# thresh = 100
# trackbar = cv2.createTrackbar("Cann:", source_wind, thresh, max_thresh, thresh_callback)


cv2.imshow('imgCountours', imgCountours)
cv2.waitKey(0)

