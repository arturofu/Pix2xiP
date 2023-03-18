#Code Pix2xip v1.0 / narrativeforces

import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
im = Image.open('external_image')
img = im.quantize(colors=200)
new_values=np.random.randint(255,size=600) 
new_values=new_values.tolist()
img.putpalette(new_values)

imagrgb=img.convert('RGB')
imf=np.array(imagrgb)
cv2.imwrite('image_name',imf)

#extension2video 
#preprocessing_module
