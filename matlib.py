# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:47:12 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4 * np.pi, 1, 1000)  # Generate 1000 evenly spaced values from -4π to 1
y = np.arccos(x) + np.cos(x)  # Use numpy functions

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = arccos(x) + cos(x)')
plt.grid(False)
plt.show()


