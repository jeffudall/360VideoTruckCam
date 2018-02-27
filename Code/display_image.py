# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:04:27 2018

@author: Etcyl
"""

import cv2
 
imageA = cv2.imread('ateam.png', 0) #Get the picture in gray-scale (0 is gray-scale)


# show the images
cv2.imshow("Image A", imageA) #Display it
cv2.waitKey(0) #Add this or your kernel will crash
cv2.destroyAllWindows() #Add this, or else your kernel will definitely crash
