import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import ks_2samp

df=pd.read_excel("/Users/dingding/Desktop/calculate/10.7/table1.xlsx")
zreal=df['z']
thetareal=df['theta']

proz=[]
protheta=[]


z77num=10
for i in range(z77num):
    counter=0
    for j in range(77):
        if 10**(i*1/z77num)-1<=zreal[j]<=10**((i+1)*1/z77num)-1:
            counter=counter+1
    proz=np.append(proz,counter)
proz=proz/np.sum(proz)


thetanum=5
for i in range(thetanum):
    counter=0
    for j in range(77):
        if 10.**(-2.5+2.5/thetanum*i)<=thetareal[j]<=10.**(-2.5+2.5/thetanum*(i+1)):
            counter=counter+1
    protheta=np.append(protheta,counter)
protheta=protheta/np.sum(protheta)


# # plot z distribution in subsample:
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# x=np.arange(0,1,1/z77num)
# plt.bar(x,proz,width=1/z77num,edgecolor='b',facecolor='white',linestyle='-')
# plt.title("Sample = 77")
# plt.xlabel('$log(z+1)$')
# plt.ylabel('$Probability$')
# # plt.savefig('/Users/dingding/Desktop/calculate/9.17/zdistributioninsubsample9.17.eps')
# plt.show()

# plot the result of theta:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
t=np.arange(-2.5,0,2.5/thetanum)          #plot theta
plt.bar(t,protheta,width=2.5/thetanum,edgecolor='b',facecolor='white',linestyle='-')
plt.title("Sample = 77")
plt.xlabel(r'$log(\theta_{j}/rad)$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/theta9.17.eps')
plt.show()


# # plot z-theta distribution
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# plt.ylim(-2.5,0)
# plt.xlim(0,1)
# plt.scatter(np.log10(zreal+1),np.log10(thetareal),s=77,alpha=1,marker='o',c='',edgecolors='b')
# plt.title("Sample = 77")
# plt.xlabel('$log(z+1)$')
# plt.ylabel(r'$log(\theta_{j}/rad$)')
# # plt.savefig('/Users/dingding/Desktop/calculate/9.17/z-thetadistribution9.17.eps')
# plt.show()