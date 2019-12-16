from Calculatefunction import *


eps=0.4
alpha=-1.1
beta=-2.2
rho=2.85*10**2
samplenumber=2000
redshift_Narray=[]



# set step of log(1+z):
step=10/samplenumber
for i in range(np.int(10/step)):
    z=i*step                             #Here we dont take log!
    # pro=N(z,eps,alpha,beta,rho,(i+1)*step)
    pro=RGRB(z,eps,alpha,beta,rho)
    redshift_Narray=np.append(redshift_Narray,pro)
redshift_probability=redshift_Narray/np.sum(redshift_Narray)


# define a new array to constrain the probability distribution:
redshift_Proarray=[]
testsamplenumber=10**5  #set a sample with 'samplenumber' GRBs
for j in range(samplenumber):
    number=np.int(testsamplenumber*redshift_probability[j])
    z=j*step
    for k in range(number):
        redshift_Proarray=np.append(redshift_Proarray,z)



sampstep=0.05
mockGRBnumber=170
mocksample=[]
mockredshift=[]
for m in range(mockGRBnumber):
    num=random.randint(0,len(redshift_Proarray))
    mocksample=np.append(mocksample,redshift_Proarray[num])
for n in range(int(1/sampstep)):
    counter=0
    for b in range(len(mocksample)):
        if 10**(sampstep*n)-1<=mocksample[b]<=10**(sampstep*(n+1))-1:
            counter=counter+1
    mockredshift=np.append(mockredshift,counter)
promockredshift=mockredshift/np.sum(mockredshift)

print(len(redshift_Proarray))






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
