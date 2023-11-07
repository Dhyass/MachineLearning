# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:47:51 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pn

data= pn.read_csv(r'C:/Users/NONZOOU/Downloads/ZAR=X.csv', index_col='Date', parse_dates = True)
datam=data['Close'].resample('W').agg(['mean', 'std', 'min', 'max'])
plt.figure(figsize=(9.6, 6.8))
print(datam)
datam['mean']['2022':'2023'].plot(label='moyenne par semaine')
plt.fill_between(datam.index, datam['max'], datam['min'], alpha=0.2, label ='Min-max par sempaine')

print(data.head())
### moving average sipmple
data.loc['2022':'2023','Close'].rolling(window=14).mean().plot(label='Moyenne mobile sur 14 jours', ls= ':')
data.loc['2022':'2023','Close'].rolling(window=14, center=True).mean().plot(label='Moyenne mobile sur 14 jours', ls= ':') #centrer la moyenne mobile
## moyenne mobile exponentielle
data.loc['2022':'2023','Close'].ewm(alpha=0.5).mean().plot(label='Moyenne mobile Exponentielle', ls= '-.', c='r', alpha= 0.3)
plt.legend()