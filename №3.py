from phyconst import g
import numpy as np
t = np.arange(0, 6, 0.01)
x0 = 0
y0 = 0
V0 = 0
A = np.ndarray(shape=(10,3))
for i in t:
    x = x0 + V0*t
    y = y0 + V0*t- (g*t**2)/2
    print(A)
    
    
