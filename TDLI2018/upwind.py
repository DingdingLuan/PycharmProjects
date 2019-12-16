import numpy as np
import matplotlib.pyplot as plt

nx = 100
u = np.zeros(nx)
total_length = 1

dx = total_length / float (nx)
x = np.arange(0, total_length, dx)

tmax = 0.5
time = 0.0

dt = 0.7* dx

u[x<0.5] = 1.0
u[x>=0.5] = 0.0

plt.plot(x,u)
plt.ylim((-1,2))
plt.xlabel('x')
plt.ylabel('u')
plt.show(block=False)

while(time<tmax):
    print('current time is',time)
    u=u+(np.roll(u,1)-u)/dx*dt
    time = time + dt
    plt.cla()
    plt.ylim((-1, 2))
    plt.xlabel('x')
    plt.ylabel('u')
    plt.plot(x, u)
    plt.show(block=False)
    plt.pause(0.005)
plt.plot(x,u)
plt.show()