from Calculatefunction import *
eps=0.4
alpha=-1.1
beta=-2.2
rho=1
samplenumber=170

#------------------------------------------------------------------------------------------------------
zmocksample=[]
lmocksample=[]
thetamocksample=[]
lmin=46
lmax=52
P_mock=[]
i=0
while i<samplenumber:
    a=random.uniform(10**(-2.5),10**(0.))
    b=random.uniform(0,2.1)
    theta=a/np.pi*180
    if b<=thetalogdistri(a):
        while True:
            a=random.uniform(0.01, 10)
            b=random.uniform(0,2.5)
            z=a
            if b<=RGRB(a,eps,alpha,beta,rho):
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
        if p<80: #and l/(1-np.cos(theta/180*np.pi))<10**55 :
            a=random.uniform(0,1)
            b=random.uniform(0,1)
            c=random.uniform(0,1)
            if 0<a*b*c<eta_t(p)*eta_z(p)*eta_a(theta/180*np.pi):
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
for i in range(20):
    counter=0
    for j in range(170):
        if 10**(i*0.05)-1<=zmock[j]<=10**((i+1)*0.05)-1:
            counter=counter+1
    proz=np.append(proz,counter)
proz=proz/np.sum(proz)

# n=20
# for i in range(n):
#     proz[i]=proz[i]/(10**((i+1)*1/n)-10**(i*1/n))
# ------------------------------------------------------------------------------------------------------

for i in range(20):
    counter=0
    for j in range(170):
        if 10.**(49+i*0.3)<=lmock[j]<=10.**(49+(i+1)*0.3):
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

for i in range(10):
    counter=0
    for j in range(77):
        if 10.**(-2.5+0.25*i)<=subsampletheta[j]/180*np.pi<=10.**(-2.5+0.25*(i+1)):
            counter=counter+1
    protheta=np.append(protheta,counter)
protheta=protheta/np.sum(protheta)

# n=10
# for i in range(n):         # assign the weight
#     protheta[i]=protheta[i]/(10**(min+(max-min)/n*(i+1))-10**(min+(max-min)/n*i))

for i in range(10):
    counter=0
    for j in range(77):
        if 10**(i*0.1)-1<=subsamplez[j]<=10**((i+1)*0.1)-1:
            counter=counter+1
    prothetaz=np.append(prothetaz,counter)
prothetaz=prothetaz/np.sum(prothetaz)

# n=10
# for i in range(n):
#     prothetaz[i]=prothetaz[i]/(10**((i+1)*1/n)-10**(i*1/n))

#------------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#
#
#
#
#
#------------------------------------------------------------------------------------------------------


# plot the cumulation figure of P:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.arange(-1,2,3/num)           #plot z
# plt.plot(x,np.log10(prop),linewidth=2,c='red',linestyle='--')
plt.bar(x,np.log10(prop),width=3/num,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 170")
plt.xlabel(r'$P(photons cm^{-2}s^{-1})$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/z9.17.eps')
plt.show()


# plot the result of theta:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
t=np.arange(-2.5,0,0.25)          #plot theta
plt.bar(t,protheta,width=0.25,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 77")
plt.xlabel(r'$log(\theta_{j}/rad)$')
plt.ylabel('$Probability$')
plt.savefig('/Users/dingding/Desktop/calculate/9.17/theta9.17.eps')
# plt.show()


# plot the result of z:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.arange(0,1,0.05)           #plot z
plt.bar(x,proz,width=0.05,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 170")
plt.xlabel('$log(z+1)$')
plt.ylabel('$Probability$')
plt.savefig('/Users/dingding/Desktop/calculate/9.17/z9.17.eps')
# plt.show()





# plot the result of luminosity:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
y=np.arange(49,54,0.25)            #plot l
plt.bar(y,prol,width=0.25,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 170")
plt.xlabel('$log(L/ erg  s^{-1})$')
plt.ylabel('$Probability$')
plt.savefig('/Users/dingding/Desktop/calculate/9.17/luminosity9.17.eps')
# plt.show()
#
#
#
# plot z-l distribution
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
plt.scatter(np.log10(zmock+1),np.log10(lmock),s=5,alpha=1,marker='o',c='r')
plt.title("Mock sample = 170")
plt.xlabel('$log(z+1)$')
plt.ylabel('$log(L/ erg  s^{-1})$')
plt.savefig('/Users/dingding/Desktop/calculate/9.17/z-ldistribution.eps')
# plt.show()


# plot z-theta distribution
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
plt.scatter(np.log10(subsamplez+1),np.log10(subsampletheta/180*np.pi),s=5,alpha=1,marker='o',c='r')
plt.title("Mock sample = 77")
plt.xlabel('$log(z+1)$')
plt.ylabel(r'$log(\theta_{j}/rad$)')
plt.savefig('/Users/dingding/Desktop/calculate/9.17/z-thetadistribution9.17.eps')
# plt.show()

# plot z distribution in subsample:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.arange(0,1,0.1)
plt.bar(x,prothetaz,width=0.1,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 77")
plt.xlabel('$log(z+1)$')
plt.ylabel('$Probability$')
plt.savefig('/Users/dingding/Desktop/calculate/9.17/zdistributioninsubsample9.17.eps')

#------------------------------------------------------------------------------------------------------