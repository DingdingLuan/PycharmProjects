import numpy as np
import matplotlib.pyplot as plt

tmax = 20.0
dt = 0.02
time = np.arange(0.0, tmax, dt)


lambd = 100.0
u = np.zeros(len(time))
u[0] = 1.0
for i in range(len(time)-1):
    dudt = -lambd * (u[i+1] - np.sin(time[i+1]))
    u[i+1] = u[i]  + dt * dudt

    plt.cla()
    plt.xlabel('t')
    plt.ylabel('u')
    plt.plot(time,u,label='numerical solution')
    plt.plot(time,np.sin(time),ls='dashed',label=r'$\sin t$')
    plt.title(f'time={time[i]:.2f}')
    plt.legend()
    plt.show(block = False)
    plt.pause(0.0001)
plt.plot(time,u,label='numerical solution')
plt.show()