# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:46:16 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pn
from scipy import ndimage as nd

image = plt.imread(r'C:/Users/NONZOOU/Pictures/bact.png') #image en 3 dimentions
print(image.shape)
plt.figure(figsize=(9.6 , 6.8))
## image sorting pour la renmener sur deux dimensions
plt.subplot(2,3, 1)
image= image[ : , : , 0] # on annule la 3eme dimension
plt.imshow(image, cmap='gray')
plt.title("Image Originale")

##J Histograme des couleurs de l'image 
plt.subplot(2,3,2)
im2= np.copy(image)
plt.hist(im2.ravel(), bins= 255)
plt.title("Histograme de couleur")
plt.show()

#" extraction des bacteries
plt.subplot(2,3,3)
ima3 =image<0.62
plt.imshow(ima3)
plt.title("Extraction des bacteries")
print(ima3)

## elimination des artéfactes

plt.subplot(2,3,4)
opnima3 = nd.binary_opening(ima3)
plt.imshow(opnima3)
plt.title("Elimination des artéfactes")

## Label de ndimage pour segmenteger l'image et mettre une etiquette sur chacune des bactéries qu'on peut voire
plt.subplot(2,3,5)
label_iamge, n_labels = nd.label(ima3)
print(n_labels) # nombres d'tiquette sur l'image
plt.imshow(label_iamge)
plt.title("Groupage et étiquetage des Bactéries")

## mesure de la taille relative des bactéries sur l'image
plt.subplot(2,3,6)
sizes= nd.sum(ima3, label_iamge, range(n_labels))
print(sizes)
plt.scatter(range(n_labels), sizes, c='r')
plt.title("Taille relative des bactéries")
