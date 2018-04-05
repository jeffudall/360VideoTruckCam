from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import imutils
import time
from rotate import rotate_bound
import cv2
from warp_matrix import find_points
from warp_matrix import four_point_transform
#
Stream0 = VideoStream(3).start()
Stream3 = VideoStream(4).start()
time.sleep(2.0)

#stitcher = Stitcher()
total = 0

streamL = Stream0.read()
streamB = Stream3.read()

streamL = imutils.resize(streamL, width=400) 
streamB = imutils.resize(streamB, width=400)

screenCntL = find_points(streamL)
screenCntB = find_points(streamB)

ML = four_point_transform(streamL, screenCntL.reshape(4, 2))
MB = four_point_transform(streamB, screenCntB.reshape(4, 2))

while True:
    streamL = Stream0.read()
    streamB = Stream3.read()
    
    streamL = imutils.resize(streamL, width=400) 
    streamB = imutils.resize(streamB, width=400)
    
    warpedL = cv2.warpPerspective(streamL, ML, (600, 400))
    warpedB = cv2.warpPerspective(streamB, MB, (600, 400))
    
    warpedL_R = rotate_bound(warpedL,90)
    warpedB_B = rotate_bound(warpedB,180)
    
    #result = stitcher.stitch([warpedL_R, warpedB_B])

  #  stitcher = cv2.createStitcher(False)
    #result = stitcher.stitch((warpedL_R,warpedB_B))

    cv2.imshow("Right", warpedL_R)
    cv2.imshow("Back", warpedB_B)
  #  cv2.imshow("Result", result)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()