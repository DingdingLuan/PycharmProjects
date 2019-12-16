from Calculatefunction import *


#generate the theta distribution
samplenumber=2000
testsamplenumber=10**4
mockGRBnumber=170
#
#
#
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


mocktheta_sample=[]
for m in range(mockGRBnumber):
    num=random.randint(0,len(theta_Proarray))
    mocktheta_sample=np.append(mocktheta_sample,theta_Proarray[num]/np.pi*180)

count=0
sss=2.5/10
counter=[]
for n in range(10):
    count=0
    for i in range(len(mocktheta_sample)):
        if 10**(0-sss*(n+1))<=mocktheta_sample[i]/180*np.pi<=10**(0-sss*n):
            count=count+1
    counter=np.append(counter,count)
print(counter/len(mocktheta_sample))
# mocktheta=[]
# densitystep=2.5/20
# for n in range(20):
#     counter=0
#     b=0
#     for b in range(170):
#         if 0-densitystep*(n+1)<=np.log10(mocktheta_sample[b]/180*np.pi)<=0-densitystep*n:
#             counter=counter+1
#     mocktheta=np.append(mocktheta,counter)
#     # print(np.log10(mocktheta_sample[b]/180*np.pi))
# promocktheta=mocktheta/np.sum(mocktheta)



#
#
# z=1.5
# theta=2.2
#
# lmin=49
# lmax=54
# a=10**lmax
# luminusrange=10**lmax-10**lmin
# luminusstep=round(luminusrange/samplenumber/a,32)*a
# luminus_Narray=[]
# for i in range(np.int(luminusrange/luminusstep)+1):
#     luminosity=round((10**lmin+1.0*luminusstep*i)/a,32)*a
#     # pro=Nluminus(z,theta,luminosity,luminosity+luminusstep)
#     pro=Luminosityfunction(luminosity)
#     luminus_Narray=np.append(luminus_Narray,pro)
# luminus_probability=luminus_Narray/np.sum(luminus_Narray)
#
#
# luminus_Proarray=[]
# for j in range(samplenumber):
#
#     number=np.int(testsamplenumber*luminus_probability[j])
#     luminosity=round((10**lmin+j*luminusstep)/a,32)*a
#     for k in range(number):
#         luminus_Proarray=np.append(luminus_Proarray,round(luminosity/a,32)*a)
#
#
# mockluminus_sample=[]
# mockluminus=[]
# for m in range(mockGRBnumber):
#     num1=random.randint(0,len(luminus_Proarray))
#     mockluminus_sample=np.append(mockluminus_sample,round(luminus_Proarray[num1]/a,32)*a)
#
#
# luminusarray=[]
# for i in range(len(mocktheta_sample)):
#     num2=random.randint(0,170)
#     luminusarray=np.append(luminusarray,round(mockluminus_sample[i]/a,32)*a/(1-np.cos(mocktheta_sample[i])))
#
#
# luminusplotrange=lmax-lmin
# for n in range(20):
#     counter=0
#     for b in range(len(mockluminus_sample)):
#         if 10**(lmin+luminusplotrange/20*n)<=luminusarray[b]<=10**(lmin+luminusplotrange/20*(n+1)):
#             counter=counter+1
#     mockluminus=np.append(mockluminus,counter)
# promockluminus=mockluminus/np.sum(mockluminus)




# # 设置xtick的方向，in,out,inout
# matplotlib.rcParams['xtick.direction'] = 'in'
# matplotlib.rcParams['ytick.direction'] = 'in'
# x=np.arange(0,np.log10(np.pi/2),np.log10(np.pi/2)/len(theta_probability))
# # x=np.arange(0,90,90/len(mocktheta_sample))
# # x=np.arange(0,len(promockluminus),1)
# plt.figure(figsize=(7, 7))
# # plt.scatter(x,probability,s=5,alpha=1,marker='o',c='r')
# # plt.bar(x,promocktheta,width=densitystep,edgecolor='r',facecolor='white',linestyle='--')
# plt.bar(x,theta_probability,width=thetastep,edgecolor='r',facecolor='white',linestyle='--')
# # plt.bar(x,promockluminus,width=1,edgecolor='r',facecolor='white',linestyle='--')
# # plt.xlabel("log(z+1)")
# # plt.ylabel('probability')
# # plt.savefig('/Users/dingding/Desktop/origin.eps')
# plt.show()
