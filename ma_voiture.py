# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:35:26 2023

@author: NONZOOU
"""

class Voiture:
    def __init__(self, marque, modele, annee_fabrication, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee_fabrication = annee_fabrication
        self.kilometrage = kilometrage

    def afficher_details(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année de fabrication : {self.annee_fabrication}")
        print(f"Kilométrage : {self.kilometrage} km")

    def mettre_a_jour_kilometrage(self, nouveau_kilometrage):
        if nouveau_kilometrage >= self.kilometrage:
            self.kilometrage = nouveau_kilometrage
            print("Kilométrage mis à jour avec succès.")
        else:
            print("Le nouveau kilométrage ne peut pas être inférieur à l'ancien.")

# Créez une instance de la classe Voiture
ma_voiture = Voiture("Toyota", "Corolla", 2020, 30000)

# Affichez les détails de la voiture
ma_voiture.afficher_details()

# Mettez à jour le kilométrage
ma_voiture.mettre_a_jour_kilometrage(35000)

# Affichez à nouveau les détails de la voiture après la mise à jour
ma_voiture.afficher_details()


import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 25]

# Créer un graphique linéaire
plt.plot(x, y)

# Ajouter des étiquettes aux axes
plt.xlabel('Axe X')
plt.ylabel('Axe Y')

# Ajouter un titre
plt.title('Exemple de graphique linéaire')

# Afficher le graphique
plt.show()
