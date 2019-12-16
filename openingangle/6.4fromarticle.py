import pandas as pd
import numpy as np
from Calculatefunction import*

df=pd.read_excel("/Users/dingding/Desktop/calculate/fromarticle/zsmall1.5.xlsx")
grbname=df['grb']
z = df['z']
alpha=df['alpha']
beta=df['beta']
ep=df['ep']
s=df['s']*10**(-6)
bandmin=df['Band1']
bandmax=df['Band2']
print(len(z))

grbname1=[]
z1=[]
alpha1=[]
beta1=[]
ep1=[]
s1=[]
luminositydistance1=[]
egamma1=[]
eiso1=[]
k1=[]
seita1=[]
for i in range(17):
    seita1=np.append(seita1,seita(float(z[i]),float(ep[i]),float(s[i]),float(alpha[i]),float(beta[i]),bandmin[i],bandmax[i]))
    grbname1=np.append(grbname1,grbname[i])
    z1=np.append(z1,z[i])
    alpha1=np.append(alpha1,alpha[i])
    beta1=np.append(beta1,beta[i])
    ep1=np.append(ep1,ep[i])
    s1=np.append(s1,s[i])
    luminositydistance1=np.append(luminositydistance1,dl(z[i]))
    egamma1=np.append(egamma1,egamma(z[i],ep[i]))
    eiso1=np.append(eiso1,eiso(float(z[i]),float(ep[i]),float(s[i]),float(alpha[i]),float(beta[i]),bandmin[i],bandmax[i]))
    k1=np.append(k1,k(ep[i],z[i],alpha[i],beta[i],bandmin[i],bandmax[i]))

# dataframename=pd.DataFrame(grbname1)
# dataframename.to_csv('/users/dingding/desktop/grbname.csv',sep=',')
#
# dataframename=pd.DataFrame(z1)
# dataframename.to_csv('/users/dingding/desktop/z.csv',sep=',')
#
# dataframename=pd.DataFrame(alpha1)
# dataframename.to_csv('/users/dingding/desktop/alpha.csv',sep=',')
#
# dataframename=pd.DataFrame(beta1)
# dataframename.to_csv('/users/dingding/desktop/beta.csv',sep=',')
#
# dataframename=pd.DataFrame(ep1)
# dataframename.to_csv('/users/dingding/desktop/ep.csv',sep=',')
#
# dataframename=pd.DataFrame(s1)
# dataframename.to_csv('/users/dingding/desktop/s.csv',sep=',')
#
# dataframename=pd.DataFrame(luminositydistance1)
# dataframename.to_csv('/users/dingding/desktop/ld.csv',sep=',')
#
# dataframename=pd.DataFrame(egamma1)
# dataframename.to_csv('/users/dingding/desktop/egamma.csv',sep=',')
#
# dataframename=pd.DataFrame(eiso1)
# dataframename.to_csv('/users/dingding/desktop/eiso.csv',sep=',')
#
# dataframename=pd.DataFrame(k1)
# dataframename.to_csv('/users/dingding/desktop/k.csv',sep=',')
#
# dataframename=pd.DataFrame(seita1)
# dataframename.to_csv('/users/dingding/desktop/seita.csv',sep=',')