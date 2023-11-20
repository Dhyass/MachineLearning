import matplotlib.pyplot as plt
import numpy as np

# Créez des données pour le cercle
rayon = 2.0
theta = np.linspace(0, 2*np.pi, 100)  # 100 points autour du cercle
x = rayon * np.cos(theta)
y = rayon * np.sin(theta)

rayon_1 =0.2


# Paramètres pour personnaliser le cercle
epaisseur_ligne = 12  # Épaisseur de la ligne du cercle
couleur_ligne = 'red'  # Couleur de la ligne du cercle

# Tracez le cercle
plt.figure(figsize=(6, 6))  # Définissez la taille de la figure
plt.plot(x, y, linewidth=epaisseur_ligne, color=couleur_ligne)
plt.title("Cercle en Python")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.grid(True)  # Affichez la grille
plt.axis('equal')  # Assurez-vous que les axes ont la même échelle

# Affichez le cercle
plt.show()
