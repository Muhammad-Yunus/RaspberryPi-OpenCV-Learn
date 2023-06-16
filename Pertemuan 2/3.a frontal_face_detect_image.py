import cv2 

# load model haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread("people.jpg")

# conver to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect face on gray image
faces = face_cascade.detectMultiScale(gray, 1.7, 5)

for (x,y,w,h) in faces:
    # draw rectangle on detected face coordinate
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()