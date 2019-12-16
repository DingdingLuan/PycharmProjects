import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Calculatefunction import seita

def smallnew():
    df = pd.read_excel("/Users/dingding/Desktop/Angle/5.7/zsmall1.5.xlsx")
    z = df['z']
    s = df['Fluence']
    tbreak=df['tj']
    epeak = df['Epeak']
    alpha=df['α']
    beita=df['β']
    bandmin=df['Band1']
    bandmax=df['Band2']     #Loading the data from excel
    i=0
    a=[]
    for i in range (16):
        a=np.append(a,seita(z[i],epeak[i],s[i]*10**(-6),alpha[i],beita[i],bandmin[i],bandmax[i]))
        i=i+1
    dataframeseita = pd.DataFrame(a)
    dataframeseita.to_csv('/Users/dingding/Desktop/seitasmall5.9.csv', sep=',')
    print(a)


def largernew():
    df = pd.read_excel("/Users/dingding/Desktop/Angle/5.7/zlarger1.5.xlsx")
    z = df['z']
    s = df['Fluence']
    tbreak = df['tj']
    epeak=df['Epeak']
    alpha=df['α']
    beita=df['β']
    bandmin=df['Band1']
    bandmax=df['Band2']
    i=0
    a=[]
    for i in range (7):
        a=np.append(a,seita(z[i],epeak[i],s[i]*10**(-6),alpha[i],beita[i],bandmin[i],bandmax[i]))
        i=i+1
    dataframeseita = pd.DataFrame(a)
    dataframeseita.to_csv('/Users/dingding/Desktop/seitalarge5.9.csv', sep=',')
    print(a)

smallnew()
largernew()