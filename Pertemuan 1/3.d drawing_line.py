import cv2 

img = cv2.imread("lena.jpg") 

#  horizontal line (red), y0 = yt
cv2.line(img,  # input image matrix
         (100, 150),  # (x1, y1)
         (190, 250),  # (x2, y2)    
         (50,0,255),  # (B, G, R)   
         2, # thickness 
         cv2.LINE_AA)           

# show image
cv2.imshow('myapp', img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()