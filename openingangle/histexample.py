from scipy.stats import kstest
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


# create data with specific distribution
# data = np.random.normal(0, 1, 1000)
data = np.random.uniform(0, 1, 50)


# KS test and output the results
test_stat = kstest(data, 'norm')
print(test_stat)

# Choose how many bins you want here
num_bins = 20

# create cdf of random sample
ecdf = sm.distributions.ECDF(data)
x = np.linspace(min(data), max(data),num_bins)
y = ecdf(x)

# create cdf of normal distribution
yy = norm.cdf((x-x.mean())/x.std(), 0, 1)

# find D's index
z = abs(yy-y).tolist()
ind = z.index(max(z))
print(x)
print(len(y))
print(yy)


# # plot
# fig1 = plt.figure('fig1')
# n, bins, patches = plt.hist(data, bins=30, normed=1, facecolor='green', alpha=0.75)
# plt.title("random sample's pdf")
# fig2 = plt.figure('fig2')
# plt.step(x,y,label="Fn(x)")
plt.step(x,yy,label="F0(x)")
# plt.errorbar(((x[ind]+x[ind-1])/2),(abs(yy[ind]+y[ind]))/2,abs(yy[ind]-y[ind])/2,fmt='-ro',label="D")
# plt.legend(loc='upper left')
# plt.title("random sample and normal distribution's cdf")
#
# fig3 =  plt.figure('fig3')
# plt.plot(data)
plt.show()
