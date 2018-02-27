# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:18:58 2018

Driver script for stitch.py (both) created by Adrian Rosebrock:
    
    https://www.pyimagesearch.com/2016/01/11/opencv-panorama-stitching/

@author: Etcyl
"""

# import the necessary packages
import stitch
import imutils
import cv2
 
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread('A.png')
imageB = cv2.imread('B.png')
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)
 
# stitch the images together to create a panorama
#stitcher = stitch.Stitcher()
#(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
 
# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
#cv2.imshow("Keypoint Matches", vis)
#cv2.imshow("Result", result)
#cv2.waitKey(0)