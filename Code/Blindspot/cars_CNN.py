# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:20:55 2018

Using a Keras CNN (Convolutional Neural Network) to identify cars in the image versus no cars in the image.
Version 1.0

@author: Etcyl
"""

import build_cnn
import imutils
from keras.datasets import cifar10
import random 

set_size = 32

(x_train, y_train), (x_test, y_test) = cifar10.load_data() #Load dataset to store the new car images

#Load and resize all of the images to be (32, 3)
"""
for i in range(set_size):
    random_test_val = random.randint(1, 32)
    img = cv2.imread('1.jpg',3)
    img = imutils.resize(img, width=32)
    x_test[i] = 
    x_train[i] = 
    y_test[i] = 
    y_train[i] = 
"""

#(x_train, y_train), (x_test, y_test) = #Set the training and testing, in this case images of cars and image of the road


cnn = build_cnn.buildCNN()

"""
cnn.fit(x_train[0:1000], y_train[0:1000], batch_size=batch_size, epochs=epochs,
                  validation_data=(x_test[0:32], y_test[0:32]), shuffle=True)
            scores = cnn.evaluate(x_test[0:32], y_test[0:32], verbose=1)
 """