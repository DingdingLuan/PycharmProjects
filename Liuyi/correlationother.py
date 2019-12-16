import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from allkindsoffunctions import *

c0102=pd.read_excel('/Users/dingding/Desktop/4c+01.02/0102selected.xlsx')
fluence1=c0102['flux_0p1_300_gev']
c2807=pd.read_excel('/Users/dingding/Desktop/4c+28.07/2807selected.xlsx')
fluence2=c2807['flux_0p1_300_gev']

convolve=correlationothersfunction(fluence1,fluence2)
x=np.arange(0,len(convolve),1)
plt.figure(figsize=(20,10))
plt.scatter(x, np.log10(convolve),s=0.5,alpha=1,marker='o',c='r')
plt.title("4C+01.02&4C+29.07 correlative Function(value) distribution")
plt.xlabel("Series Number")
plt.ylabel("log10_Function value")
plt.show()


