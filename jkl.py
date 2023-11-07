# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:16:56 2023

@author: NONZOOU
"""

import numpy as np 

from matplotlib import pyplot as plt
import pandas as pn
from scipy import ndimage as nd

image = plt.imread(r'C:/Users/NONZOOU/Desktop/301205V/New folder/bague.PNG') #image en 3 dimentions



t= np.linspace(-4*np.pi, 4*np.pi, 30)
x=np.cos(t)**2
y=np.sin(t)**2

plt.figure(figsize=(9.8,6.8))
plt.subplot(231)
plt.plot(t, x+y)
plt.title('cos(t)**2 + sin(t)**2')

plt.subplot(232)
plt.plot(t, x*y)
plt.title('cos(t)**2*sin(t)**2')

plt.subplot(233)
plt.plot(t, x-y)
plt.title('cos(t)**2-sin(t)**2')

plt.subplot(234)
#plt.plot(t, x/y, label = 'cos(t)**2/sin(t)**2')
plt.plot(t, y/x, label ='sin(t)**2/cos(t)**2')
plt.title('sin(t)**2/cos(t)**2')

plt.subplot(235)
plt.plot(t, x/y, label = 'cos(t)**2/sin(t)**2')
#plt.plot(t, y/x, label ='sin(t)**2/cos(t)**2')
plt.title('cos(t)**2/sin(t)**2')
plt.xlabel('Selon ces bagues Quel serait la meilleure courbe ?')

plt.subplot(236)

image= image[ : , : , 0] # on annule la 3eme dimension
plt.imshow(image, cmap='gray')
plt.title("Image Originale")