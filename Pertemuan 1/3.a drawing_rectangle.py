import cv2

img = cv2.imread("lena.jpg") 

cv2.rectangle(img,              # input image
              (100,125),          # (x1, y1)
              (250,250),        # (x2, y2)
              (0,255,255),    # (B, G, R)
              -1)                # thickness

# show image
cv2.imshow('myapp',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()