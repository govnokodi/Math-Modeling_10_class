import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], marker='o')
def circle_m(R, t):
    x = R*(t - np.sin(t))
    y = R*(1 - np.cos(t))
    return x, y

edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    anim_object.set_data(circle_m(R=3, t=i))
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=np.arange(-4, 4, 0.1),
                              interval=200)

ani.save('animate.gif')
