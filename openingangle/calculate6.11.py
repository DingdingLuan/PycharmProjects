from Calculatefunction import*
import pandas as pd
import matplotlib.pyplot as plt

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
    for i in range(34):
        seita1=np.append(seita1,seita(ez[i],eep[i],efluence[i],ealpha[i],ebeta[i],ebandmin[i],ebandmax[i]))
        # eegamma=np.append(eegamma,egamma(ez[i],eep[i]))
    return seita1

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
    for i in range(15):
        seita2=np.append(seita2,pseita(pz[i],pep[i],pfluence[i],palpha[i],pbeta[i],pbandmin[i],pbandmax[i]))
        # pegamma=np.append(pegamma,egamma(pz[i],pep[i]))
    return seita2

# z = np.append(ez,pz)
# seita= np.append(seita1,seita2)
# egamma=np.log10(np.append(eegamma,pegamma))
#
# plt.figure(figsize=(10, 5))
# plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
# plt.xlim(0, 8)
# plt.ylim(0,50)
# plt.axis()
# plt.title("Z-Seita")
# plt.xlabel("z")
# plt.ylabel("Seita[degree]")
# plt.savefig("/Users/dingding/Desktop/Z-Seita6.11.jpg")
# plt.show()
#
# plt.figure(figsize=(10, 5))
# plt.scatter(z, egamma, s=5, alpha=1, marker='o', c='r')
# plt.xlim(0, 8)
# plt.ylim(47,54)
# plt.axis()
# plt.title("Z-Egamma")
# plt.xlabel("z")
# plt.ylabel("log_Egamma")
# # plt.savefig("/Users/dingding/Desktop/Z-Egamma6.11.eps")
# plt.show()
#
# grbname=np.append(egrbname,pgrbname)

#
# dataframename=pd.DataFrame(grbname)
# dataframename.to_csv('/users/dingding/desktop/grbname.csv',sep=',')
# dataframename=pd.DataFrame(seita)
# dataframename.to_csv('/users/dingding/desktop/seita.csv',sep=',')
# dataframename=pd.DataFrame(egamma)
# dataframename.to_csv('/users/dingding/desktop/egamma.csv',sep=',')