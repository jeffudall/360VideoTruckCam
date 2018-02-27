# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:39:00 2018

Modified real-time stitching from: https://www.pyimagesearch.com/2016/01/25/real-time-panorama-and-image-stitching-with-opencv/

@author: Etcyl
"""

# USAGE
# python realtime_stitching.py

# import the necessary packages
from __future__ import print_function
from pyimagesearch.basicmotiondetector import BasicMotionDetector
from pyimagesearch.panorama import Stitcher
from imutils.video import VideoStream
import datetime
import imutils
import cv2

# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
leftStream = VideoStream(1).start()
rightStream = VideoStream(0).start()
second_right = VideoStream(2).start()

# initialize the image stitcher, motion detector, and total
# number of frames read
stitcher = Stitcher()
motion = BasicMotionDetector(minArea=500)
total = 0

while True:
    left=leftStream.read()
    right=rightStream.read()
    s_right=second_right.read()
    
    left=imutils.resize(left, width=400)
    right=imutils.resize(right, width=400)
    s_right=imutils.resize(s_right, width=400)
    
    result=stitcher.stitch([right, s_right])
    #result0=stitcher.stitch([left, right])
    result1=stitcher.stitch([left, result])
    
    if result is None:
        print("[INFO] homography could not be computed")
        break
    
    timestamp=datetime.datetime.now()
    ts=timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(result, ts, (10, result.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.putText(result1, ts, (10, result1.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
    cv2.imshow("First result", result)
    cv2.imshow("Left frame", left)
    cv2.imshow("Right frame", right)
    cv2.imshow("Second right frame", s_right)
    cv2.imshow("Second result", result1)
    key = cv2.waitKey(1) & 0xFF
    
    if key==ord("q"):
        break
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
rightStream.stop()
second_right.stop()
