# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:10:10 2023

@author: NONZOOU
"""

"""
        Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.
"""
import math
import random

def volumedecone(r, h):
    if r < 0 or h < 0:
        print("Erreur mathématique : Les valeurs de rayon et de hauteur doivent être positives.")
        return None
    else:
        volume = (r**2) * h * math.pi / 3
        return volume

print("Ce programme calcule le volume d'un cône")
r = float(input("Entrez le rayon du cône en m : "))
h = float(input("Entrez la hauteur du cône en m : "))

volume = round(volumedecone(r, h),2)

if volume is not None:
    print(f"Le volume du cône est : {volume} m³")

