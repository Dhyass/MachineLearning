# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:21:31 2023

@author: NONZOOU
"""

class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def demarrer(self):
        print(f"{self.marque} {self.modele} démarre.")

    def arreter(self):
        print(f"{self.marque} {self.modele} s'arrête.")

ma_voiture = Voiture("Toyota", "Camry")

ma_voiture.demarrer()