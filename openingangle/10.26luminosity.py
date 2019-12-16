from Calculatefunction import *
import pandas as pd


df=pd.read_excel("/Users/dingding/Desktop/calculate/10.22/10.26.xlsx")
z_obseved=df['z']
s_observed=df['s']
s_observed=s_observed*10**(-7)
t90_observed=df['t90']

L=[]
P=[]
for i in range(len(z_obseved)):
    l=luminosity(z_obseved[i],s_observed[i],t90_observed[i])
    p=P_obseved(z_obseved[i],s_observed[i],t90_observed[i])
    L=np.append(L,l)
    P=np.append(P,p)


# dataframename=pd.DataFrame(L)
# dataframename.to_csv('/users/dingding 1/desktop/L10.25.csv',sep=',')
# dataframename=pd.DataFrame(P)
# dataframename.to_csv('/users/dingding 1/desktop/P10.25.csv',sep=',')