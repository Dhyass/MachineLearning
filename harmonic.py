import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
y = 15 * np.exp(-0.5 * x) * np.cos(x**2 - np.pi / 15)
curve, = ax.plot(x, y)
point, = ax.plot(x[0], y[0], 'o', lw=4)

def update(t):
    curve.set_data(x[:t], y[:t])
    point.set_data(x[t], y[t])  # Update all points up to the current frame
    return point, curve

# Animate the radar chart
ani = FuncAnimation(fig, update, frames=len(x), interval=20, blit=True)
plt.show()
