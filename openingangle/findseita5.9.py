from Calculatefunction import k,dl,seita
import csv
import pandas as pd
import numpy as np

sourcenamelist=csv.reader(open('/Users/dingding/Desktop/sample5.9.csv','r'))
GRBname=[column[0]for column in sourcenamelist]
Znamelist=csv.reader(open('/Users/dingding/Desktop/sample5.9.csv','r'))
z=[column[1]for column in Znamelist]
Epeaknamelist=csv.reader(open('/Users/dingding/Desktop/sample5.9.csv','r'))
ep=[column[2]for column in Epeaknamelist]
Enamelist=csv.reader(open('/Users/dingding/Desktop/sample5.9.csv','r'))
s=[column[3]for column in Enamelist]

i=0
seitalist=[]
for i in range(296):
    seitalist=np.append(seitalist,seita(float(z[i]),149.3,float(s[i]),-1,-2.5,15,350))
    i=i+1
print(seitalist)
dataframeseita=pd.DataFrame(seitalist)
dataframeseita.to_csv('/Users/dingding/Desktop/seita5.18.csv',sep=',')