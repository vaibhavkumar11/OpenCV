import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
   _, frame = cap.read()
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   lower_limit = np.array([10, 100, 100])
   upper_limit = np.array([179, 255, 255])

   mask = cv2.inRange(hsv, lower_limit, upper_limit)
   res = cv2.bitwise_and(frame, frame, mask = mask)

   cv2.imshow('frame', frame)
   # cv2.imshow('hsv', hsv)
   cv2.imshow('mask', mask)
   cv2.imshow('res', res)

   k = cv2.waitKey(5) & 0xFF
   if k == 27 :
      break

cv2.destroyAllWindows()
cap.release()


