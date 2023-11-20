# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:29:51 2023

@author: NONZOOU
"""

import matplotlib.pyplot as plt

def draw_h():
    # Coordonnées des points pour dessiner la lettre H
    x = [1, 1, 1, 2, 2, 0, 0, 2]
    y = [0, 2, 1, 1, 0, 0, 2, 2]

    # Tracer la lettre H
    plt.plot(x, y, marker='o')

    # Ajouter des étiquettes et des titres
    plt.title('Dessin de la lettre H')
    plt.xlabel('Axe X')
    plt.ylabel('Axe Y')

    # Afficher la grille
    plt.grid(True)

    # Afficher le graphique
    plt.show()

# Appeler la fonction pour dessiner la lettre H
draw_h()
