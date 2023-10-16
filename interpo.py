# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:11:49 2023

@author: NONZOOU
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Generate random data
x = np.linspace(0, 10, 10)
y = x**2

# Create the interpolation function
f = interp1d(x, y, kind="quadratic")

# Generate new random data
X_2 = np.linspace(0, 10, 50)  # Use more points for a smoother curve
y_2 = f(X_2)

# Plot the original and interpolated data
plt.scatter(x, y, label="Original Data")
plt.scatter(X_2, y_2, c="r", label="Interpolated Data")
plt.legend()
plt.show()
