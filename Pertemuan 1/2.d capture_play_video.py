import cv2

# load video
cap = cv2.VideoCapture(0)
           
# iterate for each frame in video
while cap.isOpened():
    
    # get image on each frame
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (0,0), fx=0.125, fy=0.125)
    cv2.imshow('Frame',frame)

    # wait 25ms per frame and close using 'q' 
    if cv2.waitKey(25) == ord('q'):
          break


cap.release()
cv2.destroyAllWindows()