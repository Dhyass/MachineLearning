import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams.update({'figure.max_open_warning': 25})
# commande "magique" pour améliorer la visualiation
#%matplotlib notebook
fig1 = plt.figure()
def f(x, y):
    return np.sin(x) + np.cos(y)
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
ims = []
for i in range(60):
    x += np.pi / 15.
y += np.pi / 20.
im = plt.imshow(f(x, y), animated=True)
ims.append([im])
ani = animation.ArtistAnimation(fig1, ims, interval=50, blit=True,
repeat_delay=1000)
plt.show()