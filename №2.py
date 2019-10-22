from phyconst import Hh, g, k, e 
from math import tan, sqrt, pi, cos 
B = 0.52 
h = 100
alf = pi/3
v = sqrt(g*h*1/(tan(B))**2/2*(cos(alf))**2*(1-tan(B)*tan(alf)))
print(v)

T = 200
ee = 300    
N = 2/sqrt(pi)*Hh/(k*T)**1.5*e**(-ee/k*T)*ee**(T/2)
print(N)

