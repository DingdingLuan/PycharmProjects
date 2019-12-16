import numpy as np
from scipy.integrate import quad
import pandas as pd


# calculate the k-corrention in erg.s-1.cm-2:
def NE(E,Epeak,alpha,beita):
    if (alpha-beita)*Epeak/(2+alpha)>=E:
        NE=(E/100)**alpha*np.exp(-E*(2+alpha)/Epeak)
        return NE
    elif (alpha-beita)*Epeak/(2+alpha)<=E:
        NE=(((alpha-beita)*Epeak/(100*(2+alpha)))**(alpha-beita)*np.exp(beita-alpha)*(E/100)**beita)
        return NE
def k(Epeak,Z,alpha,beita,bandmin,bandmax):
    a1=quad(lambda E:E*NE(E,Epeak,alpha,beita),1/(1+Z),10**4/(1+Z))
    a2=quad(lambda E:E*NE(E,Epeak,alpha,beita),bandmin,bandmax)
    k=a1[0]/a2[0]
    return k


# calculate the k-corrention in photons.s-1.cm-2:
def nk(Epeak,Z,alpha,beita,bandmin,bandmax):
    a1=quad(lambda E:E*NE(E,Epeak,alpha,beita),1/(1+Z),10**4/(1+Z))
    a2=quad(lambda E:NE(E,Epeak,alpha,beita),bandmin,bandmax)
    k=a1[0]/a2[0]
    # return k
    return k*1.6*10**(-9)          #transform kev to erg


# calculate the luminosity distance
omegal=0.734
omegam=0.266
h=0.71
H0=1/(3.09*10**17)
H0yr=1/(9.78*10**9)
# H0=70*10**5
c=2.99792458*10**8
def dl(Z):
    integrateportion=quad(lambda x:1/np.sqrt(omegam*(1+x)**3+omegal),0,Z)
    dl=c*(1+Z)/(h*H0)*integrateportion[0]
    # dl =c/H0*integrateportion[0]
    return dl*10**2       # transform m to cm


#Calculate the opening angle
def seita(z,ep,s,alpha,beita,bandmin,bandmax):
    eiso=4*np.pi*dl(z)**2*s*k(ep,z,alpha,beita,bandmin,bandmax)/(1+z)
    Egama=(ep*(1+z)/10**2.57)**(1/0.61)*3.8*10**50
    seitaradian=np.arccos(1-Egama/eiso)
    seita=seitaradian/(2*np.pi)*360
    return seita

# calculate seita for photons.s-1.cm-2
def pseita(z,ep,s,alpha,beita,bandmin,bandmax):
    eiso=4*np.pi*dl(z)**2*s*nk(ep,z,alpha,beita,bandmin,bandmax)/(1+z)
    Egama=(ep*(1+z)/10**2.57)**(1/0.61)*3.8*10**50
    seitaradian=np.arccos(1-Egama/eiso)
    seita=seitaradian/(2*np.pi)*360
    return seita


#Calculate the Egamma
def egamma(z,ep):
    Egama = (ep * (1 + z) / 10 ** 2.57) ** (1 / 0.61) * 3.8 * 10 ** 50
    return Egama

#Calculate the Eiso
def eiso(z,ep,s,alpha,beita,bandmin,bandmax):
    eiso=4*np.pi*dl(z)**2*s*k(ep,z,alpha,beita,bandmin,bandmax)/(1+z)
    return eiso




#Define a new spectrum calculate method @2018.6.20 [the cases only contain 'alpha']
def alphaNE(E,Epeak,alpha):
    NE=(E/100)**alpha*np.exp(-(2+alpha)*E/Epeak)
    return NE

def alphaek(Epeak,alpha,Z,bandmin,bandmax):
    a1=quad(lambda E:E*alphaNE(E,Epeak,alpha),1/(1+Z),10**4/(1+Z))
    a2=quad(lambda E:E*alphaNE(E,Epeak,alpha),bandmin, bandmax)
    k=a1[0]/a2[0]
    return k

def alphapk(Epeak,alpha,Z,bandmin,bandmax):
    a1=quad(lambda E:E*alphaNE(E,Epeak,alpha),1/(1+Z),10**4/(1+Z))
    a2=quad(lambda E:alphaNE(E,Epeak,alpha),bandmin,bandmax)
    k=a1[0]/a2[0]
    return k*1.6*10**(-9)

def seitaerg6_20(z,ep,s,alpha,bandmin,bandmax):
    eiso=4*np.pi*dl(z)**2*s*alphaek(ep,alpha,z,bandmin,bandmax)/(1+z)
    Egama=(ep*(1+z)/10**2.57)**(1/0.61)*3.8*10**50
    seitaradian=np.arccos(1-Egama/eiso)
    seita=seitaradian/(2*np.pi)*360
    # k = alphaek(ep,alpha,z,bandmin, bandmax)
    return seita,z,Egama

def seitaphoton6_20(z,ep,s,alpha,bandmin,bandmax):
    eiso=4*np.pi*dl(z)**2*s*alphapk(ep,alpha,z,bandmin,bandmax)/(1+z)
    Egama=(ep*(1+z)/10**2.57)**(1/0.61)*3.8*10**50
    seitaradian=np.arccos(1-Egama/eiso)
    seita=seitaradian/(2*np.pi)*360
    # k=alphapk(ep,alpha,z,bandmin,bandmax)*(1/1.6)*10**(9)
    return seita,z,Egama

#refer the 6.11 work:
def erg6_11():
    df = pd.read_excel("/Users/dingding/Desktop/calculate/6.9/erg.xlsx")
    ebandmin = df['bandmin']
    ebandmax=df['bandmax']
    egrbname=df['GRB']
    ez=df['z']
    eep=df['ep']
    ealpha=df['alpha']
    ebeta=df['beta']
    efluence=df['fluence']
    i=0
    seita1=[]
    eegamma=[]
    for i in range(len(egrbname)):
        seita1=np.append(seita1,seita(ez[i],eep[i],efluence[i],ealpha[i],ebeta[i],ebandmin[i],ebandmax[i]))
        eegamma=np.append(eegamma,egamma(ez[i],eep[i]))
    return seita1,ez,eegamma

def photon6_11():
    dp = pd.read_excel("/Users/dingding/Desktop/calculate/6.9/photons.xlsx")
    pbandmin = dp['bandmin']
    pbandmax=dp['bandmax']
    pgrbname=dp['GRB']
    pz=dp['z']
    pep=dp['ep']
    palpha=dp['alpha']
    pbeta=dp['beta']
    pfluence=dp['fluence']
    i=0
    seita2=[]
    pegamma=[]
    for i in range(len(pgrbname)):
        seita2=np.append(seita2,pseita(pz[i],pep[i],pfluence[i],palpha[i],pbeta[i],pbandmin[i],pbandmax[i]))
        pegamma=np.append(pegamma,egamma(pz[i],pep[i]))
    return seita2,pz,pegamma


#Calculate the Linear regression equation:
def linearregressionEQ(series1,series2):
    up=[]
    down=[]
    xmean=np.mean(series1)
    ymean=np.mean(series2)
    for i in range(len(series1)):
        up=np.append(up,series1[i]*series2[i]-len(series1)*xmean*ymean)
        down=np.append(down,series1[i]**2-len(series1)*xmean**2)
    u=np.sum(up)
    d=np.sum(down)
    b=u/d
    a=ymean-b*xmean
    return a,b

def linearnew(series1,series2):
    up1=[]
    up2=[]
    up3=[]
    up4=[]
    down1=[]
    down2=[]
    for i in range(len(series1)):
        up1=np.append(up1,series1[i]**2)
        up2=np.append(up2,series2[i])
        up3=np.append(up3,series1[i])
        up4=np.append(up4,series1[i]*series2[i])
        down1=np.append(down1,series1[i]**2)
        down2=np.append(down2,series1[i])
    up1=np.sum(up1)
    up2=np.sum(up2)
    up3=np.sum(up3)
    up4=np.sum(up4)
    down1=np.sum(down1)
    down2=np.sum(down2)
    up=up1*up2-up3*up4
    down=down1*len(series1)-down2**2
    a0=up/down
    up=len(series1)*up4-up3*up2
    down=len(series1)*down1-down2**2
    a1=up/down
    return a0,a1








# 8.31
# Define a model to describe the distribution of GRB with redshift z
    # define the complete gamma function:
def comGammaFunc(v):
    gamma=quad(lambda t:t**(v-1)*np.e**(-t),0,float("inf"))
    return gamma[0]
    #define the incomplete gamma function:
def incomGammaFunc(v,z):
    sgamma=quad(lambda u:u**(v-1)*np.e**(-u),0,z)[0]
    bgamma=quad(lambda u:u**(v-1)*np.e**(-u),z,float('inf'))[0]
    return bgamma,sgamma
    #and define the Seitafunction:
def SeitaFunc(eps,z,alpha,beta):
    Seita1=incomGammaFunc(alpha+2,eps**beta*10**(0.15*beta*z))[1]
    Seita2=comGammaFunc(alpha+2)
    Seita=Seita1/Seita2
    return Seita
    # define the star formation rate segment function:
def RSFR(z):
    zpeak=1
    if z<=zpeak:
        Rsfr=(1+z)**(3.44)
        return Rsfr
    elif z>=zpeak:
        Rsfr=(1+zpeak)**(3.44)
        return Rsfr
    # define the grb rate function:
def RGRB(z,eps,alpha,beta,rho):
    A=1/(33.30270146296203)
    RGRB=A*rho*RSFR(z)*SeitaFunc(eps,z,alpha,beta)
    return RGRB
    #define a number calculate function without duration  T
def N(z,eps,alpha,beta,rho,zmax):
    convertfactor=c*3600*24*365*10**2*3.26164*10**9
    dlgpc=dl(z)/convertfactor
    E=np.sqrt(omegam*(1+z)**3+omegal)
    n=RGRB(z,eps,alpha,beta,rho)/(1+z)*4*np.pi*c*dlgpc**2/(H0yr*(1+z)**2*E)
    N=quad(lambda z:n,z,zmax)
    return N[0]






import matplotlib.pyplot as plt
import matplotlib
import random


# 9.6
# Here during the defination, normalized constant A_{L} is ellipsis:
def Luminosityfunction(L_gamma):
    L_critical=10**(49.69)      #unit is erg
    sigma_L=0.4
    A_L=1/(1.7235434382660358e+50)
    luminosityfunc=A_L*np.exp(-(np.log10(L_gamma)-np.log10(
        L_critical))**2/(2*sigma_L**2))/(np.sqrt(2*np.pi)*sigma_L)
    return luminosityfunc
# Define the angle distribution as log-normal distribution:
def thetalogdistri(theta_jet):
    theta_critical=10**(-1.27)
    sigema_theta=0.6
    A_theta=1/0.32112249370542306
    Psi=A_theta*np.exp(-(np.log10(theta_jet)-np.log10(theta_critical))**2/
               (2*sigema_theta**2))/(np.sqrt(2*np.pi)*sigema_theta)
    return Psi-0.22039824379156006-0.688381515339374
#-0.22039824379156006
# def Ntheta(thetamin,thetamax):
#     N=quad(lambda theta_jet:thetalogdistri(theta_jet),thetamin,thetamax)
#     return N[0]
# Define peak flux P:
def P(z,L_gamma,theta_jet):
    L=L_gamma/(1-np.cos(theta_jet/180*np.pi))
    C=random.uniform(0.1,1)
    ep=200*(L/10**52)**0.5/C/(1+z)
    P=L/(4*np.pi*dl(z)**2*nk(ep,z,-1.1,-2.2,15,150))    #15-150 kev of swift/BAT
    return P

# BAT trigger probability:
def eta_t(P):
    if P<0.45:
        eta_t=P**2
        return eta_t/0.67            #noamalize the probability of p-detectable
    elif P>=0.45:
        eta_t=0.67*(1.0-0.4/P)**0.52
        return eta_t/0.67            #noamalize the probability of p-detectable
# weak dependence of probability on the observed peak flux:
def eta_z(P):
    eta_z=0.26+0.032*np.e**(1.61*np.log10(P))
    return eta_z
# the probability of alignment for a GRB with jet opening angle theta_{j}:
def eta_a(theta_jet):
    # eta_a=1.4*(1-np.cos(theta_jet))/(4*np.pi)      #where 1.4 sr is instrument solid angle
    normal=1-np.cos(theta_jet)
    return normal

# def Nluminus(z,theta_jet,Luminusmin,Luminusmax):
#     N=quad(lambda L_gamma:eta_a(theta_jet)*eta_t(P(z,L_gamma,theta_jet)
#                 )*eta_z(P(z,L_gamma,theta_jet))*Luminosityfunction(L_gamma),
#            Luminusmin,Luminusmax)
#     return N[0]



def luminosity(z,s,t90):
    l=4*np.pi*dl(z)**2*s*k(80,z,-1,-2.5,15,150)*(1+z)/t90
    return l

def P_obseved(z,s,t90):
    l=luminosity(z,s,t90)
    p=l/(4*np.pi*dl(z)**2*nk(80,z,-1,-2.5,15,150))
    return p


def pdflog(series,down,up,num):
    step=(up-down)/num
    pdf=[]
    for i in range(num):
        counter=0
        for j in range(len(series)):
            if 10**(down+i*step)<series[j]<10**(down+(i+1)*step):
                counter=counter+1
        pdf=np.append(pdf,counter)
    pdf=pdf/np.sum(pdf)
    return pdf





















# #Define a operation to delete the 'nan' element:
# def deletenan(series1,series2):
#     series=np.append(series1,series2)
#     a=series[:len(series):3]
#     b=series[1:len(series):3]
#     c=series[2:len(series):3]
#     a=np.nan_to_num(a)
#     itemindex=np.argwhere(a==0)
#     a=np.delete(a,itemindex,axis=0)
#     b=np.delete(b,itemindex,axis=0)
#     c=np.delete(c,itemindex,axis=0)
#     return a,b,c