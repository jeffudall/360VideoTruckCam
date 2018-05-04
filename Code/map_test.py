# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:57:46 2018

Test program for mapping one interval of values onto another interval.
The Arduino reads analog values from [0, 1023], and our desired output mapping is [-90, 90]
because it is ideal for our image output in terms of rotating the image left or right.

@author: etcyl
"""

from scipy.interpolate import interp1d as intp

#Create the data structure to store the input-output mapping from [0, 1023] onto [-90, 90].
sens_to_angle = intp([0, 1023], [-90, 90])

"""
Example function call:

current_value = (...) #get the current value for the kink angle sensor

sens_to_angle(current_value) #get the mapped value (onto [-90, 90])

Example 1: Current kink angle sensor value, read from the Arduino, is equal to 0

>>sens_to_angle(0) 
>>array(-90.)

Example 2: Sensor value is 511

>>sens_to_angle(511) 
>>array(-0.08797654)
"""
