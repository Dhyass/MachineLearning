import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow

# Créez une figure circulaire pour représenter le cadran de l'horloge
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Tracez le cadran de l'horloge
circle = plt.Circle((0, 0), 1, color='black', fill=False, lw=2)
ax.add_artist(circle)

# Tracez les marques des heures
for hour in range(1, 13):
    angle = np.deg2rad(hour * 30)  # 30 degrés par heure
    x = 0.85 * np.sin(angle)
    y = 0.85 * np.cos(angle)
    ax.text(x, y, str(hour), ha='center', va='center', fontsize=12, fontweight='bold')

# Fonction pour mettre à jour les aiguilles de l'horloge
def update_clock():
    current_time = np.datetime64('now')
    seconds = current_time.astype('datetime64[s]').second
    minutes = current_time.astype('datetime64[m]').minute
    hours = current_time.astype('datetime64[h]').hour % 12

    # Dessinez l'aiguille des secondes
    angle_sec = np.deg2rad(6 * seconds)
    ax.patches.pop(0)  # Supprimez l'aiguille précédente
    ax.add_patch(FancyArrow(0, 0, 0.8 * np.sin(angle_sec), 0.8 * np.cos(angle_sec), color='red', width=0.01, head_width=0.03))

    # Dessinez l'aiguille des minutes
    angle_min = np.deg2rad(6 * (minutes + seconds / 60))
    ax.patches.pop(1)  # Supprimez l'aiguille précédente
    ax.add_patch(FancyArrow(0, 0, 0.7 * np.sin(angle_min), 0.7 * np.cos(angle_min), color='blue', width=0.02, head_width=0.05))

    # Dessinez l'aiguille des heures
    angle_hour = np.deg2rad(30 * (hours + minutes / 60))
    ax.patches.pop(2)  # Supprimez l'aiguille précédente
    ax.add_patch(FancyArrow(0, 0, 0.6 * np.sin(angle_hour), 0.6 * np.cos(angle_hour), color='black', width=0.03, head_width=0.07))

    fig.canvas.draw()

# Mettez à jour l'horloge pendant 60 secondes
update_interval = 60  # Temps en secondes pour mettre à jour l'horloge
start_time = np.datetime64('now')
end_time = start_time + np.timedelta64(update_interval, 's')

plt.ion()
while np.datetime64('now') < end_time:
    update_clock()
    plt.pause(1)

plt.ioff()
plt.show()
