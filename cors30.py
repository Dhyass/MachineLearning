# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:16:37 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

matrice = np.random.randint(0, 20, [5, 5])

print(matrice)

## somme de tous les elements
print(matrice.sum())

## somme selonn l'axe zero  (axe zero est la vertical donc les colonnes, et l'axe 1 est l'horizontal donc les olinges)

print(matrice.sum(axis=0))
print(matrice.sum(axis=1))
## somme cumuler

print(matrice.cumsum())
print(matrice.prod(axis=0)) ## produit

### mimi
print(matrice.min(axis=1))
## position du minimum
print(matrice.argmin(axis=0))

### les maths

E = np.exp(matrice)
print(E)
L = np.log(E)
print(L)

#### statistics

S= np.corrcoef(E)
print(S)

print(S[0,1])

## Entité du tableau et leur repetitions

T= np.unique(matrice, return_counts=True)
print(T)

value, counts =T

print(counts) ## pour trier du plus petit au plus grand

print(value[counts.argsort()]) 

for i , j in zip(value[counts.argsort()], counts[counts.argsort()]):
    print(f"valeur {i} apparait {j} fois")

## statistics avec les nombres vides

A=np.random.randn(5,5)
print(A)
A[0,2]=np.nan
A[4,3]=np.nan
print(A)

## calcul avec nan dans un tableau

print(np.mean(A)) ## resulta nan

print(np.nanmean(A)) ## calcul en ignorant le nan

## le nombre de fois qu'il ya nan ds un tableau

print(np.isnan(A)) ## un tableau masqu

print (np.isnan(A).sum())

## calcul de repartition de nan dan le tableau

print(np.isnan(A).sum()/A.size)

## donne une valeur à nan et reinjecter dzns le tableau

A[np.isnan(A)]=0

print(A)

