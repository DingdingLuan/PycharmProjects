import numpy as np
from main import k,dl
import csv
import pandas as pd


sourcenamelist=csv.reader(open('/Users/dingding/Desktop/Final5.11.csv','r'))
GRBname=[column[0]for column in sourcenamelist]
Znamelist=csv.reader(open('/Users/dingding/Desktop/Final5.11.csv','r'))
Z=[column[1]for column in Znamelist]
Epeaknamelist=csv.reader(open('/Users/dingding/Desktop/Final5.11.csv','r'))
Epeak=[column[2]for column in Epeaknamelist]
Enamelist=csv.reader(open('/Users/dingding/Desktop/Final5.11.csv','r'))
Eiso=[column[3]for column in Enamelist]
T90namelist=csv.reader(open('/Users/dingding/Desktop/Final5.11.csv','r'))
T90=[column[4]for column in T90namelist]
Snamelist=csv.reader(open('/Users/dingding/Desktop/Final5.11.csv','r'))
S=[column[5]for column in Snamelist]



def seita1(z,ep,s):
    eiso=4*np.pi*dl(z)**2*s*k(ep,z)/(1+z)
    Egama=(ep*(1+z)/10**2.57)**(1/0.61)*3.8*10**50
    seita=np.arccos(1-Egama/eiso)
    return seita
def iso(z,ep,s):
    eiso=4*np.pi*dl(z)**2*s*k(ep,z)/(1+z)
    Egama=(ep*(1+z)/10**2.57)**(1/0.61)*3.8*10**50
    seita=np.arccos(1-Egama/eiso)
    return eiso
def gamma(z,ep,s):
    eiso=4*np.pi*dl(z)**2*s*k(ep,z)/(1+z)
    Egama=(ep*(1+z)/10**2.57)**(1/0.61)*3.8*10**50
    seitaradian=np.arccos(1-Egama/eiso)
    seita=seitaradian/(2*np.pi)*360
    return Egama



i=0
seitalist=[]
for i in range(296):
    seitalist=np.append(seitalist,gamma(float(Z[i]),float(Epeak[i]),float(S[i])))
    i=i+1
dataframeseita=pd.DataFrame(seitalist)
dataframeseita.to_csv('/Users/dingding/Desktop/egamma5.6.csv',sep=',')