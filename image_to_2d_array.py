import PIL
from skimage.io import imread
import numpy as np


# https://stackoverflow.com/questions/27026866/convert-an-image-to-2d-array-in-python
im = imread("avatar.png")
indices = np.dstack(np.indices(im.shape[:2]))
data = np.concatenate((im, indices), axis=-1)
print(data)


