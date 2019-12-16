import numpy as np
from test import LaxFriedrichs
import matplotlib.pyplot as plt


a=100
b=25
x=np.arange(0,1,1/a)
LaxFriedrichs(a,b)
# plt.figure(figsize=(8, 8))
# # plt.scatter(x,LaxFriedrichs(a,b),s=3,alpha=1,marker='o',c='r')
# plt.plot(x,LaxFriedrichs(a,b),marker='*',c='r')
# plt.xlabel('x')
# plt.ylabel('u')
# plt.title('Normal Advection Equation for t=0.5')
# plt.show()


# tmax = 0.5  # Time to perform integration to
# time = 0.0
# while(time < tmax):    # While time has not yet reached tmax
#     print("time:",time) # Print the current time
#     # Lax-Friedrichs scheme:
#     #   Where the solution at x_i, t_n is u(i, n),
#     #   u(i,n+1) = 0.5*(u(i-1,n)+u(i+1,n)) + dt*(u(i+1)-u(i-1))/(2*dx)
#     # For brief description, see: https://en.wikipedia.org/wiki/Lax-Friedrichs_method
#     #   Note: in our case, a=1
#     # NumPy trick:
#     #   np.roll will shift the entire array by the specified amount, so the finite differences
#     #   can be calculated in a single vector operation, rather than in a loop
#     u = LaxFriedrichs(a,b)
#
#     time = time + dt    # Increment time
#     # plt.cla()          # Clear the axis to prevent repeatedly plotting on top of old lines
#     plt.ylim((0,2))   # Set the plotting limits in the y-direction
#     plt.xlabel('x')    # x-label for plot
#     plt.ylabel('u')    # y-label for plot
#     plt.plot(x,u)      # Plot updated data
#     plt.show(block=False) # Tell matplotlib to show the plot (block=False allows the code to continue)
#     plt.pause(0.01) # Pa