# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:07:46 2023

@author: NONZOOU
"""

# LabelEncoder : encode chaque clasee de la variable en une valeur numérique (0, n_classe-1)
# la méthode inverse_transform permet de décoder les données

import numpy as np  
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder , OrdinalEncoder

y=np.array(['chat', 'chien','chat', 'oiseau','Vache', 'vache', 'mouton'])
encoder = LabelEncoder()
"""
encoder.fit(y)

transfor = encoder.transform(y)
print(transfor)
"""
## ou 

transform = encoder.fit_transform(y)
print(transform)

## decodage avec inverse_tansform()

cont = encoder.inverse_transform(np.array([0, 0, 1,1,3,2,2,4,]))
print(cont)

## ordinalEncoder

x = np.array([['chat','Poils'],
              ['Chien','Poils'],
              ['chat','Poils']
              ['oiseau','Plumes']
    ])

encoder1=OrdinalEncoder()
encoder1.fit_transform(x)