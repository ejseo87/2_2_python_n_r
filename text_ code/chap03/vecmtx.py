# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:09:07 2020

@author: Sim
"""

import numpy as np
xv = np.array([1, 2, 3, 4, 5, 6, 7, 9])
xv = np.arange(1,10)
print(xv[4])
print(xv[1:4])
print(len(xv))
print(xv.size)

xm = np.array([[1,2,3], [3,4,5], [6,7,9]])
xm = np.arange(1,10) # 또는 xm = np.array(range(1,10))
xm = xm.reshape(3,3)
print(xm)
print(xm.shape)
print(xm[1,2])
print(xm[:, 0] )
print(xm[0:2, :])


xv[3] = 11
print(xv)
xm[0, 2] = 11
print(xm)