import matplotlib
import matplotlib.pyplot as plt
from calculate import *

a=np.arange(0,1,1/100)



test0=[]
test1=[]
testm1=[]
for i in range(100):
    test0=np.append(test0,nn(a[i],0))
    test1=np.append(test1,nn(a[i],1))
    testm1=np.append(testm1,nn(a[i],-1))


matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(9,9))
# plt.text(0.2,3.0,'$k=-1$',fontsize='14',ha='left',wrap=True)
plt.plot(a,test0,linewidth=1,color='r',label='k=0')
plt.plot(a,test1,linewidth=1,color='b',label='k=1')
plt.plot(a,testm1,linewidth=1,color='g',label='k=-1')
plt.legend()
plt.savefig('/users/dingding 1/desktop/homework9.26.eps')
plt.show()
