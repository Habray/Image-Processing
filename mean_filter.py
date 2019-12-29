import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path = '/home/habray/Image_Processing/Image-Processing/image/'
img = plt.imread(path + 'lena.bmp')
new_img = np.copy(img)
def mean_filter(image):
    row, col = img.shape
    for i in range(3, row-3):
        for j in range(3, col-3):
            kernal = []
            for fx in range(-3, 4):
                for fy in range(-3, 4):
                    a = img.item(i+fx, j+fy)
                    kernal.append(a)
            mean = sum(kernal)/49
            new_img[i,j] = mean
    return new_img

outputs = [img, mean_filter(img)]
titles = ["Original", "Mean Filter (7*7)"]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(outputs[i], cmap="gray")
    plt.title(titles[i])
    plt.axis(False)
plt.show()