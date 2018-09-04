import numpy as np
import cv2

img = cv2.imread('bookpage.jpg')

retval, colored = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval , thres_gray = cv2.threshold(grayscaled, 9, 255, cv2.THRESH_BINARY)

thres_adaptive_mean = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 1)
thres_adaptive_gaussian = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 1) #Great Results

retval2,threshold_otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original', img)
# cv2.imshow('colored', colored)
# cv2.imshow('grayscaled', grayscaled)
# cv2.imshow('gray_thres', thres_gray)
# cv2.imshow('adaptive_mean', thres_adaptive_mean)
cv2.imshow('adaptive_gaussian', thres_adaptive_gaussian)
# cv2.imshow('otsu_threshold', threshold_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()