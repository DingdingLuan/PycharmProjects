from Calculatefunction import *

eps=0.4
alpha=-1.1
beta=-2.2
rho=1
samplenumber=170
generatenum=1000
#------------------------------------------------------------------------------------------------------
zmocksample=[]
lmocksample=[]
thetamocksample=[]
lmin=46
lmax=52
P_mock=[]

zgenerate=[]
lgenerate=[]
thetagenerate=[]
#------------------------------------------------------------------------------------------------------
#Generate bulk of z:
i=0
while i<generatenum:
    a = random.uniform(0.01, 10)
    b = random.uniform(0, 0.301)
    z = a
    if b <= RGRB(z, eps, alpha, beta, rho):
        zgenerate=np.append(zgenerate,a)
        i=i+1
    else:
        continue

#Generate bulk of L_gamma:
i=0
while i<generatenum:
    a = random.uniform(lmin, lmax)
    b = random.uniform(0, 6 * 10. ** (-51))
    l = 10 ** a
    if b <= Luminosityfunction(l):
        lgenerate=np.append(lgenerate,10**a)
        i=i+1
    else:
        continue

#Generate bulk of theta_jet:
i=0
while i<generatenum:
    a = random.uniform(-2., 0.5)
    b = random.uniform(0, 1.1617)
    theta = 10 ** a / np.pi * 180
    if b <= thetalogdistri(10 ** a):
        thetagenerate=np.append(thetagenerate,theta)
        i=i+1
    else:
        continue
#------------------------------------------------------------------------------------------------------
# mock sample generating:
i=0
while i<samplenumber:
    a = random.randint(0, generatenum-1)
    b = random.randint(0, generatenum-1)
    c = random.randint(0, generatenum-1)
    p=P(zgenerate[a],lgenerate[b],thetagenerate[c])
    x=random.uniform(0,1)
    if p<89:
        if eta_t(p)>x:
            y=random.uniform(0,1)
            if eta_z(p)>y:
                z = random.uniform(0, 1)
                if eta_a(thetagenerate[c]/180*np.pi)>z:
                    i=i+1
                    P_mock=np.append(P_mock,p)
                    zmocksample=np.append(zmocksample, zgenerate[a])
                    thetamocksample=np.append(thetamocksample,thetagenerate[c])
                    lmocksample=np.append(lmocksample,lgenerate[b]/(1-np.cos(thetagenerate[c]/180*np.pi)))
#------------------------------------------------------------------------------------------------------








# #------------------------------------------------------------------------------------------------------
#
#previously work:
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


# ------------------------------------------------------------------------------------------------------

for i in range(20):
    counter=0
    for j in range(170):
        if 10.**(49+i*0.3)<=lmock[j]<=10.**(49+(i+1)*0.3):
            counter=counter+1
    prol=np.append(prol,counter)
prol=prol/np.sum(prol)


# calculate the cumulation of the P:
num=40
for i in range(num):
    counter=0
    for j in range(samplenumber):
        if pmock[j]>=10**(-1+3/num*i):
            counter=counter+1
    prop=np.append(prop,counter)
prop=prop/prop[0]

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

thetastep=2.5/12
for i in range(12):
    counter=0
    for j in range(77):
        if 10.**(-2.5+thetastep*i)<=subsampletheta[j]/180*np.pi<=10.**(-2.5+thetastep*(i+1)):
            counter=counter+1
    protheta=np.append(protheta,counter)
protheta=protheta/np.sum(protheta)

# n=10
# for i in range(n):         # assign the weight
#     protheta[i]=protheta[i]/(10**(min+(max-min)/n*(i+1))-10**(min+(max-min)/n*i))

subzstep=1/12
for i in range(12):
    counter=0
    for j in range(77):
        if 10**(i*subzstep)-1<=subsamplez[j]<=10**((i+1)*subzstep)-1:
            counter=counter+1
    prothetaz=np.append(prothetaz,counter)
prothetaz=prothetaz/np.sum(prothetaz)







#------------------------------------------------------------------------------------------------------

# plot the result of theta:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
t=np.arange(-2.5,0,thetastep)          #plot theta
plt.xlim(-2.5,0)
plt.bar(t,protheta,width=thetastep,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 77")
plt.xlabel(r'$log(\theta_{j}/rad)$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/theta9.17.eps')
plt.savefig('/home/luantch/calculate10.22/theta.eps')
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
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/z9.17.eps')
# plt.show()
plt.savefig('/home/luantch/calculate10.22/z.eps')


# plot z distribution in subsample:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.arange(0,1,subzstep)
plt.bar(x,prothetaz,width=subzstep,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 77")
plt.xlabel('$log(z+1)$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/zdistributioninsubsample9.17.eps')
# plt.show()
plt.savefig('/home/luantch/calculate10.22/subz.eps')


# plot the result of luminosity:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
y=np.arange(49,55,0.3)            #plot l
plt.bar(y,prol,width=0.3,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 170")
plt.xlabel('$log(L/ erg  s^{-1})$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/luminosity9.17.eps')
# plt.show()
plt.savefig('/home/luantch/calculate10.22/luminous.eps')


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
# plt.show()
plt.savefig('/home/luantch/calculate10.22/p.eps')