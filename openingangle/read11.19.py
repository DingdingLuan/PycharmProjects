import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import ks_2samp


range=pd.read_csv('/users/dingding 1/desktop/calculate/11.19/observedEisoPDF.txt')
eiso=pd.read_csv('/users/dingding 1/desktop/calculate/11.19/Eisoindex.txt')

# print(range)
# print(eiso)
plt.step(range,eiso,linewidth=0.7,linestyle='--',c='r')
plt.xlim(46,52)
plt.ylim(0,0.2)
plt.show()