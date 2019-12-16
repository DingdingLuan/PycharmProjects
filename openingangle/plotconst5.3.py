import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

df=pd.read_excel('/Users/dingding/Desktop/calculate/5.3result/const.xlsx')

pconst=df['pvalue']
sigmae=df['sigma_e']
logec=df['log_ec']

logbin=logec[:12:1]
sigmabin=sigmae[:108:12]



#process matrix:
def makematrix(str1,str2):
    nx=len(str1)
    ny=len(str2)
    xarray=str1
    str2=np.vstack(str2)
    yarray=str2
    for i in range(ny-1):
        xarray=np.vstack((xarray,str1))
    for i in range(nx-1):
        yarray=np.hstack((yarray,str2))
    return xarray,yarray


logmatrix=makematrix(logbin,sigmabin)[0]
sigmamatrix=makematrix(logbin,sigmabin)[1]


#correlate excel with three matrixs:
def pvalue(max1,max2):
    len1=len(max1[:,0])
    len2=len(max2[0])
    # creat a 12-9 dimensions zeros-array bin for pvalue:
    pvaluematrix=np.zeros((len1,len2),dtype=float)
    for i in range(len1):
        for j in range(len2):
            pvaluematrix[i][j]=pconst[i*(len2)+j]
    return pvaluematrix

#plot
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
fig,(ax1) = plt.subplots(figsize=(12, 7))
plt.title('$Constant\;model\;parameters\;K-S\;test\;with\;obsEiso$',fontsize=13)
plt.xlabel('$Log \quad \epsilon c$',fontsize=13)
plt.ylabel('$\sigma_{\epsilon e}$',fontsize=18)
plt.xlim(0,11)
plt.ylim(0,8)
scale_sigma=range(9)

index_sigma=[0.2,0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ]
scale_logec = range(12)
index_logec=np.arange(48.5,54.5,0.5)
plt.xticks(scale_logec,index_logec)
plt.yticks(scale_sigma,index_sigma)
pos_neg_clipped = ax1.imshow(pvalue(logmatrix,sigmamatrix),cmap='Reds',vmin=0,vmax=0.5,interpolation='none')
fig.colorbar(pos_neg_clipped, ax=ax1,label='pvalue')
# plt.savefig('/users/dingding/desktop/calculate/2019result/firsttime/const_colorbar.jpg')
plt.show()








