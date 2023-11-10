import numpy as np 
import matplotlib.pyplot as plt
r=5
angle= np.arange(0, 3*np.pi, np.pi/15)

x=r*np.cos(angle)
y=r*np.sin(angle)
z=np.linspace(0, x, 5)
t=np.linspace(0, y, 5)
plt.figure(figsize=(8, 8))
plt.plot(x,y, c='r', lw=3)
plt.plot(z,t, lw=3, alpha = 0.3)
plt.show()
  
