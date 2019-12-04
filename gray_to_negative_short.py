import matplotlib.pyplot as plt

path = '/home/habray/Image_Processing/Working_Folder/Image-Processing/image/'

img = plt.imread(path + 'panda.jpg')
plt.imshow(255 - img, cmap="gray")
plt.show()