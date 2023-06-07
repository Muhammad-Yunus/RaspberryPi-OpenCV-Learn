import cv2

img = cv2.imread("lena.jpg") 

cv2.putText(img, 
            "Hello world", 
            (50, 50),                   
            cv2.FONT_HERSHEY_SIMPLEX,     
            1.5,                          
            (0, 255, 127),                
            1,
            cv2.LINE_AA) 

# show image
cv2.imshow('myapp',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()