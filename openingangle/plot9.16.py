import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

df=pd.read_excel("/Users/dingding/Desktop/calculate/9.15/result9.15.xlsx")
zmock= df['z']
lmock=df['luminosity']
thetamock=df['theta_jet']
pmock=df['peak_flux']


proz=[]
prol=[]
protheta=[]

for i in range(20):
    counter=0
    for j in range(170):
        if 10**(i*0.05)-1<=zmock[j]<=10**((i+1)*0.05)-1:
            counter=counter+1
    proz=np.append(proz,counter)
proz=proz/np.sum(proz)

for i in range(20):
    counter=0
    for j in range(170):
        if 10.**(49+i*0.3)<=lmock[j]<=10.**(49+(i+1)*0.3):
            counter=counter+1
    prol=np.append(prol,counter)
prol=prol/np.sum(prol)

for i in range(10):
    counter=0
    for j in range(170):
        if 10.**(-2.5+0.25*i)<=thetamock[j]/180*np.pi<=10.**(-2.5+0.25*(i+1)):
            counter=counter+1
    protheta=np.append(protheta,counter)
protheta=protheta/np.sum(protheta)

# 设置xtick的方向，in,out,inout
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
# plt.scatter(np.log10(zmock+1),np.log10(thetamock/180*np.pi),s=5,alpha=1,marker='o',c='r')
# x=np.arange(0,1,0.05)           #plot z
# y=np.arange(49,55,0.3)            #plot l
t=np.arange(-2.5,0,0.25)          #plot theta
# plt.bar(x,proz,width=0.05,edgecolor='r',facecolor='white',linestyle='--')
# plt.bar(y,prol,width=0.3,edgecolor='r',facecolor='white',linestyle='--')
plt.bar(t,protheta,width=0.25,edgecolor='r',facecolor='white',linestyle='--')
# plt.xlabel('$log(z+1)$')
# plt.xlabel('$log(L/ erg  s^{-1})$')
plt.xlabel(r'$log(\theta_{j}/rad)$')
plt.ylabel('$Probability$')
# plt.ylabel('$log(L/erg /s^{-1})$')
# plt.ylabel(r'$log(\theta_{j}/rad$)')
plt.savefig('/Users/dingding/Desktop/Theta_distribution9.16.eps')
plt.show()