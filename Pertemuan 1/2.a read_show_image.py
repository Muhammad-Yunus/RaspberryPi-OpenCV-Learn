import cv2

img = cv2.imread("lena.jpg") # read image from file `lena.jpg`

# show image
cv2.imshow('myapp',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()