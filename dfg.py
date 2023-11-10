import numpy as np 
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = 4,3
from matplotlib.animation import FuncAnimation

r1=5
r0=0.1

# draw circle with initial point in left Axes
fig, ax= plt.subplots()
x = np.linspace(0, 2 * np.pi, 50)
t=np.linspace(0, r1*np.cos(x[-1]), 5)
z=np.linspace(0, r1*np.sin(x[-1]), 5)
ax.plot(r1*np.cos(x), r1*np.sin(x), "k", lw=1)
ax.plot(r0*np.cos(x), r0*np.sin(x), "k", lw=3)
point, = ax.plot(r1*np.cos(x[0]), r1*np.sin(x[0]), "o", lw=2, c='b')
line, = ax.plot(t,z, c='r', lw=3)

ax.set_aspect("equal")

# Updating function, to be repeatedly called by the animation
def update(i):
    # obtain point coordinates 
    x = np.linspace(0, 2 * np.pi, 50)
    t=np.linspace(0, r1*np.cos(x[i]), 5)
    z=np.linspace(0, r1*np.sin(x[i]), 5)
    point.set_data(r1*np.cos(x[i]), r1*np.sin(x[i]))
    line.set_data(t, z)
    # set point's coordinates
    
    return point, line, 

# create animation with 10ms interval, which is repeated,
# provide the full circle (0,2pi) as parameters
ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                    frames=np.linspace(0,2*np.pi,360, endpoint=False))

plt.show()
