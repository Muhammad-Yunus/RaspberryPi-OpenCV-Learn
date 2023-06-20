import cv2
import numpy as np

import drawer 

dw = drawer.Drawer()

# define range of object color in HSV
lower = np.array([0, 7, 62])
upper = np.array([180, 30, 137])


img = cv2.imread('sample2-removebg-edited.png')
f = 320 / img.shape[1]
img = cv2.resize(img, (0,0), fx=f, fy=f)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv.copy(), lower, upper)
res = cv2.bitwise_and(img, img, mask= mask)


# find contour from mask image using RETR_EXTERNAL method
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# draw contour to the original image
# write bounding rectangle at position x,y
for contour_item in contours:
    
    x, y, w, h = cv2.boundingRect(contour_item)
    area = cv2.contourArea(contour_item)
    
    # calculate aspect_ratio & extent
    aspect_ratio = float(w)/h 
    rect_area = w*h
    extent = float(area)/rect_area

    
    # filter contour with aspect ratio and extend object
    if aspect_ratio < 3 and aspect_ratio > 1 and extent > 0.1 and  extent < 0.3 and area > 700:    

        # draw line and put text via drawer.py draw_distance
        img = dw.draw_distance(img, 0, y+h, x, y+h)

# draw line and put text via drawer.py draw cross line 
img = dw.draw_cross_line(img)

# show image
cv2.imshow('Draw Contour',img)
cv2.imshow('Threshold Image', res)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()        