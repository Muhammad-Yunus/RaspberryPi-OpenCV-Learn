import cv2

img = cv2.imread("lena.jpg") 

cv2.rectangle(img,              # input image
              (15,25),          # (x1, y1)
              (200,150),        # (x2, y2)
              (255,255,255),    # (B, G, R)
              3)                # thickness

# show image
cv2.imshow('myapp',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()