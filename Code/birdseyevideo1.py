from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import imutils
import time
from rotate import rotate_bound
import cv2
from warp_matrix import find_points
from warp_matrix import four_point_transform

height = 1100
width = 800
size = height
depth = width
channels = 3
y_offset1 = 0
x_offset1 = 50
y_offset2 = 250
x_offset2 = 300
y_offset3 = 250
x_offset3 = 0
y_offset4 = 700
x_offset4 = 50


imageCanvas = np.zeros((height, width, channels), np.uint8)

Stream0 = VideoStream(3).start()
Stream1 = VideoStream(1).start()
Stream2 = VideoStream(2).start()
Stream3 = VideoStream(4).start()
time.sleep(2.0)

streamL = Stream0.read()
streamF = Stream1.read()
streamR = Stream2.read()
streamB = Stream3.read()

streamL = imutils.resize(streamL, width=400) 
streamF = imutils.resize(streamF, width=400)
streamR = imutils.resize(streamR, width=400)
streamB = imutils.resize(streamB, width=400)

screenCntL = find_points(streamL)
screenCntF = find_points(streamF)
screenCntR = find_points(streamR)
screenCntB = find_points(streamB)

ML = four_point_transform(streamL, screenCntL.reshape(4, 2))
MF = four_point_transform(streamF, screenCntF.reshape(4, 2))
MR = four_point_transform(streamR, screenCntR.reshape(4, 2))
MB = four_point_transform(streamB, screenCntB.reshape(4, 2))

while True:
    streamL = Stream0.read()
    streamF = Stream1.read()
    streamR = Stream2.read()
    streamB = Stream3.read()
    
    streamL = imutils.resize(streamL, width=400) 
    streamF = imutils.resize(streamF, width=400)
    streamR = imutils.resize(streamR, width=400)
    streamB = imutils.resize(streamB, width=400)
    
    warpedL = cv2.warpPerspective(streamL, ML, (600, 400))
    warpedF = cv2.warpPerspective(streamF, MF, (600, 400))
    warpedR = cv2.warpPerspective(streamR, MR, (600, 400))
    warpedB = cv2.warpPerspective(streamB, MB, (600, 400))
    
    warpedL_R = rotate_bound(warpedL,90)
    warpedR_L = rotate_bound(warpedR,270)
    warpedB_B = rotate_bound(warpedB,180)
    
    imageCanvas[y_offset1:y_offset1+warpedF.shape[0], x_offset1:x_offset1+warpedF.shape[1]] = warpedF
    imageCanvas[y_offset2:y_offset2+warpedL_R.shape[0], x_offset2:x_offset2+warpedL_R.shape[1]] = warpedL_R
    imageCanvas[y_offset3:y_offset3+warpedR_L.shape[0], x_offset3:x_offset3+warpedR_L.shape[1]] = warpedR_L
    imageCanvas[y_offset4:y_offset4+warpedB_B.shape[0], x_offset4:x_offset4+warpedB_B.shape[1]] = warpedB_B
    
    cv2.imshow("Birds Eye", imageCanvas)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()