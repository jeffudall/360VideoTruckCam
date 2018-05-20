# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:20:55 2018

Using a Keras CNN (Convolutional Neural Network) to identify cars in the image versus no cars in the image.
Version 2.0

@author: Etcyl
"""

import build_cnn
import keras
from keras.datasets import cifar10
import random 

set_size = 32 #How many images are in the dataset
num_classes = 10 #Change this to 2 when y_test and y_train are made separately from the cifar10 labels
(x_train, y_train), (x_test, y_test) = cifar10.load_data() #Datastructure for all of the images

#Convert class vectors to binary class matrices
#E.G. 3 --> 0011, assuming 4 total labels (cars, no cars, pedestrian, bike, etc.)
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

#Load and resize all of the images to be (32, 3)
"""
for i in range(set_size):
    img_name = str(i) + '.jpg' #Current for-loop value of i plus a .jpg label creates the (saved) image name
    random_test_val = random.randint(1, 32) #Get a random image to train on on the interval [1, 32]
    img = cv2.imread(img_name, 3) #Read the current image into variable img
    img = cv2.resize(img, (32, 32)) #Resize to the shape of the expected CNN, in this case 32, 32
    #Change the old x_train and y_train CIFAR-10 images to the newly created images
    x_train[i] =  
    y_train[i] = 
    
    #Set the test data
    img_name = str(random_test_val) + '.jpg'
    img = cv2.imread(img_name, 3)
    img = cv2.resize(img, (32, 32))
    x_test[i] =
    y_test[i] = 

#Make a CNN using the buildCNN() function
cnn = build_cnn.buildCNN()

#Train the CNN using the training and testing data
cnn.fit(x_train[0:1000], y_train[0:1000], batch_size=batch_size, epochs=epochs,
                  validation_data=(x_test[0:32], y_test[0:32]), shuffle=True)
            scores = cnn.evaluate(x_test[0:32], y_test[0:32], verbose=1)
 """
