import matplotlib.pyplot as plt
from Calculatefunction import *
import matplotlib

dp=pd.read_excel('/users/dingding/desktop/calculate/6.9/only_alpha/photons.xlsx')
pz=dp['z']
pbandmin=dp['band1']
pbandmax=dp['band2']
pgrbname=dp['GRB']
palpha=dp['alpha']
pfluence=dp['flux_cm']
pep=dp['ep']
seita3=[]
pegamma=[]
k=[]
for i in range(len(pgrbname)):
    seita3=np.append(seita3,seitaphoton6_20(pz[i],pep[i],pfluence[i],palpha[i],pbandmin[i],pbandmax[i]))



de=pd.read_excel('/users/dingding/desktop/calculate/6.9/only_alpha/erg.xlsx')
ez=de['z']
ebandmin=de['band1']
ebandmax=de['band2']
egrbname=de['GRB']
ealpha=de['alpha']
efluence=de['flux_cm']
eep=de['ep']
seita4=[]
eegamma=[]
for i in range(len(egrbname)):
    seita4=np.append(seita4,seitaerg6_20(ez[i],eep[i],efluence[i],ealpha[i],ebandmin[i],ebandmax[i]))


seitapartone=np.append(photon6_11()[:len(photon6_11()):3],erg6_11()[:len(erg6_11()):3])
zpartone=np.append(photon6_11()[1:len(photon6_11()):3],erg6_11()[1:len(erg6_11()):3])
egammapartone=np.append(photon6_11()[2:len(photon6_11()):3],erg6_11()[2:len(erg6_11()):3])
seitaparttwo=np.append(seita3[:len(seita3):3],seita4[:len(seita4):3])
zparttwo=np.append(seita3[1:len(seita3):3],seita4[1:len(seita4):3])
egammaparttwo=np.append(seita3[2:len(seita3):3],seita4[2:len(seita4):3])


seitapartonenew=np.nan_to_num(seitapartone)
itemindex=np.argwhere(seitapartonenew==0)
seitapartonenew=np.delete(seitapartonenew,itemindex,axis=0)
zpartonenew=np.delete(zpartone,itemindex,axis=0)
egammapartonenew=np.delete(egammapartone,itemindex,axis=0)

seitaparttwonew=np.nan_to_num(seitaparttwo)
itemindex=np.argwhere(seitaparttwonew==0)
seitaparttwonew=np.delete(seitaparttwonew,itemindex,axis=0)
zparttwonew=np.delete(zparttwo,itemindex,axis=0)
egammaparttwonew=np.delete(egammaparttwo,itemindex,axis=0)



coefficient1=linearnew(zpartonenew,seitapartonenew)
a1=coefficient1[0]
b1=coefficient1[1]
coefficient=linearnew(np.append(zpartonenew,zparttwonew),np.append(seitapartonenew,seitaparttwonew))
a=coefficient[0]
b=coefficient[1]
print(coefficient)
print(coefficient1)

x1=np.arange(0,8,1)
y1=b1*x1+a1
y=b*x1+a
plt.figure(figsize=(10, 5))

#设置xtick的方向，in,out,inout
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.scatter(zpartonenew, seitapartonenew, s=7, alpha=1, marker='o', c='r',label='with alpha&beta')
plt.scatter(zparttwonew, seitaparttwonew, s=7, alpha=1, marker='*', c='blue',label='only contain alpha')
plt.plot(x1,y1,linewidth=0.5,c='red',label='only the samples with alpha&beta')
plt.plot(x1,y,linewidth=0.5,c='green',label='all data(127 samples)')
plt.xlim(0, 8)
plt.ylim(0,50)
plt.axis()
plt.title("Z-Seita")
plt.xlabel("z")
plt.ylabel("Seita[degree]")
plt.legend(loc='best')
# plt.savefig('/users/dingding/desktop/6.24.jpg')



plt.show(Block=False)

# plt.figure(figsize=(7, 5))
# plt.scatter(np.log10(egamma), np.log10(epz), s=5, alpha=1, marker='o', c='r')
# plt.xlim(48, 53)
# plt.ylim(1, 4)
# plt.axis()
# plt.title("Egamma-Ep,z_FromArticle_byFortran")
# plt.ylabel("log[Ep,z]")
# plt.xlabel("log[Egamma]")

