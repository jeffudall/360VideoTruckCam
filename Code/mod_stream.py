# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:32:23 2018

@author: etcyl
"""

#Stream is the video stream, x_ and y_val are the canvas constants 
def mod_stream_vals(stream, x_val, y_val): 
    direction = [0, 0]
    direction[0] = x_val
    direction[1] = y_val
    cont = True
    while(cont):
        position = input("Enter A for left, D for right, W for up, S for down:")
        print("Old X direction is: ", direction[0], "Old Y direction is: ", direction[1])
        if(position == "W" or position == "w"): #Go up
            direction[1] += 1
        elif(position == "S" or position == "s"): #Go down
            direction[1] -= 1
        elif(position == "A" or position == "a"): #Go left
            direction[0] -= 1
        elif(position == "D" or position == "d"): #Go right
            direction[0] += 1
        else:
            print("Error, invalid position value.")
        
        print("Detected position is: ", position)
        print("New X direction is: ", direction[0], "New Y direction is: ", direction[1])
        cont = input("Enter Y to continue, N to quit:")
        if (cont == "Y" or cont == "y"):
            cont = True
        elif(cont == "N" or cont == "n"):
            cont = False
        else:
            print("Error: invalid input, halting program execution.")
            return -1
    new_x = direction[0]
    new_y = direction[1]
    return (new_x, new_y)
