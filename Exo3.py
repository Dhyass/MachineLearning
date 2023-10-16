# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:17:28 2023

@author: NONZOOU
"""
"""
Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. Comptez combien il y avait de données et combien étaient supérieures à 100.

Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.
"""
def sommedenombre(list_des_nombres):
    somme = 0.0
    nombre = 0
    supde100 = 0
    while nombre >= 0:
        nombre = float(input("Entrer un nombre : "))
        if nombre < 0:
            print("Erreur : fin ")
        else:
            list_des_nombres.append(nombre)
            somme += nombre  # Fixed the += operator here to accumulate the sum.
        if nombre > 100 :
              supde100 += 1
                
    nbrtotal = len(list_des_nombres)
    print(f"Vous avez saisi {nbrtotal} nombres")
    print(f"La somme de vos nombres est : {somme}")
    print(f"Vous avez {supde100} nombres > à 100")
    
    return somme, supde100

list_des_nombres = []

result = sommedenombre(list_des_nombres)
print(f"La liste des nombres saisis :\n {list_des_nombres}")