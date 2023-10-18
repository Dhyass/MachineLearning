# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:30:01 2023

@author: NONZOOU
"""

import numpy as np
from scipy import ndimage as nd
import matplotlib.pyplot as plt

plt.figure(figsize=(9.6, 6.8))
np.random.seed(0)
x=np.zeros((32,32))
plt.subplot(2, 1, 1)
x[10:-10, 10:-10]=1
x[np.random.randint(0,32,30), np.random.randint(0,32,30),] = 1
plt.imshow(x)

plt.subplot(2,1,2)
open_x =nd.binary_opening(x)
plt.imshow(open_x)