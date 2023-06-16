import cv2 
import numpy as np 

# define range of blue color in HSV
lower = np.array([110, 50, 50])
upper = np.array([130, 255, 255])

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

    cv2.imshow('Original Image', frame)
    cv2.imshow('Result Image', res)
    cv2.imshow('Mask Image', mask)
    
    if cv2.waitKey(25) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()