# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:42:02 2019

@author: root
"""

import pandas as pd
import numpy as np

d = {'name': ['Kim', 'Lee', 'Park'], 'height': [170, 180, 175]}
df1 = pd.DataFrame(data=d)
print(df1)

df2 = pd.DataFrame([['kim', 170], ['Lee', 180], ['Park', 175]],
                   columns=['name', 'height'])
print (df2)

df3 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
print (df3)
print(df3.describe())

x = df1['height']
print(x)
y = df1.iloc[0:2]
print(y)

print(df1.iloc[:, 1])
print(df1.iloc[:, 1])
print(df1.iloc[[1,2], 0])

df3
Out[77]: 
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9

# 변수 선택

cols = ['a','b']

df3[cols]
Out[79]: 
   a  b
0  1  2
1  4  5
2  7  8

df3.iloc[:, 0:2]
Out[80]: 
   a  b
0  1  2
1  4  5
2  7  8

df3.loc[:, 'a':'b']
Out[81]: 
   a  b
0  1  2
1  4  5
2  7  8