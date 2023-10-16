# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:43:32 2023

@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target

print(f'x contient {x.shape[0]} exmples et {x.shape[1]} variables')
print(f'il y a {np.unique(y).size} classes')

plt.hist(x[: , 0], bins= 20)
plt.hist(x[ :, 1])
plt.hist(x[ :, 2])

## la representation des données en 2d lorsquelles suivent la distrbution deux variables

plt.hist2d(x[: , 0], x[: , 1], cmap='Blues')
plt.xlabel("longeur sépal")
plt.ylabel('largeur petal')

plt.colorbar()
############################## va vleur de rendonm

