# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:02:04 2023

@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy import misc

iris = load_iris()
x = iris.data
y = iris.target

"""
face = misc.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()
face.shape
"""
plt.tight_layout()

plt.imshow(np.corrcoef(x.T), cmap='afmhot') ## les variables en fortes coretlatoiosn les unes avec les autrez
plt.colorbar(label="Valeur de correlation")
plt.show()