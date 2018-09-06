import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
   _, frame = cap.read()
   
   laplacian = cv2.Laplacian(frame, cv2.CV_64F)
   sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
   sobely = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)

   cv2.imshow('frame', frame)
   cv2.imshow('laplacian', laplacian)
   cv2.imshow('sobelx', sobelx)
   cv2.imshow('sobely', sobely)

   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break
   
cv2.destroyAllWindows()
cap.release()

# img = cv2.imread('download.jpg')

# laplacian = cv2.Laplacian(img, cv2.CV_64F)

# cv2.imshow('image', laplacian)

# cv2.waitKey(0)
# cv2.destroyAllWindows()