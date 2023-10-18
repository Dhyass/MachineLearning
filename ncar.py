# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:51:23 2023

@author: NONZOOU
"""
import time

## tous les carrés de nombre de 0 à n

stat =time.time()
n = int(input("entre le nombre en n : "))
carres_des_n_entiers =[]
for i in range (n):
    carres_des_n_entiers.append(i**3)
print(carres_des_n_entiers)

end =time.time()
print(end-stat)


#list comprehension consiste à inserer la bocle for à l'interreir de la lisyte elle-meme
debut =time.time()
k = int(input("entre le nombre en k : "))
cube_des_n_entiers =[i**3 for i in range(k)] #♥ liste comprension 
print(cube_des_n_entiers)
fin =time.time()
print(fin-debut)
#pourquoi utiliser une liste comprehension ?
# pour 3 raison
'''
    1- reduction de nombre d'instructions et donc de nombre deurer'
    2- plus professionnel en python
    3- temps d'exc"cution '
'''

#utilisation de liste comprehension pour creer de Nexted list (une liste qui contien d'autres listes)
n = int(input("entre le nombre en n : "))
k = int(input("entre le nombre en k : "))
neted_list = [[i**j for i in range(k) ] for j in range(n)] # chaque i_liste contient i**j (jallant de 0 à n) et i de à k

print(neted_list)


#dict comprehension 
disco = {
        "Lomé":"Togo",
        "Rabat":"Maroc",
        "Abidjan":"Cote d'ivoire",
        "Dakar":"Sénégal",
        "Livreville":"Gabon",
        "Ndjamena":"Tchad" 
    }
# dict comprehension est possible si et slmt si on a deux listes dejà créer

capitales = ["Lomé", "Rabat", "Abidjan", "Dakar", "Livreville", "Ndjamena"]
pays = ["Togo", "Maroc", "Cote d'ivoire", "Sénégal", "Gabon", "Tchad"]
dico = {P: C for P, C in zip(pays, capitales)}

print(dico)

pays = ["Togo", "Maroc", "Cote d'ivoire", "Sénégal", "Gabon", "Tchad"]
pib =[2608, 9519,6538, 4209,16471,2400]

dicopid={P: B for P, B in zip(pays,pib) if B >6000 }

print("Voici les pays Emergentes " )

print(dicopid)

## tuple comprehension 

tuple_jk = tuple(i**2 for i in range(17))
