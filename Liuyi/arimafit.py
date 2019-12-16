import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt
from allkindsoffunctions import *


# 读取数据，pd.read_csv默认生成DataFrame对象，需将其转换成Series对象
df = pd.read_csv('/users/dingding/desktop/4c+28.07/2807arimaselected.csv', encoding='utf-8', index_col='date')
df.index = pd.to_datetime(df.index)  # 将字符串索引转换成时间索引
ts = df['flux']  # 生成pd.Series对象
# 查看数据格式
# print(ts.head())
# print(ts.head().index)

# draw_trend(ts,size=30)
# draw_ts(ts)
# draw_acf_pacf(ts)

ts_log=np.log10(ts)
rol_mean = ts_log.rolling(window=12).mean()
rol_mean.dropna(inplace=True)
ts_diff_1 = rol_mean.diff(1)
ts_diff_1.dropna(inplace=True)
# print(testStationarity(ts_diff_1))


ts_diff_2 = ts_diff_1.diff(1)
ts_diff_2.dropna(inplace=True)

from statsmodels.tsa.arima_model import ARMA
model = ARMA(ts_diff_2, order=(1, 1))
result_arma = model.fit( disp=-1, method='css')

ts_log = np.log(ts)
# draw_ts(ts_log)
# draw_trend(ts_log, 12)


diff_12 = ts_log.diff(12)
diff_12.dropna(inplace=True)
diff_12_1 = diff_12.diff(1)
diff_12_1.dropna(inplace=True)
testStationarity(diff_12_1)

from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(ts_log, model="additive")

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid


rol_mean = ts_log.rolling(window=12).mean()
rol_mean.dropna(inplace=True)
ts_diff_1 = rol_mean.diff(1)
ts_diff_1.dropna(inplace=True)
print(testStationarity(ts_diff_1))

ts_diff_2 = ts_diff_1.diff(1)
ts_diff_2.dropna(inplace=True)


from statsmodels.tsa.arima_model import ARMA,ARIMA


model = ARMA(ts_diff_2, order=(1, 1))
result_arma = model.fit( disp=-1, method='css')



predict_ts = result_arma.predict()
# 一阶差分还原
diff_shift_ts = ts_diff_1.shift(1)
diff_recover_1 = predict_ts.add(diff_shift_ts)
# 再次一阶差分还原
rol_shift_ts = rol_mean.shift(1)
diff_recover = diff_recover_1.add(rol_shift_ts)
# 移动平均还原
rol_sum = ts_log.rolling(window=11).sum()
rol_recover = diff_recover*12 - rol_sum.shift(1)
# 对数还原
log_recover = np.exp(rol_recover)
log_recover.dropna(inplace=True)





ts = ts[log_recover.index]  # 过滤没有预测的记录
plt.figure(facecolor='white')
log_recover.plot(color='blue', label='Predict')
ts.plot(color='red', label='Original')
plt.legend(loc='best')
plt.title('RMSE: %.4f'% np.sqrt(sum((log_recover-ts)**2)/ts.size))
plt.show()


diffed_ts = diff_ts(ts_log, d=[12, 1])
model = arima_model.ARIMA(diffed_ts)
model.certain_model(1, 1)
predict_ts = model.properModel.predict()
diff_recover_ts = predict_diff_recover(predict_ts, d=[12, 1])
log_recover = np.exp(diff_recover_ts)