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

   kernel = np.ones((15, 15), np.float32)/225
   # Homogeneous Filter, -1, kernel
   homo_blur = cv2.filter2D(res, -1, kernel)
   # Median filter
   median_blur = cv2.medianBlur(res, 15)
   # Gaussian Blur
   gaussian_blur = cv2.GaussianBlur(res, (15, 15), 0)
   # Bilateral Blur
   bilateral_blur = cv2.bilateralFilter(res, 9, 75, 75)

   # cv2.imshow('frame', frame)
   # cv2.imshow('hsv', hsv)
   # cv2.imshow('mask', mask)
   # cv2.imshow('res', res)
   cv2.imshow('homo_blur', homo_blur)
   cv2.imshow('median_blur', median_blur)
   cv2.imshow('gaussian_blur', gaussian_blur)
   cv2.imshow('bilateral_blur', bilateral_blur)

   k = cv2.waitKey(5) & 0xFF
   if k == 27 :
      break

cv2.destroyAllWindows()
cap.release()


