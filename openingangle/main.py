import numpy as np
import csv
import pandas as pd
from scipy.integrate import quad


# Import the data(leave the head)
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


# calculate the k-corrention:
alpha=-1
beita=-2.5
def NE(E,Epeak):
    if (alpha-beita)*Epeak/(2+alpha)>=E:
        NE=(E/100)**alpha*np.exp(-E*(2+alpha)/Epeak)
        return NE
    elif (alpha-beita)*Epeak/(2+alpha)<=E:
        NE=(((alpha-beita)*Epeak/(100*(2+alpha)))**(alpha-beita)*np.exp(beita-alpha)*(E/100)**beita)
        return NE
def k(Epeak,Z):
    a1=quad(lambda E:E*NE(E,Epeak),1/(1+Z),10**4/(1+Z))
    a2=quad(lambda E:E*NE(E,Epeak),15,350)
    k=a1[0]/a2[0]
    return k


# calculate the luminosity distance
omegal=0.734
omegam=0.266
h=0.71
H0=1/(3.09*10**17)
c=2.99792458*10**8
def dl(Z):
    integrateportion=quad(lambda x:1/np.sqrt(omegam*(1+x)**3+omegal),0,Z)
    dl=c*(1+Z)/(h*H0)*integrateportion[0]
    return dl*10**2       # transform m to cm


# calculate the jet opening angle
gg=10**2.57
mm=0.61
def seita(Z,Epeak,S):
    seita=np.arccos(1-(3.8*10**50/4*np.pi)*((1+Z)/dl(Z)**2*S*10**6*k(Epeak,Z))*(Epeak*(1+Z)/gg)**(1/mm))
    return seita


# export the seita list
i=0
seitalist=[]
for i in range(296):
    seitalist=np.append(seitalist,seita(float(Z[i]),float(Epeak[i]),float(S[i])))
    i=i+1
dataframeseita=pd.DataFrame(seitalist)
dataframeseita.to_csv('/Users/dingding/Desktop/seita5.1.csv',sep=',')