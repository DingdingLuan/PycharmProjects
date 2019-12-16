import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Calculatefunction import *

df = pd.read_excel("/Users/dingding/Desktop/calculate/5.9/containseita5.9.xlsx")

zpartone = np.array(df['z'])
seitapartone = np.array(df['seita5.18'])

seitapartonenew=np.nan_to_num(seitapartone)
itemindex=np.argwhere(seitapartonenew==0)
seitapartonenew=np.delete(seitapartonenew,itemindex,axis=0)
zpartonenew=np.delete(zpartone,itemindex,axis=0)

coefficient1=linearregressionEQ(zpartonenew,seitapartonenew)
a1=coefficient1[0]
b1=coefficient1[1]
x1=np.arange(0,7,1)
y1=b1*x1+a1
print(coefficient1)
plt.figure(figsize=(10, 5))
plt.scatter(zpartonenew, seitapartonenew,s=5,alpha=1,marker='o',c='r')
plt.plot(x1,y1,linewidth=0.5,c='red')
plt.xlim(0, 7)
plt.ylim(0, 50)
plt.axis()
plt.title("Z-seita")
plt.xlabel("z")
plt.ylabel("seita[degree]")
# plt.savefig("/Users/dingding/Desktop/zseita5.9.jpg")
plt.show()
