# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:48:03 2018

@author: etcyl
"""

def boundary_check(x_val, y_val, canvas_x, canvas_y):
    if(x_val < 0):
        print("Error: x_val is less than canvas_x")
        return 0
    elif(y_val < 0):
        print("Error: y_val is less than canvas_y")
        return 0
    elif(x_val > canvas_x):
        print("Error: x_val is greater than canvas_x")
        return 0
    elif(y_val > canvas_y):
        print("Error: y_val is greater than canvas_y")
        return 0
    else:
        print("Coordinates OK")
        return 1
