import cv2
import utils

img = cv2.imread('lena.jpg')

# draw_ped(image, label, x0, y0, x1, y1)
img = utils.draw_ped(img, "name : lena.jpg", 50, 50, 300, 300, color=(0, 0, 255), text_color=(0,0,0))

# show image
cv2.imshow('myapp',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()