# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:35:37 2023

@author: NONZOOU
"""

def mon_age(annee_de_naissance):
    # Calcul de l'âge en soustrayant l'année de naissance de 2023.
    age = 2023 - annee_de_naissance

    if age >= 18:
        # Début d'un bloc conditionnel.
        print("Vous avez :", age, "ans")
        print("Très cher(e), vous êtes majeur(e).")
        # Fin du bloc conditionnel.
    else:
        # Début de la structure else
        print("Vous avez :", age, "ans")
        print("Vous êtes mineur(e).")
        # Fin de la structure else
    # Fin de la fonction

# Appel de la fonction avec une année de naissance en argument.
annee = int(input("Veuillez entrer votre année de naissance :"))
mon_age(annee)
