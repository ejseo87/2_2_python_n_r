# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:37:05 2019

@author: Sim
"""

import numpy as np
x1 = [1,2,3,4]; x2 = [5,6,7,8]
y1 = np.array([1,2,3,4]); y2 = np.array([5,6,7,8])

#print(x1+2) # x1은 리스트, 2는 스칼라라 연산이 안됨.
print (x1 +[2])
print(y1+2)
print(x1+x2)
print(y1+y2)
