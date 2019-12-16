from Calculatefunction import *
import matplotlib.mlab as mlab


thetamock=[]
protheta=[]
proz=[]
prol=[]
samplenumber=5000
zmock=[]
lmock=[]
#
# #------------------------------------------------------------------------------------------------------
# i=0
# while i<samplenumber:
#     a=np.random.uniform(0.,10)
#     b=np.random.uniform(0,0.35)
#     if RGRB(a,0.4,-1.1,-2.2,1)>=b:
#         zmock=np.append(zmock,a)
#         i=i+1
#     else:
#         continue
# n=100
# for i in range(n):
#     counter=0
#     for j in range(samplenumber):
#         if 10**(i*1/n)-1<=zmock[j]<=10**((i+1)*1/n)-1:
#             counter=counter+1
#     proz=np.append(proz,counter)
# proz=proz/np.sum(proz)
# for i in range(n):
#     proz[i]=proz[i]/(10**((i+1)*1/n)-10**(i*1/n))
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# x=np.arange(0,1,1/n)           #plot z
# plt.bar(x,proz,width=1/n,edgecolor='r',facecolor='white',linestyle='--')
# plt.savefig('/Users/dingding 1/Desktop/calculate/10.11/mockzpdf.eps')
# # plt.show()
#
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# y=np.arange(0,1,0.001)
# z=[]
# for i in range(len(y)):
#     z=np.append(z,RGRB(10**y[i]-1,0.4,-1.1,-2.2,1))
# plt.bar(y,z,width=0.001,edgecolor='r',facecolor='white',linestyle='--')
# plt.savefig('/Users/dingding 1/Desktop/calculate/10.11/z_pdf.eps')
# # plt.show()

#------------------------------------------------------------------------------------------------------
i=0
while i<samplenumber:
    a=np.random.uniform(46,52)
    b=np.random.uniform(0,6*10.**(-51))
    if Luminosityfunction(10**a)>=b:
        lmock=np.append(lmock,10**a)
        i=i+1
    else:
        continue
n=150
for i in range(n):
    counter=0
    for j in range(samplenumber):
        if 10.**(46+i*(6/n))<=lmock[j]<=10.**(46+(i+1)*(6/n)):
            counter=counter+1
    prol=np.append(prol,counter)
prol=prol/np.sum(prol)
# for i in range(n):
#     prol[i]=prol[i]/(10.**(46+(i+1)*(6/n))-10.**(46+i*(6/n)))


matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
plt.xlim(46,53)
y=np.arange(46,52,6/n)            #plot l
plt.bar(y,prol,width=6/n,edgecolor='r',facecolor='white',linestyle='--')
# plt.savefig('/Users/dingding 1/Desktop/calculate/10.11/mockLpdf1.eps')
plt.show()

# #------------------------------------------------------------------------------------------------------
# i=0
# min=-4
# max=2
# while i<samplenumber:
#     # a=np.random.uniform(10**min,10**max)
#     a=np.random.uniform(min,max)
#     b=np.random.uniform(0,2.1)
#     # if thetalogdistri(a)>=b:
#     if thetalogdistri(10**a)>=b:
#         thetamock = np.append(thetamock,a)
#         # thetamock=np.append(thetamock,np.log10(a))
#         i=i+1
#     else:
#         continue
# n=20
# for i in range(n):
#     counter=0
#     for j in range(samplenumber):
#         if min+(max-min)/n*i<=thetamock[j]<=min+(max-min)/n*(i+1):
#             counter=counter+1
#     protheta=np.append(protheta,counter)
# protheta=protheta/np.sum(protheta)
#
#
# # for i in range(n):         # assign the weight
# #     protheta[i]=protheta[i]/(10**(min+(max-min)/n*(i+1))-10**(min+(max-min)/n*i))
#
#
#
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# t=np.arange(min,max,(max-min)/n)          #plot theta
# plt.bar(t,protheta,width=(max-min)/n,edgecolor='r',facecolor='white',linestyle='--')
# plt.savefig('/users/dingding 1/desktop/calculate/10.11/mocktheta.eps')
# plt.show()
#
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# y=np.arange(-4,2,0.005)
#
# plt.bar(y,thetalogdistri(10**y),width=0.005,edgecolor='r',facecolor='white',linestyle='--')
# plt.savefig('/Users/dingding 1/Desktop/calculate/10.11/thetapdf.eps')
# plt.show()
