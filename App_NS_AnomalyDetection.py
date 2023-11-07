# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:45:49 2023

@author: NONZOOU
"""
import numpy as np
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from sklearn.ensemble import IsolationForest

X, y = make_blobs(n_samples=50, centers=1, cluster_std=0.1, random_state=0)
X[-1,:] = np.array([2.25, 5])

plt.scatter(X[:,0], X[:, 1])

#set contamination value
model = IsolationForest(contamination=0.01)
model.fit(X)

# Identification of the contamination
plt.figure()
plt.scatter(X[:,0], X[:, 1], c=model.predict(X))
     
