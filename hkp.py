# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:59:24 2023

@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = lambda x, y : np.cos(x+y)*np.sin(x-y)

x= np.linspace(-4*np.pi, 4*np.pi, 100)
y= np.linspace(-4*np.pi, 4*np.pi, 100)

x,y =np.meshgrid(x,y)

z=f(x,y)

fig = plt.figure(figsize=(18,16))

ax=fig.add_subplot(111, projection='3d' )
ax.plot_surface(x,y,z, cmap='plasma')

plt.savefig('Z_cos(x+y)_sin(x-y).png')

plt.show()

