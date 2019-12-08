import matplotlib.pyplot as plt

path = '/home/habray/Image_Processing/Working_Folder/Image-Processing/image/'

img = plt.imread(path + 'mri.jpg')

y = 0.8

plt.imshow(img ** y, cmap="gray")
plt.xticks([])
plt.yticks([])
plt.show()