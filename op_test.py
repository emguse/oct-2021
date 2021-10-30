import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Equations of motion for the two-body problem
def func(x, t):
    GM = 398600.4354360959 # km3/s2
    r = np.linalg.norm(x[0:3])
    dxdt = [x[3],
            x[4],
            x[5],
            -GM*x[0]/(r**3),
            -GM*x[1]/(r**3),
            -GM*x[2]/(r**3)]
    return dxdt

# Initial conditions for differential equations
x0 = [10000, 0, 0, 0, 7, 0] # position(x,y,z)+speed(vx,vy,vz)
t = np.linspace(0, 86400, 1000) # for one day Orbit Propagation

# Numerical computation of differential equations
sol = odeint(func, x0, t)

# plot
plt.plot(sol[:,0],sol[:,1], 'b')
plt.grid()
plt.gca().set_aspect('equal')
plt.show()

plt.savefig('./test/OP.png')