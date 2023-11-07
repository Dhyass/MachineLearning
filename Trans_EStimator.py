# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:41:11 2023

@author: NONZOOU
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_iris
from scipy import misc
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV


iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y)

## creation du transformer 

scaler = StandardScaler()
x_train_transformed = scaler.fit_transform(x_train)

## estimateur 
model = SGDClassifier(random_state=0)
model.fit(x_train_transformed, y_train)
## test

x_test_transformed = scaler.transform(x_test)
result=model.predict(x_test_transformed)

print(result)

## le tout en utilisant Pipline et Estimator composite

modep= make_pipeline(StandardScaler(), SGDClassifier())
modep.fit(x_train, y_train)
nobel = modep.predict(x_test)

print(nobel)

modeg = make_pipeline(StandardScaler(), SGDClassifier(random_state=0))