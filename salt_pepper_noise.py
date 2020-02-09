# Adding Salt Noise, Pepper Noise and Salt & Pepper Noise

import matplotlib.pyplot as plt 
import numpy as np 
import cv2

path = '/home/habray/Image_Processing/Working_Folder/image/'

img = plt.imread(path + 'cameraman.png')

def salt_pepper_noise(image):
    
    s_vs_p = 0.5
    amount = 0.2
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0
    return out

def salt_noise(image):
    s_vs_p = 0.5
    amount = 0.2
    out = np.copy(image)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1
    return out

def pepper_noise(image):
    s_vs_p = 0.5
    amount = 0.2
    out = np.copy(image)
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0
    return out

s_image = salt_noise(img)
p_image = pepper_noise(img)
sp_image = salt_pepper_noise(img)

cv2.imshow("Original", img)
cv2.imshow("Salt Noise", s_image)
cv2.imshow("Pepper Noise", p_image)
cv2.imshow("Salt & Pepper Noise", sp_image)
cv2.waitKey(0)

# plt.subplot(141)
# plt.title("Original")
# plt.imshow(img, cmap="gray")
# plt.subplot(142)
# plt.title("Salt Noise")
# plt.imshow(s_image, cmap="gray")
# plt.subplot(143)
# plt.title("Pepper Noise")
# plt.imshow(p_image, cmap="gray")
# plt.subplot(144)
# plt.title("Salt & Pepper Noise")
# plt.imshow(sp_image, cmap="gray")
# plt.show()