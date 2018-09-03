import numpy as np
import cv2


img1 = cv2.imread('download.jpg')
img2 = cv2.imread('image.jpeg')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2_gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

# cv2.imshow('image1', img1)
# cv2.imshow('image2', img2)
# cv2.imshow('grayscale_image', img2_gray)
# cv2.imshow('masked_image', mask)
# cv2.imshow('inv_masked_image', mask_inv)
# cv2.imshow('img1_bg', img1_bg)
# cv2.imshow('img2_fg', img2_fg)
# cv2.imshow('image_total', dst)
cv2.imshow('image', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()