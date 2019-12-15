# To do:
# need image
# r = intensity value of that pixel position
# y = positive constants
# S = cr**y
# show those pixel position with new intensity value S

import matplotlib.pyplot as plt 
import numpy as np 

path = '/home/habray/Image_Processing/Working_Folder/image/'

img = plt.imread(path + 'girl.jpg')

def gama_transformation(image):
    row, col = image.shape
    gama_image = np.copy(image)
    for i in range(row):
        for j in range(col):
            r = image[i, j]
            y = .5
            s = r ** y
            gama_image[i,j] = s
    return gama_image

output = [img, gama_transformation(img)]
titles = ['Original', 'Gama Transformation']
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()