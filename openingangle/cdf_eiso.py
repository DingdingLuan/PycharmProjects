import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dconst=pd.read_csv('result/output_constantEiso.txt')
dgauss=pd.read_csv('result/output_gaussEiso.txt')
dpl=pd.read_csv('result/output_plEiso.txt')
dindex=pd.read_csv('result/generateEisoindex.txt')

const=dconst[' Eiso']
gauss=dgauss[' Eiso']
pl=dpl[' Eiso']
index=dindex[' index']

ccc=np.sum(const)
gga=np.sum(gauss)
ppl=np.sum(pl)

cc=np.sum(const)
gg=np.sum(gauss)
pp=np.sum(pl)

c=[]
g=[]
p=[]
for i in range(len(index)):
    c=np.append(c,cc/ccc)
    g=np.append(g,gg/gga)
    p=np.append(p,pp/ppl)
    cc=cc-const[i]
    gg=gg-gauss[i]
    pp=pp-pl[i]

plt.plot(index,c,c='r',label='const')
plt.plot(index,g,c='g',label='gauss')
plt.plot(index,p,c='b',label='pl')
plt.legend(loc='best')
plt.show()