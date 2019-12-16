from Calculatefunction import *
eps=0.4
alpha=-1.1
beta=-2.2
rho=1
samplenumber=2


zmocksample=[]
lmocksample=[]
thetamocksample=[]
lmin=46
lmax=52
P_mock=[]
i=0
while i<samplenumber:
    a=random.uniform(0.00001, 10)
    b=random.uniform(0.00001, 11)
    z=a
    if b<=RGRB(a,eps,alpha,beta,rho):
        a=random.uniform(10.**lmin,10.**lmax)
        b=random.uniform(10.**(-20),1)
        l=a
        if b<=Luminosityfunction(a):
            a=random.uniform(-2.5, 0)
            b=random.uniform(0, 1)
            theta=10.**a/np.pi*180
            if b<=thetalogdistri(10.**(a)):
                p=P(z,l,theta)
                a=random.uniform(0,1)
                if 0<a<eta_t(p):
                    a=random.uniform(0,1)
                    if 0<a<eta_z(p):
                        P_mock=np.append(P_mock,p)
                        zmocksample=np.append(zmocksample,z)
                        thetamocksample=np.append(thetamocksample,theta)
                        lmocksample=np.append(lmocksample,l/(1-np.cos(theta/180*np.pi)))
                        i=i+1



print('pmock:',P_mock)
print('zmock:',zmocksample)
print('lmock:',lmocksample)
print('thetamock:',thetamocksample)