# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 01:20:40 2018

@author: Etcyl
"""

from keras.preprocessing.image import img_to_array
from imutils.video import VideoStream
from keras.models import load_model
import numpy as np
import pickle
import imutils
import cv2

#load the model and label binarizer
print("[INFO] loading network...")
model = load_model("model")
lb = pickle.loads(open("labelbin", "rb").read())

bbox = (287, 23, 86, 320)
p1 = (int(bbox[0]), int(bbox[1]))
p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))

#load the camera stream (only 1 camera for this demo, but more could be used)
cam = VideoStream(0).start() 

while(True):
    image = cam.read()
    output = image.copy()
    # pre-process the image for classification
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # classify the input image
    print("[INFO] classifying image...")
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    # we'll mark our prediction as "correct" of the input image filename
    # contains the predicted label text (obviously this makes the
    # assumption that you have named your testing image files this way)
    # build the label and draw the label on the image
    if label == "truck" or label == "car":
        cv2.rectangle(output, p1, p2, (255,0,0), 2, 1)
    output = imutils.resize(output, width=400)
    cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
                	0.7, (0, 255, 0), 2)
    # show the output image
    print("Class detected {}".format(label))
    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF 
    if key==ord("q"):
        break
    
cv2.destroyAllWindows()
cam.stop()
