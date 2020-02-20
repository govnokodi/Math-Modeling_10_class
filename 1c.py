import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np
 
fig = plt.figure()
ax = p3.Axes3D(fig)

h = 10 
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 6*np.pi, 100)

x = np.outer(phi , np.cos(theta))
y = np.outer(phi , np.sin(theta))
z = h*np.outer(np.ones(np.size(theta)), theta)
 
ax.plot_surface(x, y, z, color='w')
plt.show()