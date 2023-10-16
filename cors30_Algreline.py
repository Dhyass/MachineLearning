# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:21:20 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
A= np.ones((5,4))
B= np.random.randn(4,3)
print(A ,"\n", B)
tpA = A.T  ##• transposeé

print(tpA)
prodAB = A.dot(B) ## produit matricielle

print(prodAB)

C= np.random.randint(0, 10, [4, 4])

## calclu de determinan

print(np.linalg.det(C))

## calcullmatri inveese

Cin=np.linalg.inv(C)
print(Cin)

### les valeur propres et vecteurs propres

Vp, VP = np.linalg.eig(C)

print(Vp)
print(VP)

##################################################
print("Standardisez la Matrice Q sur chaque colonne")

## A-mean(A)/ sdt(A)

Q= np.random.randint(0, 100, [10, 5])
print(Q)

moy =Q.mean(axis = 0)
eqd= Q.std(axis=0)
print(moy)
print(eqd)
Q[0:, 0:1] = (Q[0:, 0:1]-moy[1])/eqd[0]
print(Q[0:, 0:1])
print(moy[4])

D=(Q-moy)/eqd

print(D)