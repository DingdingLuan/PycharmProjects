import numpy as np

a= np.linspace(0,1,100)


# plt.show(block=False)  #let the code continun

n=np.zeros(10)
n=np.append(1,n)
n=np.append(n,1)
print(n)
m=np.roll(n,3)
print(m)