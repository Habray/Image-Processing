from PIL import Image

path = '/home/habray/Image_Processing/Working_Folder/Image-Processing/image/'

img = Image.open(path + 'cameraman.png').convert('LA')
img.save(path + 'greyscale.png')