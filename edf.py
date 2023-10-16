# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:50:15 2023

@author: NONZOOU
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Générer des données
x = np.linspace(0, 10, 20)
y = x ** 2  # Par exemple, y sera le carré de x pour cet exemple

# Créer un graphique en utilisant Matplotlib
plt.plot(x, y)

# Ajouter des étiquettes aux axes et un titre
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.title('Exemple de graphique avec Matplotlib')

# Afficher le graphique
plt.show()