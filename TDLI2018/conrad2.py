import numpy as np                  # NumPy library for arrays
import matplotlib.pyplot as plt     # Matplotlib library for plotting
from test import oldu

nx = 100            # Number of grid points
u = np.zeros(nx)    # Initialise the grid of u values
total_length = 1    # Physical length of the grid

dx = total_length / float (nx)      # Calculate dx using the length divided by number of grid points
x = np.arange(0, total_length, dx)  # x-coordinate of each grid point

tmax = 0.5  # Time to perform integration to
time = 0.0  # Initial time

dt = 1 * dx   # Set the timestep based on the CFL (Courant-Friedrichs-Lewy) condition

# Initial condition: u=1 where x<0.5, and u=0 where x>=0.5
u[x<0.5] = 1.0
u[x>=0.5] = 0.0

plt.plot(x,u)      # Plot initial condition
plt.ylim((0,2))   # Set the plotting limits in the y-direction
plt.xlabel('x')    # x-label for plot
plt.ylabel('u')    # y-label for plot
plt.draw()         # Tell matplotlib to draw the plot

plt.show(block=False)   # Tell matplotlib to show the plot (block=False allows the code to continue)

i=1
while(time < tmax):    # While time has not yet reached tmax
    print("time:",time) # Print the current time
    # Lax-Friedrichs scheme:
    #   Where the solution at x_i, t_n is u(i, n),
    #   u(i,n+1) = 0.5*(u(i-1,n)+u(i+1,n)) + dt*(u(i+1)-u(i-1))/(2*dx)
    # u = 0.5 * (np.roll (u,-1) + np.roll (u,1)) + \
    #     dt * (np.roll (u,1) - np.roll (u,-1)) / (2.0 * dx)
    utemporary=[]
    for i in range(98):
        a=1/2*(oldu[i+1]+oldu[i-1]-0.5*(oldu[i+1]-oldu[i-1]))
        utemporary=np.append(utemporary,a)
        b=np.zeros(1)
        i=i+1
    oldu = np.append(np.append(b, utemporary), b)
    time = time + dt    # Increment time
    plt.cla()          # Clear the axis to prevent repeatedly plotting on top of old lines
    plt.ylim((0,2))   # Set the plotting limits in the y-direction
    plt.xlabel('x')    # x-label for plot
    plt.ylabel('u')    # y-label for plot
    plt.plot(x,oldu)      # Plot updated data
    plt.show(block=False) # Tell matplotlib to show the plot (block=False allows the code to continue)
    plt.pause(0.01) # Pause for a short time for animation
plt.plot(x,oldu)
plt.show()