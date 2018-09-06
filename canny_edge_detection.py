import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
   _, frame = cap.read()
   
   edge = cv2.Canny(frame, 10, 200)

   cv2.imshow('frame', frame)
   cv2.imshow('edges', edge)

   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break
   
cv2.destroyAllWindows()
cap.release()

