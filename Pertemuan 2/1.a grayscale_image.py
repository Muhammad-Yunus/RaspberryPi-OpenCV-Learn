import cv2

# convert BGR to Gray
img = cv2.imread("lena.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show image
cv2.imshow('myapp',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()