# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 21:49:25 2018

Function for classifying an image, given a model, and the label binarizer. 

Uses modified source code: https://www.pyimagesearch.com/2018/04/16/keras-and-convolutional-neural-networks-cnns/
@author: Etcyl
"""
# import the necessary packages
from keras.preprocessing.image import img_to_array
import numpy as np
import cv2

def blindspotDetect(model, image, lb):
    # pre-process the image for classification
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # classify the input image
    print("[INFO] classifying image...")
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    return label
