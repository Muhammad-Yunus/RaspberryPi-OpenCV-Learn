import cv2
import numpy as np
import os
import utils 
import coco
utility = utils.Utils()

# load class name
classNames = coco.load_coco_class_names_yolo()

# load model
model = "model/yolov3-tiny.weights"
config = "model/yolov3-tiny.cfg"
net = cv2.dnn.readNet(model, config)

# setup opencv dnn
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
layerOutput = net.getUnconnectedOutLayersNames()

# load image
img = cv2.imread("image1.jpg")

# convert to blob
resize_h, resize_w = 416, 416 
blob = cv2.dnn.blobFromImage(img, 1/255.0, (resize_w, resize_h), (0, 0, 0), swapRB=True, crop=True)

# do a forward pass
net.setInput(blob)
output = net.forward(layerOutput)

# postprocessing (draw detection box)
img = utility.postprocessYolo(output, img, classNames, font_size=0.8)

# display results
cv2.imshow("detection result", img)
cv2.waitKey()
cv2.destroyAllWindows()