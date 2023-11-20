# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:50:57 2023

@author: NONZOOU
"""

import pandas as pd
import matplotlib.pyplot as plt

# Créez un DataFrame fictif avec des âges
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Population': [5000, 6000, 8000, 9000, 8500, 7000, 6000, 5500, 5000, 4500, 4000, 3500, 3000, 2500, 2000]
}

df = pd.DataFrame(data)

# Créez un histogramme d'âge
plt.figure(figsize=(10, 6))
plt.bar(df['Age'], df['Population'], width=5, color='skyblue')
plt.xlabel('Âge')
plt.ylabel('Population')
plt.title('Histogramme d\'âge à New York')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Créez un DataFrame fictif avec des âges
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Population': [5000, 6000, 8000, 9000, 8500, 7000, 6000, 5500, 5000, 4500, 4000, 3500, 3000, 2500, 2000]
}

df = pd.DataFrame(data)

# Créez une palette de couleurs personnalisée pour chaque groupe d'âge
colors = plt.cm.viridis(np.linspace(0, 1, len(df)))

# Créez un histogramme d'âge avec des couleurs différentes pour chaque groupe d'âge
plt.figure(figsize=(10, 6))
plt.bar(df['Age'], df['Population'], width=5, color=colors)
plt.xlabel('Âge')
plt.ylabel('Population')
plt.title('Histogramme d\'âge à New York')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Créez un DataFrame avec vos données
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Population': [5000, 6000, 8000, 9000, 8500, 7000, 6000, 5500, 5000, 4500, 4000, 3500, 3000, 2500, 2000]
}

df = pd.DataFrame(data)

# Créez une palette de couleurs personnalisée pour chaque groupe d'âge
num_bars = len(df)
colors = plt.cm.viridis(np.linspace(0, 1, num_bars))

# Créez un histogramme d'âge avec des couleurs différentes pour chaque groupe d'âge
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Age'], df['Population'], width=5, color=colors)
plt.xlabel('Âge')
plt.ylabel('Population')
plt.title('Histogramme d\'âge à New York')

# Ajoutez une légende avec les couleurs correspondantes aux groupes d'âge
legend_labels = [f'Âge {age}' for age in df['Age']]
plt.legend(bars, legend_labels, loc='upper right', title='Groupes d\'âge')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()