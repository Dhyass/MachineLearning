# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:29:57 2023

@author: NONZOOU
"""

import numpy as np

import matplotlib.pyplot as plt

import pandas as pn 

data= pn.read_excel(r'C:/Users/NONZOOU/Downloads/Python-Machine-Learning-master/Python-Machine-Learning-master/Dataset/titanic3 (3).xls')

#print(data)
print(data.head())
print(data.shape) # dimensions de nos donnees
## Elimination des colon inutiles poour l'analyse avec la fonctipon drop()
dataf=data.drop(['name','sibsp', 'parch','ticket','fare','cabin','embarked','boat','body','home.dest'], axis=1)

print(dataf.head())

## moyenne pour chaque colone avec describe()

m = dataf.describe() ## un constat de 1309 pasager et seulement 1046 dont l'age est s^écifié. 
print(m)

##pour aulieur remplacer les ages vides par une valeur on élimine plutot ces passagersq.

dataff= dataf.dropna(axis=0)
print(dataff.head())
print(dataff.shape) # dimensions de nos donnees

## au final on travaille avec les 40 pourcent des urvivant
## on va chercer à connaitre leur class e dans le bateau

nclasse =dataff['pclass'].value_counts()
print(nclasse)

plt.figure(figsize=(9.6, 6.8))
## creation d'un graphique en circumlaire
plt.subplot(2,2,1)
nclasse =dataff['pclass'].value_counts().plot.pie()

## creation d'un graphique en bar
plt.subplot(2,2,2)
nclasse =dataff['pclass'].value_counts().plot.bar()

## creation d'un graphique en bar
plt.subplot(2,2,3)
plt.hist(dataff['age'])

## analyse pard gtoupage, par sex, et classe de voyage
g= dataff.groupby(['sex', 'pclass']).mean()

print(g)