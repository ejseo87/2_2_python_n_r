
# https://kongdols-room.tistory.com/112
# loc : 레이블을 이용한 인덱싱
# iloc : 위치 정수를 이용하여 인덱싱

import pandas as pd
import numpy as np

ex_df = pd.DataFrame([[0,1,2],[3,4,5],[6,7,8]],
           index=['r0','r1','r2'],
           columns = ['c0','c1','c2'])
ex_df
Out[3]: 
    c0  c1  c2
r0   0   1   2
r1   3   4   5
r2   6   7   8

ex_df.loc['r1']  # 행에 대한 접근
Out[4]: 
c0    3
c1    4
c2    5
Name: r1, dtype: int64

ex_df.loc['r1','c0'] # 하나의 요소에 대한 접근
Out[5]: 3

ex_df.loc['r0':'r1', 'c1':'c2']
Out[6]: 
    c1  c2
r0   1   2
r1   4   5

ex_df.loc['r1':'r2']
Out[7]: 
    c0  c1  c2
r1   3   4   5
r2   6   7   8

ex_df.loc[:, 'c1':'c2']
Out[11]: 
    c1  c2
r0   1   2
r1   4   5
r2   7   8

ex_df.iloc[1]    # 행에 대한 접근
Out[12]: 
c0    3
c1    4
c2    5
Name: r1, dtype: int64

ex_df.iloc[1,2]
Out[13]: 5

ex_df.iloc[:, 1:3]
Out[15]: 
    c1  c2
r0   1   2
r1   4   5
r2   7   8
