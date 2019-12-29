import matplotlib.pyplot as plt
import numpy as np

path = '/home/habray/Image_Processing/Image-Processing/image/'
img = plt.imread(path + 'cameraman.png')

row = img.shape[0]
col = img.shape[1]

new_img = np.copy(img)
def median_filter(image):
    for i in range(3, row-3):
        for j in range(3, col-3):
            kernel = []
            for fx in range(-2, 3):
                for fy in range(-2, 3):
                    a = img.item(i+fx, j+fy)
                    kernel.append(a)
            kernel.sort()
            median = kernel[13]
            new_img[i, j] = median
    return new_img

outputs = [img, median_filter(img)]
titles = ["Original", "Median Filter (5*5)"]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(outputs[i], cmap="gray")
    plt.title(titles[i])
    plt.axis(False)
plt.show()
