#import libs for wroking with pictures and getting the histogram of it
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#read the image
img = cv2.imread('Q8.jpg',0)

#show the image
cv2.imshow('image',img)
