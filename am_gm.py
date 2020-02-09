# Apply Arithmetic mean and Geometric Mean Filter to Gaussian noise image

import matplotlib.pyplot as plt 
import numpy as np 
from my_modules import mean_filter, gaussian_noise
import cv2

path = '/home/habray/Image_Processing/Working_Folder/image/'
img = plt.imread(path + 'guss_noise.jpg')

#guss = gaussian_noise(img)
mean = mean_filter(img)
# plt.imshow(mean_filter(img), cmap="gray")
# plt.show()

cv2.imshow("Original", img)
cv2.imshow("Aritmetic Mean to Gaussian Noise", mean)
cv2.waitKey(0)