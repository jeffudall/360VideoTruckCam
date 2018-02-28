# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 03:23:43 2018

@author: Etcyl
"""

# -*- coding: utf-8 -*-
# USAGE
# python realtime_stitching.py

# import the necessary packages
from imutils.video import VideoStream
import datetime
import imutils
import cv2
import numpy as np

H = np.matrix('0.7494203, 0.0063932, 118.9597; -0.156886, 0.9848, 2.9166; -0.000986577, 0.0002825271, 1')

# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
leftStream = VideoStream(0).start()
rightStream = VideoStream(1).start()
#second_right = VideoStream(2).start()


while True:
    imageB=leftStream.read()
    imageA=rightStream.read()
    #s_right=second_right.read()
    
    imageB=imutils.resize(imageB, width=400)
    imageA=imutils.resize(imageA, width=400)
    #s_right=imutils.resize(s_right, width=400)
    
    #result=stitcher.stitch([right, s_right])
    #result=stitcher.stitch([left, right])
    #result1=stitcher.stitch([left, result])
    #h_mtx = stitcher.H
    #B should be from the left frame
    result = cv2.warpPerspective(imageA, H,
			(imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
    result2 = cv2.warpPerspective(imageB, H,
			(imageB.shape[1] + imageA.shape[1], imageB.shape[0]))      
    result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
    if result is None:
        print("[INFO] homography could not be computed")
        break
    
    timestamp=datetime.datetime.now()
    ts=timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(result, ts, (10, result.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.putText(result2, ts, (10, result2.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
    cv2.imshow("Combined", result)
    cv2.imshow("Left frame", imageB)
    cv2.imshow("Right frame", imageA)
   # cv2.imshow("Second right frame", s_right)
    cv2.imshow("Warped left", result2)
    key = cv2.waitKey(1) & 0xFF
    
    if key==ord("q"):
        break
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
rightStream.stop()
#second_right.stop()
