import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
   vid, frame = cap.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   cv2.imshow('frame', frame)
   cv2.imshow('gray', gray)
   cv2.imshow('hsv', hsv)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()