from allkindsoffunctions import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# a=np.random.normal(0,0.1,1000)
# # b=np.arange(0,1000,1)
# #
# # plt.plot(b,a)
# # plt.show()
# # a=np.arange(0,1000,1)
# # print(a)
# i=1
# print(len(a[:5]))
# print(len(a[i:5+i]))
# print(correlationselffunction(a))

import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

# pltsampleNo = 100000
# # 一维正态分布
# # 下面三种方式是等效的
# mu = 3
# sigma = 0.1
# # np.random.seed(0)
# s = np.random.normal(mu, sigma, sampleNo)
# plt.subplot(111)
# plt.hist(s, 300, normed=True)   #中间的数指的是柱子的个数
# plt.show()

# from allkindsoffunctions import *
# a=np.random.beta(10,1,200)
# b=np.arange(0,200,1)
# new=Gauss_multiFlat(a,1,20,4)
# plt.figure(figsize=(20,10))
# plt.plot(b,a,linewidth=0.5)
# plt.plot(b,new,linewidth=1)
# plt.show()



#
# c2807=pd.read_excel('/Users/dingding/Desktop/4c+28.07/2807selected.xlsx')
# fluence2=c2807['flux_0p1_300_gev']
# print(len(optimizedgaussflat(fluence2,1,43)))
# print(len(fluence2))


# print(new-a)
# a=np.arange(0,10,1)
# b=a
# print(b)
# b[0]=66
# print(b)

# cf=correlationothersfunction(a,b)
# x=np.arange(0,len(cf),1)
# plt.figure(figsize=(20,10))
# plt.scatter(x, cf,s=10,alpha=1,marker='*',c='green',label='Interrelation-func of 4c0102&4c2807')
# plt.axhline(0.0, color= 'black')
# plt.grid(True, linestyle = "-.", color = "grey", linewidth = "0.2")
# plt.title("4C+01.02&4C+29.07 Interrelation Function distribution")
# plt.legend(loc='best')
# plt.xlabel("τ")
# plt.ylabel("Interrelation Functionn")
# plt.show()
# print(a[3])

# def optimizedgaussflat(ts, a, part):
#     import numpy as np
#     unitnumber = int(len(ts) / part)
#     leftnumber=len(ts)-unitnumber*part
#     newts=np.append(ts[len(ts)-int(unitnumber/2):len(ts)],ts)
#     newts=np.append(newts,ts[:unitnumber-leftnumber])       #构造新的鬼魂序列
#     if (unitnumber%2)==0:                                  #判断采样值的奇偶性
#         miu=int(unitnumber/2)
#     else:
#         miu=int(unitnumber/2+1)
#     j=0
#     window = newts[:unitnumber]
#     x_prime = np.zeros_like(newts)
#     for j in range(len(newts)-int(unitnumber/2)):
#         k = 0
#         m = []
#         s = []
#         for k in range(unitnumber):
#             mm = np.abs(p(k, miu, a) - p(k + 1, miu, a)) * np.exp(-(k - miu) ** 2 / (2 * a ** 2))
#             ss = mm * window[k]
#             m = np.append(m, mm)
#             s = np.append(s, ss)
#             k = k + 1
#         M = np.sum(m)
#         S = np.sum(s)
#         x_prime[miu + j] = S / M
#         j = j + 1
#         window =newts[j:unitnumber + j]
#     return x_prime
#
