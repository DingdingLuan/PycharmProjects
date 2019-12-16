from Calculatefunction import*
import pandas as pd

df=pd.read_excel("/Users/dingding/Desktop/sample5.9.xlsx")
grbname=df['grb']
z=df['z']
ep=149.804392
s=df['s']
#GRBname	z	ep[kev]	s[erg/cm^-2]	luminositydistance[cm]	egamma[erg]	eiso[erg]	kcorrection	seita[degree]
alpha=-1
beta=-2.5
grbname1=[]
z1=[]
alpha1=[]
beta1=[]
s1=[]
luminositydistance1=[]
egamma1=[]
eiso1=[]
k1=[]
seita1=[]
for i in range(296):
    seita1=np.append(seita1,seita(float(z[i]),float(ep),float(s[i]),float(alpha),float(beta),15,350))
    grbname1=np.append(grbname1,grbname[i])
    z1=np.append(z1,z[i])
    alpha1=np.append(alpha1,alpha)
    beta1=np.append(beta1,beta)
    s1=np.append(s1,s[i])
    luminositydistance1=np.append(luminositydistance1,dl(z[i]))
    egamma1=np.append(egamma1,egamma(z[i],ep))
    eiso1=np.append(eiso1,eiso(float(z[i]),float(ep),float(s[i]),float(alpha),float(beta),15,350))
    k1=np.append(k1,k(ep,z[i],alpha,beta,15,350))

print(seita1)
dataframename=pd.DataFrame(grbname1)
dataframename.to_csv('/users/dingding/desktop/grbname.csv',sep=',')

dataframename=pd.DataFrame(z1)
dataframename.to_csv('/users/dingding/desktop/z.csv',sep=',')

dataframename=pd.DataFrame(s1)
dataframename.to_csv('/users/dingding/desktop/s.csv',sep=',')

dataframename=pd.DataFrame(luminositydistance1)
dataframename.to_csv('/users/dingding/desktop/ld.csv',sep=',')

dataframename=pd.DataFrame(egamma1)
dataframename.to_csv('/users/dingding/desktop/egamma.csv',sep=',')

dataframename=pd.DataFrame(eiso1)
dataframename.to_csv('/users/dingding/desktop/eiso.csv',sep=',')

dataframename=pd.DataFrame(k1)
dataframename.to_csv('/users/dingding/desktop/k.csv',sep=',')

dataframename=pd.DataFrame(seita1)
dataframename.to_csv('/users/dingding/desktop/seita.csv',sep=',')