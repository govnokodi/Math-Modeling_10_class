import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import ArtistAnimation

fig = plt.figure()
ax = p3.Axes3D(fig)

N = 200
t = np.linspace(0, 4.3, N)

def func (s,t):
    x, v_x, y, v_y, z, v_z = s
    dxdt = v_x
    dv_dxt = (x/a**2)*(g -v_x**2/a**2 - v_y/b**2 - v_z/c**2)/(x**2/a**4 + y**2/b**4 + z**2/c**4)
    dydt = v_y
    dv_dyt = (y/b**2)*(g -v_x**2/a**2 - v_y/b**2 - v_z/c**2)/(x**2/a**4 + y**2/b**4 + z**2/c**4)
    dzdt = v_z
    dv_dzt = -g*(y/b**2)*(g -v_x**2/a**2 - v_y/b**2 - v_z/c**2)/(x**2/a**4 + y**2/b**4 + z**2/c**4)
    
    return(dxdt,dv_dxt,
           dydt,dv_dyt,
           dzdt,dv_dzt)

g = 9.8

a = 3
b = 4
z = 5

x0 = 11
v_x0 = 0

y0 = 5
v_y0 = 0

z0 = 3 
v_z0 = 0

s0 = x0,v_x0,y0,v_y0,z0,v_z0

sol = odeint(s0,func,t)

