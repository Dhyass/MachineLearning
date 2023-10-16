# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:28:45 2023

@author: NONZOOU
"""

"""
 Execices
     créer une fonction qui permet de classer un tout nombre dans un classeur 
     soit il est négalive soit iil est positif
"""
# Créer un dictionnaire vide pour la fonction clas
mon_classeur = {"Positif": [], "Negatif": []}

def clas(classeur, n):
    if type(n) != int:
        print("Votre nombre n'est pas un entier")
    elif n < 0:
        classeur["Negatif"].append(n)
    else:
        classeur["Positif"].append(n)
    return classeur

# Appeler la fonction clas avec le dictionnaire et un nombre en argument
resultat = clas(mon_classeur, -8)
resultat = clas(mon_classeur, 6)

print(resultat)


