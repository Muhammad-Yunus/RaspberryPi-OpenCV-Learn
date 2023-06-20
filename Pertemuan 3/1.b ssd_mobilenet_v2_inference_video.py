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

# load video
cap = cv2.VideoCapture(1)
           
# iterate for each frame in video
while cap.isOpened():
    
    # get image on each frame
    ret, frame = cap.read()
    if not ret:
        break

    # resize original frame to max 300 x 300
    frame = cv2.resize(frame, (300,300))

    # convert to blob
    resize_h, resize_w = 300, 300 
    blob = cv2.dnn.blobFromImage(frame, 1.0, (resize_w, resize_h), (0, 0, 0), swapRB=True, crop=False)

    # do a forward pass
    net.setInput(blob)
    output = net.forward(layerOutput)

    # postprocessing (draw detection box)
    frame = utility.postprocessTensorflow(output, frame, classNames, font_size=0.3)

    # resize processed frame to max 320 x 240
    frame = cv2.resize(frame, (320,240))

    cv2.imshow('Frame',frame)

    # wait 1ms per frame and close using 'q' 
    if cv2.waitKey(1) == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()