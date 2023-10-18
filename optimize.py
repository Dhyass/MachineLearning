# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:33:59 2023

@author: NONZOOU
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d as p1d 
from scipy import optimize

x=np.linspace(0, 2, 100)
y=  1/3*x**3 -3/5*x**2+ 2 +np.random.randn(x.shape[0])/20


plt.scatter(x, y)
 
def f(x,a,b,c,d) :
    return a*x**3 +b*x**2 + c*x + d

opt= optimize.curve_fit(f, x, y)

params, param_co = opt

plt.plot(x, f(x, params[0],params[1],params[2],params[3]), lw=3, c='r')
