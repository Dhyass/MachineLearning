# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:09:20 2023

@author: NONZOOU
"""

import pandas as pd
import matplotlib.pyplot as plt

# Charger les données démographiques de New York depuis un fichier CSV hypothétique
data = pd.read_csv('donnees_demographiques_new_york.csv')

# Nettoyer les données (gérer les valeurs manquantes, les doublons, etc.)
data_cleaned = data.drop_duplicates().dropna()

# Analyser les tendances démographiques au fil des ans
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['Annee'], data_cleaned['Population'], marker='o', linestyle='-')
plt.title('Évolution de la population de New York au fil des ans')
plt.xlabel('Année')
plt.ylabel('Population')
plt.grid(True)
plt.show()

# Analyser la structure de la population
age_distribution = data_cleaned['Age'].value_counts()
gender_distribution = data_cleaned['Sexe'].value_counts()

# Afficher les résultats
print("Répartition de la population par âge :")
print(age_distribution)
print("\nRépartition de la population par sexe :")
print(gender_distribution)

# Faire des prévisions démographiques (hypothétiques)
from sklearn.linear_model import LinearRegression

X = data_cleaned['Annee'].values.reshape(-1, 1)
y = data_cleaned['Population'].values

model = LinearRegression()
model.fit(X, y)

future_years = [2030, 2040, 2050]
population_predictions = model.predict([[year] for year in future_years])

print("\nPrévisions démographiques pour les années futures :")
for year, population in zip(future_years, population_predictions):
    print(f"Année {year}: Population prévue = {int(population)}")

# Analyser la migration (hypothétique)
migration_data = data_cleaned['Migration'].value_counts()

# Afficher la répartition de la migration
print("\nRépartition de la migration :")
print(migration_data)
