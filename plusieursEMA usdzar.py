# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:34:35 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pn

dataUSDZAR = pn.read_csv(r'C:/Users/NONZOOU/Downloads/ZAR=X.csv', index_col='Date', parse_dates=True)

dataUSDZAR.loc['2022':'2023', 'Close'].plot(label='USDZAR en 2022:2023')

for i in np.arange(0.2, 1, 0.2):
    dataUSDZAR.loc['2022':'2023', 'Close'].ewm(alpha=i).mean().plot(label=f'EWM alpha {i}', alpha=0.8, ls=':')

plt.legend()
plt.title('Here We are')
plt.show()



