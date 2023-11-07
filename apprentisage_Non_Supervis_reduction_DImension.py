# -*- coding: utf-8 -*-
"""
Created on Tue Nov 7 17:06:17 2023
@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# Load the digits dataset
digits = load_digits()
X = digits.data
y = digits.target

# Perform PCA dimensionality reduction
model = PCA(n_components=2)
X_reduced = model.fit_transform(X)

# Scatter plot the data points, coloring them according to their class labels (handwritten digit)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y)
plt.colorbar()

# Print the components of the PCA model
print(model.components_)
print(model.components_.shape)  # Each component contains 64 values: each component is a linear combination of the 64 features

# Perform dimensionality reduction to preserve between 95% and 99% of the data's variance
model = PCA(n_components=64)  # Train the model with the same number of variables contained in the data (64)
X_reduced = model.fit_transform(X)

# Calculate the explained variance ratio for each component
explained_variance_ratios = model.explained_variance_ratio_

# Calculate the cumulative sum of explained variances
cumulative_variances = np.cumsum(explained_variance_ratios)

# Plot the cumulative explained variances
plt.figure()
plt.plot(cumulative_variances)

# Check if 99% of variance is preserved
print(np.argmax(cumulative_variances > 0.99) + 1)  # Add 1 to get the correct number of components

# Perform dimensionality reduction to preserve between 95% and 99% of the data's variance
model = PCA(n_components=29)  # Train the model with the same number of variables contained in the data (64)
X_reduced = model.fit_transform(X)
# decompress features
X_recovered=model.inverse_transform(X_reduced)
plt.figure()
plt.imshow(X_recovered[0].reshape((8,8)))