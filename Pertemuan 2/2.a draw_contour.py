import cv2

img = cv2.imread('hierarchy.png')

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find contour
contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# draw contours on image
for contour_item in contours:
    cv2.drawContours(img, contour_item, -1, (0, 255, 255), 3)

# show image
cv2.imshow('Draw Contour',img)
cv2.waitKey(0) # display the window infinitely until any keypress
cv2.destroyAllWindows()