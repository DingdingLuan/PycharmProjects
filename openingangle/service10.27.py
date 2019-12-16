from Calculatefunction import *
import time

start=time.clock()
eps=0.4
alpha=-1.1
beta=-2.2
rho=1
samplenumber=170
generatenum=500000
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
    b = random.uniform(0, 0.308)
    if b <= RGRB(a, eps, alpha, beta, rho):
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
    a = random.uniform(-2.,-0.5)
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
for i in range(generatenum):
        p = P(zgenerate[i], lgenerate[i], thetagenerate[i])
        if p>0.2:
            x=random.uniform(0,1)
            if eta_t(p)>x:
                y=random.uniform(0,1)
                if eta_z(p)>y:
                    z = random.uniform(0, 1)
                    if eta_a(thetagenerate[i] / 180 * np.pi) > z:
                        P_mock=np.append(P_mock,p)
                        zmocksample=np.append(zmocksample, zgenerate[i])
                        thetamocksample=np.append(thetamocksample,thetagenerate[i])
                        lmocksample=np.append(lmocksample,lgenerate[i]/(1-np.cos(thetagenerate[i]/180*np.pi)))

#------------------------------------------------------------------------------------------------------
print('original samplenumber:',len(zmocksample))



#------------------------------------------------------------------------------------------------------
zmock= zmocksample
lmock=lmocksample
thetamock=thetamocksample
pmock=P_mock

proz=[]
prol=[]
protheta=[]
prothetaz=[]
prop=[]

# print('complete-zmocksample:',zmocksample)
data = pd.DataFrame(zmocksample)
data.to_csv('/home/luantch/calculate10.27/csvresult/complete-zmocksample.csv')

# print('complete-lmocksample:',lmock)
data = pd.DataFrame(lmock)
data.to_csv('/home/luantch/calculate10.27/csvresult/complete-lmocksample.csv')

# print('complete-pmock:',pmock)
data = pd.DataFrame(pmock)
data.to_csv('/home/luantch/calculate10.27/csvresult/complete-pmock.csv')
#------------------------------------------------------------------------------------------------------
#take a subsample of 170 grbs:
i=0
yiqilingzmock=[]
yiqilinglmock=[]
yiqilingpmock=[]
yiqilingthetamock=[]
array=np.arange(0,len(zmocksample),1)
array=list(array)
for i in range(samplenumber):
    a=random.randint(0,len(array)-1)
    yiqilingzmock=np.append(yiqilingzmock,zmocksample[array[a]])
    yiqilinglmock=np.append(yiqilinglmock,lmocksample[array[a]])
    yiqilingpmock=np.append(yiqilingpmock,P_mock[array[a]])
    yiqilingthetamock=np.append(yiqilingthetamock,thetamocksample[array[a]])
    del array[a]





#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
for i in range(20):
    counter=0
    for j in range(len(yiqilingzmock)):
        if 10**(i*0.05)-1<=yiqilingzmock[j]<=10**((i+1)*0.05)-1:
            counter=counter+1
    proz=np.append(proz,counter)
proz=proz/np.sum(proz)
#------------------------------------------------------------------------------------------------------
prol=pdflog(yiqilinglmock,49,55,20)
#------------------------------------------------------------------------------------------------------
num=40
for i in range(num):
    counter=0
    for j in range(len(yiqilingzmock)):
        if yiqilingpmock[j]>=10**(-1+3/num*i):
            counter=counter+1
    prop=np.append(prop,counter)
prop=prop/prop[0]
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# randomly pick 77 grbs subsample from mock sample with mimics grbs:
i=0
subsamplez=[]
subsampletheta=[]
min=-2.5
max=0

array=np.arange(0,170,1)
array=list(array)
while i<77:
    a=random.randint(0,len(array)-1)
    subsamplez=np.append(subsamplez,yiqilingzmock[array[a]])
    subsampletheta=np.append(subsampletheta,yiqilingthetamock[array[a]])
    i=i+1
    del array[a]

thetastep=2.5/12
protheta=pdflog(subsampletheta/180*np.pi,-2.5,0,12)

subzstep=1/12
for i in range(12):
    counter=0
    for j in range(77):
        if 10**(i*subzstep)-1<=subsamplez[j]<=10**((i+1)*subzstep)-1:
            counter=counter+1
    prothetaz=np.append(prothetaz,counter)
prothetaz=prothetaz/np.sum(prothetaz)

end = time.clock()

#------------------------------------------------------------------------------------------------------
# print('170zmock:',yiqilingzmock)
data = pd.DataFrame(yiqilingzmock)
data.to_csv('/home/luantch/calculate10.27/csvresult/170zmock.csv')

# print('170lmock:',yiqilinglmock)
data = pd.DataFrame(yiqilinglmock)
data.to_csv('/home/luantch/calculate10.27/csvresult/170lmock.csv')

# print('170pmock:',yiqilingpmock)
data = pd.DataFrame(yiqilingpmock)
data.to_csv('/home/luantch/calculate10.27/csvresult/170pmock.csv')

# print('77subsamplez:',subsamplez)
data = pd.DataFrame(subsamplez)
data.to_csv('/home/luantch/calculate10.27/csvresult/77subsamplez.csv')

# print('77thetamocksample:',subsampletheta)
data = pd.DataFrame(subsampletheta)
data.to_csv('/home/luantch/calculate10.27/csvresult/77thetamocksample.csv')


# print('proz:',proz)
data = pd.DataFrame(proz)
data.to_csv('/home/luantch/calculate10.27/csvresult/proz.csv')

# print('prol:',prol)
data = pd.DataFrame(prol)
data.to_csv('/home/luantch/calculate10.27/csvresult/prol.csv')

# print('prothetaz:',prothetaz)
data = pd.DataFrame(prothetaz)
data.to_csv('/home/luantch/calculate10.27/csvresult/prothetaz.csv')

# print('protheta:',protheta)
data = pd.DataFrame(protheta)
data.to_csv('/home/luantch/calculate10.27/csvresult/protheta.csv')

# print('prop:',np.log10(prop))
data = pd.DataFrame(np.log10(prop))
data.to_csv('/home/luantch/calculate10.27/csvresult/prop.csv')

print('Running time: %s Seconds'%(end-start))

#------------------------------------------------------------------------------------------------------
proz=list(proz)
proz.insert(0,proz[0])

prol=list(prol)
prol.insert(0,prol[0])

protheta=list(protheta)
protheta.insert(0,protheta[0])

prothetaz=list(prothetaz)
prothetaz.insert(0,prothetaz[0])

prop=list(np.log10(prop))
prop.insert(0,prop[0])


linewidth=0.7
# plot the result of theta:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
# t=np.arange(-2.5,0,thetastep)          #plot theta
t=np.linspace(-2.5,0,13)
plt.xlim(-2.5,0)
plt.step(t,protheta,c='r',linestyle='--',linewidth=linewidth)
# plt.bar(t,protheta,width=thetastep,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 77")
plt.xlabel(r'$log(\theta_{j}/rad)$')
plt.ylabel('$Probability$')
plt.savefig('/home/luantch/calculate10.27/theta10.27.eps')
# plt.show()
#
#
# plot the result of z:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.linspace(0,1,21)           #plot z
# plt.bar(x,proz,width=0.05,edgecolor='r',facecolor='white',linestyle='--')
plt.step(x,proz,c='r',linestyle='--',linewidth=linewidth)
plt.title("Mock sample = complete sample")
plt.xlabel('$log(z+1)$')
plt.ylabel('$Probability$')
plt.savefig('/home/luantch/calculate10.27/z_complete10.27.eps')
# plt.show()
#
#
# plot z distribution in subsample:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.linspace(0,1,13)
plt.step(x,prothetaz,c='r',linestyle='--',linewidth=linewidth)
# plt.bar(x,prothetaz,width=subzstep,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 77")
plt.xlabel('$log(z+1)$')
plt.ylabel('$Probability$')
plt.savefig('/home/luantch/calculate10.27/z_subsample10.27.eps')
# plt.show()
#
# plot the result of luminosity:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
y=np.linspace(49,55,21)            #plot l
# plt.bar(y,prol,width=0.3,edgecolor='r',facecolor='white',linestyle='--')
plt.step(y,prol,c='r',linestyle='--',linewidth=linewidth)
plt.title("Mock sample = complete sample")
plt.xlabel('$log(L/ erg  s^{-1})$')
plt.ylabel('$Probability$')
plt.savefig('/home/luantch/calculate10.27/l10.27.eps')
# plt.show()
#
# plot the cumulation figure of P:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
x=np.linspace(-1,2,num+1)           #plot z
# plt.plot(x,np.log10(prop),linewidth=2,c='red',linestyle='--')
plt.step(x,prop,c='r',linestyle='--',linewidth=linewidth)
# plt.bar(x,np.log10(prop),width=3/num,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = complete sample")
plt.xlabel(r'$P(photons cm^{-2}s^{-1})$')
plt.ylabel('$Probability$')
plt.savefig('/home/luantch/calculate10.27/P10.27.eps')
# plt.show()
#
# plot z-l distribution
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
plt.scatter(np.log10(zmock+1),np.log10(lmock),s=5,alpha=1,marker='o',c='r')
plt.ylim(49,54.5)
plt.xlim(0.0,1.0)
plt.title("Mock sample = 170")
plt.xlabel('$log(z+1)$')
plt.ylabel('$log(L/ erg  s^{-1})$')
plt.savefig('/home/luantch/calculate10.27/z-l10.27.eps')
# plt.show()
#
# plot z-theta distribution
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
plt.scatter(np.log10(subsamplez+1),np.log10(subsampletheta/180*np.pi),s=5,alpha=1,marker='o',c='r')
plt.title("Mock sample = 77")
plt.xlim(0.0,1.0)
plt.ylim(-2.5,0.0)
plt.xlabel('$log(z+1)$')
plt.ylabel(r'$log(\theta_{j}/rad$)')
plt.savefig('/home/luantch/calculate10.27/z-theta10.27.eps')
# plt.show()
