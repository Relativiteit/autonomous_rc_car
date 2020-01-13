import cv2
import numpy as np

#number gives 1 if you use a webcam 0 if it is built in
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # hue saturation value, different way to represent colours
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #defining upper and lower yellow, first digit determines hue, to have a different colour use a different range for upper and lower
    lower_yellow = np.array([10, 100, 100])
    upper_yellow = np.array([60, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res,(15,15), 0)
    median = cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res )
    #cv2.imshow('smoothed', smoothed)
    #cv2.imshow('blur', blur)
    #cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
#release webcam or it cannot be used in other applications

cap.release()



