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
R = 3

x_m = np.linspace(-5, 5, N)
y_m = x_m**2 + x_m 

anim_list = []
for i in range (0, N, 1):
    x_cir,y_cir = circle_func(x_m[i], y_m[i], R, N)
    liniaq, = plt.plot(x_m, y_m, 'g-', lw=2)
    circle, = plt.plot(x_cir, y_cir, 'y-', lw=2)
    parabol, = plt.plot(x_m[:i], y_m[:i], 'r-', lw=2)
    point, = plt.plot(x_m[i], y_m[i], 'bo')
    anim_list.append([liniaq,circle,parabol,point])
    
plt.axes().set_aspect('equal')

ani = ArtistAnimation(fig, anim_list, interval=50)
ani.save('kkkk.gif')

