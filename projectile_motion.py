import numpy as np
import matplotlib.pylab as plot
import math as m


# constants
m = 2.0  # mass of cannonball
g = 9.81  # acceleration due to gravity
dt = 0.1  # time step


def compute_forces(x):
    f = np.array([0.0, -m*g])
    return f


def step_euler(x, v, dt):
    f = compute_forces(x)
    x = x + v * dt
    v = v + (f/m)*dt
    return x, v


#  Initial variables
t = 0.0  # Initial time
# Initial position (position 0 is x and position 1 is y)
x = np.array([0.0, 0.0])
v = np.array([50.0, 50.0])  # Initial velocity
# trajectory is a list that will accumulate the values of x in the different
# time steps
traj = []
# Main Program
# Integrate until  y < 0 (cannonball hits the ground)

while x[1] >= 0.0:
    x, v = step_euler(x, v, dt)  # propagate the cannonball
    t += dt  # time step
    # append current position of cannonball to trajectory
    traj.append(x.copy())

traj = np.array(traj)
plot.plot(traj[:, 0], traj[:, 1], '-')
plot.show()
