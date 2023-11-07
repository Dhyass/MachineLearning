# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:28:36 2023

@author: NONZOOU
"""

import numpy as np 
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest, chi2
iris = load_iris()
x= iris.data
y=iris.target

plt.plot(x)
plt.legend(iris.feature_names)
plt.show()

var=x.var(axis=0)
print(var)

# creation d'un selector qui va etrer notre transformer

selector = VarianceThreshold(threshold=0.2)
transformer=selector.fit_transform(x)
print(transformer)
supp = selector.get_support()
print(supp)

tableau= np.array(iris.feature_names)[selector.get_support()]

## lesection de variable (transforme )

best1 = chi2(x, y)
selector2= SelectKBest(chi2, k=2)
transformer2= selector2.fit_transform(x,y)
supp2=selector2.get_support()
print(transformer2)
print(supp2)

