# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:33:30 2020

@author: Sim
"""

a=[2, 3, 'c']
x=[1, 2, 'a', a]
print(x)
print(x[3])
 
x2 = [ [1,2,3], [4,5,6], [7,8,9] ]
print(x2[0][2])
print(x2[2])
print([row[2] for row in x2])
print([column[2] for column in x2])

tpl = (1,2,3)
print(type(tpl))
print(tpl[2])
#tpl[2] = 3 # 에러