import numpy as np
import pandas as pd

df=pd.read_excel('/Users/dingding 1/Desktop/calculate/2.28/findalpha.xlsx')
src=pd.read_excel('/Users/dingding 1/Desktop/calculate/2.28/src.xlsx')

targetname=df['##GRBname']
targetalpha=df[' alpha ']

localname=src['##GRBname']

srcnum=len(targetname)
localnum=len(localname)

selectedalpha=[]
for i in range(localnum):
    for j in range(srcnum):
        if localname[i]==targetname[j]:
            if targetalpha[j]!=' N/A ':
                selectedalpha=np.append(selectedalpha,targetalpha[j])
            else:
                selectedalpha=np.append(selectedalpha,np.nan)
            break
        else:
            continue

print(len(selectedalpha))
print(localnum)

