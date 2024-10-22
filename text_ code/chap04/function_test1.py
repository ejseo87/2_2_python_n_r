# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:29:11 2019

@author: Sim
"""
# function_test1.py
def my_sums(a=0, b=10):
  import numpy as np
  sum1 = 0; sum2 = 0
  data = np.arange(a,b+1)
  for i in data: 
    sum1 = sum1 + i
    sum2 = sum2 + i**2
  return sum1, sum2, len(data)
# end of function my_sums
  
# try my_sums(1, 10) ; my_sums(); my_sums(b=100, a=0); my_sums(a=0, b=100)
  
a = my_sums(1,10)
mm = a[0]/a[2]
vv = (a[1] - a[2]*(mm**2)) / (a[2] - 1)
