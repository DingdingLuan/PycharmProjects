import numpy as np
import matplotlib.pyplot as plt
import csv


Znamelist=csv.reader(open('/Users/dingding/Desktop/containseita5.6cut.csv','r'))
Z1=[column[1]for column in Znamelist]
seitalist=csv.reader(open('/Users/dingding/Desktop/containseita5.6cut.csv','r'))
seita1=[column[6]for column in seitalist]

Z=np.array(Z1)
seita=np.array(seita1)
# print(Z[0],seita[0])

x=np.random.normal(0,1,10000)
y=np.random.normal(0,1,10000)
# color=np.arctan2(y,x)
plt.scatter(x,y,s=100,alpha=0.5)
plt.xlim((0,1))
plt.ylim((0,1))
plt.show()
