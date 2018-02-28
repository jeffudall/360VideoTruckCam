# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 06:08:22 2018

@author: Etcyl
"""

# import the necessary packages
from imutils.video import VideoStream
import cv2
import numpy as np

# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
leftStream = VideoStream(0).start()
rightStream = VideoStream(2).start()

# create constants and the "image" canvas
height = 1200*2
width = 1200*2
size = height
depth = width
channels = 3
x_offset=0
y_offset=50
y_offset2=50
x_offset2=600

image = np.zeros((height, width, 3), np.uint8)

# continuously loop over reading both video streams and stuff them into the canvas
while True:
    imageB=leftStream.read()
    imageC=rightStream.read()
    image[y_offset:y_offset+imageB.shape[0], x_offset:x_offset+imageB.shape[1]] = imageB
    image[y_offset2:y_offset2+imageC.shape[0], x_offset2:x_offset2+imageC.shape[1]] = imageC   
    cv2.imshow("Blank", image)
    key = cv2.waitKey(1) & 0xFF
    
    if key==ord("q"): # if the user presses "q" while looking at the canvas, then quit
        break
        
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
rightStream.stop()
