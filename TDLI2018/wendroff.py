import numpy as np
import matplotlib.pyplot as plt

nx = 200
u = np.zeros(nx)
total_length = 1

dx = total_length / float (nx)
x = np.arange(0, total_length, dx)

tmax = 0.5
time = 0.0

dt = 0.5* dx

u[x<0.5] = 1.0
u[x>=0.5] = 0.0

plt.plot(x,u)
plt.ylim((-1,2))
plt.xlabel('x')
plt.ylabel('u')
plt.show(block=False)

while(time<tmax):
    print('current time is',time)
    # u=u+(np.roll(u,1)-np.roll(u,-1))/(2*dx)*dt+dt**2/(2*dx**2)*(np.roll(u,1)-2*u+np.roll(u,-1))+\
    # 1/6*dt**3/dx**3*(np.roll(u,1)-3*u+3*np.roll(u,-1)-np.roll(u,-2))                             #3th order approximate
    u=u-(np.roll(u,1)-np.roll(u,-1))/(2*dx)*dt+dt**2/(2*dx**2)*(np.roll(u,1)-2*u+np.roll(u,-1))     #2sd order approximate
    # u=u-(np.roll(u,1)-np.roll(u,-1))/(2*dx)*dt                                                      #1st order approximate
    time = time + dt
    plt.cla()
    plt.ylim((-1, 2))
    plt.xlabel('x')
    plt.ylabel('u')
    plt.plot(x, u,c='r')
    plt.show(block=False)
    plt.pause(0.0001)

plt.plot(x,u,c='r')
plt.savefig('/users/dingding/Desktop/31order.jpg')
plt.show()