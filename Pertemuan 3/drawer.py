import cv2 
import numpy as np

class Drawer :
    def draw_cross_line(self, img):
        h, w, c = img.shape
        cw = w // 2
        ch = h // 2

        # vertical line
        cv2.line(img, (cw, 0), (cw, h), (0, 255, 0), 1)

        # horizontal line
        cv2.line(img, (0, ch), (w, ch), (0, 255, 0), 1)

        return img

    def check_cross_line(self, img, x, y):
        h, w, c = img.shape
        cw = w // 2
        ch = h // 2


        if x >= 0 and x < cw and y >= 0 and y < ch : 
            return 0 # top left
        if x >= cw and x < w and y >= 0 and y < ch : 
            return 1 # top right
        if x >= 0 and x < cw and y >= ch and y < h : 
            return 2 # bottom left
        if x >= cw and x < w and y >= ch and y < h : 
            return 3 # bottom right

    def draw_distance(self, img, x0, y0, xt, yt):
        cx = (xt - x0) // 2
        cy = (yt - y0) // 2
        if cx == 0 : 
            cx = x0 
        if cy == 0 :
            cy = y0 

        text = str(max(cx, cy))

        shift_y = 0
        cl = self.check_cross_line(img, xt, yt)

        if cl == 1 or cl == 3 : 
            shift_y += 20

        (w, h), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1)
        cv2.rectangle(img,
                    (cx, cy - h - baseline - 5 + shift_y),  
                    (cx + w, cy + baseline - 5 + shift_y), 
                    (0,0,255), 
                    -1)
        cv2.putText(img, text, (cx,cy + shift_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1)
        cv2.line(img, (x0, y0 + shift_y), (xt, yt + shift_y), (0, 0, 255), 1)
        cv2.line(img, (x0, y0 - 5 + shift_y), (x0, y0 + 5 + shift_y), (0, 0, 255), 1)
        cv2.line(img, (xt, yt - 5 + shift_y), (xt, yt + 5 + shift_y), (0, 0, 255), 1)

        return img