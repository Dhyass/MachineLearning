# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:11:08 2023

@author: NONZOOU
"""
#Turtle strategy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pn

data = pn.read_csv(r'C:/Users/NONZOOU/Downloads/EURGBP=X (1).csv', index_col='Date', parse_dates=True)

data_copy = data.copy() # copie de des données pour la sécurité

data['Buy']=np.zeros(len(data)) # ajout d'une colnne Buy avec des 0
data['Sell']=np.zeros(len(data))

data['RollMax']=data['Close'].shift(2).rolling(window=28).max() #↕" collone des valeurs max
data['Rollmin']=data['Close'].shift(2).rolling(window=28).min()

data.loc[data['RollMax']<data['Close'], 'Buy']=1 ##♣ écrire  dans la colonne Buy maxi < au signal close
data.loc[data['Rollmin']>data['Close'], 'Sell']=-1

start = '2015'
end = '2023'

fig, ax = plt.subplots(2, figsize=(12,8), sharex=True)

ax[0].plot(data['Close'][start:end]) ## le graphe de signal close
ax[0].plot(data['RollMax'][start:end]) ## courbe des maximus sur cur 28 
ax[0].plot(data['Rollmin'][start:end]) 
plt.title('Turtle Strtegy')
ax[0].legend(['Close', 'Max', 'Min'])
ax[1].plot(data['Buy'][start:end], c='g') ## reprisentation des ordres d'achat
ax[1].plot(data['Sell'][start:end], c='r')
ax[1].legend(["Buy", "Sell"])