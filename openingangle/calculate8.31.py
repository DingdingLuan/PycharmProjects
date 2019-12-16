from Calculatefunction import *
import matplotlib.pyplot as plt
import matplotlib
import random

# redshift from 0-9,with interval 10**0.1
eps=0.4
alpha=-1.1
beta=-2.2
rho=2.85*10**2
Narray=[]

# set step of log(1+z):
step=0.05


for i in range(np.int(1/step)):
    z=10**(i*step)-1
    # pro=RGRB(z,eps,alpha,beta,rho)
    pro=N(z,eps,alpha,beta,rho,10)
    Narray=np.append(Narray,pro)

probability=Narray/np.sum(Narray)

# define a new array to constrain the probability distribution:
Proarray=[]
samplenumber=100000  #set a sample with 'samplenumber' GRBs
for j in range(np.int(1/step)):
    number=np.int(samplenumber*probability[j])
    z=10**(j*step)-1
    for k in range(number):
        Proarray=np.append(Proarray,z)

#Generate Monte Carlo mimic method:
mockGRBnumber=170
mocksample=[]
mockredshift=[]
for m in range(mockGRBnumber):
    num=random.randint(0,len(Proarray))
    mocksample=np.append(mocksample,Proarray[num])
for n in range(np.int(1/step)):
    counter=0
    for b in range(len(mocksample)):
        if 10**(step*n)-1<=mocksample[b]<=10**(step*(n+1))-1:
            counter=counter+1
    mockredshift=np.append(mockredshift,counter)
promockredshift=mockredshift/np.sum(mockredshift)





#设置xtick的方向，in,out,inout
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
x=np.arange(0,1,step)
plt.figure(figsize=(7, 7))
# plt.scatter(x,probability,s=5,alpha=1,marker='o',c='r')
plt.bar(x,promockredshift,width=step,edgecolor='r',facecolor='white',linestyle='--')
plt.xlabel("log(z+1)")
plt.ylabel('probability')
# plt.savefig('/Users/dingding/Desktop/origin.eps')
plt.show()

