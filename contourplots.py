# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:59:32 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = lambda x,y : np.cos(x+y)*np.sin(x-y)

x= np.linspace(-4*np.pi, 4*np.pi, 100)
y= np.linspace(-4*np.pi, 4*np.pi, 100)

x,y=np.meshgrid(x,y)

z=f(x,y)
"""
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
#ax.plot_surface(x,y,z, cmap="Reds")
plt.contour(x,y,z)
plt.colorbar()
plt.show()
"""
plt.title('cos(x+y)*np.sin(x-y) By NONZOOU')
plt.contour(x,y,z, 20,  cmap='viridis')

#####
plt.colorbar()
plt.contourf(x,y,z, 20,  cmap='RdGy')