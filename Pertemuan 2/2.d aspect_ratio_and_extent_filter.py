import cv2
import numpy as np

# define range of green box in object_sample.png
lower = np.array([32, 0, 0])
upper = np.array([71, 255, 255])

img = cv2.imread('object_sample.png')

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

    
    # filter contour with aspect ratio less than 1 and more than 0.1 
    # and extent greater than 0.4 (rejecting long contour with small filled area)
    # area more than 200 pixel (rejecting small contour)
    if aspect_ratio < 2 and aspect_ratio > 1 and extent > 0.7 and area > 1500:
        
        cv2.drawContours(img, contour_item, -1, (0,255,255), 1)
        
        text = "(%d, %d, %d, %d)" % (x, y, w, h)
        cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1)

        cv2.rectangle(img,              # input image
            (x, y),               # (x1, y1)
            (x + w, y + h),       # (x2, y2)
            (0,0,255),            # (B, G, R)
            2)                   # thickness
        print ("aspect ratio : %.2f, extent : %.2f, area : %.2f" % (aspect_ratio, extent, area))

# show image
cv2.imshow('Draw Contour',img)
cv2.imshow('Threshold Image', res)
cv2.waitKey(0) # display the window infinitely until any keypresource/s
cv2.destroyAllWindows()        