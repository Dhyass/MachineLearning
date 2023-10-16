# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:32:33 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = lambda x, y : np.sin(x) + np.cos(y+x)*np.cos(x)

x=np.linspace(-4*np.pi, 4*np.pi, 50)
y=np.linspace(-4*np.pi, 4*np.pi, 50)

x,y= np.meshgrid(x,y)

z= f(x,y)
"""
fig =plt.figure(figsize=(18,16))
ax=fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z, cmap="spring_r")
"""
#plt.contour(x,y,z, 50, colors='black')
plt.contourf(x,y,z, 20, cmap="gist_rainbow_r")
plt.colorbar(label="Bar de couleurs ")

