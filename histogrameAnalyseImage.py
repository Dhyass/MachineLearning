# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:36:25 2023

@author: NONZOOU
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
## upload the image
image=cv2.imread(r'C:\Users\NONZOOU\Downloads\Animal-Totem-Aigle.jpg')



if image is not None :
    ##convert image to numpay array
    aigle = np.array(image)
    plt.figure() ## create figure 
    ## convert image to gray scale (Balck and white color)
    aigleim = cv2.cvtColor(aigle, cv2.COLOR_BGR2GRAY)
    
    ##plt.imshow(aigleim, cmap="gray")
  
    plt.hist(aigleim.ravel(), bins=255, label= "Image d'aigle volant")
    plt.title("Les coleurs entre 0 et 255")
    plt.legend()
    plt.show()