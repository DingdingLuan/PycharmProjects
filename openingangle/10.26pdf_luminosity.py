from Calculatefunction import *
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import ks_2samp

df=pd.read_excel("/Users/dingding/Desktop/calculate/10.22/result10.25.xlsx")
l=df['luminosity']

lnum=100
prol=pdflog(l,49,55,lnum)
print(prol)

# plot the result of luminosity:
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(7, 7))
y=np.arange(49,55,(55-49)/lnum)            #plot l
plt.bar(y,prol,width=(55-49)/lnum,edgecolor='r',facecolor='white',linestyle='--')
plt.title("Mock sample = 170")
plt.xlabel('$log(L/ erg  s^{-1})$')
plt.ylabel('$Probability$')
# plt.savefig('/Users/dingding/Desktop/calculate/9.17/luminosity9.17.eps')
plt.show()