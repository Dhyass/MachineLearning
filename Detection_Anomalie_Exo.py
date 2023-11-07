# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:06:17 2023

@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits 
from sklearn.ensemble import IsolationForest
digits = load_digits()
images=digits.images 
X=digits.data
y=digits.target

#print(X.shape)
#plt.imshow(images[45])

model=IsolationForest(random_state=0, contamination=0.02)
model.fit(X)
md_predict= model.predict(X)
print(md_predict)
outliers =md_predict==-1
# injecter les outliers dans images
images[outliers]
## choisir une images d'outliers et l'afficher
plt.imshow(images[outliers][3])
plt.title(y[outliers][0])