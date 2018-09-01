import numpy as np
import cv2

img = cv2.imread('image.jpeg', cv2.IMREAD_COLOR)

# Normal operations on images
cv2.line(img, (0,0), (50,100), (0,0,0), 10)
cv2.rectangle(img, (40,70), (200,300), (255,0,0), 8)
cv2.circle(img, (45,75), 20, (0,0,255), -1)

# Polygon over image
pts = np.array([[10,15], [28,17], [43,33], [79,61]])
cv2.polylines(img, [pts], True, (0,255,255), 7)

# Font over image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Tutorial', (0,120) ,font, 1, (0, 0, 0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()