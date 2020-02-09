import matplotlib.pyplot as plt 
import numpy as np 
from my_modules import median_filter, salt_pepper_noise
import cv2

path = '/home/habray/Image_Processing/Working_Folder/image/'
img = plt.imread(path + 'cameraman.png')

sp = salt_pepper_noise(img)
md = median_filter(sp)
# plt.imshow(mean_filter(img), cmap="gray")
# plt.show()

cv2.imshow("Original", sp)
cv2.imshow("Median Filter to S&P Noise", md)
cv2.waitKey(0)