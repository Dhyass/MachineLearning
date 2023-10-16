# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:38:43 2023

@author: NONZOOU
"""

import matplotlib.pyplot as plt
import numpy as np

# Créez une figure et un axe
fig, ax = plt.subplots()

# Les coordonnées du centre et du rayon du premier cercle
x1, y1 = 5, 5
rayon1 = 0.1

# Les coordonnées du centre et du rayon du deuxième cercle
x2, y2 = 5, 5
rayon2 = 1.5

# Dessinez les deux cercles
cercle1 = plt.Circle((x1, y1), rayon1, fill=False, color='blue')
cercle2 = plt.Circle((x2, y2), rayon2, fill=False, color='red')

# Ajoutez les cercles à l'axe
ax.add_patch(cercle1)
ax.add_patch(cercle2)

# Définissez les limites de l'axe pour assurer que les cercles sont visibles
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)

# Affichez le graphique
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

import matplotlib.pyplot as plt

# Coordonnées des points de la droite
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 3, 4]

# Tracé de la droite
plt.plot(x, y, label='Droite')

# Ajouter un titre et des étiquettes d'axe
plt.title('Tracé d\'une droite')
plt.xlabel('Axe des x')
plt.ylabel('Axe des y')

# Afficher une légende (optionnel)
plt.legend()

# Afficher le graphique
plt.show()

