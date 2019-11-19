import numpy as np
import matplotlib.pyplot as  plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()

def circle_func(x_c, y_c, R, N):
    alpha = np.linspace(0, N, 1)
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range (0, N, 1):
        alpha = np.linspace(0, 2*np.pi, N)
        x = x_c + R*np.cos(alpha) 
        y = y_c + R*np.sin(alpha)
    return x,y

N = 100
R = 1
x = np.linspace(-5, 5, N)
y = x**2 + x 

anim_list = []
for i in range (0, N, 1):

    x, y = circle_func(x_c, y_c, R, N)
    circle, = plt.plot(x, y, 'g-', lw=2)
    parabol, = plt.plot(x[:i+1], y[:i+1], 'r-', lw=2)
    point, = plt.plot(x[i], y[i], 'bo')
    anim_list.append([circle,parabol,point])
    
plt.axes().set_aspect('equal')

ani = ArtistAnimation(fig, anim_list, interval=50)
ani.save('kkkk.gif')

