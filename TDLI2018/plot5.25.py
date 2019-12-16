import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

example=pd.read_excel('/users/dingding/desktop/buildingtry/time_10.xlsx')
x=example['x']
rho=example['rho']
eps=example['eps']
pre=example['pre']
cs=example['cs']

plt.figure(figsize=(10,5))
plt.xlabel('x')
plt.ylabel()