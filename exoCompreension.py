# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 18:09:00 2023

@author: NONZOOU
"""

"""
    creer un dictionnaire k:v
    k = 0 à 20
    v= k**2
"""
keys=[i+1 for i in range(20)]
valeurs= [(i+1)**2 for i in range(20)]
carre_de_nombres = {k:v for k, v in zip(keys, valeurs)}

print(carre_de_nombres)

