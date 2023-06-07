import cv2

# load video source
cap = cv2.VideoCapture('video.mp4')
           
# iterate for each frame in video
while cap.isOpened():
    
    # get image on each frame
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Frame',frame)

    # wait 25ms per frame and close using 'q' 
    if cv2.waitKey(25) == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()