#import libs for wroking with pictures and getting the histogram of it
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#read the image
#load the image from images folder
img = cv2.imread('images/1.jpg',0)

#display it
plt.imshow(img, cmap = 'gray')