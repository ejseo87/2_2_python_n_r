# from scipy import stats
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import seaborn as sns
import numpy as np
from matplotlib import rc

import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# setting a workiing directory
import os
print(os.getcwd())
os.chdir(os.getcwd()+"/data")
print(os.getcwd())
# matpplot 에 한글설정
# from matplotlib import rc
rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False

# 291페이지 산점도
health = pd.read_csv("health.csv")
print("health.head(3) =\n", health.head(3))
plt.scatter(health.weight, health.time)
plt.title('산점도 (weight, time)')
plt.xlabel('weight')
plt.ylabel('time')
plt.show()
# 상관계수
r = np.corrcoef(health.weight, health.time)
print("np.corrcoef(health.weight, health.time) = \n", r)
# 산점도 행렬
# import seaborn as sns
cols = ['weight', 'pulse', 'muscle', 'quarter', 'time']
print("type(cols) = ", type(cols))
health2 = health[cols]
print("health2.head(3) =\n", health2.head(3))
sns.set_theme(style='ticks')
sns.pairplot(health2)
plt.show()
# 회귀분석
# import statsmodels.api as sm
x_cols = ['weight', 'pulse', 'muscle', 'quarter']
x = health[x_cols]
x = sm.add_constant(x)
y = health['time']
print("x.head(3) = \n", x.head(3))
model = sm.OLS(y, x)
result = model.fit()
print("result.summary() = \n", result.summary())
y_predict = result.predict(x)
print("y_predict[0:5] =\n", y_predict[0:5])
print("result.params = \n", result.params)
# 또 다른 회귀분석 방법 : sklearn.linear_model
# from sklearn.linear_model import LinearRegression
x2 = health[x_cols]
sresult = LinearRegression().fit(x2, y)
print("sresult.coef_ = ", sresult.coef_)
print("sresult.intercept_ = ", sresult.intercept_)
spredict = sresult.predict(x2)
print("spredict[0:5] = \n", spredict[0:5])
