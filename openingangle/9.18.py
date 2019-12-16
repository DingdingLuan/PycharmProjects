from Calculatefunction import *
import matplotlib.mlab as mlab

# def gauss(x,sigma,miu):
#     fx=1/np.sqrt(2*np.pi)/sigma*np.e**(-(np.log10(x)-miu)**2/(2*sigma**2))
#     return fx
# #
# result=quad(lambda x:gauss(x,0.4,20),10**(13),10**(27))[0]
# print(result)

# result=quad(lambda x:Luminosityfunction(x),10**46,10**53)[0]
# print(result)

# print(Luminosityfunction(10**49.69))
# print(gauss(49.69,0.4,49.69))

# #
# result=quad(lambda x:thetalogdistri(x),10**(-4),10**2)[0]
# print(result)
# result=quad(lambda x:RGRB(x,0.4,-1.1,-2.2,1),0,1)[0]
# print(result)
thetamock=[]
protheta=[]
proz=[]
prol=[]
samplenumber=1000
zmock=[]
lmock=[]
#
# #------------------------------------------------------------------------------------------------------
i=0
min=-2.5
max=0
while i<samplenumber:
    a=np.random.uniform(10**min,10**max)
    b=np.random.uniform(0,2.1)
    if thetalogdistri(a)>=b:
        # c=np.random.uniform(0,1)
        # if eta_a(a)>c:
            thetamock=np.append(thetamock,np.log10(a))
            i=i+1
    else:
        continue
n=10
for i in range(n):
    counter=0
    for j in range(samplenumber):
        if min+(max-min)/n*i<=thetamock[j]<=min+(max-min)/n*(i+1):
            counter=counter+1
    protheta=np.append(protheta,counter)
protheta=protheta/np.sum(protheta)
print(protheta)

for i in range(n):         # assign the weight
    protheta[i]=protheta[i]/(10**(min+(max-min)/n*(i+1))-10**(min+(max-min)/n*i))

# counter=0
# for i in range(samplenumber):
#     if 0>thetamock[i]>=-0.5:
#         counter=counter+1
# print(counter)

matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
t=np.arange(min,max,(max-min)/n)          #plot theta
plt.bar(t,protheta,width=(max-min)/n,edgecolor='r',facecolor='white',linestyle='--')
# plt.savefig('/users/dingding/desktop/calculate/9.18/conditionmocktheta.eps')
plt.show()

# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# y=np.arange(-2.5,0,0.005)
#
# plt.bar(y,thetalogdistri(10**y),width=0.005,edgecolor='r',facecolor='white',linestyle='--')
# # plt.savefig('/Users/dingding/Desktop/calculate/9.18/conditiontheta_pdf.eps')
# plt.show()


#------------------------------------------------------------------------------------------------------

# i=0
# while i<samplenumber:
#     a=np.random.uniform(0.01,10)
#     b=np.random.uniform(0,2.5)
#     if RGRB(a,0.4,-1.1,-2.2,1)>=b:
#         zmock=np.append(zmock,a)
#         i=i+1
#     else:
#         continue
# n=10
# for i in range(n):
#     counter=0
#     for j in range(170):
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
# plt.bar(x,proz,width=1/len(x),edgecolor='r',facecolor='white',linestyle='--')
# # plt.savefig('/Users/dingding/Desktop/calculate/9.18/mockz.eps')
# plt.show()

# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# y=np.arange(0,1,0.001)
# z=[]
# for i in range(len(y)):
#     z=np.append(z,RGRB(10**y[i]-1,0.4,-1.1,-2.2,1))
# plt.bar(y,z,width=0.001,edgecolor='r',facecolor='white',linestyle='--')
# #plt.savefig('/Users/dingding/Desktop/calculate/9.18/z_pdf.eps')
# plt.show()


#------------------------------------------------------------------------------------------------------


# i=0
# while i<samplenumber:
#     a=np.random.uniform(10.**46,10.**52)
#     b=np.random.uniform(0,6*10.**(-51))
#     if Luminosityfunction(a)>=b:
#         lmock=np.append(lmock,a)
#         i=i+1
#     else:
#         continue
# n=20
# for i in range(n):
#     counter=0
#     for j in range(170):
#         if 10.**(46+i*(6/n))<=lmock[j]<=10.**(46+(i+1)*(6/n)):
#             counter=counter+1
#     prol=np.append(prol,counter)
# prol=prol/np.sum(prol)
# for i in range(n):
#     prol[i]=prol[i]/(10.**(46+(i+1)*(6/n))-10.**(46+i*(6/n)))
#
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# y=np.arange(46,52,6/n)            #plot l
# plt.bar(y,prol,width=6/n,edgecolor='r',facecolor='white',linestyle='--')
# # plt.savefig('/Users/dingding/Desktop/calculate/9.18/mockL.eps')
# plt.show()