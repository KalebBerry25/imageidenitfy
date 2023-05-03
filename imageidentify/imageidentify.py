# import necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
import cv2
import numpy as np


def identify_image(img_path):
	# load pre-trained InceptionV3 model
	model = InceptionV3(weights='imagenet')

	# load image and preprocess data
	img = cv2.imread(img_path)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img = cv2.resize(img, (299, 299))
	img = np.expand_dims(img, axis=0)
	img = preprocess_input(img)

	# make prediction using InceptionV3 model
	preds = model.predict(img)
	preds_decoded = decode_predictions(preds, top=1)[0][0]
	return preds_decoded

def final_description(preds_decoded):
	final = preds_decoded[1]
	final = final.replace("_", " ")
	return "Image contains a " + final + "."



