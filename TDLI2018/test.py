import matplotlib.pyplot as plt
import numpy as np



k=0
# N=100
# M=50
x1=[]
x2=[]
# t=[]
# axixx=np.arange(0,100,1)

# build the position and time array:
for k in range(50):
    x1=np.append(x1,1)
    k=k+1
for k in range(50):
    x2=np.append(x2,0)
x=np.append(x1,x2)
oldu=np.append(x1,x2)

# for k in range(50):
#     t=np.append(t,0.5/50)
#     k=k+1
# # use Lax-Friedrichs Method:
# # set the position element x and time variation t for the next time interval:
# xnew=[]
#
# for i in range(99):
#     for j in range(49):
#         a=1/2*(x[i+1]+x[i-1])-0.01/(2*0.01)*(x[i+1]-x[i-1])
#         j=j+1
#     xnew=np.append(xnew,a)
#     i=i+1
# newx=np.append(0,xnew)
# print(newx[80])
# print(oldx[80])


# plt.figure(figsize=(8, 8))
# plt.scatter(axixx,newx,s=5,alpha=1,marker='o',c='r')
# plt.show()
# def LaxFriedrichs(M,N):
#     global oldu
#     i=1
#     j=1
#     utemporary=[]
#     for j in range(N):
#         for i in range(M-2):
#             a=1/2*(oldu[i+1]+oldu[i-1]-0.5/N/(2*(1/M))*(oldu[i+1]-oldu[i-1]))
#             utemporary=np.append(utemporary,a)
#             i=i+1
#         b=np.zeros(1)
#         oldu=np.append(np.append(b,utemporary),b)   there is the problem .this is not append 0 but roll!!!!!!!!5.18
#         utemporary=[]
#         plt.cla()
#         plt.ylim((0, 2))  # Set the plotting limits in the y-direction
#         plt.xlabel('x')  # x-label for plot
#         plt.ylabel('oldu')  # y-label for plot
#         plt.plot(x, oldu)  # Plot updated data
#         plt.show(block=False)  # Tell matplotlib to show the plot (block=False allows the code to continue)
#         plt.pause(0.01)
#         j=j+1
#     return plt.show
#


