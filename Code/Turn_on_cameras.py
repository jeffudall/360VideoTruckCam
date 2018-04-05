# import the necessary packages
from __future__ import print_function
from pyimagesearch.basicmotiondetector import BasicMotionDetector
from pyimagesearch.panorama import Stitcher
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
leftStream = VideoStream(2).start()
rightStream = VideoStream(3).start()
backStream = VideoStream(4).start()
frontStream = VideoStream(1).start()

time.sleep(2.0)

total = 0

while True:
    right = rightStream.read()
    left = leftStream.read()
    back = backStream.read()
    front = frontStream.read()


    left = imutils.resize(left, width=400)
    right = imutils.resize(right, width=400)
    back = imutils.resize(back, width=400)
    front = imutils.resize(front, width=400)

    cv2.imshow("Left Frame", left)
    cv2.imshow("Right Frame", right)
    cv2.imshow("Back Frame", back)
    cv2.imshow("Front Frame", front)

    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break

print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
rightStream.stop()