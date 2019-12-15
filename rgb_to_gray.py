import matplotlib.pyplot as plt
import numpy as np

path = '/home/habray/Image_Processing/Working_Folder/image/'

img = plt.imread(path + 'lena.tiff')

row,col,ch = img.shape

def to_gray(image):
    img1 = np.copy(img)
    for i in range(row):
        for j in range(col):
            r,g,b = img[i,j][0],img[i,j][1],img[i,j][2]
            y = 0.2126*r + 0.7152*g + 0.0722*b
            img1[i,j] = y
    return img1

outputs = [img, to_gray(img)]
titles = ["Original", "Gray"]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()