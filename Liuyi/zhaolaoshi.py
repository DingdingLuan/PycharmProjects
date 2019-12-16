import numpy as np
from allkindsoffunctions import *
from scipy.stats import kstest
from scipy.stats import ks_2samp

# *******读取4C+01.02头文件
c0102=pd.read_excel('/Users/dingding/Desktop/88.xlsx')
start_time1=c0102['date']
fluence1=c0102['flux']


# *******做出4C+01.02原始的光变曲线
# plt.figure(figsize=(20,10))
# plt.plot(start_time1,np.log10(fluence1),label='4c0102',linewidth=0.2,color='r',marker='o',markerfacecolor='blue',markersize=3)
# plt.xlabel('time[day]')
# plt.ylabel('log10_fluence[erg s$^{-1}$ cm$^{-2}$]')
# plt.title('4C+0102 Light Curve Origin')
# plt.legend(loc='best')
# plt.show()
# self=correlationselffunction(fluence1)
# x=np.arange(0,len(self),1)
# plt.figure(figsize=(20,10))
# plt.scatter(x, self,s=5,alpha=1,marker='*',c='blue',label='Correlation-func of 4c0102')
# plt.axhline(0.0, color= 'black')
# plt.grid(True, linestyle = "-.", color = "grey", linewidth = "0.2")
# plt.legend(loc='best')
# plt.title("4C+0102 Self-correlative Function distribution\nSample number=%a" %(len(fluence1)))
# plt.xlabel("τ")
# plt.ylabel("Correlation Function")
# plt.show()


# #******ks检验
# kstest_0102=kstest(fluence1, 'norm')
# kstest_2807=kstest(fluence2,'norm')
# if kstest_0102[1]<=0.05:
#     print('4c+0102 is not normal distribution\npvalue=%a' %(kstest_0102[1]))
# else:
#     print('4c+0102 is normal distribution\npvalue=%a' %(kstest_0102[1]))
#
# if kstest_2807[1]<=0.05:
#     print('4c+2807 is not normal distribution\npvalue=%a' %(kstest_2807[1]))
# else:
#     print('4c+2807 is normal distribution\npvalue=%a' %(kstest_2807[1]))
#
#
# # ********对两个源进行z-score标准化处理，并生成新的流量序列
# new0102fluence=z_score(fluence1)
# new2807fluence=z_score(fluence2)
# a=ks_2samp(new0102fluence,new2807fluence)
# if a[1]<=0.05:
#     print('After z-score standardization,4c+0102 and 4c+2807 are not in same distribution,pvalue=%a' %(a[1]))
# else:
#     print('After z-score standardization,4c+0102 and 4c+2807 are  in same distribution,pvalue=%a' % (a[1]))
#
#
#
# # **********p-p4c+0102:
# total_fluence=np.sum(fluence1)
# fluence1=fluence1[np.argsort(fluence1)]
# fluence1=np.array(fluence1)
# i=1
# for i in range(len(start_time1)):
#     fluence1[i]=fluence1[i]+fluence1[i-1]
#     i=i+1
# y1=fluence1
# y1=fluence1/total_fluence
# x1=start_time1-np.min(start_time1)
# x2=np.arange(0, len(start_time1), 1)
# y2=np.random.normal(0,1,len(start_time1))
# y2=np.abs(y2)
# total_normal=np.sum(y2)
# i=1
# for i in range(len(y2)):
#     y2[i]=y2[i]+y2[i-1]
#     i=i+1
# y2=y2/total_normal
# a=np.arange(0,1,0.01)
# b=np.arange(0,1,0.01)
# plt.plot(y2,y1)
# plt.title('p-p plot for 4C+0102')
# plt.xlabel('Theoritical normal Data')
# plt.ylabel('Observed Data')
# plt.plot(a,b,linewidth=2,color='r')
# plt.legend(labels=['Actual result','Perfect result'],loc='best')
# # plt.savefig('/users/dingding/desktop/output/0102/pp-plot.jpg')
# plt.show()
#
#
#
# # ***********q-q4c+0102:
# total_fluence=np.sum(fluence1)
# fluence1=fluence1[np.argsort(fluence1)]
# fluence1=np.array(fluence1)
# i=1
# for i in range(len(start_time1)):
#     fluence1[i]=fluence1[i]+fluence1[i-1]
#     i=i+1
# y1=fluence1
# x1=start_time1-np.min(start_time1)
# x2=np.arange(0, len(start_time1), 1)
# y2=np.random.normal(0,1,len(start_time1))
# y2=np.abs(y2)
# total_normal=np.sum(y2)
# i=1
# for i in range(len(y2)):
#     y2[i]=y2[i]+y2[i-1]
#     i=i+1
# a=np.arange(0,np.max(y2),np.max(y2)/len(y2))
# b=np.arange(0,np.max(y1),np.max(y1)/len(y2))
# plt.plot(y2,y1)
# plt.title('q-q plot for 4C+0102')
# plt.xlabel('Theoritical random normal data')
# plt.ylabel('Observed fluence Data')
# plt.plot(a,b,linewidth=2,color='r')
# plt.legend(labels=['Actual result','Perfect result'],loc='best')
# # plt.savefig('/users/dingding/desktop/output/0102/qq-plot.jpg')
# plt.show()

# #*********高斯平滑
# gaussfluence=Gauss_multiFlat(fluence1,1,8,3)
# plt.figure(figsize=(20,10))
# plt.plot(start_time1,np.log10(gaussfluence),label='Gauss_4c0102',linewidth=1,color='blue')
# plt.plot(start_time1,np.log10(fluence1),label='4c0102',linewidth=0.2,color='r')
# plt.xlabel('time[day]')
# plt.ylabel('log10_gaussfluence[erg s$^{-1}$ cm$^{-2}$]')
# plt.title('4C+0102 Gauss-Flat Light Curve,n=6')
# plt.legend(loc='best')
# # plt.savefig('/users/dingding/desktop/output/0102/gaussflat.jpg')
# plt.show()

