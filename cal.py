
import pandas as pd
import copy
import datetime as dt
import numpy as np

print(1 + 3 / 2)
print(2 ^ 10)
print(2 ** 10)
a = 10
print(a)
a = [1, 2, 3, 4, 5]
# 에러
# print(a/3)

a = np.arange(1, 10)
print(a)
print(a/3)  # OK
print(a//3)  # 몱
print(a % 3)  # 나머지

# 자료형
a = 100
print(type(a))
b = 100.1
print(type(b))
bool(23.7)
print(type(bool(23.7)))

# 문자열 합치기
c = "~"
d = str(a)+" "+c
print(d)

# 패키지
a = np.arange(15)
print(a)
print(a[0])
print(a[1])
m = np.mean(a)
print(m)

# 결측치
height = np.array([45, 75, 60, 51, np.nan])
print(height)
# np.mean(height)
print(np.nanmean(height))
# 무한대
# import numpy as np
x = np.array([1, -1, 0, np.infty, -np.inf])
print(x/np.Infinity)
# 날짜 시간
now = dt.datetime.now()
print(now.strftime("%Y년%m월%d일 : %A"))
print(now.year)

dob = dt.datetime(2020, 9, 8)
print(dob.strftime("%Y-%m-%d: %A"))
# matrix
xm = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(xm)
xm = np.arange(1, 10)
print(xm)
xm = xm.reshape(3, 3)
print(xm)
print(xm[:, 0])  # 콜론은 전체
print(xm[0:2, :])
# list
x2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(x2)
print("x2[0][2] = ", x2[0][2])
x22 = [row[2] for row in x2]
print("[row[2] for row in x2] = ", x22)
# tuple
x = (1, 2, 3)
print("tuple x = ", x, " : contant array")
# dictionary key, value
country_code = {
    'korea': 82,
    'us': 1,
    'china': 86
}
print("len(country_code) = ", len(country_code))
print("country_code['korea'] = ", country_code['korea'])
# deepcopy
xm2 = copy.deepcopy(xm)
xm[0, 0] = 999
print("xm = ", xm)
print("xm2 = ", xm2)
# dataframe

d = {'name': ['Kom', "Lee", "Park"], 'height': [170, 180, 175]}
df1 = pd.DataFrame(data=d)
print("df1=", df1)
print("type(df1) = ", type(df1))
df2 = pd.DataFrame([['Kim', 170], ['Lee', 180], ['Palr', 175]],
                   index=['r1', 'r2', 'r3'], columns=['name', 'height'])
print("df2=", df2)
