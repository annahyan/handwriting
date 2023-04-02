# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")




# import the necessary packages
from pyimagesearch.models import ResNet
from pyimagesearch.az_dataset import load_mnist_dataset
from pyimagesearch.az_dataset import load_az_dataset
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import build_montages
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-a", "--az", required=True,
	help="path to A-Z dataset")th
ap.add_argument("-m", "--model", type=str, required=True,
	help="path to output trained handwriting recognition model")
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output training history file")
args = vars(ap.parse_args())