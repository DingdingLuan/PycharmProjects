import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import MultipleLocator


Znamelist=csv.reader(open('/Users/dingding/Desktop/containseita5.6cut.csv','r'))
Z1=[column[1]for column in Znamelist]
seitalist=csv.reader(open('/Users/dingding/Desktop/containseita5.6cut.csv','r'))
seita1=[column[6]for column in seitalist]

Z=np.array(Z1)
seita=np.array(seita1)
# print(Z[0],seita[0])
a=Z
b=seita

x=a
y=b
# color=np.arctan2(y,x)
plt.figure(figsize=(10,5))
ax = plt.scatter(x[:296],y[:296],s=10,alpha=1,marker='o',c='r')
# f1 = plt.plot(x[:200],y[:200],'.')


# plt.xticks([])
plt.yticks([])
plt.xticks([])
plt.xlabel('z')
plt.ylabel('seita')
# plt.axis([0,5,0,2])

# new_ticks = [0,1,2,3,4,5]
# plt.xticks(new_ticks)

# xmajorLocator=MultipleLocator(1)
# ymajorLocator=MultipleLocator(1000)
# ax=subplot(111)
# ax.xaxis.set_major_locator(xmajorLocator)
# ax.yaxis.set_major_locator(ymajorLocator)
# scale=range(6)
# index=['0','1','2','3','4','5']
# plt.bar=(scale,index)


plt.show()
