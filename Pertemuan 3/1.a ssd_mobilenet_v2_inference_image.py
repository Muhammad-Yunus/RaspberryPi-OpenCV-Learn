import cv2
import numpy as np
import os
import utils 
import coco
utility = utils.Utils()

# load class name
classNames = coco.load_coco_class_names_tf()

# load model
model = "model/ssd_mobilenet_v2_coco_2018_03_29.pb"
config = "model/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
net = cv2.dnn.readNet(model, config)

# setup opencv dnn
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
layerOutput = net.getUnconnectedOutLayersNames()

# load image
img = cv2.imread("image1.jpg")

# convert to blob
resize_h, resize_w = 300, 300 
blob = cv2.dnn.blobFromImage(img, 1.0, (resize_w, resize_h), (0, 0, 0), swapRB=True, crop=True)

# do a forward pass
net.setInput(blob)
output = net.forward(layerOutput)

# postprocessing (draw detection box)
img = utility.postprocessTensorflow(output, img, classNames, font_size=0.8)

# display results
cv2.imshow("detection result", img)
cv2.waitKey()
cv2.destroyAllWindows()