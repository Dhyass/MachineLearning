# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:00:22 2023

@author: NONZOOU
"""

import numpy as np 
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel, RFE, RFECV
from sklearn.linear_model import SGDClassifier


iris = load_iris()
x=iris.data
y=iris.target

plt.plot(x)
plt.legend(iris.feature_names)
plt.show()

selector= SelectFromModel(SGDClassifier(random_state=0), threshold='mean')

choix=selector.fit_transform(x,y)
print(choix)
estim = selector.estimator_.coef_.mean(axis=0).mean()
print(estim)

## RFE et RFECV eliminent les variables moins importantes de facon recursive

selector2 = RFECV(SGDClassifier(random_state=0), step=1, min_features_to_select=2, cv=5)
#♣ step nombre de variables à eliminer à chaque etape
# min_features_to_select , nbre minim dde variabvles à la,fin

selector2.fit(x,y)
rang= selector2.ranking_ # pour voir le cclassement final de nos variable
#score = selector2.grid_scores_  # le score de REFCV à chaque itération
print(rang)
