import numpy as np
import cv2

img = cv2.imread('image.jpeg', cv2.IMREAD_COLOR)

copied = img[40:70, 100:150]

img[0:30, 0:50] = copied

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()