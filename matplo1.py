# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:55:07 2023

@author: NONZOOU
"""
import time
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0, 30, 100)
y=np.log(x)
z=np.sin(x**2+x**3)

##plt.plot(x,z, c="violet", lw=5, ls="--") ## c = couleur, lw= paisseur, ls= style de ligne
##plt.show()
time.sleep(2)
## fonction figure

plt.figure()
plt.plot(x, 1/x**2, c="violet", lw=5, ls="--", label ="Iverse quatratique") ## c = couleur, lw= paisseur, ls= style de ligne
plt.plot(x, y, label= "logarithme de x")
plt.plot(x, np.cos(x), label ="cosinus de x")
plt.title("By NONZOOU MAGNOUDEWA")
plt.xlabel("Axe x")
plt.ylabel("Axes Y")
plt.legend() ## label dans les fonction plt.plot
plt.show()
plt.savefig("Figure.png") ## sauvegarge de la figure ne format image

plt.figure()
## afficher plusieur graphiques sur un meme figure : on precise le nombre de ligbe et de colonnes de la figures
plt.subplot(2,2, 1)
plt.plot(x, np.tan(x))
plt.show()

plt.subplot(2,2,2)
plt.plot(x, x*np.log(x-1))
plt.show()

plt.subplot(2,2,3)
plt.plot(x, np.sinh(x**2 + x), c="red", lw="3")

plt.subplot(2,2,4)
plt.plot(y, x*y)