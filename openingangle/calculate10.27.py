from Calculatefunction import *

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
    z = random.uniform(0, 1)
    if eta_a(thetagenerate[i] / 180 * np.pi) > z:
        p = P(zgenerate[i], lgenerate[i], thetagenerate[i])
        if p<89:
            x=random.uniform(0,1)
            if eta_t(p)>x:
                y=random.uniform(0,1)
                if eta_z(p)>y:
                        P_mock=np.append(P_mock,p)
                        zmocksample=np.append(zmocksample, zgenerate[i])
                        thetamocksample=np.append(thetamocksample,thetagenerate[i])
                        lmocksample=np.append(lmocksample,lgenerate[i]/(1-np.cos(thetagenerate[i]/180*np.pi)))

#------------------------------------------------------------------------------------------------------
print(len(zmocksample))
print(len(thetamocksample))
print(len(lmocksample))