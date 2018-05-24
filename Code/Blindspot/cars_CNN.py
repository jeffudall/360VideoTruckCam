# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:20:55 2018

Using a Keras CNN (Convolutional Neural Network) to identify cars in the image versus no cars in the image.
Version 2.0

@author: Etcyl
"""
#from sklearn.model_selection import train_test_split
#from keras.preprocessing.image import img_to_array
#from sklearn.preprocessing import LabelBinarizer
from keras.datasets import cifar10
import keras
import build_cnn
import random 
import cv2

epochs = 5
batch_size = 32
set_size = 32
num_classes = 10 #Change this to 2 when y_test and y_train are made separately from the cifar10 labels
(x_train, y_train), (x_test, y_test) = cifar10.load_data() #Datastructure for all of the images

#Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

#Adjust the dataset to be in the category [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#This should be done with LabelBinarizer()
for i in range(32):
    y_train[i] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_test[i] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
#Load and resize all of the images to be (32, 3)
#Use img_to_array() for this after resizing, then append to the training data list
for i in range(set_size):
    #Set the training data
    img_name = str(i) + '.jpg'
    img = cv2.imread(img_name, 3)
    img = cv2.resize(img, (32, 32))
    x_train[i] =  img
    
    #Set the test data
    random_test_val = random.randint(0, 32) #Get a random image to train on 
    img_name = str(random_test_val) + '.jpg'
    img = cv2.imread(img_name, 3)
    img = cv2.resize(img, (32, 32))
    x_test[i] = img

cnn = build_cnn.buildCNN()
cnn.fit(x_train[0:set_size], y_train[0:set_size], batch_size=batch_size, epochs=epochs,
        validation_data=(x_test[0:set_size], y_test[0:set_size]), shuffle=True)

scores = cnn.evaluate(x_test[0:set_size], y_test[0:set_size], verbose=1)
print('Test accuracy:', scores[1])
