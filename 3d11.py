# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:04:24 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Créez une grille de valeurs x et y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Définissez une fonction tridimensionnelle (par exemple, une surface en forme de cloche)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Créez une figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Ajouter des étiquettes d'axe
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ajouter un titre
plt.title('Surface 3D')

# Afficher la figure
plt.show()
