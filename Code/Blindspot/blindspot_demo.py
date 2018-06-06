# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:03:49 2018

Demo script for the blindspot object detection software.
Some source code modified from: https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/

@author: Etcyl
"""
from imutils.video import VideoStream
from keras.models import load_model
from blindspot_detect import *
import pickle
import time
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
time.sleep(2) #Wait 2 seconds for the cam to warm up

while True:
    img = cam.read()
    label = blindspotDetect(img, model, lb)
    if label == "truck" or label == "car":
        cv2.rectangle(img, p1, p2, (255,0,0), 2, 1)
    cv2.imshow("Classifier frame", img)
    key = cv2.waitKey(1) & 0xFF 
    if key==ord("q"):
        break
    
cv2.destroyAllWindows()
cam.stop()
