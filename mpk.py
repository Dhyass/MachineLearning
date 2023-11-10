import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to create parametric equations
def parametric_equations(angle):
    x = (np.sin(angle))**3
    y = (13/16)*np.cos(angle) - (5/16)*np.cos(2*angle) - (1/8)*np.cos(3*angle) - (1/16)*np.cos(4*angle)
    z = 30*(1/16)*x**6
    return x, y, z

# Create a figure with three subplots
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(12, 5), sharex=True)

# Hide axes for all subplots
for ax in [ax0, ax1, ax2]:
    ax.axis('off')

# Set up data for parametric equations
angle = np.linspace(-np.pi, np.pi, 100)
x, y, z = parametric_equations(angle)

# Second subplot
couer, = ax1.plot(x, y, linewidth=20, color='blue')
point_coeur, = ax1.plot(x[0], y[0], 'o', markersize=28, color='red')

# Third subplot
you, = ax2.plot(x, z, linewidth=20, color='green')
point_you, = ax2.plot(x[0], z[0], 'o', markersize=28, color='red')

# Add a vertical line at x = x_value in the first subplot
x_value = 0.0
ax0.axvline(x=x_value, color='red', label='Vertical Line', ymin=-0.75, ymax=1, linewidth=20)

def update(i):
    couer.set_data(x[:i], y[:i])
    point_coeur.set_data(x[i], y[i])
    you.set_data(x[:i], z[:i])
    point_you.set_data(x[i], z[i])

    return couer, point_coeur, you, point_you

# Create animation for all frames
interval = 50  # Set your desired interval in milliseconds
animation = FuncAnimation(fig, update, frames=len(x), interval=interval, blit=True)

# Save the animation as an MP4 file
animation.save('parametric_animation.mp4', writer='ffmpeg', fps=30)

plt.tight_layout()
plt.show()
