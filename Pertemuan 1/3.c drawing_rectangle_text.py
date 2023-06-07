import cv2
import draw_ped from untils

img = cv2.imread('lena.jpg')

# draw_ped(image, label, x0, y0, x1, y1)
img = draw_ped(img, "name : lena.jpg", 50, 50, 300, 300)

# show image
cv2.imshow('myapp',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()