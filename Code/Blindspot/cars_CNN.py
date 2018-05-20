# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:20:55 2018

Using a Keras CNN (Convolutional Neural Network) to identify cars in the image versus no cars in the image.
Version 1.0

@author: Etcyl
"""

import build_cnn
from keras.datasets import cifar10
import random 

set_size = 32

(x_train, y_train), (x_test, y_test) = cifar10.load_data() #Datastructure for all of the images

#Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
        
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

#Load and resize all of the images to be (32, 3)
"""
for i in range(set_size):
    #Set the training data
    img_name = str(i) + '.jpg'
    random_test_val = random.randint(1, 32) #Get a random image to train on 
    img = cv2.imread(img_name, 3)
    img = cv2.resize(img, (32, 32))
    x_train[i] =  
    y_train[i] = 
    
    #Set the test data
    img_name = str(random_test_val) + '.jpg'
    img = cv2.imread(img_name, 3)
    img = cv2.resize(img, (32, 32))
    x_test[i] =
    y_test[i] = 
"""

cnn = build_cnn.buildCNN()

"""
cnn.fit(x_train[0:1000], y_train[0:1000], batch_size=batch_size, epochs=epochs,
                  validation_data=(x_test[0:32], y_test[0:32]), shuffle=True)
            scores = cnn.evaluate(x_test[0:32], y_test[0:32], verbose=1)
 """
