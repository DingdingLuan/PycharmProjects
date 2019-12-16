
# import plotly.plotly as py
# import plotly
# import plotly.graph_objs as go
# import numpy as np
# plotly.tools.set_credentials_file(username='dingdingluan', api_key='UfHllkH5gR0sFeVkWShY')
#
# pts=np.loadtxt('/users/dingding/desktop/mesh_dataset.txt')
# x,y,z=zip(*pts)
#
# trace = go.Mesh3d(x=x,y=y,z=z,color='#FFB6C1',opacity=0.50)
# py.iplot([trace])
#


import numpy as np
import matplotlib.pyplot as plt

#生成绘图数据
N = 100
x, y = np.mgrid[:10, :10]
def Z(x,y):
    Z = np.cos(x*0.05+np.random.rand()) + np.sin(y*0.05+np.random.rand())+2*np.random.rand()-1
    return Z

# mask out the negative and positive values, respectively
# Zpos = np.ma.masked_less(Z, 0)   #小于零的部分
# Zneg = np.ma.masked_greater(Z, 0)  #大于零的部分

fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 3), ncols=3)

# pos = ax1.imshow(Zpos, cmap='Reds', interpolation='none')
# fig.colorbar(pos, ax=ax1)  #这里使用colorbar来制定需要画颜色棒的图的轴，以及对应的cmap，与pos对应
#
# neg = ax2.imshow(Zneg, cmap='Blues_r', interpolation='none')
# fig.colorbar(neg, ax=ax2)

# pos_neg_clipped = ax3.imshow(Z(x,y), cmap='jet',interpolation='none')  #-2,2的区间
# fig.colorbar(pos_neg_clipped, ax=ax3)
# plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 计算x,y坐标对应的高度值
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


# 生成x,y的数据
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# 把x,y数据生成mesh网格状的数据，因为等高线的显示是在网格的基础上添加上高度值
X, Y = np.meshgrid(x, y)

# 填充等高线
plt.contourf(X, Y, f(X, Y))
# 显示图表
plt.show()
