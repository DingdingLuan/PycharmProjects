import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

dconstant=pd.read_csv('/users/dingding 1/desktop/calculate/11.19/result/output_constantEiso.txt')
dgauss=pd.read_csv('/users/dingding 1/desktop/calculate/11.19/result/output_gaussEiso.txt')
dpl=pd.read_csv('/users/dingding 1/desktop/calculate/11.19/result/output_plEiso.txt')
dindex=pd.read_csv('/users/dingding 1/desktop/calculate/11.19/result/generateEisoindex.txt')

const=dconstant['Eiso']
gauss=dgauss['Eiso']
pl=dpl['Eiso']
eiso=dindex['index']

plt.step(eiso,const,linewidth=0.9,linestyle='-',c='r')
plt.step(eiso,gauss,linewidth=0.7,linestyle='-.-',c='g')
plt.step(eiso,pl,linewidth=0.7,linestyle='--',c='b')
# plt.xlim(46,52)
# plt.ylim(0,0.2)
plt.show()