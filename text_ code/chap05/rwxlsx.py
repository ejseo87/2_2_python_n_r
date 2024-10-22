# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:21:44 2019

@author: Sim
"""

import pandas as pd

data = pd.read_excel (r'K:\HWP\books\PR4DS\height.xlsx', header=None, 
                      names=['height','gender']) 
df1 = pd.DataFrame(data)
print(df1)


data = pd.read_excel ('http://jupiter.hallym.ac.kr/ftpdata/data/bmi.xlsx',
                     index_col=2) 
df2 = pd.DataFrame(data) #, columns= ['Product','Price'])
print(df2)

cars = {'make': ['Hyundai','Kia','Ford','Chevrolet'],
        'model': ['Sonata', 'K5', 'Taurus', 'Impala'],
        'price':  [3200,3100,3500,3700] }
df3 = pd.DataFrame(cars)
export_excel = df3.to_excel (r'K:\HWP\books\PR4DS\cars.xlsx', 
  index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

'''
'''