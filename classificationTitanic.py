# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:35:30 2023

@author: NONZOOU
"""

import pandas as pn
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.shape

titanic=titanic[['survived','pclass','sex','age']]
titanic.dropna(axis=0, inplace=True)
titanic['sex'].replace(['male', 'femelle'], [0,1], inplace=True)