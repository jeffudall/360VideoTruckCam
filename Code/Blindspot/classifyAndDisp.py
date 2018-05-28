# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:52:47 2018

Function for classifying an image, given a model, the label binarizer, and the
class name (fn). 

Uses modified source code: https://www.pyimagesearch.com/2018/04/16/keras-and-convolutional-neural-networks-cnns/

@author: Etcyl
"""
# import the necessary packages
from keras.preprocessing.image import img_to_array
import numpy as np
import imutils
import cv2

def classifyAndDisp(model, image, lb, fn):
    output = image.copy()
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
    # we'll mark our prediction as "correct" of the input image filename
    # contains the predicted label text (obviously this makes the
    # assumption that you have named your testing image files this way)
    filename = fn
    correct = "correct" if filename.rfind(label) != -1 else "incorrect"
    # build the label and draw the label on the image
    label = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, correct)
    output = imutils.resize(output, width=400)
    cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
                	0.7, (0, 255, 0), 2)
    # show the output image
    print("[INFO] {}".format(label))
    cv2.imshow("Output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
