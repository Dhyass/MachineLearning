# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:43:42 2023

@author: NONZOOU
"""

import matplotlib.pyplot as plt
import numpy as np

class cercle_python():
    def __init__(self, nom):
        self.nom = nom
        self.rayon = None  # Initialize the radius, color, and thickness
        self.couleur = None
        self.epaisseur = None
        
    def parametrescercle(self, rayon, couleur, epaisseur):
        self.rayon = rayon
        self.couleur = couleur
        self.epaisseur = epaisseur

    def dessiner_cercle(self):
        if self.rayon is None or self.couleur is None or self.epaisseur is None:
            raise ValueError("Circle parameters are not set")
        
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.rayon * np.cos(theta)
        y = self.rayon * np.sin(theta)

        plt.figure(figsize=(6, 6))
        plt.plot(x, y, linewidth=self.epaisseur, color=self.couleur)
        plt.axis('equal')  # Ensure the aspect ratio is equal for a circular plot
        plt.title(self.nom)
        plt.show()



