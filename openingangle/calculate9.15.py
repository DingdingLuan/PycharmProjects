from Calculatefunction import *

eps=0.4
alpha=-1.1
beta=-2.2
rho=1
samplenumber=10000


# thetalogdistri(theta_jet)
#
# P(z,L_gamma,theta_jet)

#Generate parameter z from RGRB:
# zmocksample=[]
# i=0
# while i<samplenumber:
#     a=random.uniform(0.00001,10)
#     b=random.uniform(0.00001,11)
#     if b<=RGRB(a,eps,alpha,beta,rho):
#         zmocksample=np.append(zmocksample,a)
#         i=i+1
# zprostep=20
# zpromocksample=[]
# for i in range(zprostep):
#     counter=0
#     for j in range(samplenumber):
#         if 10**(1/zprostep*i)-1<=zmocksample[j]<=10**(1/zprostep*(i+1))-1:
#             counter=counter+1
#     zpromocksample=np.append(zpromocksample,counter)
# prozsample=zpromocksample/np.sum(zpromocksample)
#
#
# # Generate parameter L_gamma from Luminosityfunction:
# L_gammamocksample=[]
# lmin=49
# lmax=54
# i=0
# while i<samplenumber:
#     a=random.uniform(10.**lmin,10.**lmax)
#     b=random.uniform(10.**(-20),1)
#     if b<=Luminosityfunction(a):
#         L_gammamocksample=np.append(L_gammamocksample,a)
#         i=i+1
# lprostep=20
# lpromocksample=[]
# lrange=lmax-lmin
# for i in range(lprostep):
#     counter=0
#     for j in range(samplenumber):
#         if 10.**(lmin+lrange/lprostep*i)<=L_gammamocksample[j]<=10.**(lmin+lrange/lprostep*(i+1)):
#             counter=counter+1
#     lpromocksample=np.append(lpromocksample,counter)
# prolsample=lpromocksample/np.sum(lpromocksample)


# Gnerate parameter theta from thetalogdistri:
thetamocksample=[]
i=0
while i<samplenumber:
    a=random.uniform(-2.5,0)
    b=random.uniform(0,1)
    if b<=thetalogdistri(10.**(a)):
        thetamocksample=np.append(thetamocksample,10.**a/np.pi*180)
        i=i+1
thetastep=1000
thetarange=2.5
thetapromocsample=[]
for i in range(thetastep):
    counter=0
    for j in range(samplenumber):
        if 10.**(-2.5+thetarange/thetastep*i)<=thetamocksample[j]/180*np.pi<=10.**(-2.5+thetarange/thetastep*(i+1)):
            counter=counter+1
    thetapromocsample=np.append(thetapromocsample,counter)
prothetasample=thetapromocsample/np.sum(thetapromocsample)


# 9.15:
# # draw the logL and log(1+z) plot:
# Lmocksample=[]
# for i in range(samplenumber):
#     l=L_gammamocksample[i]/(1-np.cos(thetamocksample[i]/180*np.pi))
#     Lmocksample=np.append(Lmocksample,l)
#
#
# plt.figure(figsize=(7,7))
# plt.scatter(np.log10(zmocksample+1),np.log10(Lmocksample),s=5,alpha=1,marker='o',c='r')
# plt.show()





# 设置xtick的方向，in,out,inout
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
# plt.scatter(x,probability,s=5,alpha=1,marker='o',c='r')
# y=np.arange(0,1,1/zprostep)
# l=np.arange(lmin,lmax,lrange/lprostep)
t=np.arange(-2.5,0,thetarange/thetastep)
# plt.bar(x,zdistribution,width=0.01,edgecolor='r',facecolor='white',linestyle='--')
# plt.bar(y,prozsample,width=1/zprostep,edgecolor='r',facecolor='white',linestyle='--')
# plt.bar(l,prolsample,width=lrange/lprostep,edgecolor='r',facecolor='white',linestyle='--')
plt.bar(t,prothetasample,width=thetarange/thetastep,edgecolor='r',facecolor='white',linestyle='--')
# plt.savefig('/users/dingding/desktop/thetadistribution.eps')
plt.show()
