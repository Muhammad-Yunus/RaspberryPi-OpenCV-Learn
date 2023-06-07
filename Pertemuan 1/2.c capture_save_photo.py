import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if ret :
    cv2.imwrite("my_photo.jpg", frame)
else :
    print("can't save photo")
    
cap.release()