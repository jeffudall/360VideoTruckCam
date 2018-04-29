# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:34:11 2018

Test program for demonstrating "saving" (i.e. saving) the camera positions.

@author: etcyl
"""

import pickle

#Create empty lists to store the (x, y, theta) values for each 
#of the six cams
cam_positions = [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]

#Create the filename to save the pickled data
filename = 'cam_pos.p'
#Pickle the data
pickle.dump(cam_positions, open(filename, 'wb'))
#Load the data as an arbitrary structure named "x":
#x = pickle.load( open(filename, "rb" ))
