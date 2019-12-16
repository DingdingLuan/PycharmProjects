from Calculatefunction import *
import numpy as np

integralnumber=10000
eps=0.4
alpha=-1.1
beta=-2.2
rho=1
samplenumber=300

proz=[]
prol=[]
zmock=[]


#generate the new z-distribution function from N:
zpdf=[]
for i in range(integralnumber):
    # z=10**(i*1/integralnumber)-1
    # zmax=10**((i+1)*1/integralnumber)-1
    z=10/integralnumber*i
    zmax=10/integralnumber*(i+1)
    zpdf=np.append(zpdf,N(z,eps,alpha,beta,rho,zmax))
zpdf=zpdf/np.sum(zpdf)



#test monte carlo for z:
# standard=np.max(zpdf)
# i=0
# while i<samplenumber:
#     a=np.random.uniform(0.,10)
#     b=np.random.uniform(0,standard)
#     aa=np.int(np.log10(a+1)*integralnumber)
#     if aa<=integralnumber:
#         if zpdf[aa]>=b:
#             zmock=np.append(zmock,a)
#             i=i+1
#         else:
#             continue
# n=20
# for i in range(n):
#     counter=0
#     for j in range(170):
#         if 10**(i*1/n)-1<=zmock[j]<=10**((i+1)*1/n)-1:
#             counter=counter+1
#     proz=np.append(proz,counter)
# proz=proz/np.sum(proz)
#
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# x=np.arange(0,1,1/n)           #plot z
# plt.bar(x,proz,width=1/len(x),edgecolor='r',facecolor='white',linestyle='--')
# # plt.savefig('/Users/dingding/Desktop/calculate/9.18/mockz.eps')
# plt.show()





#------------------------------------------------------------------------------------------------------
zmocksample=[]
lmocksample=[]
thetamocksample=[]
lmin=46
lmax=52
P_mock=[]
i=0
standard=np.max(zpdf)


while i<samplenumber:
    a=random.uniform(10**(-2.),10**(-0.5))
    b=random.uniform(0,1.87960)
    theta=a/np.pi*180
    if b<=thetalogdistri(a):
        # c=random.uniform(0,1-np.cos(10**(-1.27)))
        # c=random.uniform(0,1)
        # if eta_a(a)>c:
            while True:
                a=random.uniform(0.,10)
                b=np.random.uniform(0,standard)
                z=a
                aa=np.int(a/10*integralnumber)
                if aa<integralnumber:
                    if zpdf[aa]>=b:
                        break
                    else:
                        continue
            while True:
                a=random.uniform(10.**lmin,10.**lmax)
                b=random.uniform(0,6*10.**(-51))
                l=a
                if b<=Luminosityfunction(a):
                    break
                else:
                    continue
            p=P(z,l,theta)
            if p<85:                                                #normalize the probability of p-z
                a=random.uniform(0,1)
                if 0<a<eta_t(p):
                    a=random.uniform(0,1)
                    if 0<a<eta_z(p):
                        P_mock=np.append(P_mock,p)
                        zmocksample=np.append(zmocksample,z)
                        thetamocksample=np.append(thetamocksample,theta)
                        lmocksample=np.append(lmocksample,l/(1-np.cos(theta/180*np.pi)))
                        # lmocksample=np.append(lmocksample,l)
                        i=i+1
#------------------------------------------------------------------------------------------------------
# print('pmock:',P_mock)
# print('zmock:',zmocksample)
# print('lmock:',lmocksample)
# print('thetamock:',thetamocksample)
zmock= zmocksample
lmock=lmocksample
thetamock=thetamocksample
pmock=P_mock

proz=[]
prol=[]
protheta=[]
prothetaz=[]
prop=[]

#------------------------------------------------------------------------------------------------------
z170num=22
for i in range(z170num):
    counter=0
    for j in range(170):
        if 10**(i*1/z170num)-1<=zmock[j]<=10**((i+1)*(1/z170num))-1:
            counter=counter+1
    proz=np.append(proz,counter)
proz=proz/np.sum(proz)

# n=20
# for i in range(n):
#     proz[i]=proz[i]/(10**((i+1)*1/n)-10**(i*1/n))
# ------------------------------------------------------------------------------------------------------
lnum=22
for i in range(lnum):
    counter=0
    for j in range(170):
        if 10.**(49+i*6/lnum)<=lmock[j]<=10.**(49+(i+1)*6/lnum):
            counter=counter+1
    prol=np.append(prol,counter)
prol=prol/np.sum(prol)

# n=20
# for i in range(n):
#     prol[i]=prol[i]/(10.**(46+(i+1)*(6/n))-10.**(46+i*(6/n)))

# calculate the cumulation of the P:
num=40
for i in range(num):
    counter=0
    for j in range(samplenumber):
        if pmock[j]>=10**(-1+3/num*i):
            counter=counter+1
    prop=np.append(prop,counter)
prop=prop/prop[0]
# print(pmock)
#------------------------------------------------------------------------------------------------------

# randomly pick 77 grbs subsample from mock sample with 170 grbs:
i=0
subsamplez=[]
subsampletheta=[]
min=-2.5
max=0
while i<77:
    a=random.randint(0,169)
    subsamplez=np.append(subsamplez,zmock[a])
    subsampletheta=np.append(subsampletheta,thetamock[a])
    i=i+1

thetanum=12
for i in range(thetanum):
    counter=0
    for j in range(77):
        if 10.**(-2.5+2.5/thetanum*i)<=subsampletheta[j]/180*np.pi<=10.**(-2.5+2.5/thetanum*(i+1)):
            counter=counter+1
    protheta=np.append(protheta,counter)
protheta=protheta/np.sum(protheta)

# n=10
# for i in range(n):         # assign the weight
#     protheta[i]=protheta[i]/(10**(min+(max-min)/n*(i+1))-10**(min+(max-min)/n*i))

z77num=10
for i in range(z77num):
    counter=0
    for j in range(77):
        if 10**(i*1/z77num)-1<=subsamplez[j]<=10**((i+1)*1/z77num)-1:
            counter=counter+1
    prothetaz=np.append(prothetaz,counter)
prothetaz=prothetaz/np.sum(prothetaz)

# n=10
# for i in range(n):
#     prothetaz[i]=prothetaz[i]/(10**((i+1)*1/n)-10**(i*1/n))

#------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df=pd.read_excel("/Users/dingding/Desktop/calculate/10.7/table1.xlsx")
zreal=df['z']
thetareal=df['theta']

proz1=[]
protheta1=[]


z77num=10
for i in range(z77num):
    counter=0
    for j in range(77):
        if 10**(i*1/z77num)-1<=zreal[j]<=10**((i+1)*1/z77num)-1:
            counter=counter+1
    proz1=np.append(proz1,counter)
proz1=proz1/np.sum(proz1)


thetanum=12
for i in range(thetanum):
    counter=0
    for j in range(77):
        if 10.**(-2.5+2.5/thetanum*i)<=thetareal[j]<=10.**(-2.5+2.5/thetanum*(i+1)):
            counter=counter+1
    protheta1=np.append(protheta1,counter)
protheta1=protheta1/np.sum(protheta1)
#
#
from scipy.stats import ks_2samp

print(ks_2samp(prothetaz,proz1)[1])
print(ks_2samp(protheta,protheta1)[1])

#
#
#
#
#
#
#
#------------------------------------------------------------------------------------------------------


# # plot the cumulation figure of P:

matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.arange(-1,2,3/num)           #plot z
# plt.plot(x,np.log10(prop),linewidth=2,c='red',linestyle='--')
plt.bar(x,np.log10(prop),width=3/num,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 170")
plt.xlabel(r'$P(photons cm^{-2}s^{-1})$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/p.eps')
plt.show()

#
# plot the result of theta:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
t=np.arange(-2.5,0,2.5/thetanum)          #plot theta
plt.bar(t,protheta,width=2.5/thetanum,edgecolor='r',facecolor='w',linestyle='--')
# plt.bar(t,protheta1,width=2.5/thetanum,edgecolor='b',facecolor='yellow',linestyle='-')
plt.title("Mock sample = 77")
plt.xlabel(r'$log(\theta_{j}/rad)$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/theta9.17.eps')
plt.show()
# #
#
# # plot the result of z:
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# x=np.arange(0,1,1/z170num)           #plot z
# plt.bar(x,proz,width=1/z170num,edgecolor='r',facecolor='white',linestyle='--')
# plt.title("Mock sample = 170")
# plt.xlabel('$log(z+1)$')
# plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/z9.17.eps')
# plt.show()
#
#
#
#
#
# plot the result of luminosity:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
y=np.arange(49,55,6/lnum)            #plot l
plt.bar(y,prol,width=6/lnum,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 170")
plt.xlabel('$log(L/ erg  s^{-1})$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/luminosity9.17.eps')
plt.show()
# #
# #
# #
# plot z-l distribution
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
plt.xlim(0,1)
plt.ylim(49,54.5)
plt.scatter(np.log10(zmock+1),np.log10(lmock),s=77,alpha=1,marker='o',c='',edgecolors='r')
plt.title("Mock sample = 170")
plt.xlabel('$log(z+1)$')
plt.ylabel('$log(L/ erg  s^{-1})$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/z-ldistribution.eps')
plt.show()
#
#
# plot z-theta distribution
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
plt.ylim(-2.5,0)
plt.xlim(0,1)
plt.scatter(np.log10(subsamplez+1),np.log10(subsampletheta/180*np.pi),s=77,alpha=1,marker='o',c='',edgecolors='r')
plt.scatter(np.log10(zreal+1),np.log10(thetareal),s=77,alpha=1,marker='o',c='',edgecolors='b')
plt.title("Mock sample = 77")
plt.xlabel('$log(z+1)$')
plt.ylabel(r'$log(\theta_{j}/rad$)')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/z-thetadistribution9.17.eps')
plt.show()
#
# plot z distribution in subsample:
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# x=np.arange(0,1,1/z77num)
# plt.bar(x,prothetaz,width=1/z77num,edgecolor='r',facecolor='red',linestyle='--')
# plt.bar(x,proz1,width=1/z77num,edgecolor='b',facecolor='yellow',linestyle='-')
# plt.title("Mock sample = 77")
# plt.xlabel('$log(z+1)$')
# plt.ylabel('$Probability$')
# # plt.savefig('/Users/dingding/Desktop/calculate/9.17/zdistributioninsubsample9.17.eps')
# plt.show()
#------------------------------------------------------------------------------------------------------