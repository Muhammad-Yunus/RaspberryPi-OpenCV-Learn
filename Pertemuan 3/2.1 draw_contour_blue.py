import cv2
import numpy as np

# define range of blue color in HSV
lower = np.array([96, 83, 89])
upper = np.array([117, 255, 255])


img = cv2.imread('sample2-removebg.png')
f = 320 / img.shape[1]
img = cv2.resize(img, (0,0), fx=f, fy=f)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv.copy(), lower, upper)
res = cv2.bitwise_and(img, img, mask= mask)

# find contour from mask image using RETR_EXTERNAL method
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# draw contour to the original image
for contour_item in contours:
    cv2.drawContours(img, contour_item, -1, (0, 0, 255), 2)

# show image
cv2.imshow('Draw Contour',img)
cv2.imshow('Threshold Image', res)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()