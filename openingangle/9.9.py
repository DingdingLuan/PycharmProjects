from Calculatefunction import *

eps=0.4
alpha=-1.1
beta=-2.2
rho=2.85*10**2
samplenumber=2000
redshift_Narray=[]
testsamplenumber=10**5
mockGRBnumber=170


# set step of log(1+z):
step=10/samplenumber
for i in range(np.int(10/step)):
    z=i*step                             #Here we dont take log!
    # pro=N(z,eps,alpha,beta,rho,(i+1)*step)
    pro=RGRB(z,eps,alpha,beta,rho)
    redshift_Narray=np.append(redshift_Narray,pro)
redshift_probability=redshift_Narray/np.sum(redshift_Narray)
redshift_Proarray=[]
testsamplenumber=10**5  #set a sample with 'samplenumber' GRBs
for j in range(samplenumber):
    number=np.int(testsamplenumber*redshift_probability[j])
    z=j*step
    for k in range(number):
        redshift_Proarray=np.append(redshift_Proarray,z)




thetastep=np.pi/2/samplenumber
theta_Narray=[]
for i in range(np.int(np.pi/2/thetastep)+1):
    theta=thetastep*(i+1)
    # pro=Ntheta(theta,theta+thetastep)
    pro=thetalogdistri(theta)
    theta_Narray=np.append(theta_Narray,pro)
theta_probability=theta_Narray/np.sum(theta_Narray)

# define a new array to constrain the angle-probability distribution:
theta_Proarray=[]
for j in range(samplenumber):
    number=np.int(testsamplenumber*theta_probability[j])
    theta=j*thetastep
    for k in range(number):
        theta_Proarray=np.append(theta_Proarray,theta)


lmin=49
lmax=54
a=10**lmax
luminusrange=10**lmax-10**lmin
luminusstep=round(luminusrange/samplenumber/a,32)*a
luminus_Narray=[]
for i in range(np.int(luminusrange/luminusstep)+1):
    luminosity=round((10**lmin+1.0*luminusstep*i)/a,32)*a
    # pro=Nluminus(z,theta,luminosity,luminosity+luminusstep)
    pro=Luminosityfunction(luminosity)
    luminus_Narray=np.append(luminus_Narray,pro)
luminus_probability=luminus_Narray/np.sum(luminus_Narray)
luminus_Proarray=[]
for j in range(samplenumber):
    number=np.int(testsamplenumber*luminus_probability[j])
    luminosity=round((10**lmin+j*luminusstep)/a,32)*a
    for k in range(number):
        luminus_Proarray=np.append(luminus_Proarray,round(luminosity/a,32)*a)

# # test
# for i in range(7):
#     num1=random.randint(0,len(redshift_Proarray))
#     num2 = random.randint(0, len(redshift_Proarray))
#     num3 = random.randint(0, len(redshift_Proarray))
#     theta11=theta_Proarray[num1]
#     redshift11=redshift_Proarray[num2]
#     luminus11=luminus_Proarray[num3]
#     print('theta',theta11,'z',redshift11,'L',luminus11)
#     print('p',P(redshift11,luminus11,theta11))

#generate mock procedure

# sampstep=0.05
# mockGRBnumber=3
# mocksample=[]
# mockredshift=[]
# mockluminus_sample=[]
# mockluminus=[]
# mocktheta_sample=[]
# b=0
# Proarray_len=np.min(len([len(redshift_Proarray),len(theta_Proarray),len(luminus_Proarray)]))
#
# while True:
#     num1=random.randint(0,Proarray_len)
#     num2=random.randint(0,Proarray_len)
#     num3=random.randint(0,Proarray_len)
#     peak=P(redshift_Proarray[num1],round(luminus_Proarray[num2]/a,32)*a,theta_Proarray[num3]/np.pi*180)
#     if peak>=0.45 and theta_Proarray[num3]*redshift_Proarray[num1]!=0:
#         mocksample=np.append(mocksample,redshift_Proarray[num1])
#         mockluminus_sample=np.append(mockluminus_sample,round(luminus_Proarray[num2]/a,32)*a)
#         mocktheta_sample=np.append(mocktheta_sample,theta_Proarray[num3]/np.pi*180)
#         print(peak)
#     b=len(mockluminus_sample)
#     if b>=mockGRBnumber:
#         break
#
#
# for n in range(int(1/sampstep)):
#     counter=0
#     for b in range(len(mocksample)):
#         if 10**(sampstep*n)-1<=mocksample[b]<=10**(sampstep*(n+1))-1:
#             counter=counter+1
#     mockredshift=np.append(mockredshift,counter)
# promockredshift=mockredshift/np.sum(mockredshift)
#
#
# luminusplotrange=lmax-lmin
# for n in range(20):
#     counter=0
#     for b in range(len(mockluminus_sample)):
#         if 10**(lmin+luminusplotrange/20*n)<=mockluminus_sample[b]<=10**(lmin+luminusplotrange/20*(n+1)):
#             counter=counter+1
#     mockluminus=np.append(mockluminus,counter)
# promockluminus=mockluminus/np.sum(mockluminus)






# luminusarray=[]
# for i in range(len(mocktheta_sample)):
#     luminusarray=np.append(luminusarray,round(mockluminus_sample[i]/a,32)*a/(1-np.cos(mocktheta_sample[i])))
# print(luminusarray)





# draw the accumulation plot dN-dP:
#
# pnumber=500
# Np=[]
# for i in range(pnumber):
#     num1 = random.randint(0, Proarray_len)
#     num2 = random.randint(0, Proarray_len)
#     num3 = random.randint(0, Proarray_len)
#     num3=random.randint(0,len(redshift_Proarray))
#     # P=P(redshift_Proarray[num1],luminus_Proarray[num2],theta_Proarray[num3])
#     N_normal=quad(lambda L:eta_a(theta_Proarray[num3])*eta_z(P(redshift_Proarray[num1],L,theta_Proarray[num3]
#                     ))*eta_t(P(redshift_Proarray[num1],L,theta_Proarray[num3]
#                                ))*Luminosityfunction(L),10**46,10**52)
#     Np=np.append(Np,N_normal)
# Np1=np.argsort(Np)
# Np=Np[Np1]
#
#
# AccumulateP=[]
# pstep=0.15
# j=-1
# for i in range(20):
#     if j<=2:
#         n=np.int(10**(j-2)*pnumber)
#         AccumulateP=np.append(AccumulateP,np.sum(Np[n:len(Np):1]))
#         j=j+pstep
# proAccumulateP=AccumulateP/np.sum(Np)
#
# # print(proAccumulateP)
# # print(len(proAccumulateP))
#
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# x=np.arange(-1,2,pstep)
# plt.figure(figsize=(7, 7))
# plt.bar(x,proAccumulateP,width=pstep,edgecolor='r',facecolor='white',linestyle='--')
# plt.show()




# #设置xtick的方向，in,out,inout
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# plt.figure(figsize=(7, 7))
# # plt.scatter(np.log10(mocksample+1),mocktheta_sample,s=15,alpha=1,marker='o',c='r')
# plt.scatter(np.log10(mocksample+1),np.log10(mockluminus_sample),s=15,alpha=1,marker='o',c='r')
# plt.show()




# #设置xtick的方向，in,out,inout
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# # x=np.arange(0,10,step)
# x=np.arange(0,1,sampstep)
# plt.figure(figsize=(7, 7))
# # plt.scatter(x,probability,s=5,alpha=1,marker='o',c='r')
# plt.bar(x,promockredshift,width=sampstep,edgecolor='r',facecolor='white',linestyle='--')
# plt.xlabel("log(z+1)")
# plt.ylabel('probability')
# # plt.savefig('/Users/dingding/Desktop/origin.eps')
# plt.show()



#
# # 设置xtick的方向，in,out,inout
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# x=np.arange(0,90,90/len(mocktheta_sample))
# # x=np.arange(0,len(promockluminus),1)
# plt.figure(figsize=(7, 7))
# # plt.scatter(x,probability,s=5,alpha=1,marker='o',c='r')
# plt.bar(x,mocktheta_sample,width=thetastep,edgecolor='r',facecolor='white',linestyle='--')
# # plt.bar(x,promockluminus,width=1,edgecolor='r',facecolor='white',linestyle='--')
# # plt.xlabel("log(z+1)")
# # plt.ylabel('probability')
# # plt.savefig('/Users/dingding/Desktop/origin.eps')
# plt.show()