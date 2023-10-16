import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Créez une figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Définissez la trajectoire du drone
t = np.linspace(0, 10, 100)
x = np.sin(t)
y = np.cos(t)
z = 0.1 * t  # Mouvement vertical du drone dans l'espace

# Créez le point de départ du drone
drone = ax.scatter([x[0]], [y[0]], [z[0]], color='red', s=50)

# Fonction d'animation pour mettre à jour la position du drone
def update(frame):
    drone.set_offsets(np.c_[x[frame], y[frame]])
    drone.set_3d_properties(z[frame], 'z')
    return drone,

# Créez l'animation
ani = FuncAnimation(fig, update, frames=len(t), blit=True, repeat=False)

# Définissez les limites des axes
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 1)

# Ajoutez des étiquettes d'axe
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Affichez l'animation
plt.show()
