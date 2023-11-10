# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:49:46 2023

@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pn

Gbpusd = pn.read_csv(r'C:/Users/NONZOOU/Downloads/GBPUSD=X.csv', index_col='Date', parse_dates=True)
Eurgbp = pn.read_csv(r'C:/Users/NONZOOU/Downloads/EURGBP=X.csv', index_col='Date', parse_dates=True)
plt.figure(figsize=(9.8,6.8))
plt.subplot(2,1,1)
Gbpusd.loc['2023','Close'].plot()

plt.subplot(2,1,2)
Eurgbp.loc['2023','Close'].plot()

data=pn.merge(Gbpusd, Eurgbp, on='Date', how='inner')

print(data)