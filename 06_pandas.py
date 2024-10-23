import statsmodels.api as sm
import numpy as np
import pandas as pd
import os
# setting a workiing directory
print(os.getcwd())
os.chdir(os.getcwd()+"/data")
print("***os.getcwd() = ", os.getcwd())

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
df = pd.DataFrame(s, columns=["A"])
print("***s = ", s)
print("***df = ", df)
# print("dir(df) = ", dir(df))
print("***s.__class__ = ", s.__class__)
print("***df.__class__ = ", df.__class__)
print("***type(s) = ", type(s))
# 142p 에제2
print("***s.to_numpy() = ", s.to_numpy())
print("***df.to_numpy() = ", df.to_numpy())
print("***s.to_numpy().shape = ", s.to_numpy().shape)
print("***df.to_numpy().shape = ", df.to_numpy().shape)
print("***df.columns = ", df.columns)
print("***s.index = ", s.index)
print("***df.index = ", df.index)
# 예제 1.3
dict = {
    'one': pd.Series([1, 2], index=['a', 'b']),
    'two': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
}
print("*** dict = \n", dict)
df = pd.DataFrame(dict)
print("*** df = \n", df)

x = np.arange(4).reshape((2, 2))
print("***x = \n", x)
df = pd.DataFrame(x)
df.columns = ['A', 'B']
df.index = [11, 12]
print("***df =\n", df)
# 예제 1.4
faithful = pd.read_csv("faithful.csv")
print("***faithful.shape = ", faithful.shape)
print("***faithful.head(3) \n", faithful.head(3))
print("faithful.__class__ = ", faithful.__class__)
print("type(faithful) = ", type(faithful))
faithful.to_csv("faithful_tmp.csv")
# 예제 1.5 R데이터 불러오기
trees = sm.datasets.get_rdataset("trees")['data']
print("***trees.head(3) \n", trees.head(3))
iris = sm.datasets.get_rdataset("iris")['data']
print("***iris.head(3) \n", iris.head(3))
print("***type(trees)=", type(trees))
print("***trees.__class__ = ", trees.__class__)
# 1.6예제, Series   자료 이용
s1 = pd.Series([1.0, 2, 3])
sa = pd.Series([1.0, 2, 3], index=['a', 'b', 'c'])
sc = pd.Series([0.0, 2, 3], index=['a', 'b', 'd'])

print("***s1 = \n", s1)
print("***s1 - 2 = \n", s1-2)
print("***sa = \n", sa)
print("***sc = \n", sc)

sac = sa + sc
print("***sac = \n", sac)
# 1.7 결측치 NaN 처리
print("sac.isnull() = ", sac.isnull())
print("sac.notnull() = ", sac.notnull())

print("***sac = \n", sac.fillna(-1.0))
sx = sac.dropna()
print("***sx = \n", sx)
sy = sx._append(sc[:2])
print("***sy = \n", sy)
print("***sy.drop('a') = \n", sy.drop('a'))
# 1.8 Series method
sn = pd.Series([1, 2, 1, 3, 3, 5, 3, 4])
print("***sn = \n", sn)
print("*** sn.head() = ", sn.head())
print("*** sn.describe() = ", sn.describe())
print("*** list(sn.unique()) = ", list(sn.unique()))
print("*** sn.nunique() = ", sn.nunique())
print("*** sn.replace([1, 2], 0) = ", sn.replace([1, 2], 0))
# 1.9 trees dataset 알뷰선택
tree4 = trees[0:4].copy()
print("***tree4= \n", tree4)
tree4.index = ['B', 'C', 'D', 'E']
print("***tree4= \n", tree4)
print("***tree4[tree4 > 10]= \n", tree4[tree4 > 10])
print("***tree4[tree4.Height > 65 ] \n", tree4[tree4.Height > 65])
print("***tree4['E':'C'] = \n", tree4['E':'C'])
cols = ['Girth', 'Height']
print("tree4[cols] =\n", tree4[cols])
# 예제11 데이터의 전치와 정렬
print("***tree4.T = \n", tree4.T)
print("***tree4.sort_index() = \n", tree4.sort_index())
print("***tree4.sort_values('Height') =\n", tree4.sort_values('Height'))
print("***tree4.sort_values('Height', ascending=False)=\n",
      tree4.sort_values('Height', ascending=False))
tree5 = tree4.copy()
tree5.iloc[1, 0] = 12.8
tree5.iloc[1, 1] = 63
print("***tree5.sort_values(by=['Height','Girth'])=\n",
      tree5.sort_values(by=['Height', 'Girth']))
# 예제1,12 dataframe 에 통계/계산 메소드의 적용
print("***tree4.mean() = \n", tree4.mean())
print("***tree4.mean(1) = \n", tree4.mean(1))  # 케이스의 평균
print("***tree4.cumsum() = \n", tree4.cumsum())  # 누적합
print("***tree4.apply(np.cumsum) = \n", tree4.apply(np.cumsum))
print("***tree4.apply(lambda x: x.max()) = \n", tree4.apply(lambda x: x.max()))
# 예제1.13 crosstab과 groupby
mtcars = sm.datasets.get_rdataset("mtcars")['data']
print("***mtcars.head(3) \n", mtcars.head(3))
cols = ['mpg', 'cyl', 'hp', 'gear']
mtx = mtcars[cols].copy()
print("mtx.head(3) =\n", mtx.head(3))
print("pd.crosstab(mtx.cyl, mtx.gear) =\n", pd.crosstab(mtx.cyl, mtx.gear))
mtn = mtx.groupby(by=['cyl', 'gear']).mean()
print("mtn =\n", mtn)
# 예졔 1.14 unstack, multi-index 이용
print("mtn['mpg'].unstack(0) =\n", mtn['mpg'].unstack(0))
# unstack과 동일한 결과를 가져오는 코드
mi = mtn.index
print("mi = \n", mi)
lvs0 = mi.levels[0]
cds0 = mi.codes[0]
lvx0 = lvs0[cds0].values
lvs1 = mi.levels[1]
cds1 = mi.codes[1]
lvx1 = lvs1[cds1].values
mpgx = mtn['mpg'].to_numpy()
d = {mi.names[0]: lvx0, mi.names[1]: lvx1, 'mpg': mpgx}
mpga = pd.DataFrame(d)
print("mpga =\n", mpga)
mpga.pivot(index='gear', columns='cyl', values='mpg')
print("mpga.pivot(index='gear', columns='cyl', values='mpg') =\n",
      mpga.pivot(index='gear', columns='cyl', values='mpg'))
