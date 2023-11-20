import matplotlib.pyplot as plt
import numpy as np

class cercle_python():
    def __init__(self, nom):
        self.nom = nom
        
    def parametrescercle(self, rayon, couleur, epaisseur):
        self.rayon = rayon
        self.couleur =couleur
        self.epaisseur =epaisseur
        
        theta= np.linspace(0, 2*np.pi, 100)
        x=self.rayon*np.cos(theta)
        y=self.rayon*np.sin(theta)

        plt.figure(figsize=(6,6))
        plt.plot(x, y, linewidth = self.epaisseur, color = self.couleur)
        plt.axis('equal')  # Ensure the aspect ratio is equal for a circular plot
        plt.show()

mon_cercle = cercle_python("MonCercle")
rayon= float(input("Rayon du cercle : "))
couleur= str(input("couleur du cercle : "))
epaisseur= float(input("Epaisseur du cercle : "))
mon_cercle.parametrescercle(rayon, couleur, epaisseur)
