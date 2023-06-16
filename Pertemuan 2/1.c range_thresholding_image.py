import cv2 
import numpy as np 

# define range of blue color in HSV
lower = np.array([110, 50, 50])
upper = np.array([130, 255, 255])

img = cv2.imread('blocks.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv.copy(), lower, upper)
res = cv2.bitwise_and(img, img, mask= mask)

cv2.imshow('frame',img)
cv2.imshow('res',res)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()