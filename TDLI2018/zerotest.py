import matplotlib.pyplot as plt
import numpy as np

k=0
x1=[]
x2=[]
for k in range(500):
    x1=np.append(x1,1)
    k=k+1
for k in range(500):
    x2=np.append(x2,0)
x=np.append(x1,x2)
oldu=np.append(x1,x2)
def LaxFriedrichs(M,N):
    global oldu
    i=1
    j=1
    utemporary=[]
    for j in range(N):
        for i in range(M-2):
            a=1/2*(oldu[i+1]+oldu[i-1]-0.5/N/(2*(1/M))*(oldu[i+1]-oldu[i-1]))
            utemporary=np.append(utemporary,a)
            i=i+1
        b=np.zeros(1)
        oldu=np.append(np.append(b,utemporary),b)
        utemporary=[]
        j=j+1
    return oldu
a=1000
b=250
x=np.arange(0,1,1/a)
plt.figure(figsize=(8, 8))
plt.plot(x,LaxFriedrichs(a,b),marker='o',c='r')
plt.xlabel('x')
plt.ylabel('u')
plt.title('Normal Advection Equation for t=0.5')
plt.show()