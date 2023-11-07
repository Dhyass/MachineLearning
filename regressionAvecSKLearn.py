# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:36:08 2023

@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

np.random.seed(0)
m = 100 ##☺ creating 
X=np.linspace(0,10,m).reshape(m,1)
y=X + np.random.randn(m,1)
plt.scatter(X,y)

model = LinearRegression()
model.fit(X,y)
r2=model.score(X, y) # r carré de la méthode des moindre carrés coefficient de determination
print(r2)
predictions=model.predict(X)
plt.scatter(X,y)
plt.plot(X, predictions, c='r')