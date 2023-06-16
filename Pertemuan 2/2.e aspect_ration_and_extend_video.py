import cv2 
import numpy as np 

# define range of blue color in HSV
lower = np.array([88, 194, 62])
upper = np.array([124, 255, 199])

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # resize image to width ~ 320px
    w = frame.shape[1] 
    f = 320 / w 
    frame = cv2.resize(frame, (0,0), fx=f, fy=f)

    # apply range thresholding
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv.copy(), lower, upper)
    res = cv2.bitwise_and(frame, frame, mask= mask)

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
        if aspect_ratio < 1.5 and aspect_ratio > 0.5 and extent > 0.3 and area > 500:
            
            text = "(%d, %d, %d, %d)" % (x, y, w, h)
            cv2.putText(frame, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,0), 1)

            cv2.rectangle(frame,        # input image
                (x, y),               # (x1, y1)
                (x + w, y + h),       # (x2, y2)
                (0,0,255),            # (B, G, R)
                2)                    # thickness
            print ("aspect ratio : %.2f, extent : %.2f, area : %.2f" % (aspect_ratio, extent, area))

    cv2.imshow('Original Image', frame)
    cv2.imshow('Result Image', res)
    
    if cv2.waitKey(25) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()