# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:20:55 2018
Using a Keras CNN (Convolutional Neural Network) to identify cars in the image versus no cars in the image.
Version 2.0
@author: Etcyl
"""
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
#rom sklearn.preprocessing import LabelBinarizer
#from keras.datasets import cifar10
import keras
import build_cnn
import random 
import cv2

IMAGE_WIDTH = 32
IMAGE_HEIGHT = 32
EPOCHS = 5
BATCH_SIZE = 32
SET_SIZE = 32
NUM_CLASSES = 2 #Change this to 2 when y_test and y_train are made separately from the cifar10 labels

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

#Scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

#Binarize the labels
lb = LabelBinarizer()
labels = lb.fit_transform(labels)

#Partition the data into training and testing splits using 80% of
#the data for training and the remaining 20% for testing
(trainX, testX, trainY, testY) = train_test_split(data,
    labels, test_size = 0.2, random_state = 42)

#Create the image generator for data augmentation
aug = ImageDataGenerator(rotation_range = 25, width_shift_range = 0.1,
    height_shift_range = 0.1, shear_range = 0.2, zoom_range = 0.2,
    horizontal_flip = True, fill_mode = "nearest")



cnn = build_cnn.buildCNN()
cnn.fit_generator(aug.flow(trainX, trainY, batch_size = BATCH_SIZE),
                  validation_data = (testX, testY),
                  steps_per_epoch = len(trainX) // BATCH_SIZE
                  epochs = EPOCHS, verbose = 1)

#Save the model to disk
print("Serializing network. . . ")
cnn.save(args["cnn"])

#Save the label binarizer to disk
print("Serializing label binarizer. . . ")
f = open(args["labelbin"], "wb")
f.write(pickle.dumps(lb))
f.close()

#Plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
N = EPOCHS
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="upper left")
plt.savefig(args["plot"])
"""
