import pandas as pd
import numpy as np

df = pd.read_excel("/Users/dingding/Desktop/Angle/5.7/zsmall1.5.xlsx")
grbname=df['GRB']
z = df['z']
s = df['Fluence']
epeak = df['Epeak']
alpha=df['α']
beita=df['β']
bandmin=df['Band1']
bandmax=df['Band2']

i=1
h=[]

for i in range(17):
    a=np.append(grbname[i], z[i])
    b=np.append(a, s[i])
    c=np.append(b, epeak[i])
    d=np.append(c,alpha[i])
    e=np.append(d,beita[i])
    f=np.append(e,bandmin[i])
    g=np.append(f,bandmax[i])
    h=np.append(h,g)
    i=i+1
dataframeseita=pd.DataFrame(h)
dataframeseita.to_csv('/Users/dingding/Desktop/fuckyou.csv',sep=',')
