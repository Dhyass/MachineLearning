# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:17:33 2023

@author: NONZOOU
"""
import numpy as np
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

# Create the dataset
# Génération de données
X, y = make_blobs(n_samples=100, centers=3, cluster_std=0.4, random_state=0)
plt.scatter(X[:,0], X[:,1])

model=KMeans(n_clusters=3)
model.fit(X)
print(model.labels_)
model.predict(X)
plt.scatter(X[:,0], X[:, 1], c=model.predict(X))
print(model.cluster_centers_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], c='r')
#calcul d'inertia
inertia = model.inertia_
print(inertia)

# pour des cas incetains tres eparpillés
plt.figure()
ineria= []
K_range = range(1,20)
for k in K_range :
    model2=KMeans(n_clusters=k).fit(X)
    ineria.append(model2.inertia_)

plt.plot(K_range, ineria)
plt.xlabel('Nombre de clusters')
plt.ylabel('Cout du model()')