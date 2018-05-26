# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:20:55 2018
Using a Keras CNN (Convolutional Neural Network) to identify cars in the image versus no cars in the image.
Version 2.0
@author: Etcyl
"""
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
#from sklearn.preprocessing import LabelBinarizer
#from keras.datasets import cifar10
import keras
import build_cnn
import random 
import cv2

IMAGE_WIDTH = 32
IMAGE_HEIGHT = 32
epochs = 5
batch_size = 32
set_size = 32
num_classes = 2

#Make a list of training data and class labels
data = []
labels = []

#Get image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)
"""

#Load and resize all of the images to be (32, 3)
for imagePath in imagePaths:
    img = cv2.imread(imagePath)
    img = cv2.resize(img, (IMAGE_WIDTH, IMAGE_HEIGHT))
    img = img_to_array(img)
    data.append(img)
    
    #Set the class label
    random_test_val = random.randint(0, 32) #Get a random image to train on 
    img_name = str(random_test_val) + '.jpg'
    #Get the label from the imagePath
    #label = imagePath.split(os.path.sep)[-2]
    labels.append(label)
    
cnn = build_cnn.buildCNN()
cnn.fit(x_train[0:set_size], y_train[0:set_size], batch_size=batch_size, epochs=epochs,
        validation_data=(x_test[0:set_size], y_test[0:set_size]), shuffle=True)

scores = cnn.evaluate(x_test[0:set_size], y_test[0:set_size], verbose=1)
print('Test accuracy:', scores[1])
"""
