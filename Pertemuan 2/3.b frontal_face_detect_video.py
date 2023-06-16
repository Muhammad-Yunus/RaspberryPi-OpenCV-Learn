import cv2 

# load model haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # resize image to width ~ 320px
    w = frame.shape[1] 
    f = 320 / w 
    frame = cv2.resize(frame, (0,0), fx=f, fy=f)

    # conver to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect face on gray image
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        # draw rectangle on detected face coordinate
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        
    cv2.imshow('Detect Face', frame)
    if cv2.waitKey(25) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()